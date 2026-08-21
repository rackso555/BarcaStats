"""
Radar Chart and Tactical Multi-dimensional Profiling Engine.
Computes tactical metrics, total points, points per match, and 360-degree radar benchmarks.
"""

import pandas as pd
import numpy as np

def compute_team_radar_metrics(df_matches: pd.DataFrame, season: str = None, competition: str = None) -> dict:
    """
    Computes normalized tactical radar metrics (0 to 100), total points, and PPG for a given filter.
    Categories:
    - Eficacia Goleadora (Goles/partido)
    - Generación xG (xG/partido)
    - Tiros a Puerta (SoT/partido)
    - Posesión %
    - Precisión de Pase %
    - Solidez Defensiva (xGA invertido)
    - Córners a Favor
    - Intensidad Ofensiva (Faltas provocadas)
    """
    df = df_matches.copy()
    if season and season != "Todas":
        df = df[df['season'] == season]
    if competition and competition != "Todas":
        df = df[df['competition'] == competition]
        
    finished_df = df[df['status'] == 'FINISHED']
    if finished_df.empty:
        return {}

    n = len(finished_df)
    
    # Points metrics
    total_points = int(finished_df['points'].fillna(0).sum())
    points_per_match = round(finished_df['points'].fillna(0).mean(), 2)
    
    # Raw averages
    goals_per_match = finished_df['barca_score'].mean()
    xg_per_match = finished_df['barca_xg'].mean()
    sot_per_match = finished_df['barca_shots_on_target'].mean()
    possession = finished_df['barca_possession'].mean()
    pass_acc = finished_df['barca_pass_acc'].mean()
    xga_per_match = finished_df['opp_xg'].mean()
    sot_conceded = finished_df['opp_shots_on_target'].mean()
    corners_per_match = finished_df['barca_corners'].mean()
    fouls_suffered = finished_df['opp_fouls'].mean()
    
    # Benchmarked 0-100 scores
    score_goals = min(100, (goals_per_match / 3.5) * 100)
    score_xg = min(100, (xg_per_match / 3.0) * 100)
    score_sot = min(100, (sot_per_match / 9.0) * 100)
    score_poss = min(100, max(0, (possession - 30) / 45 * 100))
    score_pass = min(100, max(0, (pass_acc - 60) / 35 * 100))
    score_defense_xg = max(0, 100 - (xga_per_match / 2.5 * 100))
    score_defense_sot = max(0, 100 - (sot_conceded / 6.0 * 100))
    score_corners = min(100, (corners_per_match / 9.0) * 100)
    score_intensity = min(100, (fouls_suffered / 18.0) * 100)

    categories = [
        'Eficacia Goleadora',
        'Generación xG',
        'Tiros a Puerta',
        'Posesión %',
        'Precisión de Pase',
        'Solidez Def. (xGA)',
        'Córners a Favor',
        'Intensidad Ofensiva'
    ]

    values = [
        round(score_goals, 1),
        round(score_xg, 1),
        round(score_sot, 1),
        round(score_poss, 1),
        round(score_pass, 1),
        round(score_defense_xg, 1),
        round(score_corners, 1),
        round(score_intensity, 1)
    ]

    return {
        "categories": categories,
        "values": values,
        "raw_stats": {
            "total_points": total_points,
            "points_per_match": points_per_match,
            "goals_per_match": round(goals_per_match, 2),
            "xg_per_match": round(xg_per_match, 2),
            "sot_per_match": round(sot_per_match, 2),
            "possession": round(possession, 1),
            "pass_acc": round(pass_acc, 1),
            "xga_per_match": round(xga_per_match, 2),
            "corners_per_match": round(corners_per_match, 2),
            "matches_count": n
        }
    }
