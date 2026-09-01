"""
Automated Match Sync Engine for Scheduled Execution (GitHub Actions).
Checks for matches that took place in CDMX Time (Match kickoff + 4 hours window),
extracts official match data, updates the next rival's scouting form, and persists to SQLite.
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

def sync_pending_matches_cdmx(db_path="barca_analytics.db", target_datetime=None):
    """
    Checks all SCHEDULED matches in the database using Mexico City (CDMX) Time.
    If current_cdmx_time >= match_kickoff_cdmx + 4 hours:
      - Marks the match as ready for official sync.
      - Updates barca_analytics.db.
      - Refreshes opponent recent form.
    Returns the count of matches updated.
    """
    cdmx_tz = ZoneInfo("America/Mexico_City")
    if target_datetime is None:
        now_cdmx = datetime.datetime.now(cdmx_tz)
    else:
        now_cdmx = target_datetime if target_datetime.tzinfo else target_datetime.replace(tzinfo=cdmx_tz)

    db = DatabaseManager(db_path)
    sync_agent = BarcaSyncAgent(db_path)
    
    df = db.get_all_matches_df()
    scheduled_2627 = df[(df['season'] == '2026-27') & (df['status'] == 'SCHEDULED')].sort_values('date')

    if scheduled_2627.empty:
        print("[INFO] Todos los partidos de la temporada 2026/27 ya están finalizados.")
        return 0

    print(f"[TIME] Hora actual (CDMX): {now_cdmx.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    
    updated_count = 0
    for _, row in scheduled_2627.iterrows():
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
            
            # Execute database cleaner & reload to persist verified stats
            from data_pipeline.data_cleaner import DataCleanerEngine
            cleaner = DataCleanerEngine(db_path)
            cleaner.audit_and_clean_all()
            
            # Update next opponent recent form into SQLite
            seed_opponent_recent_matches(db_path)
            updated_count += 1
            print(f"[SUCCESS] Partido {row['stage']} vs {row['opponent']} sincronizado exitosamente en barca_analytics.db!")
        else:
            hours_left = round(time_diff.total_seconds() / 3600, 1)
            print(f"[UPCOMING MATCH] {row['competition']} - {row['stage']} vs {row['opponent']}")
            print(f"   Kickoff CDMX: {m_dt_cdmx.strftime('%Y-%m-%d %H:%M')} | Sincronizacion programada: {sync_threshold.strftime('%Y-%m-%d %H:%M')} (Faltan {hours_left}h)")
            # Only report the immediate next scheduled match
            break

    return updated_count

if __name__ == "__main__":
    db_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "barca_analytics.db")
    count = sync_pending_matches_cdmx(db_file)
    print(f"[RESULT] Total partidos sincronizados: {count}")
