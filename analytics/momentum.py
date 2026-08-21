"""
Momentum and Historical Season Progression Engine.
Provides algorithmic calculation of form, cumulative trajectories, and momentum indices.
Zero-token pure analytical computations.
"""

import pandas as pd
import numpy as np

def calculate_momentum_index(row):
    """
    Computes an integrated Momentum Index (0 to 100) for a single match or rolling window.
    Factors:
    - Result (Win=50, Draw=20, Loss=0)
    - xG Dominance: (xG / (xG + xGA + 0.01)) * 30
    - Shot On Target share: (SoT / (SoT + Opp SoT + 0.01)) * 10
    - Possession bonus: (Possession - 50) * 0.2 (up to 10)
    """
    pts_score = 50 if row.get('result') == 'W' else (20 if row.get('result') == 'D' else 0)
    
    xg_for = row.get('barca_xg', 0.0) or 0.0
    xg_against = row.get('opp_xg', 0.0) or 0.0
    xg_factor = (xg_for / (xg_for + xg_against + 0.001)) * 30
    
    sot_for = row.get('barca_shots_on_target', 0) or 0
    sot_against = row.get('opp_shots_on_target', 0) or 0
    sot_factor = (sot_for / (sot_for + sot_against + 0.001)) * 10
    
    poss = row.get('barca_possession', 50.0) or 50.0
    poss_factor = max(0, min(10, (poss - 40) * 0.5))
    
    raw_score = pts_score + xg_factor + sot_factor + poss_factor
    return round(min(100.0, max(0.0, raw_score)), 1)


def get_multi_season_progression(df: pd.DataFrame, competition: str = "LaLiga") -> dict:
    """
    Aligns and prepares progression curves for 2024-25, 2025-26, and 2026-27.
    Returns a dictionary of DataFrames keyed by season, sorted cleanly by matchday.
    """
    seasons = ["2024-25", "2025-26", "2026-27"]
    result = {}
    
    for s in seasons:
        sub = df[(df['season'] == s) & (df['competition'] == competition) & (df['status'] == 'FINISHED')].copy()
        if sub.empty:
            result[s] = pd.DataFrame()
            continue
            
        # Clean sort by official matchday if present, else by date
        if 'matchday' in sub and sub['matchday'].notna().all():
            sub = sub.sort_values('matchday').reset_index(drop=True)
            sub['jornada'] = sub['matchday'].astype(int)
        else:
            sub = sub.sort_values('date').reset_index(drop=True)
            sub['jornada'] = range(1, len(sub) + 1)

        sub['cum_points'] = sub['points'].fillna(0).cumsum()
        sub['cum_goals_for'] = sub['barca_score'].fillna(0).cumsum()
        sub['cum_goals_against'] = sub['opp_score'].fillna(0).cumsum()
        sub['cum_xg_for'] = sub['barca_xg'].fillna(0).cumsum().round(2)
        sub['cum_xg_against'] = sub['opp_xg'].fillna(0).cumsum().round(2)
        sub['cum_xg_diff'] = (sub['barca_xg'].fillna(0) - sub['opp_xg'].fillna(0)).cumsum().round(2)
        
        # Momentum score for each match
        sub['momentum_score'] = sub.apply(calculate_momentum_index, axis=1)
        sub['rolling_momentum_3'] = sub['momentum_score'].rolling(3, min_periods=1).mean().round(1)
        sub['rolling_pts_5'] = sub['points'].fillna(0).rolling(5, min_periods=1).sum()
        
        result[s] = sub
        
    return result
