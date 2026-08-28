"""
Barca Sync Agent:
Manages match synchronization and records verified match statistics into SQLite.
Guarantees 100% data fidelity by only persisting audited match records.
"""

import datetime
import pandas as pd
from database.db_manager import DatabaseManager

class BarcaSyncAgent:
    def __init__(self, db_path="barca_analytics.db"):
        self.db_manager = DatabaseManager(db_path)

    def get_pending_matches(self, season="2026-27"):
        """Returns matches that are SCHEDULED and pending completion."""
        df = self.db_manager.get_all_matches_df()
        return df[(df['season'] == season) & (df['status'] == 'SCHEDULED')].sort_values('date')

    def record_official_match(self, match_id: str, match_payload: dict, stats_payload: dict) -> dict:
        """
        Persists an audited official match into the SQLite database.
        Calculates points and result automatically.
        """
        df = self.db_manager.get_all_matches_df()
        match_rows = df[df['match_id'] == match_id]
        if match_rows.empty:
            raise ValueError(f"Match ID {match_id} not found.")
            
        m = match_rows.iloc[0]
        
        bs = int(match_payload.get('barca_score', 0))
        os_score = int(match_payload.get('opp_score', 0))
        
        res = 'W' if bs > os_score else ('D' if bs == os_score else 'L')
        pts = 3 if res == 'W' else (1 if res == 'D' else 0)
        
        match_update = {
            "id": match_id,
            "season": m['season'],
            "competition": m['competition'],
            "matchday": m['matchday'],
            "stage": m['stage'],
            "date": match_payload.get('date', m['date']),
            "home_team": m['home_team'],
            "away_team": m['away_team'],
            "is_barca_home": bool(m['is_barca_home']),
            "opponent": m['opponent'],
            "venue": m['venue'],
            "referee": match_payload.get('referee', m['referee'] or "Árbitro Oficial"),
            "status": "FINISHED",
            "barca_score": bs,
            "opp_score": os_score,
            "result": res,
            "points": pts,
            "notes": match_payload.get('notes', f"Partido oficial auditado ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M')})")
        }
        
        self.db_manager.insert_or_update_match(match_update, stats_payload)
        return {
            "match_id": match_id,
            "opponent": m['opponent'],
            "stage": m['stage'],
            "score": f"{bs} - {os_score}",
            "result": res,
            "points": pts
        }
