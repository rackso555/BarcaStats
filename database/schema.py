"""
SQLAlchemy Database Schema for FC Barcelona Match Analytics.
Defines clean relational models with explicit foreign keys and constraints.
Includes Match, MatchStat, and OpponentRecentMatch models.
"""

from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, ForeignKey, Text, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import datetime

Base = declarative_base()

class Match(Base):
    __tablename__ = 'matches'

    id = Column(String(50), primary_key=True)  # e.g., '2425_LALIGA_J01'
    season = Column(String(10), nullable=False, index=True)  # '2024-25', '2025-26', '2026-27'
    competition = Column(String(50), nullable=False, index=True)  # 'LaLiga', 'Champions League', 'Copa del Rey', 'Supercopa'
    matchday = Column(Integer, nullable=True)  # Matchday number for league/fase liga
    stage = Column(String(50), nullable=True)  # e.g., 'Jornada 1', 'Fase de Liga', 'Octavos', 'Final'
    date = Column(String(20), nullable=False, index=True)  # 'YYYY-MM-DD'
    time = Column(String(10), nullable=True)  # 'HH:MM'
    home_team = Column(String(50), nullable=False)
    away_team = Column(String(50), nullable=False)
    is_barca_home = Column(Boolean, nullable=False, default=True)
    opponent = Column(String(50), nullable=False, index=True)
    venue = Column(String(100), nullable=True)
    referee = Column(String(100), nullable=True)
    status = Column(String(20), nullable=False, default='SCHEDULED')  # 'FINISHED', 'SCHEDULED', 'POSTPONED'
    
    # Core score & result
    barca_score = Column(Integer, nullable=True)
    opp_score = Column(Integer, nullable=True)
    result = Column(String(1), nullable=True)  # 'W', 'D', 'L'
    points = Column(Integer, nullable=True)  # 3, 1, 0
    notes = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # 1-to-1 relationship with detailed stats
    stats = relationship("MatchStat", back_populates="match", uselist=False, cascade="all, delete-orphan")


class MatchStat(Base):
    __tablename__ = 'match_stats'

    id = Column(Integer, primary_key=True, autoincrement=True)
    match_id = Column(String(50), ForeignKey('matches.id', ondelete='CASCADE'), nullable=False, unique=True, index=True)
    
    # Expected Goals (xG)
    barca_xg = Column(Float, default=0.0)
    opp_xg = Column(Float, default=0.0)

    # Possession & Passing
    barca_possession = Column(Float, default=50.0)
    opp_possession = Column(Float, default=50.0)
    barca_passes = Column(Integer, nullable=True)
    opp_passes = Column(Integer, nullable=True)
    barca_pass_acc = Column(Float, nullable=True)
    opp_pass_acc = Column(Float, nullable=True)

    # Shooting
    barca_shots = Column(Integer, default=0)
    opp_shots = Column(Integer, default=0)
    barca_shots_on_target = Column(Integer, default=0)
    opp_shots_on_target = Column(Integer, default=0)
    barca_shots_off_target = Column(Integer, default=0)
    opp_shots_off_target = Column(Integer, default=0)
    barca_blocked_shots = Column(Integer, default=0)
    opp_blocked_shots = Column(Integer, default=0)

    # Discipline & Set Pieces
    barca_fouls = Column(Integer, default=0)
    opp_fouls = Column(Integer, default=0)
    barca_yellow_cards = Column(Integer, default=0)
    opp_yellow_cards = Column(Integer, default=0)
    barca_red_cards = Column(Integer, default=0)
    opp_red_cards = Column(Integer, default=0)
    barca_offsides = Column(Integer, default=0)
    opp_offsides = Column(Integer, default=0)
    barca_corners = Column(Integer, default=0)
    opp_corners = Column(Integer, default=0)

    # Defense & Goalkeeping
    barca_saves = Column(Integer, default=0)
    opp_saves = Column(Integer, default=0)
    barca_big_chances = Column(Integer, default=0)
    opp_big_chances = Column(Integer, default=0)
    barca_big_chances_missed = Column(Integer, default=0)
    opp_big_chances_missed = Column(Integer, default=0)

    # Tactical formations
    barca_formation = Column(String(20), nullable=True)
    opp_formation = Column(String(20), nullable=True)

    match = relationship("Match", back_populates="stats")


class OpponentRecentMatch(Base):
    """Stores recent matches played by opponents in their respective competitions for in-depth scouting."""
    __tablename__ = 'opponent_recent_matches'

    id = Column(String(60), primary_key=True)  # e.g., 'OPP_RM_2526_J36'
    opponent = Column(String(50), nullable=False, index=True)  # The team being scouted, e.g., 'Real Madrid'
    season = Column(String(10), nullable=False, index=True)  # '2024-25', '2025-26', '2026-27'
    competition = Column(String(50), nullable=False, index=True)  # 'LaLiga', 'Champions League'
    date = Column(String(20), nullable=False, index=True)  # 'YYYY-MM-DD'
    matchday = Column(Integer, nullable=True)
    stage = Column(String(50), nullable=True)
    rival = Column(String(50), nullable=False)  # Who the opponent played against, e.g., 'Sevilla FC'
    is_home = Column(Boolean, nullable=False, default=True)  # True if opponent was home
    team_score = Column(Integer, default=0)  # Goals scored by opponent
    rival_score = Column(Integer, default=0)  # Goals conceded by opponent
    result = Column(String(1), default='W')  # 'W', 'D', 'L' from opponent perspective
    xg_for = Column(Float, default=0.0)
    xg_against = Column(Float, default=0.0)
    possession = Column(Float, default=50.0)
    shots_for = Column(Integer, default=0)
    shots_against = Column(Integer, default=0)
    sot_for = Column(Integer, default=0)  # Tiros a puerta conseguidos
    sot_against = Column(Integer, default=0)  # Tiros a puerta recibidos
    corners_for = Column(Integer, default=0)  # Córners a favor
    corners_against = Column(Integer, default=0)  # Córners en contra
    fouls_for = Column(Integer, default=0)  # Faltas recibidas (a favor)
    fouls_against = Column(Integer, default=0)  # Faltas cometidas (en contra)
    yellow_cards_for = Column(Integer, default=0)  # Tarjetas amarillas del rival
    yellow_cards_against = Column(Integer, default=0)  # Tarjetas amarillas del adversario
    notes = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.datetime.utcnow)


def get_engine(db_path="barca_analytics.db"):
    return create_engine(f"sqlite:///{db_path}")


def init_db(db_path="barca_analytics.db", force_reset=False):
    """Initializes SQLite database. If force_reset=True, drops existing tables first."""
    engine = get_engine(db_path)
    if force_reset:
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return engine
