"""
Data Loader and Seeder Pipeline.
Reads match JSON datasets, validates statistics, and inserts them into SQLite.
"""

import json
import os
from database.db_manager import DatabaseManager

def seed_season_data(matches_list: list, db_path: str = "barca_analytics.db"):
    """
    Takes a list of match dictionaries and populates the SQLite database.
    Each item contains top-level match fields and a 'stats' sub-dictionary.
    """
    db = DatabaseManager(db_path)
    count = 0
    
    for item in matches_list:
        stats_data = item.pop('stats', {})
        match_data = item
        
        # Calculate result and points if finished and not present
        if match_data.get('status') == 'FINISHED' and match_data.get('barca_score') is not None and match_data.get('opp_score') is not None:
            bs = match_data['barca_score']
            os_score = match_data['opp_score']
            if bs > os_score:
                match_data['result'] = 'W'
                match_data['points'] = 3
            elif bs == os_score:
                match_data['result'] = 'D'
                match_data['points'] = 1
            else:
                match_data['result'] = 'L'
                match_data['points'] = 0
        elif match_data.get('status') == 'SCHEDULED':
            match_data['result'] = None
            match_data['points'] = None

        db.insert_or_update_match(match_data, stats_data)
        count += 1
        
    print(f"Successfully loaded {count} matches into {db_path}")
    return count
