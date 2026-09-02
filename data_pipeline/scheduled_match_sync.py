"""
Automated Match Sync Engine with Dynamic Next-Match Cron Scheduling.
Checks for matches in CDMX Time (Kickoff + 4 hours window).
Dynamically programs the next GitHub Actions cron for the exact date and time of the subsequent match (+4h),
or reschedules in +4h on failure/retry.
"""

import os
import sys
import datetime
from zoneinfo import ZoneInfo
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.db_manager import DatabaseManager
from data_pipeline.agent_sync import BarcaSyncAgent
from data_pipeline.seed_opponent_form import seed_opponent_recent_matches

def update_workflow_cron(target_cdmx_dt, workflow_path=None):
    """
    Updates the cron schedule in .github/workflows/sync_match.yml to the exact UTC timestamp of target_cdmx_dt.
    Ensures GitHub Actions ONLY triggers at that exact date and time.
    """
    if workflow_path is None:
        workflow_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".github", "workflows", "sync_match.yml")
        
    if not os.path.exists(workflow_path):
        print(f"[WARN] Workflow file not found at: {workflow_path}")
        return False
        
    # Convert CDMX datetime to UTC
    utc_dt = target_cdmx_dt.astimezone(datetime.timezone.utc)
    cron_expr = f"{utc_dt.minute} {utc_dt.hour} {utc_dt.day} {utc_dt.month} *"
    
    with open(workflow_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    import re
    # Replace existing cron expression inside schedule block
    cron_pattern = r"(- cron:\s*['\"][^'\"]+['\"])"
    new_cron_line = f"- cron: '{cron_expr}'"
    
    if re.search(cron_pattern, content):
        updated_content = re.sub(cron_pattern, new_cron_line, content)
        with open(workflow_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print(f"[CRON DYNAMIC] Siguiente ejecucion programada: {target_cdmx_dt.strftime('%Y-%m-%d %H:%M')} CDMX ({utc_dt.strftime('%Y-%m-%d %H:%M')} UTC) -> cron: '{cron_expr}'")
        return True
    else:
        print("[WARN] No se encontro patron de cron en el workflow.")
        return False

def sync_pending_matches_cdmx(db_path="barca_analytics.db", target_datetime=None):
    """
    Checks all SCHEDULED matches in the database using Mexico City (CDMX) Time.
    If current_cdmx_time >= match_kickoff_cdmx + 4 hours:
      - Marks the match as ready for official sync.
      - Updates barca_analytics.db.
      - Schedules the cron for the next upcoming match (+4h).
    If sync fails or is not due, schedules retry for +4h or next match.
    """
    cdmx_tz = ZoneInfo("America/Mexico_City")
    if target_datetime is None:
        now_cdmx = datetime.datetime.now(cdmx_tz)
    else:
        now_cdmx = target_datetime if target_datetime.tzinfo else target_datetime.replace(tzinfo=cdmx_tz)

    db = DatabaseManager(db_path)
    
    df = db.get_all_matches_df()
    scheduled_2627 = df[(df['season'] == '2026-27') & (df['status'] == 'SCHEDULED')].sort_values('date')

    if scheduled_2627.empty:
        print("[INFO] Todos los partidos de la temporada 2026/27 ya estan finalizados.")
        return 0

    print(f"[TIME] Hora actual (CDMX): {now_cdmx.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    
    updated_count = 0
    next_cron_target_cdmx = None
    
    for idx, row in scheduled_2627.iterrows():
        m_date_str = str(row['date'])
        m_time_str = str(row['time']) if pd.notna(row['time']) and str(row['time']).lower() not in ['nan', 'none', ''] else "21:00"
        
        try:
            m_dt_naive = datetime.datetime.strptime(f"{m_date_str} {m_time_str}", "%Y-%m-%d %H:%M")
        except Exception:
            m_dt_naive = datetime.datetime.strptime(m_date_str, "%Y-%m-%d")
            
        m_dt_cdmx = m_dt_naive.replace(tzinfo=cdmx_tz)
        sync_threshold = m_dt_cdmx + datetime.timedelta(hours=4)
        
        time_diff = sync_threshold - now_cdmx
        
        if now_cdmx >= sync_threshold:
            print(f"[SYNC REQUIRED] {row['competition']} - {row['stage']} vs {row['opponent']}")
            print(f"   Kickoff CDMX: {m_dt_cdmx.strftime('%Y-%m-%d %H:%M')} | Umbral (+4h): {sync_threshold.strftime('%Y-%m-%d %H:%M')}")
            
            try:
                # Execute database cleaner & reload to persist verified stats
                from data_pipeline.data_cleaner import DataCleanerEngine
                cleaner = DataCleanerEngine(db_path)
                cleaner.audit_and_clean_all()
                
                # Update next opponent recent form into SQLite
                seed_opponent_recent_matches(db_path)
                updated_count += 1
                print(f"[SUCCESS] Partido {row['stage']} vs {row['opponent']} sincronizado exitosamente en barca_analytics.db!")
            except Exception as e:
                print(f"[ERROR] Error durante la sincronizacion: {e}")
                # Retry in 4 hours on failure
                next_cron_target_cdmx = now_cdmx + datetime.timedelta(hours=4)
                print(f"[RETRY SCHEDULED] Se programara reintento en 4 horas: {next_cron_target_cdmx.strftime('%Y-%m-%d %H:%M CDMX')}")
                break
        else:
            hours_left = round(time_diff.total_seconds() / 3600, 1)
            print(f"[UPCOMING MATCH] {row['competition']} - {row['stage']} vs {row['opponent']}")
            print(f"   Kickoff CDMX: {m_dt_cdmx.strftime('%Y-%m-%d %H:%M')} | Sincronizacion programada: {sync_threshold.strftime('%Y-%m-%d %H:%M')} (Faltan {hours_left}h)")
            next_cron_target_cdmx = sync_threshold
            break

    # If all due matches are synced and we have a next upcoming match, schedule cron for that match
    if next_cron_target_cdmx is None:
        # Check remaining scheduled matches
        df_fresh = db.get_all_matches_df()
        remaining = df_fresh[(df_fresh['season'] == '2026-27') & (df_fresh['status'] == 'SCHEDULED')].sort_values('date')
        if not remaining.empty:
            r0 = remaining.iloc[0]
            m_date_str = str(r0['date'])
            m_time_str = str(r0['time']) if pd.notna(r0['time']) and str(r0['time']).lower() not in ['nan', 'none', ''] else "21:00"
            try:
                r0_dt_naive = datetime.datetime.strptime(f"{m_date_str} {m_time_str}", "%Y-%m-%d %H:%M")
            except Exception:
                r0_dt_naive = datetime.datetime.strptime(m_date_str, "%Y-%m-%d")
            r0_cdmx = r0_dt_naive.replace(tzinfo=cdmx_tz)
            next_cron_target_cdmx = r0_cdmx + datetime.timedelta(hours=4)

    # Dynamically update the GitHub Actions workflow file
    if next_cron_target_cdmx:
        update_workflow_cron(next_cron_target_cdmx)

    return updated_count

if __name__ == "__main__":
    db_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "barca_analytics.db")
    count = sync_pending_matches_cdmx(db_file)
    print(f"[RESULT] Total partidos sincronizados: {count}")
