"""
Test Suite for Barça Analytics Engine.
Verifies all analytics functions, charts generation, and database queries.
"""

import sys
import io

# Ensure UTF-8 output on Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from database.db_manager import DatabaseManager
from analytics.momentum import get_multi_season_progression, calculate_momentum_index
from analytics.h2h import calculate_h2h_summary
from analytics.radars import compute_team_radar_metrics
from components.charts import (
    create_multi_season_points_chart,
    create_momentum_chart,
    create_xg_differential_chart,
    create_radar_comparison_chart,
    create_match_comparison_bars,
    COLOR_BARCA_BLUE,
    COLOR_BARCA_GOLD,
    COLOR_BARCA_GARNET
)

def run_tests():
    db = DatabaseManager("barca_analytics.db")
    df = db.get_all_matches_df()
    assert len(df) > 0, "DataFrame is empty!"
    print(f"[OK] Loaded {len(df)} matches from SQLite database.")

    # Test Multi-Season Progression
    prog = get_multi_season_progression(df, "LaLiga")
    assert "2024-25" in prog and "2025-26" in prog
    print(f"[OK] Momentum & Progression calculated: 24/25 has {len(prog['2024-25'])} matchdays, 25/26 has {len(prog['2025-26'])} matchdays.")

    # Test H2H vs Real Madrid
    h2h_rm = calculate_h2h_summary(df, "Real Madrid")
    assert h2h_rm['total_matches'] > 0
    print(f"[OK] H2H vs Real Madrid: {h2h_rm['total_matches']} matches, Record {h2h_rm['wins']}W-{h2h_rm['draws']}D-{h2h_rm['losses']}L.")

    # Test Radar Metrics
    radar_2425 = compute_team_radar_metrics(df, "2024-25", "LaLiga")
    assert len(radar_2425['categories']) == 8
    print(f"[OK] Radar metrics calculated for 2024-25: {radar_2425['raw_stats']}")

    # Test Charts
    fig1 = create_multi_season_points_chart(prog)
    fig2 = create_momentum_chart(prog)
    fig3 = create_xg_differential_chart(prog)
    fig4 = create_radar_comparison_chart([("2024-25", COLOR_BARCA_BLUE, radar_2425)])
    
    match_sample = df[df['status'] == 'FINISHED'].iloc[0]
    fig5 = create_match_comparison_bars(match_sample)

    assert fig1 and fig2 and fig3 and fig4 and fig5
    print("[OK] All Plotly figures generated successfully without errors!")
    print("\nALL UNIT TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_tests()
