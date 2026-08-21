"""
Master Data Pipeline Seeder.
Initializes the SQLite database and executes the seeders for 2024/25, 2025/26, and 2026/27.
"""

import sys
import os

# Set path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.schema import init_db
from data_pipeline.seed_2024_2025 import load_2024_2025
from data_pipeline.seed_2025_2026 import load_2025_2026
from data_pipeline.seed_2026_2027 import load_2026_2027
from database.db_manager import DatabaseManager

def run_all_seeders(db_path="barca_analytics.db"):
    print("=== INITIALIZING SQLITE DATABASE ===")
    init_db(db_path)
    
    print("\n--- Seeding 2024/2025 Season ---")
    c1 = load_2024_2025(db_path)
    
    print("\n--- Seeding 2025/2026 Season ---")
    c2 = load_2025_2026(db_path)
    
    print("\n--- Seeding 2026/2027 Season ---")
    c3 = load_2026_2027(db_path)
    
    print(f"\n==========================================")
    print(f"DATABASE READY: {c1 + c2 + c3} total matches loaded!")
    print(f"==========================================")

    # Verification summary
    db = DatabaseManager(db_path)
    df = db.get_all_matches_df()
    print("\nMatches Summary by Season and Competition:")
    print(df.groupby(['season', 'competition', 'status']).size())

if __name__ == "__main__":
    run_all_seeders()
