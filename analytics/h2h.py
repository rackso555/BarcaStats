"""
Head-to-Head (H2H) and Opponent Scouting Analytics Engine.
Calculates historical performance, dominance metrics, and tactical trends vs specific opponents.
Strictly filters for FINISHED matches.
"""

import pandas as pd
import numpy as np

def calculate_h2h_summary(df_matches: pd.DataFrame, opponent: str) -> dict:
    """
    Computes comprehensive H2H statistics against a specific opponent using FINISHED matches only.
    """
    matches = df_matches[
        (df_matches['opponent'].str.lower() == opponent.lower()) & 
        (df_matches['status'] == 'FINISHED')
    ].copy()
    
    if matches.empty:
        return {"total_matches": 0, "opponent": opponent, "matches_df": pd.DataFrame(), "wins": 0, "draws": 0, "losses": 0}
    
    # Sort matches by date descending (most recent first)
    matches = matches.sort_values('date', ascending=False).reset_index(drop=True)
    
    total = len(matches)
    wins = len(matches[matches['result'] == 'W'])
    draws = len(matches[matches['result'] == 'D'])
    losses = len(matches[matches['result'] == 'L'])
    
    goals_for = matches['barca_score'].sum()
    goals_against = matches['opp_score'].sum()
    
    avg_possession = matches['barca_possession'].mean() if 'barca_possession' in matches else 50.0
    avg_xg_for = matches['barca_xg'].mean() if 'barca_xg' in matches else 0.0
    avg_xg_against = matches['opp_xg'].mean() if 'opp_xg' in matches else 0.0
    
    avg_shots_for = matches['barca_shots'].mean() if 'barca_shots' in matches else 0.0
    avg_shots_on_target = matches['barca_shots_on_target'].mean() if 'barca_shots_on_target' in matches else 0.0
    avg_corners_for = matches['barca_corners'].mean() if 'barca_corners' in matches else 0.0
    avg_corners_against = matches['opp_corners'].mean() if 'opp_corners' in matches else 0.0
    
    avg_fouls_committed = matches['barca_fouls'].mean() if 'barca_fouls' in matches else 0.0
    avg_fouls_received = matches['opp_fouls'].mean() if 'opp_fouls' in matches else 0.0
    total_yellows = matches['barca_yellow_cards'].sum() if 'barca_yellow_cards' in matches else 0
    total_reds = matches['barca_red_cards'].sum() if 'barca_red_cards' in matches else 0
    
    home_matches = matches[matches['is_barca_home'] == True]
    away_matches = matches[matches['is_barca_home'] == False]
    
    return {
        "opponent": opponent,
        "total_matches": total,
        "matches_df": matches,
        "wins": wins,
        "draws": draws,
        "losses": losses,
        "win_rate": round((wins / total) * 100, 1) if total > 0 else 0,
        "goals_for": int(goals_for),
        "goals_against": int(goals_against),
        "goal_diff": int(goals_for - goals_against),
        "avg_possession": round(float(avg_possession), 1),
        "avg_xg_for": round(float(avg_xg_for), 2),
        "avg_xg_against": round(float(avg_xg_against), 2),
        "avg_shots_for": round(float(avg_shots_for), 1),
        "avg_shots_on_target": round(float(avg_shots_on_target), 1),
        "avg_corners_for": round(float(avg_corners_for), 1),
        "avg_corners_against": round(float(avg_corners_against), 1),
        "avg_fouls_committed": round(float(avg_fouls_committed), 1),
        "avg_fouls_received": round(float(avg_fouls_received), 1),
        "total_yellows": int(total_yellows),
        "total_reds": int(total_reds),
        "home_record": {
            "matches": len(home_matches),
            "wins": len(home_matches[home_matches['result'] == 'W']),
            "draws": len(home_matches[home_matches['result'] == 'D']),
            "losses": len(home_matches[home_matches['result'] == 'L'])
        },
        "away_record": {
            "matches": len(away_matches),
            "wins": len(away_matches[away_matches['result'] == 'W']),
            "draws": len(away_matches[away_matches['result'] == 'D']),
            "losses": len(away_matches[away_matches['result'] == 'L'])
        }
    }
