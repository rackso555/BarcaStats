"""
Opponent Recent Form and Competition Scouting Engine.
Computes in-depth form metrics for opponents across their last N matches in a specific tournament.
Zero-token pure analytical calculation.
"""

import pandas as pd
import numpy as np

def compute_opponent_recent_form(df_opp_matches: pd.DataFrame, opponent: str, competition: str = "LaLiga", limit: int = 5) -> dict:
    """
    Computes aggregated form metrics and discrete match breakdown for an opponent in a competition.
    Returns:
    - total_matches: int
    - form_pills: list of 'V', 'E', 'D'
    - summary: dict of averages and totals (Goles, xG, Posesión, SoT, Córners, Faltas, Tarjetas)
    - matches_df: DataFrame of individual matches
    """
    if df_opp_matches.empty:
        return {"total_matches": 0, "opponent": opponent, "competition": competition, "matches_df": pd.DataFrame()}

    df = df_opp_matches[
        (df_opp_matches['opponent'].str.lower() == opponent.lower()) & 
        (df_opp_matches['competition'] == competition)
    ].copy()

    if df.empty:
        return {"total_matches": 0, "opponent": opponent, "competition": competition, "matches_df": pd.DataFrame()}

    # Sort descending by date to get most recent matches
    df = df.sort_values('date', ascending=False).head(limit).reset_index(drop=True)
    n = len(df)

    # Form Pills (V: Victoria, E: Empate, D: Derrota)
    pills = []
    wins = 0
    draws = 0
    losses = 0
    for _, r in df.iterrows():
        res = r.get('result', 'W')
        if res == 'W':
            pills.append("<span class='badge-win'>V</span>")
            wins += 1
        elif res == 'D':
            pills.append("<span class='badge-draw'>E</span>")
            draws += 1
        else:
            pills.append("<span class='badge-loss'>D</span>")
            losses += 1

    # Totals & Averages
    gf_total = int(df['team_score'].sum())
    ga_total = int(df['rival_score'].sum())
    gf_avg = round(gf_total / n, 2)
    ga_avg = round(ga_total / n, 2)

    xg_for_avg = round(df['xg_for'].mean(), 2) if 'xg_for' in df else 0.0
    xg_against_avg = round(df['xg_against'].mean(), 2) if 'xg_against' in df else 0.0

    possession_avg = round(df['possession'].mean(), 1) if 'possession' in df else 50.0

    sot_for_total = int(df['sot_for'].sum()) if 'sot_for' in df else 0
    sot_against_total = int(df['sot_against'].sum()) if 'sot_against' in df else 0
    sot_for_avg = round(sot_for_total / n, 1)
    sot_against_avg = round(sot_against_total / n, 1)

    corners_for_total = int(df['corners_for'].sum()) if 'corners_for' in df else 0
    corners_against_total = int(df['corners_against'].sum()) if 'corners_against' in df else 0
    corners_for_avg = round(corners_for_total / n, 1)
    corners_against_avg = round(corners_against_total / n, 1)

    fouls_for_avg = round(df['fouls_for'].mean(), 1) if 'fouls_for' in df else 0.0
    fouls_against_avg = round(df['fouls_against'].mean(), 1) if 'fouls_against' in df else 0.0

    yc_for_total = int(df['yellow_cards_for'].sum()) if 'yellow_cards_for' in df else 0
    yc_against_total = int(df['yellow_cards_against'].sum()) if 'yellow_cards_against' in df else 0
    yc_for_avg = round(yc_for_total / n, 1)
    yc_against_avg = round(yc_against_total / n, 1)

    return {
        "opponent": opponent,
        "competition": competition,
        "total_matches": n,
        "wins": wins,
        "draws": draws,
        "losses": losses,
        "form_pills": pills,
        "summary": {
            "gf_total": gf_total,
            "ga_total": ga_total,
            "gf_avg": gf_avg,
            "ga_avg": ga_avg,
            "xg_for_avg": xg_for_avg,
            "xg_against_avg": xg_against_avg,
            "possession_avg": possession_avg,
            "sot_for_total": sot_for_total,
            "sot_against_total": sot_against_total,
            "sot_for_avg": sot_for_avg,
            "sot_against_avg": sot_against_avg,
            "corners_for_total": corners_for_total,
            "corners_against_total": corners_against_total,
            "corners_for_avg": corners_for_avg,
            "corners_against_avg": corners_against_avg,
            "fouls_for_avg": fouls_for_avg,
            "fouls_against_avg": fouls_against_avg,
            "yc_for_total": yc_for_total,
            "yc_against_total": yc_against_total,
            "yc_for_avg": yc_for_avg,
            "yc_against_avg": yc_against_avg
        },
        "matches_df": df
    }
