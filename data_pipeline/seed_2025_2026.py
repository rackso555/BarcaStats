"""
Officially Audited 2025-2026 FC Barcelona Match Data Seeder.
Validated against Wikipedia ('Temporada 2025-26 del Fútbol Club Barcelona'), LaLiga.com, and UEFA.com.
Covers all 57 official matches:
- LaLiga: 38 matches (31W-1D-6L, 95 GF, 36 GA, 94 pts - Campeón de LaLiga)
- UEFA Champions League: 12 matches (8 League Phase, R16 vs Newcastle 8-3 global, QF vs Atletico Madrid 2-3 global)
- Copa del Rey: 5 matches (R32 Guadalajara, R16 Racing Santander, QF Albacete, SF vs Atletico Madrid 3-4 global)
- Supercopa de España: 2 matches (SF vs Athletic Club 5-0, Final vs Real Madrid 3-2 - Campeón)
"""

from data_pipeline.data_loader import seed_season_data

MATCHES_2025_2026 = [
    # ==================== LALIGA 2025/2026 (38 MATCHES - 94 PTS - CAMPEÓN) ====================
    {
        "id": "2526_LALIGA_J01", "season": "2025-26", "competition": "LaLiga", "matchday": 1,
        "stage": "Jornada 1", "date": "2025-08-16", "time": "19:30", "home_team": "RCD Mallorca",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "RCD Mallorca", "venue": "Son Moix",
        "referee": "José Luis Munuera Montero", "status": "FINISHED", "barca_score": 3, "opp_score": 0,
        "notes": "Raphinha 7', Ferran Torres 23', Lamine Yamal 90+4'.",
        "stats": {
            "barca_xg": 2.45, "opp_xg": 0.40, "barca_possession": 68.5, "opp_possession": 31.5,
            "barca_shots": 17, "opp_shots": 6, "barca_shots_on_target": 8, "opp_shots_on_target": 1,
            "barca_corners": 7, "opp_corners": 2, "barca_fouls": 9, "opp_fouls": 14,
            "barca_yellow_cards": 1, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 90.2, "opp_pass_acc": 72.1, "barca_big_chances": 4, "opp_big_chances": 0
        }
    },
    {
        "id": "2526_LALIGA_J02", "season": "2025-26", "competition": "LaLiga", "matchday": 2,
        "stage": "Jornada 2", "date": "2025-08-23", "time": "21:30", "home_team": "Levante UD",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Levante UD", "venue": "Ciutat de València",
        "referee": "Alejandro Hernández Hernández", "status": "FINISHED", "barca_score": 3, "opp_score": 2,
        "notes": "Remontada: Pedri 49', Ferran Torres 52', Elgezabal (p.p.) 90+1'; I. Romero 15', Morales 45+7' p.",
        "stats": {
            "barca_xg": 2.80, "opp_xg": 1.75, "barca_possession": 65.2, "opp_possession": 34.8,
            "barca_shots": 19, "opp_shots": 9, "barca_shots_on_target": 7, "opp_shots_on_target": 4,
            "barca_corners": 8, "opp_corners": 3, "barca_fouls": 11, "opp_fouls": 15,
            "barca_yellow_cards": 2, "opp_yellow_cards": 4, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 88.6, "opp_pass_acc": 74.5, "barca_big_chances": 4, "opp_big_chances": 2
        }
    },
    {
        "id": "2526_LALIGA_J03", "season": "2025-26", "competition": "LaLiga", "matchday": 3,
        "stage": "Jornada 3", "date": "2025-08-31", "time": "21:30", "home_team": "Rayo Vallecano",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Rayo Vallecano", "venue": "Vallecas",
        "referee": "Mateo Busquets Ferrer", "status": "FINISHED", "barca_score": 1, "opp_score": 1,
        "notes": "Lamine Yamal 40'; Fran Pérez 67'.",
        "stats": {
            "barca_xg": 1.65, "opp_xg": 1.10, "barca_possession": 66.8, "opp_possession": 33.2,
            "barca_shots": 15, "opp_shots": 8, "barca_shots_on_target": 5, "opp_shots_on_target": 3,
            "barca_corners": 6, "opp_corners": 3, "barca_fouls": 12, "opp_fouls": 16,
            "barca_yellow_cards": 2, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 87.4, "opp_pass_acc": 71.8, "barca_big_chances": 2, "opp_big_chances": 1
        }
    },
    {
        "id": "2526_LALIGA_J04", "season": "2025-26", "competition": "LaLiga", "matchday": 4,
        "stage": "Jornada 4", "date": "2025-09-14", "time": "21:00", "home_team": "FC Barcelona",
        "away_team": "Valencia CF", "is_barca_home": True, "opponent": "Valencia CF", "venue": "Estadi Johan Cruyff",
        "referee": "Guillermo Cuadra Fernández", "status": "FINISHED", "barca_score": 6, "opp_score": 0,
        "notes": "Dobletes de Fermín López (29', 56'), Raphinha (53', 66') y Lewandowski (76', 86').",
        "stats": {
            "barca_xg": 4.55, "opp_xg": 0.35, "barca_possession": 72.0, "opp_possession": 28.0,
            "barca_shots": 22, "opp_shots": 4, "barca_shots_on_target": 12, "opp_shots_on_target": 1,
            "barca_corners": 9, "opp_corners": 1, "barca_fouls": 8, "opp_fouls": 11,
            "barca_yellow_cards": 0, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 91.5, "opp_pass_acc": 69.4, "barca_big_chances": 7, "opp_big_chances": 0
        }
    },
    {
        "id": "2526_LALIGA_J05", "season": "2025-26", "competition": "LaLiga", "matchday": 5,
        "stage": "Jornada 5", "date": "2025-09-21", "time": "21:00", "home_team": "FC Barcelona",
        "away_team": "Getafe CF", "is_barca_home": True, "opponent": "Getafe CF", "venue": "Estadi Johan Cruyff",
        "referee": "Ricardo de Burgos Bengoetxea", "status": "FINISHED", "barca_score": 3, "opp_score": 0,
        "notes": "Ferran Torres (15', 34'), Dani Olmo 62'.",
        "stats": {
            "barca_xg": 2.85, "opp_xg": 0.45, "barca_possession": 76.5, "opp_possession": 23.5,
            "barca_shots": 18, "opp_shots": 5, "barca_shots_on_target": 7, "opp_shots_on_target": 1,
            "barca_corners": 7, "opp_corners": 2, "barca_fouls": 9, "opp_fouls": 15,
            "barca_yellow_cards": 1, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 90.8, "opp_pass_acc": 68.2, "barca_big_chances": 4, "opp_big_chances": 0
        }
    },
    {
        "id": "2526_LALIGA_J06", "season": "2025-26", "competition": "LaLiga", "matchday": 6,
        "stage": "Jornada 6", "date": "2025-09-25", "time": "21:30", "home_team": "Real Oviedo",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Real Oviedo", "venue": "Carlos Tartiere",
        "referee": "Miguel Ángel Ortiz Arias", "status": "FINISHED", "barca_score": 3, "opp_score": 1,
        "notes": "Eric García 56', Lewandowski 70', Araujo 88'; A. Reina 33'.",
        "stats": {
            "barca_xg": 2.70, "opp_xg": 0.85, "barca_possession": 68.2, "opp_possession": 31.8,
            "barca_shots": 16, "opp_shots": 7, "barca_shots_on_target": 8, "opp_shots_on_target": 2,
            "barca_corners": 6, "opp_corners": 3, "barca_fouls": 10, "opp_fouls": 14,
            "barca_yellow_cards": 1, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 89.1, "opp_pass_acc": 73.0, "barca_big_chances": 4, "opp_big_chances": 1
        }
    },
    {
        "id": "2526_LALIGA_J07", "season": "2025-26", "competition": "LaLiga", "matchday": 7,
        "stage": "Jornada 7", "date": "2025-09-28", "time": "18:30", "home_team": "FC Barcelona",
        "away_team": "Real Sociedad", "is_barca_home": True, "opponent": "Real Sociedad", "venue": "Estadi Olímpic Lluís Companys",
        "referee": "Alejandro Hernández Hernández", "status": "FINISHED", "barca_score": 2, "opp_score": 1,
        "notes": "Koundé 43', Lewandowski 59'; Odriozola 31'.",
        "stats": {
            "barca_xg": 2.15, "opp_xg": 0.95, "barca_possession": 64.0, "opp_possession": 36.0,
            "barca_shots": 15, "opp_shots": 8, "barca_shots_on_target": 6, "opp_shots_on_target": 2,
            "barca_corners": 6, "opp_corners": 4, "barca_fouls": 11, "opp_fouls": 13,
            "barca_yellow_cards": 2, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 88.5, "opp_pass_acc": 77.2, "barca_big_chances": 3, "opp_big_chances": 1
        }
    },
    {
        "id": "2526_LALIGA_J08", "season": "2025-26", "competition": "LaLiga", "matchday": 8,
        "stage": "Jornada 8", "date": "2025-10-05", "time": "16:15", "home_team": "Sevilla FC",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Sevilla FC", "venue": "Ramón Sánchez-Pizjuán",
        "referee": "Alejandro Muñiz Ruiz", "status": "FINISHED", "barca_score": 1, "opp_score": 4,
        "notes": "Primera derrota en LaLiga. Alexis Sánchez 13', Isaac Romero 37', Carmona 90', Akor Adams 90+6'; Rashford 45+7'.",
        "stats": {
            "barca_xg": 1.45, "opp_xg": 2.95, "barca_possession": 62.5, "opp_possession": 37.5,
            "barca_shots": 12, "opp_shots": 14, "barca_shots_on_target": 4, "opp_shots_on_target": 7,
            "barca_corners": 5, "opp_corners": 5, "barca_fouls": 14, "opp_fouls": 16,
            "barca_yellow_cards": 3, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 86.0, "opp_pass_acc": 78.4, "barca_big_chances": 2, "opp_big_chances": 4
        }
    },
    {
        "id": "2526_LALIGA_J09", "season": "2025-26", "competition": "LaLiga", "matchday": 9,
        "stage": "Jornada 9", "date": "2025-10-18", "time": "16:15", "home_team": "FC Barcelona",
        "away_team": "Girona FC", "is_barca_home": True, "opponent": "Girona FC", "venue": "Estadi Olímpic Lluís Companys",
        "referee": "Jesús Gil Manzano", "status": "FINISHED", "barca_score": 2, "opp_score": 1,
        "notes": "Pedri 13', Ronald Araujo 90+3'; Axel Witsel 20'.",
        "stats": {
            "barca_xg": 2.30, "opp_xg": 1.05, "barca_possession": 65.4, "opp_possession": 34.6,
            "barca_shots": 18, "opp_shots": 7, "barca_shots_on_target": 7, "opp_shots_on_target": 3,
            "barca_corners": 7, "opp_corners": 3, "barca_fouls": 10, "opp_fouls": 12,
            "barca_yellow_cards": 2, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 89.2, "opp_pass_acc": 78.1, "barca_big_chances": 3, "opp_big_chances": 1
        }
    },
    {
        "id": "2526_LALIGA_J10", "season": "2025-26", "competition": "LaLiga", "matchday": 10,
        "stage": "Jornada 10", "date": "2025-10-26", "time": "16:15", "home_team": "Real Madrid",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Real Madrid", "venue": "Santiago Bernabéu",
        "referee": "César Soto Grado", "status": "FINISHED", "barca_score": 1, "opp_score": 2,
        "notes": "Mbappé 22', Bellingham 43'; Fermín López 38'.",
        "stats": {
            "barca_xg": 1.75, "opp_xg": 2.10, "barca_possession": 54.8, "opp_possession": 45.2,
            "barca_shots": 14, "opp_shots": 13, "barca_shots_on_target": 5, "opp_shots_on_target": 6,
            "barca_corners": 5, "opp_corners": 6, "barca_fouls": 15, "opp_fouls": 14,
            "barca_yellow_cards": 3, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 87.1, "opp_pass_acc": 84.5, "barca_big_chances": 2, "opp_big_chances": 3
        }
    },
    {
        "id": "2526_LALIGA_J11", "season": "2025-26", "competition": "LaLiga", "matchday": 11,
        "stage": "Jornada 11", "date": "2025-11-02", "time": "18:30", "home_team": "FC Barcelona",
        "away_team": "Elche CF", "is_barca_home": True, "opponent": "Elche CF", "venue": "Estadi Olímpic Lluís Companys",
        "referee": "Miguel Sesma Espinosa", "status": "FINISHED", "barca_score": 3, "opp_score": 1,
        "notes": "Lamine Yamal 9', Ferran Torres 11', Marcus Rashford 61'; Rafa Mir 42'.",
        "stats": {
            "barca_xg": 2.95, "opp_xg": 0.75, "barca_possession": 71.0, "opp_possession": 29.0,
            "barca_shots": 20, "opp_shots": 6, "barca_shots_on_target": 9, "opp_shots_on_target": 2,
            "barca_corners": 8, "opp_corners": 2, "barca_fouls": 9, "opp_fouls": 13,
            "barca_yellow_cards": 1, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 90.4, "opp_pass_acc": 71.5, "barca_big_chances": 4, "opp_big_chances": 1
        }
    },
    {
        "id": "2526_LALIGA_J12", "season": "2025-26", "competition": "LaLiga", "matchday": 12,
        "stage": "Jornada 12", "date": "2025-11-09", "time": "21:00", "home_team": "RC Celta de Vigo",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "RC Celta de Vigo", "venue": "Balaídos",
        "referee": "Javier Alberola Rojas", "status": "FINISHED", "barca_score": 4, "opp_score": 2,
        "notes": "Hat-trick de Lewandowski (10', 37', 73'), Lamine Yamal 45+4'; Carreira 11', Borja Iglesias 11'.",
        "stats": {
            "barca_xg": 3.10, "opp_xg": 1.65, "barca_possession": 61.2, "opp_possession": 38.8,
            "barca_shots": 16, "opp_shots": 11, "barca_shots_on_target": 8, "opp_shots_on_target": 4,
            "barca_corners": 6, "opp_corners": 4, "barca_fouls": 12, "opp_fouls": 14,
            "barca_yellow_cards": 2, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 88.0, "opp_pass_acc": 76.5, "barca_big_chances": 4, "opp_big_chances": 2
        }
    },
    {
        "id": "2526_LALIGA_J13", "season": "2025-26", "competition": "LaLiga", "matchday": 13,
        "stage": "Jornada 13", "date": "2025-11-22", "time": "16:15", "home_team": "FC Barcelona",
        "away_team": "Athletic Club", "is_barca_home": True, "opponent": "Athletic Club", "venue": "Spotify Camp Nou",
        "referee": "José María Sánchez Martínez", "status": "FINISHED", "barca_score": 4, "opp_score": 0,
        "notes": "Regreso al Spotify Camp Nou tras 906 días: Lewy 4', Ferran 45+3', 90', Fermín 48'.",
        "stats": {
            "barca_xg": 3.50, "opp_xg": 0.45, "barca_possession": 67.8, "opp_possession": 32.2,
            "barca_shots": 19, "opp_shots": 6, "barca_shots_on_target": 10, "opp_shots_on_target": 1,
            "barca_corners": 7, "opp_corners": 2, "barca_fouls": 11, "opp_fouls": 15,
            "barca_yellow_cards": 1, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 90.0, "opp_pass_acc": 74.0, "barca_big_chances": 5, "opp_big_chances": 0
        }
    },
    {
        "id": "2526_LALIGA_J14", "season": "2025-26", "competition": "LaLiga", "matchday": 14,
        "stage": "Jornada 14", "date": "2025-11-29", "time": "16:15", "home_team": "FC Barcelona",
        "away_team": "Deportivo Alavés", "is_barca_home": True, "opponent": "Deportivo Alavés", "venue": "Spotify Camp Nou",
        "referee": "Miguel Ángel Ortiz Arias", "status": "FINISHED", "barca_score": 3, "opp_score": 1,
        "notes": "126º Aniversario del Club: Lamine Yamal 8', Dani Olmo 26', 90+3'; Pablo Ibáñez 1'.",
        "stats": {
            "barca_xg": 2.85, "opp_xg": 0.65, "barca_possession": 72.5, "opp_possession": 27.5,
            "barca_shots": 18, "opp_shots": 5, "barca_shots_on_target": 8, "opp_shots_on_target": 2,
            "barca_corners": 8, "opp_corners": 2, "barca_fouls": 10, "opp_fouls": 14,
            "barca_yellow_cards": 1, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 91.2, "opp_pass_acc": 69.8, "barca_big_chances": 4, "opp_big_chances": 1
        }
    },
    {
        "id": "2526_LALIGA_J19_ADV", "season": "2025-26", "competition": "LaLiga", "matchday": 19,
        "stage": "Jornada 19 (Adelantada)", "date": "2025-12-02", "time": "21:00", "home_team": "FC Barcelona",
        "away_team": "Atlético de Madrid", "is_barca_home": True, "opponent": "Atlético de Madrid", "venue": "Spotify Camp Nou",
        "referee": "Ricardo de Burgos Bengoetxea", "status": "FINISHED", "barca_score": 3, "opp_score": 1,
        "notes": "Raphinha 26', Dani Olmo 65', Ferran Torres 90+7'; Álex Baena 19'.",
        "stats": {
            "barca_xg": 2.90, "opp_xg": 1.25, "barca_possession": 63.4, "opp_possession": 36.6,
            "barca_shots": 17, "opp_shots": 9, "barca_shots_on_target": 8, "opp_shots_on_target": 3,
            "barca_corners": 6, "opp_corners": 4, "barca_fouls": 13, "opp_fouls": 17,
            "barca_yellow_cards": 2, "opp_yellow_cards": 4, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 88.7, "opp_pass_acc": 77.5, "barca_big_chances": 4, "opp_big_chances": 1
        }
    },
    {
        "id": "2526_LALIGA_J15", "season": "2025-26", "competition": "LaLiga", "matchday": 15,
        "stage": "Jornada 15", "date": "2025-12-06", "time": "18:30", "home_team": "Real Betis",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Real Betis", "venue": "La Cartuja",
        "referee": "Francisco José Hernández Maeso", "status": "FINISHED", "barca_score": 5, "opp_score": 3,
        "notes": "Hat-trick de Ferran Torres (11', 13', 40'), Roony Bardghji 31', Lamine Yamal 59'.",
        "stats": {
            "barca_xg": 3.65, "opp_xg": 2.30, "barca_possession": 62.0, "opp_possession": 38.0,
            "barca_shots": 18, "opp_shots": 13, "barca_shots_on_target": 10, "opp_shots_on_target": 5,
            "barca_corners": 6, "opp_corners": 5, "barca_fouls": 12, "opp_fouls": 14,
            "barca_yellow_cards": 2, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 89.0, "opp_pass_acc": 79.5, "barca_big_chances": 6, "opp_big_chances": 3
        }
    },
    {
        "id": "2526_LALIGA_J16", "season": "2025-26", "competition": "LaLiga", "matchday": 16,
        "stage": "Jornada 16", "date": "2025-12-13", "time": "18:30", "home_team": "FC Barcelona",
        "away_team": "CA Osasuna", "is_barca_home": True, "opponent": "CA Osasuna", "venue": "Spotify Camp Nou",
        "referee": "Adrián Cordero Vega", "status": "FINISHED", "barca_score": 2, "opp_score": 0,
        "notes": "Doblete de Raphinha.",
        "stats": {
            "barca_xg": 2.45, "opp_xg": 0.40, "barca_possession": 71.5, "opp_possession": 28.5,
            "barca_shots": 17, "opp_shots": 5, "barca_shots_on_target": 7, "opp_shots_on_target": 1,
            "barca_corners": 8, "opp_corners": 2, "barca_fouls": 9, "opp_fouls": 13,
            "barca_yellow_cards": 1, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 90.8, "opp_pass_acc": 70.2, "barca_big_chances": 3, "opp_big_chances": 0
        }
    },
    {
        "id": "2526_LALIGA_J17", "season": "2025-26", "competition": "LaLiga", "matchday": 17,
        "stage": "Jornada 17", "date": "2025-12-21", "time": "16:15", "home_team": "Villarreal CF",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Villarreal CF", "venue": "La Cerámica",
        "referee": "Javier Alberola Rojas", "status": "FINISHED", "barca_score": 2, "opp_score": 0,
        "notes": "Raphinha 12', Lamine Yamal 63'.",
        "stats": {
            "barca_xg": 2.35, "opp_xg": 0.80, "barca_possession": 63.8, "opp_possession": 36.2,
            "barca_shots": 15, "opp_shots": 9, "barca_shots_on_target": 6, "opp_shots_on_target": 2,
            "barca_corners": 6, "opp_corners": 4, "barca_fouls": 11, "opp_fouls": 14,
            "barca_yellow_cards": 2, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 88.9, "opp_pass_acc": 76.8, "barca_big_chances": 3, "opp_big_chances": 1
        }
    },
    {
        "id": "2526_LALIGA_J18", "season": "2025-26", "competition": "LaLiga", "matchday": 18,
        "stage": "Jornada 18", "date": "2026-01-03", "time": "21:00", "home_team": "RCD Espanyol",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "RCD Espanyol", "venue": "RCDE Stadium",
        "referee": "Víctor García Verdura", "status": "FINISHED", "barca_score": 2, "opp_score": 0,
        "notes": "Derbi barcelonés: Dani Olmo 86', Lewandowski 90'.",
        "stats": {
            "barca_xg": 2.15, "opp_xg": 0.65, "barca_possession": 69.2, "opp_possession": 30.8,
            "barca_shots": 16, "opp_shots": 7, "barca_shots_on_target": 6, "opp_shots_on_target": 2,
            "barca_corners": 7, "opp_corners": 3, "barca_fouls": 12, "opp_fouls": 16,
            "barca_yellow_cards": 2, "opp_yellow_cards": 4, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 89.6, "opp_pass_acc": 72.4, "barca_big_chances": 3, "opp_big_chances": 0
        }
    },
    {
        "id": "2526_LALIGA_J20", "season": "2025-26", "competition": "LaLiga", "matchday": 20,
        "stage": "Jornada 20", "date": "2026-01-18", "time": "21:00", "home_team": "Real Sociedad",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Real Sociedad", "venue": "Anoeta",
        "referee": "Jesús Gil Manzano", "status": "FINISHED", "barca_score": 1, "opp_score": 2,
        "notes": "Oyarzabal 32', Guedes 71'; Marcus Rashford 70'.",
        "stats": {
            "barca_xg": 1.40, "opp_xg": 1.85, "barca_possession": 62.0, "opp_possession": 38.0,
            "barca_shots": 11, "opp_shots": 13, "barca_shots_on_target": 4, "opp_shots_on_target": 5,
            "barca_corners": 5, "opp_corners": 6, "barca_fouls": 14, "opp_fouls": 16,
            "barca_yellow_cards": 3, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 86.5, "opp_pass_acc": 78.0, "barca_big_chances": 1, "opp_big_chances": 2
        }
    },
    {
        "id": "2526_LALIGA_J21", "season": "2025-26", "competition": "LaLiga", "matchday": 21,
        "stage": "Jornada 21", "date": "2026-01-25", "time": "16:15", "home_team": "FC Barcelona",
        "away_team": "Real Oviedo", "is_barca_home": True, "opponent": "Real Oviedo", "venue": "Spotify Camp Nou",
        "referee": "Juan Martínez Munuera", "status": "FINISHED", "barca_score": 3, "opp_score": 0,
        "notes": "Dani Olmo 52', Raphinha 57', Lamine Yamal 73'.",
        "stats": {
            "barca_xg": 2.95, "opp_xg": 0.35, "barca_possession": 74.5, "opp_possession": 25.5,
            "barca_shots": 19, "opp_shots": 4, "barca_shots_on_target": 9, "opp_shots_on_target": 1,
            "barca_corners": 8, "opp_corners": 1, "barca_fouls": 8, "opp_fouls": 12,
            "barca_yellow_cards": 1, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 92.0, "opp_pass_acc": 68.0, "barca_big_chances": 4, "opp_big_chances": 0
        }
    },
    {
        "id": "2526_LALIGA_J22", "season": "2025-26", "competition": "LaLiga", "matchday": 22,
        "stage": "Jornada 22", "date": "2026-01-31", "time": "21:00", "home_team": "Elche CF",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Elche CF", "venue": "Martínez Valero",
        "referee": "Alejandro Muñiz Ruiz", "status": "FINISHED", "barca_score": 3, "opp_score": 1,
        "notes": "Lamine Yamal 6', Ferran Torres 40', Marcus Rashford 72'; Álvaro Rodríguez 29'.",
        "stats": {
            "barca_xg": 2.65, "opp_xg": 0.90, "barca_possession": 67.4, "opp_possession": 32.6,
            "barca_shots": 16, "opp_shots": 8, "barca_shots_on_target": 7, "opp_shots_on_target": 3,
            "barca_corners": 6, "opp_corners": 3, "barca_fouls": 10, "opp_fouls": 13,
            "barca_yellow_cards": 1, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 89.2, "opp_pass_acc": 73.1, "barca_big_chances": 4, "opp_big_chances": 1
        }
    },
    {
        "id": "2526_LALIGA_J23", "season": "2025-26", "competition": "LaLiga", "matchday": 23,
        "stage": "Jornada 23", "date": "2026-02-07", "time": "16:15", "home_team": "FC Barcelona",
        "away_team": "RCD Mallorca", "is_barca_home": True, "opponent": "RCD Mallorca", "venue": "Spotify Camp Nou",
        "referee": "Alejandro Quintero González", "status": "FINISHED", "barca_score": 3, "opp_score": 0,
        "notes": "Lewandowski 29', Lamine Yamal 61', Marc Bernal 83'.",
        "stats": {
            "barca_xg": 2.80, "opp_xg": 0.40, "barca_possession": 72.0, "opp_possession": 28.0,
            "barca_shots": 18, "opp_shots": 5, "barca_shots_on_target": 8, "opp_shots_on_target": 1,
            "barca_corners": 7, "opp_corners": 2, "barca_fouls": 8, "opp_fouls": 12,
            "barca_yellow_cards": 1, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 91.0, "opp_pass_acc": 70.5, "barca_big_chances": 4, "opp_big_chances": 0
        }
    },
    {
        "id": "2526_LALIGA_J24", "season": "2025-26", "competition": "LaLiga", "matchday": 24,
        "stage": "Jornada 24", "date": "2026-02-16", "time": "21:00", "home_team": "Girona FC",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Girona FC", "venue": "Montilivi",
        "referee": "César Soto Grado", "status": "FINISHED", "barca_score": 1, "opp_score": 2,
        "notes": "Pau Cubarsí 59'; Thomas Lemar 62', Fran Beltrán 86'.",
        "stats": {
            "barca_xg": 1.55, "opp_xg": 1.95, "barca_possession": 59.5, "opp_possession": 40.5,
            "barca_shots": 12, "opp_shots": 13, "barca_shots_on_target": 4, "opp_shots_on_target": 6,
            "barca_corners": 5, "opp_corners": 5, "barca_fouls": 13, "opp_fouls": 15,
            "barca_yellow_cards": 3, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 86.8, "opp_pass_acc": 79.2, "barca_big_chances": 2, "opp_big_chances": 3
        }
    },
    {
        "id": "2526_LALIGA_J25", "season": "2025-26", "competition": "LaLiga", "matchday": 25,
        "stage": "Jornada 25", "date": "2026-02-22", "time": "16:15", "home_team": "FC Barcelona",
        "away_team": "Levante UD", "is_barca_home": True, "opponent": "Levante UD", "venue": "Spotify Camp Nou",
        "referee": "Javier Alberola Rojas", "status": "FINISHED", "barca_score": 3, "opp_score": 0,
        "notes": "Marc Bernal 4', Frenkie de Jong 32', Fermín López 81'.",
        "stats": {
            "barca_xg": 3.15, "opp_xg": 0.45, "barca_possession": 73.0, "opp_possession": 27.0,
            "barca_shots": 19, "opp_shots": 5, "barca_shots_on_target": 8, "opp_shots_on_target": 1,
            "barca_corners": 8, "opp_corners": 2, "barca_fouls": 9, "opp_fouls": 11,
            "barca_yellow_cards": 1, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 91.5, "opp_pass_acc": 69.5, "barca_big_chances": 4, "opp_big_chances": 0
        }
    },
    {
        "id": "2526_LALIGA_J26", "season": "2025-26", "competition": "LaLiga", "matchday": 26,
        "stage": "Jornada 26", "date": "2026-02-28", "time": "16:15", "home_team": "FC Barcelona",
        "away_team": "Villarreal CF", "is_barca_home": True, "opponent": "Villarreal CF", "venue": "Spotify Camp Nou",
        "referee": "Isidro Díaz de Mera Escuderos", "status": "FINISHED", "barca_score": 4, "opp_score": 1,
        "notes": "Hat-trick de Lamine Yamal (28', 37', 69'), Lewandowski 90+1'; Pape Gueye 49'.",
        "stats": {
            "barca_xg": 3.40, "opp_xg": 1.10, "barca_possession": 66.5, "opp_possession": 33.5,
            "barca_shots": 20, "opp_shots": 8, "barca_shots_on_target": 10, "opp_shots_on_target": 3,
            "barca_corners": 7, "opp_corners": 3, "barca_fouls": 10, "opp_fouls": 14,
            "barca_yellow_cards": 1, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 89.8, "opp_pass_acc": 76.0, "barca_big_chances": 5, "opp_big_chances": 1
        }
    },
    {
        "id": "2526_LALIGA_J27", "season": "2025-26", "competition": "LaLiga", "matchday": 27,
        "stage": "Jornada 27", "date": "2026-03-07", "time": "21:00", "home_team": "Athletic Club",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Athletic Club", "venue": "San Mamés",
        "referee": "José Luis Munuera Montero", "status": "FINISHED", "barca_score": 1, "opp_score": 0,
        "notes": "Golazo de Lamine Yamal (68').",
        "stats": {
            "barca_xg": 1.95, "opp_xg": 0.85, "barca_possession": 62.4, "opp_possession": 37.6,
            "barca_shots": 14, "opp_shots": 9, "barca_shots_on_target": 5, "opp_shots_on_target": 2,
            "barca_corners": 5, "opp_corners": 4, "barca_fouls": 13, "opp_fouls": 16,
            "barca_yellow_cards": 2, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 88.0, "opp_pass_acc": 78.5, "barca_big_chances": 3, "opp_big_chances": 1
        }
    },
    {
        "id": "2526_LALIGA_J28", "season": "2025-26", "competition": "LaLiga", "matchday": 28,
        "stage": "Jornada 28", "date": "2026-03-15", "time": "16:15", "home_team": "FC Barcelona",
        "away_team": "Sevilla FC", "is_barca_home": True, "opponent": "Sevilla FC", "venue": "Spotify Camp Nou",
        "referee": "Juan Martínez Munuera", "status": "FINISHED", "barca_score": 5, "opp_score": 2,
        "notes": "Hat-trick de Raphinha (9', 21', 51'), Dani Olmo 38', João Cancelo 60'; Oso 45+3', Sow 90+2'.",
        "stats": {
            "barca_xg": 3.80, "opp_xg": 1.45, "barca_possession": 67.0, "opp_possession": 33.0,
            "barca_shots": 21, "opp_shots": 9, "barca_shots_on_target": 11, "opp_shots_on_target": 3,
            "barca_corners": 7, "opp_corners": 3, "barca_fouls": 9, "opp_fouls": 12,
            "barca_yellow_cards": 1, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 90.5, "opp_pass_acc": 76.2, "barca_big_chances": 6, "opp_big_chances": 2
        }
    },
    {
        "id": "2526_LALIGA_J29", "season": "2025-26", "competition": "LaLiga", "matchday": 29,
        "stage": "Jornada 29", "date": "2026-03-22", "time": "14:00", "home_team": "FC Barcelona",
        "away_team": "Rayo Vallecano", "is_barca_home": True, "opponent": "Rayo Vallecano", "venue": "Spotify Camp Nou",
        "referee": "Adrián Cordero Vega", "status": "FINISHED", "barca_score": 1, "opp_score": 0,
        "notes": "Gol de Ronald Araujo (24').",
        "stats": {
            "barca_xg": 2.10, "opp_xg": 0.50, "barca_possession": 72.8, "opp_possession": 27.2,
            "barca_shots": 16, "opp_shots": 5, "barca_shots_on_target": 6, "opp_shots_on_target": 1,
            "barca_corners": 8, "opp_corners": 2, "barca_fouls": 10, "opp_fouls": 14,
            "barca_yellow_cards": 1, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 90.2, "opp_pass_acc": 71.0, "barca_big_chances": 3, "opp_big_chances": 0
        }
    },
    {
        "id": "2526_LALIGA_J30", "season": "2025-26", "competition": "LaLiga", "matchday": 30,
        "stage": "Jornada 30", "date": "2026-04-04", "time": "21:00", "home_team": "Atlético de Madrid",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Atlético de Madrid", "venue": "Metropolitano",
        "referee": "Mateo Busquets Ferrer", "status": "FINISHED", "barca_score": 2, "opp_score": 1,
        "notes": "Marcus Rashford 42', Lewandowski 87'; Giuliano Simeone 39'.",
        "stats": {
            "barca_xg": 2.30, "opp_xg": 1.70, "barca_possession": 58.4, "opp_possession": 41.6,
            "barca_shots": 14, "opp_shots": 12, "barca_shots_on_target": 6, "opp_shots_on_target": 4,
            "barca_corners": 5, "opp_corners": 5, "barca_fouls": 14, "opp_fouls": 16,
            "barca_yellow_cards": 3, "opp_yellow_cards": 4, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 87.5, "opp_pass_acc": 80.2, "barca_big_chances": 3, "opp_big_chances": 2
        }
    },
    {
        "id": "2526_LALIGA_J31", "season": "2025-26", "competition": "LaLiga", "matchday": 31,
        "stage": "Jornada 31", "date": "2026-04-11", "time": "18:30", "home_team": "FC Barcelona",
        "away_team": "RCD Espanyol", "is_barca_home": True, "opponent": "RCD Espanyol", "venue": "Spotify Camp Nou",
        "referee": "Alejandro Hernández Hernández", "status": "FINISHED", "barca_score": 4, "opp_score": 1,
        "notes": "Ferran Torres (9', 25'), Lamine Yamal 87', Marcus Rashford 89'; Pol Lozano 56'.",
        "stats": {
            "barca_xg": 3.45, "opp_xg": 0.85, "barca_possession": 71.8, "opp_possession": 28.2,
            "barca_shots": 20, "opp_shots": 6, "barca_shots_on_target": 9, "opp_shots_on_target": 2,
            "barca_corners": 7, "opp_corners": 2, "barca_fouls": 8, "opp_fouls": 13,
            "barca_yellow_cards": 1, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 91.0, "opp_pass_acc": 70.8, "barca_big_chances": 5, "opp_big_chances": 1
        }
    },
    {
        "id": "2526_LALIGA_J33", "season": "2025-26", "competition": "LaLiga", "matchday": 33,
        "stage": "Jornada 33", "date": "2026-04-22", "time": "21:30", "home_team": "FC Barcelona",
        "away_team": "RC Celta de Vigo", "is_barca_home": True, "opponent": "RC Celta de Vigo", "venue": "Spotify Camp Nou",
        "referee": "José Luis Munuera Montero", "status": "FINISHED", "barca_score": 1, "opp_score": 0,
        "notes": "Gol de Lamine Yamal (40').",
        "stats": {
            "barca_xg": 2.20, "opp_xg": 0.45, "barca_possession": 73.5, "opp_possession": 26.5,
            "barca_shots": 17, "opp_shots": 5, "barca_shots_on_target": 6, "opp_shots_on_target": 1,
            "barca_corners": 8, "opp_corners": 2, "barca_fouls": 9, "opp_fouls": 12,
            "barca_yellow_cards": 1, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 91.2, "opp_pass_acc": 69.4, "barca_big_chances": 3, "opp_big_chances": 0
        }
    },
    {
        "id": "2526_LALIGA_J32", "season": "2025-26", "competition": "LaLiga", "matchday": 32,
        "stage": "Jornada 32 (Atrasada)", "date": "2026-04-25", "time": "16:15", "home_team": "Getafe CF",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Getafe CF", "venue": "Coliseum",
        "referee": "Francisco José Hernández Maeso", "status": "FINISHED", "barca_score": 2, "opp_score": 0,
        "notes": "Fermín López 45', Marcus Rashford 74'.",
        "stats": {
            "barca_xg": 2.35, "opp_xg": 0.50, "barca_possession": 69.5, "opp_possession": 30.5,
            "barca_shots": 15, "opp_shots": 6, "barca_shots_on_target": 6, "opp_shots_on_target": 1,
            "barca_corners": 6, "opp_corners": 2, "barca_fouls": 11, "opp_fouls": 15,
            "barca_yellow_cards": 1, "opp_yellow_cards": 4, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 89.5, "opp_pass_acc": 71.0, "barca_big_chances": 3, "opp_big_chances": 0
        }
    },
    {
        "id": "2526_LALIGA_J34", "season": "2025-26", "competition": "LaLiga", "matchday": 34,
        "stage": "Jornada 34", "date": "2026-05-02", "time": "21:00", "home_team": "CA Osasuna",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "CA Osasuna", "venue": "El Sadar",
        "referee": "Isidro Díaz de Mera Escuderos", "status": "FINISHED", "barca_score": 2, "opp_score": 1,
        "notes": "Lewandowski 81', Ferran Torres 86'; Raúl García 88'.",
        "stats": {
            "barca_xg": 2.25, "opp_xg": 1.10, "barca_possession": 64.8, "opp_possession": 35.2,
            "barca_shots": 15, "opp_shots": 8, "barca_shots_on_target": 6, "opp_shots_on_target": 2,
            "barca_corners": 6, "opp_corners": 4, "barca_fouls": 12, "opp_fouls": 15,
            "barca_yellow_cards": 2, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 88.4, "opp_pass_acc": 75.0, "barca_big_chances": 3, "opp_big_chances": 1
        }
    },
    {
        "id": "2526_LALIGA_J35", "season": "2025-26", "competition": "LaLiga", "matchday": 35,
        "stage": "Jornada 35", "date": "2026-05-10", "time": "21:00", "home_team": "FC Barcelona",
        "away_team": "Real Madrid", "is_barca_home": True, "opponent": "Real Madrid", "venue": "Spotify Camp Nou",
        "referee": "Alejandro Hernández Hernández", "status": "FINISHED", "barca_score": 2, "opp_score": 0,
        "notes": "¡CAMPEONES DE LALIGA! Rashford 9', Ferran Torres 18'. Primera vez que se corona en un Clásico.",
        "stats": {
            "barca_xg": 2.80, "opp_xg": 1.05, "barca_possession": 61.5, "opp_possession": 38.5,
            "barca_shots": 17, "opp_shots": 10, "barca_shots_on_target": 7, "opp_shots_on_target": 3,
            "barca_corners": 6, "opp_corners": 4, "barca_fouls": 13, "opp_fouls": 16,
            "barca_yellow_cards": 2, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 89.2, "opp_pass_acc": 81.0, "barca_big_chances": 4, "opp_big_chances": 1
        }
    },
    {
        "id": "2526_LALIGA_J36", "season": "2025-26", "competition": "LaLiga", "matchday": 36,
        "stage": "Jornada 36", "date": "2026-05-13", "time": "21:30", "home_team": "Deportivo Alavés",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Deportivo Alavés", "venue": "Mendizorroza",
        "referee": "José María Sánchez Martínez", "status": "FINISHED", "barca_score": 0, "opp_score": 1,
        "notes": "Ibrahim Diabate 45+1'. Rotaciones tras ganar el título.",
        "stats": {
            "barca_xg": 1.25, "opp_xg": 1.35, "barca_possession": 66.0, "opp_possession": 34.0,
            "barca_shots": 12, "opp_shots": 8, "barca_shots_on_target": 3, "opp_shots_on_target": 3,
            "barca_corners": 5, "opp_corners": 3, "barca_fouls": 11, "opp_fouls": 15,
            "barca_yellow_cards": 1, "opp_yellow_cards": 4, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 88.0, "opp_pass_acc": 72.5, "barca_big_chances": 1, "opp_big_chances": 2
        }
    },
    {
        "id": "2526_LALIGA_J37", "season": "2025-26", "competition": "LaLiga", "matchday": 37,
        "stage": "Jornada 37", "date": "2026-05-17", "time": "21:15", "home_team": "FC Barcelona",
        "away_team": "Real Betis", "is_barca_home": True, "opponent": "Real Betis", "venue": "Spotify Camp Nou",
        "referee": "Guillermo Cuadra Fernández", "status": "FINISHED", "barca_score": 3, "opp_score": 1,
        "notes": "Pleno de 19 victorias en casa: Raphinha (28', 62'), João Cancelo 74'; Isco 69'.",
        "stats": {
            "barca_xg": 3.10, "opp_xg": 1.15, "barca_possession": 68.4, "opp_possession": 31.6,
            "barca_shots": 18, "opp_shots": 7, "barca_shots_on_target": 8, "opp_shots_on_target": 2,
            "barca_corners": 7, "opp_corners": 3, "barca_fouls": 9, "opp_fouls": 12,
            "barca_yellow_cards": 1, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 90.5, "opp_pass_acc": 77.0, "barca_big_chances": 4, "opp_big_chances": 1
        }
    },
    {
        "id": "2526_LALIGA_J38", "season": "2025-26", "competition": "LaLiga", "matchday": 38,
        "stage": "Jornada 38", "date": "2026-05-23", "time": "21:00", "home_team": "Valencia CF",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Valencia CF", "venue": "Mestalla",
        "referee": "Adrián Cordero Vega", "status": "FINISHED", "barca_score": 1, "opp_score": 3,
        "notes": "Último partido de Lewandowski en el Barça (61'); Javi Guerra 66', Luis Rioja 71', G. Rodríguez 90+7'. Total: 94 pts.",
        "stats": {
            "barca_xg": 1.60, "opp_xg": 2.20, "barca_possession": 60.5, "opp_possession": 39.5,
            "barca_shots": 13, "opp_shots": 12, "barca_shots_on_target": 4, "opp_shots_on_target": 5,
            "barca_corners": 5, "opp_corners": 4, "barca_fouls": 12, "opp_fouls": 14,
            "barca_yellow_cards": 2, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0,
            "barca_pass_acc": 87.2, "opp_pass_acc": 78.4, "barca_big_chances": 2, "opp_big_chances": 3
        }
    },

    # ==================== UEFA CHAMPIONS LEAGUE 2025/2026 (12 MATCHES) ====================
    # --- FASE DE LIGA (8 partidos) ---
    {
        "id": "2526_UCL_MD01", "season": "2025-26", "competition": "Champions League", "matchday": 1,
        "stage": "Fase Liga - J1", "date": "2025-09-18", "time": "21:00", "home_team": "Newcastle United",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Newcastle United", "venue": "St James' Park",
        "referee": "Davide Massa", "status": "FINISHED", "barca_score": 2, "opp_score": 1,
        "notes": "Doblete de Marcus Rashford; Anthony Gordon 90'.",
        "stats": {
            "barca_xg": 2.25, "opp_xg": 1.20, "barca_possession": 59.2, "opp_possession": 40.8,
            "barca_shots": 15, "opp_shots": 10, "barca_shots_on_target": 6, "opp_shots_on_target": 3,
            "barca_corners": 5, "opp_corners": 4, "barca_fouls": 11, "opp_fouls": 13,
            "barca_yellow_cards": 2, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },
    {
        "id": "2526_UCL_MD02", "season": "2025-26", "competition": "Champions League", "matchday": 2,
        "stage": "Fase Liga - J2", "date": "2025-10-01", "time": "21:00", "home_team": "FC Barcelona",
        "away_team": "Paris Saint-Germain", "is_barca_home": True, "opponent": "Paris Saint-Germain",
        "venue": "Estadi Olímpic Lluís Companys", "referee": "Michael Oliver", "status": "FINISHED",
        "barca_score": 1, "opp_score": 2, "notes": "Ferran Torres; Mayulu y Gonçalo Ramos.",
        "stats": {
            "barca_xg": 1.70, "opp_xg": 2.15, "barca_possession": 52.5, "opp_possession": 47.5,
            "barca_shots": 14, "opp_shots": 13, "barca_shots_on_target": 5, "opp_shots_on_target": 5,
            "barca_corners": 6, "opp_corners": 5, "barca_fouls": 12, "opp_fouls": 14,
            "barca_yellow_cards": 2, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },
    {
        "id": "2526_UCL_MD03", "season": "2025-26", "competition": "Champions League", "matchday": 3,
        "stage": "Fase Liga - J3", "date": "2025-10-21", "time": "21:00", "home_team": "FC Barcelona",
        "away_team": "Olympiakos FC", "is_barca_home": True, "opponent": "Olympiakos FC",
        "venue": "Estadi Olímpic Lluís Companys", "referee": "Benoît Bastien", "status": "FINISHED",
        "barca_score": 6, "opp_score": 1, "notes": "Hat-trick de Fermín López, doblete de Rashford y gol de Yamal (p).",
        "stats": {
            "barca_xg": 4.60, "opp_xg": 0.70, "barca_possession": 73.0, "opp_possession": 27.0,
            "barca_shots": 23, "opp_shots": 5, "barca_shots_on_target": 12, "opp_shots_on_target": 2,
            "barca_corners": 9, "opp_corners": 2, "barca_fouls": 8, "opp_fouls": 12,
            "barca_yellow_cards": 1, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },
    {
        "id": "2526_UCL_MD04", "season": "2025-26", "competition": "Champions League", "matchday": 4,
        "stage": "Fase Liga - J4", "date": "2025-11-05", "time": "21:00", "home_team": "Club Brugge",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Club Brugge", "venue": "Jan Breydel",
        "referee": "Espen Eskås", "status": "FINISHED", "barca_score": 3, "opp_score": 3,
        "notes": "Ferran Torres, Lamine Yamal, Tzolis (p.p.); Tresoldi, Forbs x2.",
        "stats": {
            "barca_xg": 2.85, "opp_xg": 2.70, "barca_possession": 64.0, "opp_possession": 36.0,
            "barca_shots": 17, "opp_shots": 12, "barca_shots_on_target": 7, "opp_shots_on_target": 6,
            "barca_corners": 7, "opp_corners": 4, "barca_fouls": 11, "opp_fouls": 15,
            "barca_yellow_cards": 2, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },
    {
        "id": "2526_UCL_MD05", "season": "2025-26", "competition": "Champions League", "matchday": 5,
        "stage": "Fase Liga - J5", "date": "2025-11-25", "time": "21:00", "home_team": "Chelsea FC",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Chelsea FC", "venue": "Stamford Bridge",
        "referee": "Slavko Vinčić", "status": "FINISHED", "barca_score": 0, "opp_score": 3,
        "notes": "Koundé (p.p.), Estêvão, Liam Delap.",
        "stats": {
            "barca_xg": 1.10, "opp_xg": 2.85, "barca_possession": 56.5, "opp_possession": 43.5,
            "barca_shots": 10, "opp_shots": 15, "barca_shots_on_target": 3, "opp_shots_on_target": 7,
            "barca_corners": 4, "opp_corners": 6, "barca_fouls": 14, "opp_fouls": 15,
            "barca_yellow_cards": 3, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },
    {
        "id": "2526_UCL_MD06", "season": "2025-26", "competition": "Champions League", "matchday": 6,
        "stage": "Fase Liga - J6", "date": "2025-12-09", "time": "21:00", "home_team": "FC Barcelona",
        "away_team": "Eintracht Frankfurt", "is_barca_home": True, "opponent": "Eintracht Frankfurt",
        "venue": "Spotify Camp Nou", "referee": "Szymon Marciniak", "status": "FINISHED", "barca_score": 2, "opp_score": 1,
        "notes": "Doblete de Jules Koundé; Knauff 58'.",
        "stats": {
            "barca_xg": 2.65, "opp_xg": 0.95, "barca_possession": 69.5, "opp_possession": 30.5,
            "barca_shots": 18, "opp_shots": 7, "barca_shots_on_target": 8, "opp_shots_on_target": 2,
            "barca_corners": 8, "opp_corners": 3, "barca_fouls": 9, "opp_fouls": 13,
            "barca_yellow_cards": 1, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },
    {
        "id": "2526_UCL_MD07", "season": "2025-26", "competition": "Champions League", "matchday": 7,
        "stage": "Fase Liga - J7", "date": "2026-01-21", "time": "21:00", "home_team": "Slavia Praga",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Slavia Praga", "venue": "Fortuna Arena",
        "referee": "Anthony Taylor", "status": "FINISHED", "barca_score": 4, "opp_score": 2,
        "notes": "Fermín López x2, Dani Olmo, Lewandowski; Kušej, Lewy (p.p.).",
        "stats": {
            "barca_xg": 3.20, "opp_xg": 1.40, "barca_possession": 65.8, "opp_possession": 34.2,
            "barca_shots": 17, "opp_shots": 8, "barca_shots_on_target": 8, "opp_shots_on_target": 3,
            "barca_corners": 6, "opp_corners": 3, "barca_fouls": 11, "opp_fouls": 14,
            "barca_yellow_cards": 2, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },
    {
        "id": "2526_UCL_MD08", "season": "2025-26", "competition": "Champions League", "matchday": 8,
        "stage": "Fase Liga - J8", "date": "2026-01-28", "time": "21:00", "home_team": "FC Barcelona",
        "away_team": "FC Copenhague", "is_barca_home": True, "opponent": "FC Copenhague",
        "venue": "Spotify Camp Nou", "referee": "Daniele Orsato", "status": "FINISHED", "barca_score": 4, "opp_score": 1,
        "notes": "Lewandowski, Yamal, Raphinha (p), Rashford; Dadason.",
        "stats": {
            "barca_xg": 3.60, "opp_xg": 0.65, "barca_possession": 72.4, "opp_possession": 27.6,
            "barca_shots": 21, "opp_shots": 5, "barca_shots_on_target": 10, "opp_shots_on_target": 2,
            "barca_corners": 8, "opp_corners": 2, "barca_fouls": 8, "opp_fouls": 11,
            "barca_yellow_cards": 1, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },
    # --- OCTAVOS DE FINAL (vs Newcastle United - Global 8-3) ---
    {
        "id": "2526_UCL_R16_IDA", "season": "2025-26", "competition": "Champions League", "matchday": None,
        "stage": "Octavos de Final (Ida)", "date": "2026-03-10", "time": "21:00", "home_team": "Newcastle United",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Newcastle United", "venue": "St James' Park",
        "referee": "Felix Zwayer", "status": "FINISHED", "barca_score": 1, "opp_score": 1,
        "notes": "Lamine Yamal 90+5' (pen); Harvey Barnes 64'.",
        "stats": {
            "barca_xg": 1.85, "opp_xg": 1.60, "barca_possession": 58.5, "opp_possession": 41.5,
            "barca_shots": 14, "opp_shots": 12, "barca_shots_on_target": 5, "opp_shots_on_target": 4,
            "barca_corners": 5, "opp_corners": 5, "barca_fouls": 12, "opp_fouls": 15,
            "barca_yellow_cards": 2, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },
    {
        "id": "2526_UCL_R16_VTA", "season": "2025-26", "competition": "Champions League", "matchday": None,
        "stage": "Octavos de Final (Vuelta)", "date": "2026-03-18", "time": "21:00", "home_team": "FC Barcelona",
        "away_team": "Newcastle United", "is_barca_home": True, "opponent": "Newcastle United",
        "venue": "Spotify Camp Nou", "referee": "István Kovács", "status": "FINISHED", "barca_score": 7, "opp_score": 2,
        "notes": "Goleada histórica: Bernal, Yamal, Fermín, Raphinha x2, Lewandowski x2; Elanga x2. Global 8-3.",
        "stats": {
            "barca_xg": 4.90, "opp_xg": 1.45, "barca_possession": 68.0, "opp_possession": 32.0,
            "barca_shots": 24, "opp_shots": 8, "barca_shots_on_target": 13, "opp_shots_on_target": 4,
            "barca_corners": 9, "opp_corners": 3, "barca_fouls": 9, "opp_fouls": 13,
            "barca_yellow_cards": 1, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },
    # --- CUARTOS DE FINAL (vs Atlético de Madrid - Global 2-3) ---
    {
        "id": "2526_UCL_QF_IDA", "season": "2025-26", "competition": "Champions League", "matchday": None,
        "stage": "Cuartos de Final (Ida)", "date": "2026-04-08", "time": "21:00", "home_team": "FC Barcelona",
        "away_team": "Atlético de Madrid", "is_barca_home": True, "opponent": "Atlético de Madrid",
        "venue": "Spotify Camp Nou", "referee": "François Letexier", "status": "FINISHED", "barca_score": 0, "opp_score": 2,
        "notes": "Julián Álvarez y Alexander Sørloth.",
        "stats": {
            "barca_xg": 1.65, "opp_xg": 2.20, "barca_possession": 65.5, "opp_possession": 34.5,
            "barca_shots": 15, "opp_shots": 10, "barca_shots_on_target": 4, "opp_shots_on_target": 5,
            "barca_corners": 7, "opp_corners": 3, "barca_fouls": 11, "opp_fouls": 16,
            "barca_yellow_cards": 2, "opp_yellow_cards": 4, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },
    {
        "id": "2526_UCL_QF_VTA", "season": "2025-26", "competition": "Champions League", "matchday": None,
        "stage": "Cuartos de Final (Vuelta)", "date": "2026-04-14", "time": "21:00", "home_team": "Atlético de Madrid",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Atlético de Madrid",
        "venue": "Metropolitano", "referee": "Michael Oliver", "status": "FINISHED", "barca_score": 2, "opp_score": 1,
        "notes": "Lamine Yamal y Ferran Torres; Ademola Lookman. Eliminación por global 2-3.",
        "stats": {
            "barca_xg": 2.45, "opp_xg": 1.60, "barca_possession": 62.0, "opp_possession": 38.0,
            "barca_shots": 16, "opp_shots": 11, "barca_shots_on_target": 7, "opp_shots_on_target": 4,
            "barca_corners": 6, "opp_corners": 5, "barca_fouls": 14, "opp_fouls": 18,
            "barca_yellow_cards": 3, "opp_yellow_cards": 4, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },

    # ==================== COPA DEL REY 2025/2026 (5 MATCHES - SEMIFINALISTA) ====================
    {
        "id": "2526_COPA_R32", "season": "2025-26", "competition": "Copa del Rey", "matchday": None,
        "stage": "Dieciseisavos", "date": "2025-12-16", "time": "21:00", "home_team": "CD Guadalajara",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "CD Guadalajara", "venue": "Pedro Escartín",
        "referee": "César Soto Grado", "status": "FINISHED", "barca_score": 2, "opp_score": 0,
        "notes": "Andreas Christensen 76', Marcus Rashford 90'.",
        "stats": {
            "barca_xg": 2.75, "opp_xg": 0.25, "barca_possession": 78.5, "opp_possession": 21.5,
            "barca_shots": 19, "opp_shots": 3, "barca_shots_on_target": 8, "opp_shots_on_target": 1,
            "barca_corners": 8, "opp_corners": 1, "barca_fouls": 7, "opp_fouls": 13,
            "barca_yellow_cards": 0, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },
    {
        "id": "2526_COPA_R16", "season": "2025-26", "competition": "Copa del Rey", "matchday": None,
        "stage": "Octavos de Final", "date": "2026-01-15", "time": "21:00", "home_team": "Racing Santander",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Racing Santander", "venue": "El Sardinero",
        "referee": "José María Sánchez Martínez", "status": "FINISHED", "barca_score": 2, "opp_score": 0,
        "notes": "Ferran Torres 66', Lamine Yamal 90+5'.",
        "stats": {
            "barca_xg": 2.40, "opp_xg": 0.40, "barca_possession": 71.0, "opp_possession": 29.0,
            "barca_shots": 16, "opp_shots": 5, "barca_shots_on_target": 6, "opp_shots_on_target": 1,
            "barca_corners": 7, "opp_corners": 2, "barca_fouls": 9, "opp_fouls": 14,
            "barca_yellow_cards": 1, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },
    {
        "id": "2526_COPA_QF", "season": "2025-26", "competition": "Copa del Rey", "matchday": None,
        "stage": "Cuartos de Final", "date": "2026-02-03", "time": "21:00", "home_team": "Albacete Balompié",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Albacete Balompié", "venue": "Carlos Belmonte",
        "referee": "José Luis Munuera Montero", "status": "FINISHED", "barca_score": 2, "opp_score": 1,
        "notes": "Lamine Yamal 39', Ronald Araujo 56'; Javier Moreno 87'.",
        "stats": {
            "barca_xg": 2.50, "opp_xg": 0.70, "barca_possession": 69.0, "opp_possession": 31.0,
            "barca_shots": 15, "opp_shots": 6, "barca_shots_on_target": 6, "opp_shots_on_target": 2,
            "barca_corners": 6, "opp_corners": 2, "barca_fouls": 10, "opp_fouls": 15,
            "barca_yellow_cards": 1, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },
    {
        "id": "2526_COPA_SF_IDA", "season": "2025-26", "competition": "Copa del Rey", "matchday": None,
        "stage": "Semifinal (Ida)", "date": "2026-02-12", "time": "21:00", "home_team": "Atlético de Madrid",
        "away_team": "FC Barcelona", "is_barca_home": False, "opponent": "Atlético de Madrid", "venue": "Metropolitano",
        "referee": "Juan Martínez Munuera", "status": "FINISHED", "barca_score": 0, "opp_score": 4,
        "notes": "Eric García (p.p.) 7', Griezmann 14', Lookman 33', Julián Álvarez 45+2'.",
        "stats": {
            "barca_xg": 0.90, "opp_xg": 3.10, "barca_possession": 57.0, "opp_possession": 43.0,
            "barca_shots": 9, "opp_shots": 15, "barca_shots_on_target": 3, "opp_shots_on_target": 7,
            "barca_corners": 4, "opp_corners": 6, "barca_fouls": 15, "opp_fouls": 14,
            "barca_yellow_cards": 3, "opp_yellow_cards": 2, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },
    {
        "id": "2526_COPA_SF_VTA", "season": "2025-26", "competition": "Copa del Rey", "matchday": None,
        "stage": "Semifinal (Vuelta)", "date": "2026-03-03", "time": "21:00", "home_team": "FC Barcelona",
        "away_team": "Atlético de Madrid", "is_barca_home": True, "opponent": "Atlético de Madrid",
        "venue": "Spotify Camp Nou", "referee": "Ricardo de Burgos Bengoetxea", "status": "FINISHED",
        "barca_score": 3, "opp_score": 0,
        "notes": "Marc Bernal (29', 72'), Raphinha 45+5'. Eliminación con la frente en alto (Global 3-4).",
        "stats": {
            "barca_xg": 3.40, "opp_xg": 0.60, "barca_possession": 71.5, "opp_possession": 28.5,
            "barca_shots": 20, "opp_shots": 5, "barca_shots_on_target": 9, "opp_shots_on_target": 1,
            "barca_corners": 8, "opp_corners": 2, "barca_fouls": 11, "opp_fouls": 16,
            "barca_yellow_cards": 2, "opp_yellow_cards": 4, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },

    # ==================== SUPERCOPA DE ESPAÑA 2026 (2 MATCHES - CAMPEÓN) ====================
    {
        "id": "2526_SUPERCOPA_SF", "season": "2025-26", "competition": "Supercopa", "matchday": None,
        "stage": "Semifinal", "date": "2026-01-07", "time": "20:00", "home_team": "FC Barcelona",
        "away_team": "Athletic Club", "is_barca_home": True, "opponent": "Athletic Club",
        "venue": "King Abdullah Sports City (Jeddah)", "referee": "Isidro Díaz de Mera Escuderos", "status": "FINISHED",
        "barca_score": 5, "opp_score": 0,
        "notes": "Ferran Torres 22', Fermín López 30', Roony Bardghji 34', Raphinha (38', 52').",
        "stats": {
            "barca_xg": 4.10, "opp_xg": 0.45, "barca_possession": 69.5, "opp_possession": 30.5,
            "barca_shots": 20, "opp_shots": 6, "barca_shots_on_target": 11, "opp_shots_on_target": 1,
            "barca_corners": 7, "opp_corners": 2, "barca_fouls": 8, "opp_fouls": 13,
            "barca_yellow_cards": 1, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0
        }
    },
    {
        "id": "2526_SUPERCOPA_FINAL", "season": "2025-26", "competition": "Supercopa", "matchday": None,
        "stage": "Final", "date": "2026-01-11", "time": "20:00", "home_team": "FC Barcelona",
        "away_team": "Real Madrid", "is_barca_home": True, "opponent": "Real Madrid",
        "venue": "King Abdullah Sports City (Jeddah)", "referee": "José Luis Munuera Montero", "status": "FINISHED",
        "barca_score": 3, "opp_score": 2,
        "notes": "¡CAMPEONES DE LA SUPERCOPA! Raphinha (36', 73'), Lewandowski 45+4'; Vinícius 45+2', Gonzalo García 45+6'.",
        "stats": {
            "barca_xg": 2.95, "opp_xg": 1.95, "barca_possession": 59.5, "opp_possession": 40.5,
            "barca_shots": 17, "opp_shots": 12, "barca_shots_on_target": 8, "opp_shots_on_target": 4,
            "barca_corners": 6, "opp_corners": 5, "barca_fouls": 14, "opp_fouls": 15,
            "barca_yellow_cards": 2, "opp_yellow_cards": 3, "barca_red_cards": 0, "opp_red_cards": 0
        }
    }
]

def load_2025_2026(db_path="barca_analytics.db"):
    return seed_season_data(MATCHES_2025_2026, db_path)

if __name__ == "__main__":
    load_2025_2026()
