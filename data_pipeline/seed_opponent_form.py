import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.schema import Base, get_engine, OpponentRecentMatch
from database.db_manager import DatabaseManager
import datetime

def seed_opponent_recent_matches(db_path="barca_analytics.db"):
    db = DatabaseManager(db_path)
    engine = db.engine
    # Ensure tables exist
    Base.metadata.create_all(engine)

    # Dictionary of opponents and their recent 5 league / cup matches
    # Metrics include: result, team_score, rival_score, xg_for, xg_against, possession, sot_for, sot_against, corners_for, corners_against, fouls_for, fouls_against, yellow_cards_for, yellow_cards_against
    OPPONENT_DATA = {
        "Elche CF": [
            {"date": "2026-08-16", "season": "2026-27", "comp": "LaLiga", "rival": "Real Betis", "home": True, "ts": 1, "rs": 0, "res": "W", "xg_f": 1.45, "xg_a": 0.82, "poss": 48.0, "sot_f": 4, "sot_a": 2, "c_f": 5, "c_a": 4, "f_f": 14, "f_a": 11, "yc_f": 2, "yc_a": 3},
            {"date": "2026-05-24", "season": "2025-26", "comp": "LaLiga", "rival": "RCD Mallorca", "home": False, "ts": 1, "rs": 1, "res": "D", "xg_f": 1.10, "xg_a": 1.25, "poss": 44.0, "sot_f": 3, "sot_a": 4, "c_f": 3, "c_a": 6, "f_f": 12, "f_a": 15, "yc_f": 3, "yc_a": 2},
            {"date": "2026-05-17", "season": "2025-26", "comp": "LaLiga", "rival": "Getafe CF", "home": True, "ts": 2, "rs": 0, "res": "W", "xg_f": 1.80, "xg_a": 0.65, "poss": 52.0, "sot_f": 6, "sot_a": 2, "c_f": 6, "c_a": 3, "f_f": 16, "f_a": 13, "yc_f": 1, "yc_a": 4},
            {"date": "2026-05-10", "season": "2025-26", "comp": "LaLiga", "rival": "Celta de Vigo", "home": False, "ts": 0, "rs": 2, "res": "L", "xg_f": 0.70, "xg_a": 2.10, "poss": 41.0, "sot_f": 2, "sot_a": 7, "c_f": 2, "c_a": 8, "f_f": 10, "f_a": 12, "yc_f": 4, "yc_a": 1},
            {"date": "2026-05-03", "season": "2025-26", "comp": "LaLiga", "rival": "Rayo Vallecano", "home": True, "ts": 1, "rs": 1, "res": "D", "xg_f": 1.20, "xg_a": 1.15, "poss": 49.0, "sot_f": 4, "sot_a": 4, "c_f": 4, "c_a": 5, "f_f": 13, "f_a": 14, "yc_f": 2, "yc_a": 2},
        ],
        "Real Madrid": [
            {"date": "2026-08-16", "season": "2026-27", "comp": "LaLiga", "rival": "Osasuna", "home": True, "ts": 3, "rs": 0, "res": "W", "xg_f": 2.85, "xg_a": 0.45, "poss": 66.0, "sot_f": 8, "sot_a": 2, "c_f": 8, "c_a": 2, "f_f": 15, "f_a": 9, "yc_f": 1, "yc_a": 3},
            {"date": "2026-05-24", "season": "2025-26", "comp": "LaLiga", "rival": "Real Sociedad", "home": True, "ts": 2, "rs": 1, "res": "W", "xg_f": 2.10, "xg_a": 1.05, "poss": 61.0, "sot_f": 7, "sot_a": 3, "c_f": 7, "c_a": 3, "f_f": 13, "f_a": 11, "yc_f": 2, "yc_a": 2},
            {"date": "2026-05-17", "season": "2025-26", "comp": "LaLiga", "rival": "Sevilla FC", "home": False, "ts": 2, "rs": 0, "res": "W", "xg_f": 1.95, "xg_a": 0.85, "poss": 58.0, "sot_f": 6, "sot_a": 3, "c_f": 5, "c_a": 4, "f_f": 16, "f_a": 10, "yc_f": 1, "yc_a": 4},
            {"date": "2026-05-10", "season": "2025-26", "comp": "LaLiga", "rival": "Valencia CF", "home": True, "ts": 4, "rs": 1, "res": "W", "xg_f": 3.20, "xg_a": 0.90, "poss": 64.0, "sot_f": 10, "sot_a": 2, "c_f": 9, "c_a": 2, "f_f": 14, "f_a": 8, "yc_f": 0, "yc_a": 3},
            {"date": "2026-05-03", "season": "2025-26", "comp": "LaLiga", "rival": "Villarreal CF", "home": False, "ts": 1, "rs": 1, "res": "D", "xg_f": 1.55, "xg_a": 1.40, "poss": 56.0, "sot_f": 5, "sot_a": 4, "c_f": 6, "c_a": 5, "f_f": 12, "f_a": 14, "yc_f": 2, "yc_a": 2},
        ],
        "Atlético de Madrid": [
            {"date": "2026-08-15", "season": "2026-27", "comp": "LaLiga", "rival": "Girona FC", "home": True, "ts": 2, "rs": 1, "res": "W", "xg_f": 2.05, "xg_a": 0.95, "poss": 51.0, "sot_f": 6, "sot_a": 3, "c_f": 6, "c_a": 4, "f_f": 15, "f_a": 14, "yc_f": 2, "yc_a": 2},
            {"date": "2026-05-24", "season": "2025-26", "comp": "LaLiga", "rival": "Athletic Club", "home": False, "ts": 1, "rs": 0, "res": "W", "xg_f": 1.35, "xg_a": 1.10, "poss": 47.0, "sot_f": 4, "sot_a": 3, "c_f": 4, "c_a": 7, "f_f": 13, "f_a": 16, "yc_f": 3, "yc_a": 2},
            {"date": "2026-05-17", "season": "2025-26", "comp": "LaLiga", "rival": "Real Betis", "home": True, "ts": 3, "rs": 0, "res": "W", "xg_f": 2.45, "xg_a": 0.60, "poss": 54.0, "sot_f": 7, "sot_a": 2, "c_f": 7, "c_a": 3, "f_f": 14, "f_a": 12, "yc_f": 1, "yc_a": 3},
            {"date": "2026-05-10", "season": "2025-26", "comp": "LaLiga", "rival": "Getafe CF", "home": False, "ts": 1, "rs": 1, "res": "D", "xg_f": 1.15, "xg_a": 1.05, "poss": 53.0, "sot_f": 3, "sot_a": 3, "c_f": 5, "c_a": 4, "f_f": 16, "f_a": 17, "yc_f": 3, "yc_a": 4},
            {"date": "2026-05-03", "season": "2025-26", "comp": "LaLiga", "rival": "RCD Mallorca", "home": True, "ts": 2, "rs": 0, "res": "W", "xg_f": 1.90, "xg_a": 0.50, "poss": 58.0, "sot_f": 6, "sot_a": 1, "c_f": 6, "c_a": 2, "f_f": 11, "f_a": 13, "yc_f": 1, "yc_a": 2},
        ],
        "Athletic Club": [
            {"date": "2026-08-16", "season": "2026-27", "comp": "LaLiga", "rival": "Valencia CF", "home": True, "ts": 2, "rs": 0, "res": "W", "xg_f": 2.15, "xg_a": 0.70, "poss": 55.0, "sot_f": 7, "sot_a": 2, "c_f": 8, "c_a": 3, "f_f": 14, "f_a": 13, "yc_f": 1, "yc_a": 3},
            {"date": "2026-05-24", "season": "2025-26", "comp": "LaLiga", "rival": "Atlético de Madrid", "home": True, "ts": 0, "rs": 1, "res": "L", "xg_f": 1.10, "xg_a": 1.35, "poss": 53.0, "sot_f": 3, "sot_a": 4, "c_f": 7, "c_a": 4, "f_f": 16, "f_a": 13, "yc_f": 2, "yc_a": 3},
            {"date": "2026-05-17", "season": "2025-26", "comp": "LaLiga", "rival": "Deportivo Alavés", "home": False, "ts": 2, "rs": 1, "res": "W", "xg_f": 1.75, "xg_a": 1.20, "poss": 57.0, "sot_f": 5, "sot_a": 3, "c_f": 6, "c_a": 4, "f_f": 12, "f_a": 15, "yc_f": 2, "yc_a": 2},
            {"date": "2026-05-10", "season": "2025-26", "comp": "LaLiga", "rival": "Sevilla FC", "home": True, "ts": 1, "rs": 1, "res": "D", "xg_f": 1.40, "xg_a": 1.30, "poss": 52.0, "sot_f": 4, "sot_a": 4, "c_f": 5, "c_a": 4, "f_f": 15, "f_a": 14, "yc_f": 3, "yc_a": 2},
            {"date": "2026-05-03", "season": "2025-26", "comp": "LaLiga", "rival": "Girona FC", "home": False, "ts": 2, "rs": 1, "res": "W", "xg_f": 1.85, "xg_a": 1.45, "poss": 49.0, "sot_f": 6, "sot_a": 4, "c_f": 5, "c_a": 6, "f_f": 13, "f_a": 12, "yc_f": 1, "yc_a": 2},
        ],
        "Villarreal CF": [
            {"date": "2026-08-16", "season": "2026-27", "comp": "LaLiga", "rival": "Celta de Vigo", "home": True, "ts": 2, "rs": 2, "res": "D", "xg_f": 1.80, "xg_a": 1.70, "poss": 54.0, "sot_f": 6, "sot_a": 5, "c_f": 6, "c_a": 5, "f_f": 13, "f_a": 12, "yc_f": 2, "yc_a": 2},
            {"date": "2026-05-24", "season": "2025-26", "comp": "LaLiga", "rival": "Rayo Vallecano", "home": False, "ts": 3, "rs": 1, "res": "W", "xg_f": 2.30, "xg_a": 1.10, "poss": 56.0, "sot_f": 8, "sot_a": 3, "c_f": 7, "c_a": 4, "f_f": 11, "f_a": 14, "yc_f": 1, "yc_a": 3},
            {"date": "2026-05-17", "season": "2025-26", "comp": "LaLiga", "rival": "Girona FC", "home": True, "ts": 1, "rs": 0, "res": "W", "xg_f": 1.50, "xg_a": 0.85, "poss": 51.0, "sot_f": 5, "sot_a": 2, "c_f": 5, "c_a": 4, "f_f": 14, "f_a": 13, "yc_f": 2, "yc_a": 2},
            {"date": "2026-05-10", "season": "2025-26", "comp": "LaLiga", "rival": "RCD Mallorca", "home": False, "ts": 2, "rs": 0, "res": "W", "xg_f": 1.95, "xg_a": 0.70, "poss": 59.0, "sot_f": 7, "sot_a": 2, "c_f": 6, "c_a": 3, "f_f": 10, "f_a": 15, "yc_f": 1, "yc_a": 3},
            {"date": "2026-05-03", "season": "2025-26", "comp": "LaLiga", "rival": "Real Madrid", "home": True, "ts": 1, "rs": 1, "res": "D", "xg_f": 1.40, "xg_a": 1.55, "poss": 44.0, "sot_f": 4, "sot_a": 5, "c_f": 5, "c_a": 6, "f_f": 14, "f_a": 12, "yc_f": 2, "yc_a": 2},
        ],
        "Sevilla FC": [
            {"date": "2026-08-15", "season": "2026-27", "comp": "LaLiga", "rival": "RCD Espanyol", "home": True, "ts": 1, "rs": 1, "res": "D", "xg_f": 1.40, "xg_a": 1.30, "poss": 53.0, "sot_f": 4, "sot_a": 4, "c_f": 5, "c_a": 4, "f_f": 15, "f_a": 14, "yc_f": 3, "yc_a": 2},
            {"date": "2026-05-24", "season": "2025-26", "comp": "LaLiga", "rival": "Getafe CF", "home": False, "ts": 2, "rs": 1, "res": "W", "xg_f": 1.65, "xg_a": 1.10, "poss": 52.0, "sot_f": 5, "sot_a": 3, "c_f": 4, "c_a": 5, "f_f": 16, "f_a": 17, "yc_f": 2, "yc_a": 4},
            {"date": "2026-05-17", "season": "2025-26", "comp": "LaLiga", "rival": "Real Madrid", "home": True, "ts": 0, "rs": 2, "res": "L", "xg_f": 0.85, "xg_a": 1.95, "poss": 42.0, "sot_f": 3, "sot_a": 6, "c_f": 4, "c_a": 5, "f_f": 10, "f_a": 16, "yc_f": 4, "yc_a": 1},
            {"date": "2026-05-10", "season": "2025-26", "comp": "LaLiga", "rival": "Athletic Club", "home": False, "ts": 1, "rs": 1, "res": "D", "xg_f": 1.30, "xg_a": 1.40, "poss": 48.0, "sot_f": 4, "sot_a": 4, "c_f": 4, "c_a": 5, "f_f": 14, "f_a": 15, "yc_f": 2, "yc_a": 3},
            {"date": "2026-05-03", "season": "2025-26", "comp": "LaLiga", "rival": "Real Sociedad", "home": True, "ts": 2, "rs": 1, "res": "W", "xg_f": 1.70, "xg_a": 1.25, "poss": 50.0, "sot_f": 6, "sot_a": 3, "c_f": 6, "c_a": 4, "f_f": 13, "f_a": 12, "yc_f": 2, "yc_a": 2},
        ],
        "Real Sociedad": [
            {"date": "2026-08-16", "season": "2026-27", "comp": "LaLiga", "rival": "Getafe CF", "home": True, "ts": 1, "rs": 0, "res": "W", "xg_f": 1.60, "xg_a": 0.55, "poss": 62.0, "sot_f": 5, "sot_a": 1, "c_f": 7, "c_a": 2, "f_f": 12, "f_a": 16, "yc_f": 1, "yc_a": 4},
            {"date": "2026-05-24", "season": "2025-26", "comp": "LaLiga", "rival": "Real Madrid", "home": False, "ts": 1, "rs": 2, "res": "L", "xg_f": 1.05, "xg_a": 2.10, "poss": 39.0, "sot_f": 3, "sot_a": 7, "c_f": 3, "c_a": 7, "f_f": 11, "f_a": 13, "yc_f": 2, "yc_a": 2},
            {"date": "2026-05-17", "season": "2025-26", "comp": "LaLiga", "rival": "Valencia CF", "home": True, "ts": 2, "rs": 0, "res": "W", "xg_f": 1.90, "xg_a": 0.60, "poss": 60.0, "sot_f": 6, "sot_a": 2, "c_f": 6, "c_a": 3, "f_f": 13, "f_a": 14, "yc_f": 1, "yc_a": 3},
            {"date": "2026-05-10", "season": "2025-26", "comp": "LaLiga", "rival": "Deportivo Alavés", "home": False, "ts": 1, "rs": 1, "res": "D", "xg_f": 1.20, "xg_a": 1.15, "poss": 58.0, "sot_f": 4, "sot_a": 3, "c_f": 5, "c_a": 4, "f_f": 14, "f_a": 15, "yc_f": 2, "yc_a": 2},
            {"date": "2026-05-03", "season": "2025-26", "comp": "LaLiga", "rival": "Sevilla FC", "home": False, "ts": 1, "rs": 2, "res": "L", "xg_f": 1.25, "xg_a": 1.70, "poss": 50.0, "sot_f": 3, "sot_a": 6, "c_f": 4, "c_a": 6, "f_f": 12, "f_a": 13, "yc_f": 2, "yc_a": 2},
        ],
        "Real Betis": [
            {"date": "2026-08-16", "season": "2026-27", "comp": "LaLiga", "rival": "Elche CF", "home": False, "ts": 0, "rs": 1, "res": "L", "xg_f": 0.82, "xg_a": 1.45, "poss": 52.0, "sot_f": 2, "sot_a": 4, "c_f": 4, "c_a": 5, "f_f": 11, "f_a": 14, "yc_f": 3, "yc_a": 2},
            {"date": "2026-05-24", "season": "2025-26", "comp": "LaLiga", "rival": "Valencia CF", "home": True, "ts": 2, "rs": 1, "res": "W", "xg_f": 1.85, "xg_a": 1.10, "poss": 56.0, "sot_f": 6, "sot_a": 3, "c_f": 6, "c_a": 4, "f_f": 13, "f_a": 14, "yc_f": 1, "yc_a": 3},
            {"date": "2026-05-17", "season": "2025-26", "comp": "LaLiga", "rival": "Atlético de Madrid", "home": False, "ts": 0, "rs": 3, "res": "L", "xg_f": 0.60, "xg_a": 2.45, "poss": 46.0, "sot_f": 2, "sot_a": 7, "c_f": 3, "c_a": 7, "f_f": 12, "f_a": 14, "yc_f": 3, "yc_a": 1},
            {"date": "2026-05-10", "season": "2025-26", "comp": "LaLiga", "rival": "Osasuna", "home": True, "ts": 3, "rs": 1, "res": "W", "xg_f": 2.20, "xg_a": 0.95, "poss": 59.0, "sot_f": 7, "sot_a": 3, "c_f": 7, "c_a": 3, "f_f": 14, "f_a": 12, "yc_f": 2, "yc_a": 2},
            {"date": "2026-05-03", "season": "2025-26", "comp": "LaLiga", "rival": "RCD Espanyol", "home": False, "ts": 1, "rs": 1, "res": "D", "xg_f": 1.30, "xg_a": 1.20, "poss": 54.0, "sot_f": 4, "sot_a": 4, "c_f": 5, "c_a": 5, "f_f": 15, "f_a": 16, "yc_f": 2, "yc_a": 2},
        ],
        "Valencia CF": [
            {"date": "2026-08-16", "season": "2026-27", "comp": "LaLiga", "rival": "Athletic Club", "home": False, "ts": 0, "rs": 2, "res": "L", "xg_f": 0.70, "xg_a": 2.15, "poss": 45.0, "sot_f": 2, "sot_a": 7, "c_f": 3, "c_a": 8, "f_f": 13, "f_a": 14, "yc_f": 3, "yc_a": 1},
            {"date": "2026-05-24", "season": "2025-26", "comp": "LaLiga", "rival": "Real Betis", "home": False, "ts": 1, "rs": 2, "res": "L", "xg_f": 1.10, "xg_a": 1.85, "poss": 44.0, "sot_f": 3, "sot_a": 6, "c_f": 4, "c_a": 6, "f_f": 14, "f_a": 13, "yc_f": 3, "yc_a": 1},
            {"date": "2026-05-17", "season": "2025-26", "comp": "LaLiga", "rival": "Real Sociedad", "home": False, "ts": 0, "rs": 2, "res": "L", "xg_f": 0.60, "xg_a": 1.90, "poss": 40.0, "sot_f": 2, "sot_a": 6, "c_f": 3, "c_a": 6, "f_f": 14, "f_a": 13, "yc_f": 3, "yc_a": 1},
            {"date": "2026-05-10", "season": "2025-26", "comp": "LaLiga", "rival": "Real Madrid", "home": False, "ts": 1, "rs": 4, "res": "L", "xg_f": 0.90, "xg_a": 3.20, "poss": 36.0, "sot_f": 2, "sot_a": 10, "c_f": 2, "c_a": 9, "f_f": 8, "f_a": 14, "yc_f": 3, "yc_a": 0},
            {"date": "2026-05-03", "season": "2025-26", "comp": "LaLiga", "rival": "Getafe CF", "home": True, "ts": 1, "rs": 0, "res": "W", "xg_f": 1.35, "xg_a": 0.80, "poss": 52.0, "sot_f": 4, "sot_a": 2, "c_f": 5, "c_a": 3, "f_f": 15, "f_a": 17, "yc_f": 2, "yc_a": 3},
        ],
        "Girona FC": [
            {"date": "2026-08-15", "season": "2026-27", "comp": "LaLiga", "rival": "Atlético de Madrid", "home": False, "ts": 1, "rs": 2, "res": "L", "xg_f": 0.95, "xg_a": 2.05, "poss": 49.0, "sot_f": 3, "sot_a": 6, "c_f": 4, "c_a": 6, "f_f": 14, "f_a": 15, "yc_f": 2, "yc_a": 2},
            {"date": "2026-05-24", "season": "2025-26", "comp": "LaLiga", "rival": "Deportivo Alavés", "home": True, "ts": 2, "rs": 1, "res": "W", "xg_f": 1.85, "xg_a": 1.10, "poss": 58.0, "sot_f": 6, "sot_a": 3, "c_f": 6, "c_a": 4, "f_f": 12, "f_a": 14, "yc_f": 1, "yc_a": 3},
            {"date": "2026-05-17", "season": "2025-26", "comp": "LaLiga", "rival": "Villarreal CF", "home": False, "ts": 0, "rs": 1, "res": "L", "xg_f": 0.85, "xg_a": 1.50, "poss": 49.0, "sot_f": 2, "sot_a": 5, "c_f": 4, "c_a": 5, "f_f": 13, "f_a": 14, "yc_f": 2, "yc_a": 2},
            {"date": "2026-05-10", "season": "2025-26", "comp": "LaLiga", "rival": "RCD Espanyol", "home": True, "ts": 3, "rs": 1, "res": "W", "xg_f": 2.25, "xg_a": 0.90, "poss": 62.0, "sot_f": 7, "sot_a": 2, "c_f": 7, "c_a": 3, "f_f": 11, "f_a": 16, "yc_f": 1, "yc_a": 3},
            {"date": "2026-05-03", "season": "2025-26", "comp": "LaLiga", "rival": "Athletic Club", "home": True, "ts": 1, "rs": 2, "res": "L", "xg_f": 1.45, "xg_a": 1.85, "poss": 51.0, "sot_f": 4, "sot_a": 6, "c_f": 6, "c_a": 5, "f_f": 12, "f_a": 13, "yc_f": 2, "yc_a": 1},
        ],
        "Newcastle United": [
            {"date": "2026-03-08", "season": "2025-26", "comp": "Champions League", "rival": "FC Barcelona", "home": False, "ts": 1, "rs": 3, "res": "L", "xg_f": 1.10, "xg_a": 2.65, "poss": 38.0, "sot_f": 3, "sot_a": 8, "c_f": 4, "c_a": 7, "f_f": 14, "f_a": 10, "yc_f": 3, "yc_a": 1},
            {"date": "2026-02-24", "season": "2025-26", "comp": "Champions League", "rival": "FC Barcelona", "home": True, "ts": 2, "rs": 5, "res": "L", "xg_f": 1.45, "xg_a": 3.80, "poss": 42.0, "sot_f": 4, "sot_a": 11, "c_f": 5, "c_a": 8, "f_f": 15, "f_a": 9, "yc_f": 4, "yc_a": 2},
            {"date": "2026-01-28", "season": "2025-26", "comp": "Champions League", "rival": "PSV Eindhoven", "home": True, "ts": 3, "rs": 1, "res": "W", "xg_f": 2.30, "xg_a": 1.10, "poss": 55.0, "sot_f": 7, "sot_a": 3, "c_f": 6, "c_a": 4, "f_f": 12, "f_a": 13, "yc_f": 2, "yc_a": 2},
            {"date": "2026-01-21", "season": "2025-26", "comp": "Champions League", "rival": "Juventus", "home": False, "ts": 1, "rs": 1, "res": "D", "xg_f": 1.25, "xg_a": 1.30, "poss": 47.0, "sot_f": 4, "sot_a": 4, "c_f": 4, "c_a": 6, "f_f": 13, "f_a": 12, "yc_f": 2, "yc_a": 2},
            {"date": "2025-12-10", "season": "2025-26", "comp": "Champions League", "rival": "Benfica", "home": True, "ts": 2, "rs": 0, "res": "W", "xg_f": 1.90, "xg_a": 0.75, "poss": 52.0, "sot_f": 6, "sot_a": 2, "c_f": 6, "c_a": 3, "f_f": 11, "f_a": 14, "yc_f": 1, "yc_a": 3},
        ],
        "Manchester City": [
            {"date": "2026-08-23", "season": "2026-27", "comp": "Premier League", "rival": "Ipswich Town", "home": True, "ts": 4, "rs": 1, "res": "W", "xg_f": 3.40, "xg_a": 0.45, "poss": 74.0, "sot_f": 11, "sot_a": 1, "c_f": 12, "c_a": 2, "f_f": 7, "f_a": 12, "yc_f": 1, "yc_a": 3},
            {"date": "2026-08-18", "season": "2026-27", "comp": "Premier League", "rival": "Chelsea FC", "home": False, "ts": 2, "rs": 0, "res": "W", "xg_f": 1.85, "xg_a": 0.95, "poss": 54.0, "sot_f": 5, "sot_a": 3, "c_f": 6, "c_a": 4, "f_f": 9, "f_a": 11, "yc_f": 2, "yc_a": 2},
            {"date": "2026-05-19", "season": "2025-26", "comp": "Premier League", "rival": "West Ham", "home": True, "ts": 3, "rs": 1, "res": "W", "xg_f": 2.90, "xg_a": 0.60, "poss": 72.0, "sot_f": 10, "sot_a": 2, "c_f": 11, "c_a": 1, "f_f": 6, "f_a": 10, "yc_f": 0, "yc_a": 2},
            {"date": "2026-05-14", "season": "2025-26", "comp": "Premier League", "rival": "Tottenham", "home": False, "ts": 2, "rs": 0, "res": "W", "xg_f": 2.10, "xg_a": 1.20, "poss": 53.0, "sot_f": 6, "sot_a": 4, "c_f": 5, "c_a": 6, "f_f": 10, "f_a": 13, "yc_f": 2, "yc_a": 3},
            {"date": "2026-05-11", "season": "2025-26", "comp": "Premier League", "rival": "Fulham FC", "home": False, "ts": 4, "rs": 0, "res": "W", "xg_f": 2.80, "xg_a": 0.35, "poss": 65.0, "sot_f": 8, "sot_a": 1, "c_f": 8, "c_a": 2, "f_f": 8, "f_a": 12, "yc_f": 1, "yc_a": 2},
        ],
        "Paris Saint-Germain": [
            {"date": "2026-08-23", "season": "2026-27", "comp": "Ligue 1", "rival": "Montpellier HSC", "home": True, "ts": 6, "rs": 0, "res": "W", "xg_f": 3.85, "xg_a": 0.40, "poss": 70.0, "sot_f": 12, "sot_a": 1, "c_f": 9, "c_a": 2, "f_f": 8, "f_a": 14, "yc_f": 0, "yc_a": 2},
            {"date": "2026-08-16", "season": "2026-27", "comp": "Ligue 1", "rival": "Le Havre AC", "home": False, "ts": 4, "rs": 1, "res": "W", "xg_f": 2.65, "xg_a": 0.80, "poss": 68.0, "sot_f": 8, "sot_a": 2, "c_f": 7, "c_a": 3, "f_f": 10, "f_a": 15, "yc_f": 1, "yc_a": 3},
            {"date": "2026-05-25", "season": "2025-26", "comp": "Coupe de France", "rival": "Olympique Lyon", "home": True, "ts": 2, "rs": 1, "res": "W", "xg_f": 2.15, "xg_a": 1.10, "poss": 62.0, "sot_f": 7, "sot_a": 3, "c_f": 6, "c_a": 4, "f_f": 11, "f_a": 13, "yc_f": 2, "yc_a": 3},
            {"date": "2026-05-19", "season": "2025-26", "comp": "Ligue 1", "rival": "FC Metz", "home": False, "ts": 2, "rs": 0, "res": "W", "xg_f": 1.95, "xg_a": 0.50, "poss": 64.0, "sot_f": 6, "sot_a": 2, "c_f": 5, "c_a": 3, "f_f": 7, "f_a": 11, "yc_f": 1, "yc_a": 1},
            {"date": "2026-05-15", "season": "2025-26", "comp": "Ligue 1", "rival": "OGC Nice", "home": False, "ts": 2, "rs": 1, "res": "W", "xg_f": 1.70, "xg_a": 1.30, "poss": 57.0, "sot_f": 5, "sot_a": 4, "c_f": 4, "c_a": 5, "f_f": 9, "f_a": 12, "yc_f": 2, "yc_a": 2},
        ],
        "Aston Villa": [
            {"date": "2026-08-24", "season": "2026-27", "comp": "Premier League", "rival": "Arsenal FC", "home": True, "ts": 0, "rs": 2, "res": "L", "xg_f": 1.35, "xg_a": 1.70, "poss": 48.0, "sot_f": 4, "sot_a": 5, "c_f": 5, "c_a": 6, "f_f": 13, "f_a": 12, "yc_f": 3, "yc_a": 2},
            {"date": "2026-08-17", "season": "2026-27", "comp": "Premier League", "rival": "West Ham", "home": False, "ts": 2, "rs": 1, "res": "W", "xg_f": 1.90, "xg_a": 1.15, "poss": 53.0, "sot_f": 6, "sot_a": 3, "c_f": 6, "c_a": 4, "f_f": 11, "f_a": 14, "yc_f": 2, "yc_a": 3},
            {"date": "2026-05-19", "season": "2025-26", "comp": "Premier League", "rival": "Crystal Palace", "home": False, "ts": 0, "rs": 5, "res": "L", "xg_f": 0.80, "xg_a": 3.10, "poss": 51.0, "sot_f": 3, "sot_a": 9, "c_f": 3, "c_a": 8, "f_f": 14, "f_a": 10, "yc_f": 4, "yc_a": 1},
            {"date": "2026-05-13", "season": "2025-26", "comp": "Premier League", "rival": "Liverpool FC", "home": True, "ts": 3, "rs": 3, "res": "D", "xg_f": 2.40, "xg_a": 2.10, "poss": 46.0, "sot_f": 7, "sot_a": 6, "c_f": 6, "c_a": 7, "f_f": 12, "f_a": 11, "yc_f": 2, "yc_a": 2},
            {"date": "2026-05-09", "season": "2025-26", "comp": "Conference League", "rival": "Olympiacos", "home": False, "ts": 0, "rs": 2, "res": "L", "xg_f": 1.10, "xg_a": 1.85, "poss": 60.0, "sot_f": 4, "sot_a": 5, "c_f": 7, "c_a": 3, "f_f": 10, "f_a": 15, "yc_f": 2, "yc_a": 4},
        ],
        "Sporting CP": [
            {"date": "2026-08-23", "season": "2026-27", "comp": "Primeira Liga", "rival": "SC Farense", "home": False, "ts": 5, "rs": 0, "res": "W", "xg_f": 3.50, "xg_a": 0.30, "poss": 66.0, "sot_f": 10, "sot_a": 1, "c_f": 8, "c_a": 2, "f_f": 11, "f_a": 14, "yc_f": 1, "yc_a": 3},
            {"date": "2026-08-17", "season": "2026-27", "comp": "Primeira Liga", "rival": "CD Nacional", "home": False, "ts": 6, "rs": 1, "res": "W", "xg_f": 4.10, "xg_a": 0.85, "poss": 69.0, "sot_f": 12, "sot_a": 2, "c_f": 10, "c_a": 3, "f_f": 9, "f_a": 16, "yc_f": 0, "yc_a": 4},
            {"date": "2026-08-09", "season": "2026-27", "comp": "Primeira Liga", "rival": "Rio Ave FC", "home": True, "ts": 3, "rs": 1, "res": "W", "xg_f": 2.45, "xg_a": 0.70, "poss": 63.0, "sot_f": 7, "sot_a": 2, "c_f": 7, "c_a": 2, "f_f": 12, "f_a": 13, "yc_f": 2, "yc_a": 3},
            {"date": "2026-08-03", "season": "2026-27", "comp": "Supertaça", "rival": "FC Porto", "home": True, "ts": 3, "rs": 4, "res": "L", "xg_f": 2.20, "xg_a": 2.80, "poss": 52.0, "sot_f": 6, "sot_a": 7, "c_f": 5, "c_a": 6, "f_f": 15, "f_a": 18, "yc_f": 3, "yc_a": 4},
            {"date": "2026-05-26", "season": "2025-26", "comp": "Taça de Portugal", "rival": "FC Porto", "home": True, "ts": 1, "rs": 2, "res": "L", "xg_f": 1.30, "xg_a": 1.90, "poss": 49.0, "sot_f": 4, "sot_a": 5, "c_f": 4, "c_a": 5, "f_f": 16, "f_a": 15, "yc_f": 4, "yc_a": 3},
        ],
        "Feyenoord": [
            {"date": "2026-08-25", "season": "2026-27", "comp": "Eredivisie", "rival": "Sparta Rotterdam", "home": False, "ts": 1, "rs": 1, "res": "D", "xg_f": 1.70, "xg_a": 0.90, "poss": 64.0, "sot_f": 5, "sot_a": 3, "c_f": 7, "c_a": 3, "f_f": 10, "f_a": 13, "yc_f": 2, "yc_a": 3},
            {"date": "2026-08-18", "season": "2026-27", "comp": "Eredivisie", "rival": "PEC Zwolle", "home": False, "ts": 5, "rs": 1, "res": "W", "xg_f": 3.20, "xg_a": 0.65, "poss": 67.0, "sot_f": 9, "sot_a": 2, "c_f": 9, "c_a": 2, "f_f": 8, "f_a": 11, "yc_f": 1, "yc_a": 2},
            {"date": "2026-08-10", "season": "2026-27", "comp": "Eredivisie", "rival": "Willem II", "home": True, "ts": 1, "rs": 1, "res": "D", "xg_f": 2.10, "xg_a": 0.80, "poss": 71.0, "sot_f": 6, "sot_a": 2, "c_f": 11, "c_a": 1, "f_f": 9, "f_a": 15, "yc_f": 1, "yc_a": 4},
            {"date": "2026-08-04", "season": "2026-27", "comp": "Johan Cruijff Schaal", "rival": "PSV Eindhoven", "home": False, "ts": 4, "rs": 4, "res": "D", "xg_f": 2.60, "xg_a": 2.70, "poss": 47.0, "sot_f": 7, "sot_a": 8, "c_f": 4, "c_a": 6, "f_f": 14, "f_a": 12, "yc_f": 3, "yc_a": 3},
            {"date": "2026-05-19", "season": "2025-26", "comp": "Eredivisie", "rival": "Excelsior", "home": True, "ts": 4, "rs": 0, "res": "W", "xg_f": 2.95, "xg_a": 0.40, "poss": 68.0, "sot_f": 8, "sot_a": 1, "c_f": 8, "c_a": 2, "f_f": 7, "f_a": 10, "yc_f": 0, "yc_a": 2},
        ],
        "Galatasaray": [
            {"date": "2026-08-25", "season": "2026-27", "comp": "Süper Lig", "rival": "Gaziantep FK", "home": True, "ts": 3, "rs": 1, "res": "W", "xg_f": 2.60, "xg_a": 0.85, "poss": 63.0, "sot_f": 8, "sot_a": 2, "c_f": 7, "c_a": 3, "f_f": 12, "f_a": 14, "yc_f": 2, "yc_a": 3},
            {"date": "2026-08-16", "season": "2026-27", "comp": "Süper Lig", "rival": "Konyaspor", "home": False, "ts": 2, "rs": 1, "res": "W", "xg_f": 1.95, "xg_a": 1.10, "poss": 58.0, "sot_f": 6, "sot_a": 3, "c_f": 5, "c_a": 4, "f_f": 13, "f_a": 15, "yc_f": 3, "yc_a": 2},
            {"date": "2026-08-09", "season": "2026-27", "comp": "Süper Lig", "rival": "Hatayspor", "home": True, "ts": 2, "rs": 1, "res": "W", "xg_f": 2.30, "xg_a": 0.90, "poss": 65.0, "sot_f": 7, "sot_a": 2, "c_f": 8, "c_a": 2, "f_f": 10, "f_a": 16, "yc_f": 1, "yc_a": 4},
            {"date": "2026-08-03", "season": "2026-27", "comp": "Süper Kupa", "rival": "Besiktas", "home": True, "ts": 0, "rs": 5, "res": "L", "xg_f": 1.20, "xg_a": 3.40, "poss": 55.0, "sot_f": 4, "sot_a": 9, "c_f": 6, "c_a": 5, "f_f": 15, "f_a": 14, "yc_f": 3, "yc_a": 2},
            {"date": "2026-05-26", "season": "2025-26", "comp": "Süper Lig", "rival": "Fenerbahce", "home": False, "ts": 1, "rs": 0, "res": "W", "xg_f": 1.45, "xg_a": 1.10, "poss": 48.0, "sot_f": 4, "sot_a": 3, "c_f": 4, "c_a": 5, "f_f": 18, "f_a": 19, "yc_f": 4, "yc_a": 5},
        ],
        "Como 1907": [
            {"date": "2026-08-26", "season": "2026-27", "comp": "Serie A", "rival": "Cagliari Calcio", "home": False, "ts": 1, "rs": 1, "res": "D", "xg_f": 1.30, "xg_a": 1.25, "poss": 52.0, "sot_f": 4, "sot_a": 4, "c_f": 4, "c_a": 5, "f_f": 14, "f_a": 15, "yc_f": 2, "yc_a": 2},
            {"date": "2026-08-19", "season": "2026-27", "comp": "Serie A", "rival": "Juventus", "home": False, "ts": 0, "rs": 3, "res": "L", "xg_f": 0.65, "xg_a": 2.45, "poss": 44.0, "sot_f": 2, "sot_a": 7, "c_f": 3, "c_a": 7, "f_f": 16, "f_a": 11, "yc_f": 4, "yc_a": 1},
            {"date": "2026-08-11", "season": "2026-27", "comp": "Coppa Italia", "rival": "Sampdoria", "home": False, "ts": 1, "rs": 1, "res": "D", "xg_f": 1.50, "xg_a": 1.35, "poss": 56.0, "sot_f": 5, "sot_a": 4, "c_f": 6, "c_a": 4, "f_f": 12, "f_a": 14, "yc_f": 2, "yc_a": 3},
            {"date": "2026-05-10", "season": "2025-26", "comp": "Serie B", "rival": "Cosenza", "home": True, "ts": 1, "rs": 1, "res": "D", "xg_f": 1.60, "xg_a": 0.95, "poss": 60.0, "sot_f": 5, "sot_a": 2, "c_f": 5, "c_a": 2, "f_f": 11, "f_a": 13, "yc_f": 1, "yc_a": 3},
            {"date": "2026-05-05", "season": "2025-26", "comp": "Serie B", "rival": "Modena", "home": False, "ts": 0, "rs": 0, "res": "D", "xg_f": 1.10, "xg_a": 0.85, "poss": 54.0, "sot_f": 3, "sot_a": 2, "c_f": 4, "c_a": 3, "f_f": 13, "f_a": 12, "yc_f": 2, "yc_a": 2},
        ],
        "Sabah": [
            {"date": "2026-08-25", "season": "2026-27", "comp": "Premyer Liqa", "rival": "Sumqayit", "home": True, "ts": 3, "rs": 1, "res": "W", "xg_f": 2.10, "xg_a": 0.80, "poss": 58.0, "sot_f": 6, "sot_a": 2, "c_f": 6, "c_a": 3, "f_f": 11, "f_a": 13, "yc_f": 1, "yc_a": 2},
            {"date": "2026-08-18", "season": "2026-27", "comp": "Premyer Liqa", "rival": "Neftchi Baku", "home": False, "ts": 2, "rs": 0, "res": "W", "xg_f": 1.75, "xg_a": 0.90, "poss": 51.0, "sot_f": 5, "sot_a": 3, "c_f": 4, "c_a": 5, "f_f": 14, "f_a": 12, "yc_f": 2, "yc_a": 3},
            {"date": "2026-08-11", "season": "2026-27", "comp": "Premyer Liqa", "rival": "Qarabag FK", "home": True, "ts": 1, "rs": 2, "res": "L", "xg_f": 1.20, "xg_a": 1.95, "poss": 45.0, "sot_f": 3, "sot_a": 6, "c_f": 4, "c_a": 7, "f_f": 15, "f_a": 10, "yc_f": 3, "yc_a": 2},
            {"date": "2026-08-04", "season": "2026-27", "comp": "Conference League Q", "rival": "St Patrick's", "home": True, "ts": 0, "rs": 1, "res": "L", "xg_f": 1.40, "xg_a": 1.10, "poss": 62.0, "sot_f": 4, "sot_a": 3, "c_f": 7, "c_a": 2, "f_f": 10, "f_a": 14, "yc_f": 2, "yc_a": 4},
            {"date": "2026-07-28", "season": "2026-27", "comp": "Conference League Q", "rival": "Maccabi Haifa", "home": False, "ts": 3, "rs": 6, "res": "L", "xg_f": 2.20, "xg_a": 3.80, "poss": 46.0, "sot_f": 5, "sot_a": 9, "c_f": 3, "c_a": 8, "f_f": 12, "f_a": 11, "yc_f": 2, "yc_a": 2},
        ]
    }

    # Generate synthetic matches for all other opponents so every single team has 5 recent scouted matches
    all_opponents = db.get_opponents()
    total_seeded = 0

    for opp in all_opponents:
        matches = OPPONENT_DATA.get(opp)
        if not matches:
            # Generate 5 realistic league matches for remaining teams
            import random
            random.seed(hash(opp) % 10000)
            matches = []
            sample_rivals = ["Getafe CF", "Osasuna", "RCD Mallorca", "Celta de Vigo", "Rayo Vallecano", "Deportivo Alavés", "RCD Espanyol", "Leganés", "Valladolid", "Las Palmas"]
            for i in range(5):
                ts = random.randint(0, 3)
                rs = random.randint(0, 2)
                res = "W" if ts > rs else ("D" if ts == rs else "L")
                poss = round(random.uniform(42.0, 56.0), 1)
                xg_f = round(ts * 0.75 + random.uniform(0.2, 0.8), 2)
                xg_a = round(rs * 0.70 + random.uniform(0.2, 0.7), 2)
                sot_f = max(ts, random.randint(2, 6))
                sot_a = max(rs, random.randint(1, 5))
                c_f = random.randint(3, 7)
                c_a = random.randint(2, 6)
                f_f = random.randint(10, 16)
                f_a = random.randint(9, 15)
                yc_f = random.randint(1, 3)
                yc_a = random.randint(1, 4)
                
                day = 24 - (i * 7)
                month = "05" if day > 0 else "04"
                m_day = max(1, day)
                d_str = f"2026-{month}-{m_day:02d}"
                rival_name = sample_rivals[i % len(sample_rivals)]
                if rival_name == opp:
                    rival_name = sample_rivals[(i+1) % len(sample_rivals)]
                
                matches.append({
                    "date": d_str,
                    "season": "2025-26",
                    "comp": "LaLiga",
                    "rival": rival_name,
                    "home": (i % 2 == 0),
                    "ts": ts,
                    "rs": rs,
                    "res": res,
                    "xg_f": xg_f,
                    "xg_a": xg_a,
                    "poss": poss,
                    "sot_f": sot_f,
                    "sot_a": sot_a,
                    "c_f": c_f,
                    "c_a": c_a,
                    "f_f": f_f,
                    "f_a": f_a,
                    "yc_f": yc_f,
                    "yc_a": yc_a
                })

        for idx, m in enumerate(matches):
            m_id = f"OPP_{opp.replace(' ', '_')[:10]}_{m['comp'][:3]}_{idx+1}"
            db.insert_or_update_opponent_match({
                "id": m_id,
                "opponent": opp,
                "season": m.get("season", "2025-26"),
                "competition": m.get("comp", "LaLiga"),
                "date": m["date"],
                "matchday": 38 - idx,
                "stage": f"Jornada {38 - idx}",
                "rival": m["rival"],
                "is_home": m["home"],
                "team_score": m["ts"],
                "rival_score": m["rs"],
                "result": m["res"],
                "xg_for": m["xg_f"],
                "xg_against": m["xg_a"],
                "possession": m["poss"],
                "shots_for": m["sot_f"] + 4,
                "shots_against": m["sot_a"] + 4,
                "sot_for": m["sot_f"],
                "sot_against": m["sot_a"],
                "corners_for": m["c_f"],
                "corners_against": m["c_a"],
                "fouls_for": m["f_f"],
                "fouls_against": m["f_a"],
                "yellow_cards_for": m["yc_f"],
                "yellow_cards_against": m["yc_a"],
                "notes": f"Partido previo del {opp} en {m.get('comp', 'LaLiga')}"
            })
            total_seeded += 1

    print(f"[OK] Seeded {total_seeded} opponent recent matches into SQLite database.")
    return total_seeded

if __name__ == "__main__":
    seed_opponent_recent_matches()
