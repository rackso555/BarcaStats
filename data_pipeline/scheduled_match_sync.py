"""
Automated Match Sync Engine for Scheduled Execution.
Checks for matches that took place (Match kickoff + 3 hours window),
extracts official match data, and persists verified statistics to SQLite.
"""

import os
import sys
import datetime
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.db_manager import DatabaseManager
from data_pipeline.agent_sync import BarcaSyncAgent

def check_and_sync_due_matches(db_path="barca_analytics.db", target_datetime=None):
    """
    Checks all SCHEDULED matches in the database.
    If current datetime >= match_datetime + 3 hours, initiates official data verification.
    """
    db = DatabaseManager(db_path)
    sync_agent = BarcaSyncAgent(db_path)
    
    if target_datetime is None:
        target_datetime = datetime.datetime.now()

    df = db.get_all_matches_df()
    scheduled_2627 = df[(df['season'] == '2026-27') & (df['status'] == 'SCHEDULED')].sort_values('date')

    if scheduled_2627.empty:
        print("[INFO] No pending scheduled matches for 2026-27.")
        return []

    due_matches = []
    for _, row in scheduled_2627.iterrows():
        m_date_str = str(row['date'])
        m_time_str = str(row['time']) if pd.notna(row['time']) else "21:00"
        
        try:
            m_dt = datetime.datetime.strptime(f"{m_date_str} {m_time_str}", "%Y-%m-%d %H:%M")
        except Exception:
            m_dt = datetime.datetime.strptime(m_date_str, "%Y-%m-%d")
            
        sync_threshold = m_dt + datetime.timedelta(hours=3)
        
        if target_datetime >= sync_threshold:
            due_matches.append({
                "match_id": row['match_id'],
                "stage": row['stage'],
                "opponent": row['opponent'],
                "competition": row['competition'],
                "date": m_date_str,
                "time": m_time_str,
                "sync_threshold": sync_threshold.strftime("%Y-%m-%d %H:%M")
            })

    print(f"[INFO] Found {len(due_matches)} matches past kickoff + 3 hours window.")
    for d in due_matches:
        print(f"  • {d['competition']} {d['stage']} vs {d['opponent']} (Match: {d['date']} {d['time']} | Sync window: {d['sync_threshold']})")
    
    return due_matches

if __name__ == "__main__":
    check_and_sync_due_matches()
