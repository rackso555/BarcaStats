"""
Database Manager for querying, inserting, and aggregating match data.
Pure Python + SQLAlchemy + Pandas for high speed and 0 token cost.
"""

import pandas as pd
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import desc, asc, func
from database.schema import Match, MatchStat, init_db, get_engine
import os

class DatabaseManager:
    def __init__(self, db_path="barca_analytics.db"):
        self.db_path = db_path
        self.engine = get_engine(db_path)
        self.SessionFactory = sessionmaker(bind=self.engine)

    def get_session(self) -> Session:
        return self.SessionFactory()

    def get_all_matches_df(self) -> pd.DataFrame:
        """Returns all matches joined with their stats as a Pandas DataFrame."""
        query = """
        SELECT 
            m.id as match_id,
            m.season,
            m.competition,
            m.matchday,
            m.stage,
            m.date,
            m.time,
            m.home_team,
            m.away_team,
            m.is_barca_home,
            m.opponent,
            m.venue,
            m.referee,
            m.status,
            m.barca_score,
            m.opp_score,
            m.result,
            m.points,
            m.notes,
            s.barca_xg,
            s.opp_xg,
            s.barca_possession,
            s.opp_possession,
            s.barca_passes,
            s.opp_passes,
            s.barca_pass_acc,
            s.opp_pass_acc,
            s.barca_shots,
            s.opp_shots,
            s.barca_shots_on_target,
            s.opp_shots_on_target,
            s.barca_shots_off_target,
            s.opp_shots_off_target,
            s.barca_blocked_shots,
            s.opp_blocked_shots,
            s.barca_fouls,
            s.opp_fouls,
            s.barca_yellow_cards,
            s.opp_yellow_cards,
            s.barca_red_cards,
            s.opp_red_cards,
            s.barca_offsides,
            s.opp_offsides,
            s.barca_corners,
            s.opp_corners,
            s.barca_saves,
            s.opp_saves,
            s.barca_big_chances,
            s.opp_big_chances,
            s.barca_big_chances_missed,
            s.opp_big_chances_missed,
            s.barca_formation,
            s.opp_formation
        FROM matches m
        LEFT JOIN match_stats s ON m.id = s.match_id
        ORDER BY m.date ASC;
        """
        return pd.read_sql_query(query, self.engine)

    def get_seasons(self) -> list:
        session = self.get_session()
        try:
            seasons = session.query(Match.season).distinct().order_by(desc(Match.season)).all()
            return [s[0] for s in seasons]
        finally:
            session.close()

    def get_competitions(self, season: str = None) -> list:
        session = self.get_session()
        try:
            q = session.query(Match.competition).distinct()
            if season and season != "Todas":
                q = q.filter(Match.season == season)
            comps = q.all()
            return [c[0] for c in comps]
        finally:
            session.close()

    def get_opponents(self) -> list:
        session = self.get_session()
        try:
            opps = session.query(Match.opponent).distinct().order_by(asc(Match.opponent)).all()
            return [o[0] for o in opps]
        finally:
            session.close()

    def get_h2h_matches(self, opponent: str) -> pd.DataFrame:
        """Returns all matches against a specific opponent with stats."""
        df = self.get_all_matches_df()
        return df[df['opponent'] == opponent].sort_values('date', ascending=False)

    def get_season_progression(self, season: str, competition: str = "LaLiga") -> pd.DataFrame:
        """Returns ordered season trajectory with cumulative points, goals, and xG."""
        df = self.get_all_matches_df()
        sub = df[(df['season'] == season) & (df['competition'] == competition) & (df['status'] == 'FINISHED')].copy()
        if sub.empty:
            return sub
        
        sub = sub.sort_values('date').reset_index(drop=True)
        sub['match_num'] = range(1, len(sub) + 1)
        sub['cum_points'] = sub['points'].fillna(0).cumsum()
        sub['cum_gf'] = sub['barca_score'].fillna(0).cumsum()
        sub['cum_ga'] = sub['opp_score'].fillna(0).cumsum()
        sub['cum_gd'] = sub['cum_gf'] - sub['cum_ga']
        
        # Cumulative xG
        sub['xg_diff'] = sub['barca_xg'].fillna(0) - sub['opp_xg'].fillna(0)
        sub['cum_xg_diff'] = sub['xg_diff'].cumsum()
        sub['cum_barca_xg'] = sub['barca_xg'].fillna(0).cumsum()
        sub['cum_opp_xg'] = sub['opp_xg'].fillna(0).cumsum()
        
        # Rolling 5-match form
        sub['rolling_pts_5'] = sub['points'].fillna(0).rolling(5, min_periods=1).sum()
        sub['rolling_xg_diff_5'] = sub['xg_diff'].rolling(5, min_periods=1).mean()
        
        return sub

    def insert_or_update_match(self, match_data: dict, stats_data: dict):
        """Insert or update a match and its associated stats."""
        session = self.get_session()
        try:
            match = session.query(Match).filter_by(id=match_data['id']).first()
            if not match:
                match = Match(**match_data)
                session.add(match)
            else:
                for k, v in match_data.items():
                    setattr(match, k, v)

            session.flush()

            stat = session.query(MatchStat).filter_by(match_id=match_data['id']).first()
            stats_data['match_id'] = match_data['id']
            if not stat:
                stat = MatchStat(**stats_data)
                session.add(stat)
            else:
                for k, v in stats_data.items():
                    setattr(stat, k, v)

            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_opponent_matches_df(self) -> pd.DataFrame:
        """Returns all opponent recent matches as a Pandas DataFrame."""
        try:
            return pd.read_sql("SELECT * FROM opponent_recent_matches", self.engine)
        except Exception:
            return pd.DataFrame()

    def insert_or_update_opponent_match(self, match_data: dict):
        """Insert or update an opponent recent match."""
        from database.schema import OpponentRecentMatch
        session = self.get_session()
        try:
            opp_m = session.query(OpponentRecentMatch).filter_by(id=match_data['id']).first()
            if not opp_m:
                opp_m = OpponentRecentMatch(**match_data)
                session.add(opp_m)
            else:
                for k, v in match_data.items():
                    setattr(opp_m, k, v)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
