"""
FC Barcelona Match Analytics Hub (2024/25, 2025/26 & 2026/27).
Local-first, Zero-Token Analytics & Automated Agent Sync Dashboard.
Reworked Match Center with dynamic metric controls, opponent form, and disaggregated breakdowns.
"""

import streamlit as st
import pandas as pd
import numpy as np
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import importlib
import components.charts
import analytics.momentum
import analytics.h2h
import analytics.radars
import analytics.opponent_form
import components.auth

importlib.reload(components.charts)
importlib.reload(analytics.momentum)
importlib.reload(analytics.h2h)
importlib.reload(analytics.radars)
importlib.reload(analytics.opponent_form)
importlib.reload(components.auth)

from database.db_manager import DatabaseManager
from analytics.momentum import get_multi_season_progression, calculate_momentum_index
from analytics.h2h import calculate_h2h_summary
from analytics.radars import compute_team_radar_metrics
from analytics.opponent_form import compute_opponent_recent_form
from data_pipeline.agent_sync import BarcaSyncAgent
from data_pipeline.data_cleaner import DataCleanerEngine
from components.theme import apply_barca_theme
from components.auth import render_auth_sidebar, render_tab5_admin_prompt
from components.charts import (
    create_multi_season_points_chart,
    create_momentum_chart,
    create_xg_differential_chart,
    create_radar_comparison_chart,
    create_match_comparison_bars,
    create_opponent_form_chart,
    ALL_COMPARISON_METRICS,
    COLOR_BARCA_GARNET,
    COLOR_BARCA_BLUE,
    COLOR_BARCA_GOLD
)

# Initialize Streamlit configuration
st.set_page_config(
    page_title="FC Barcelona Match Analytics Hub",
    page_icon="🔵🔴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Blaugrana UI Styles
apply_barca_theme()

# Render auth controls in sidebar (Defaults to Viewer mode, Admin login available)
user_role = render_auth_sidebar()

# Database and Sync Agent instances
db = DatabaseManager("barca_analytics.db")
sync_agent = BarcaSyncAgent("barca_analytics.db")

# Always reload fresh data from database
df_all = db.get_all_matches_df()
df_opp_matches = db.get_opponent_matches_df()

# ----------------- SIDEBAR -----------------
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 10px 0 20px 0;">
            <div style="font-size: 3rem;">🔵🔴</div>
            <h2 style="color: #EDBB00; margin: 0; font-weight: 800;">BARÇA ANALYTICS</h2>
            <p style="color: #94A3B8; font-size: 0.85rem; margin: 2px 0 0 0;">Més que un club • Hub Estadístico</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("⚙️ Filtros Globales")
    
    available_seasons = ["Todas", "2026-27", "2025-26", "2024-25"]
    selected_season = st.selectbox("Temporada", available_seasons, index=1, key="sb_season")
    
    available_comps = ["Todas", "LaLiga", "Champions League", "Copa del Rey", "Supercopa"]
    selected_comp = st.selectbox("Competición", available_comps, index=0, key="sb_comp")
    
    st.markdown("---")
    
    # Filter matches for quick stats in sidebar
    df_filtered = df_all.copy()
    if selected_season != "Todas":
        df_filtered = df_filtered[df_filtered['season'] == selected_season]
    if selected_comp != "Todas":
        df_filtered = df_filtered[df_filtered['competition'] == selected_comp]
        
    finished_matches = df_filtered[df_filtered['status'] == 'FINISHED']
    total_played = len(finished_matches)
    
    if total_played > 0:
        wins = len(finished_matches[finished_matches['result'] == 'W'])
        draws = len(finished_matches[finished_matches['result'] == 'D'])
        losses = len(finished_matches[finished_matches['result'] == 'L'])
        win_rate = round((wins / total_played) * 100, 1)
        gf = int(finished_matches['barca_score'].sum())
        ga = int(finished_matches['opp_score'].sum())
        avg_xg = round(finished_matches['barca_xg'].mean(), 2) if 'barca_xg' in finished_matches else 0
        avg_poss = round(finished_matches['barca_possession'].mean(), 1) if 'barca_possession' in finished_matches else 0
        
        st.markdown("### 📊 Balance Rápido")
        st.markdown(f"""
            <div style="background: rgba(18, 26, 44, 0.7); padding: 12px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05);">
                <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                    <span style="color: #94A3B8;">Partidos:</span>
                    <b>{total_played}</b>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                    <span style="color: #94A3B8;">Récord:</span>
                    <span><b style="color: #10B981;">{wins}V</b> - <b style="color: #F59E0B;">{draws}E</b> - <b style="color: #EF4444;">{losses}D</b></span>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                    <span style="color: #94A3B8;">Efectividad:</span>
                    <b style="color: #EDBB00;">{win_rate}%</b>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                    <span style="color: #94A3B8;">Goles (F / C):</span>
                    <b>{gf} / {ga} ({gf - ga:+d})</b>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                    <span style="color: #94A3B8;">xG Promedio:</span>
                    <b>{avg_xg}</b>
                </div>
                <div style="display: flex; justify-content: space-between;">
                    <span style="color: #94A3B8;">Posesión Media:</span>
                    <b>{avg_poss}%</b>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Sin partidos finalizados para el filtro actual.")

# ----------------- MAIN HEADER BANNER -----------------
st.markdown(f"""
    <div class="barca-banner">
        <div>
            <h1>FC BARCELONA • MATCH ANALYTICS HUB</h1>
            <p>Comparativas de Rendimiento • Temporadas 2024/25, 2025/26 y 2026/27</p>
        </div>
        <div style="text-align: right;">
            <span style="background: rgba(0,0,0,0.3); border: 1px solid rgba(237,187,0,0.5); color: #EDBB00; padding: 6px 14px; border-radius: 20px; font-weight: 700; font-size: 0.9rem;">
                ⚡ 100% Local & Zero-Tokens
            </span>
        </div>
    </div>
""", unsafe_allow_html=True)

# ----------------- TABS NAVIGATION -----------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏟️ Match Center & Previa",
    "📈 Momentum & Progresión",
    "🎯 Perfil Táctico & Radar",
    "📋 Historial de Partidos",
    "🤖 Sincronización Automática con Agente"
])

# =====================================================================
# TAB 1: MATCH CENTER & PREVIA (Desglose Individual por Partido)
# =====================================================================
with tab1:
    st.subheader("🏟️ Match Center: Previa de Jornada vs Rival")
    
    col_sel1, col_sel2, col_sel3 = st.columns([1.2, 1.2, 2.2])
    
    with col_sel1:
        match_season = st.selectbox("Temporada", ["2026-27", "2025-26", "2024-25"], index=0, key="mc_season")
    with col_sel2:
        season_comps = db.get_competitions(match_season) or ["LaLiga", "Champions League", "Copa del Rey", "Supercopa"]
        match_comp = st.selectbox("Competición", season_comps, index=0, key="mc_comp")
        
    matches_available = df_all[(df_all['season'] == match_season) & (df_all['competition'] == match_comp)].sort_values('date')
    
    if matches_available.empty:
        st.warning(f"No hay partidos registrados para {match_season} en {match_comp}.")
    else:
        with col_sel3:
            match_options = []
            for idx, r in matches_available.iterrows():
                m_day = int(r['matchday']) if pd.notna(r['matchday']) and str(r['matchday']) != 'nan' else None
                stage_label = f"J{m_day}" if m_day is not None else (str(r['stage']) if pd.notna(r['stage']) else "Partido")
                vs_label = f"vs {r['opponent']} ({'C' if r['is_barca_home'] else 'F'}) - {r['date']}"
                status_icon = "✅" if r['status'] == 'FINISHED' else "⏳"
                match_options.append((r['match_id'], f"{status_icon} {stage_label}: {vs_label}"))
            
            selected_match_tuple = st.selectbox(
                "Seleccionar Partido / Jornada",
                match_options,
                format_func=lambda x: x[1],
                key="mc_match_select"
            )
            selected_match_id = selected_match_tuple[0]
            
        # Match Data Row
        current_match = matches_available[matches_available['match_id'] == selected_match_id].iloc[0]
        opponent_name = current_match['opponent']
        
        # Header Scoreboard Card
        home_name = current_match['home_team']
        away_name = current_match['away_team']
        is_finished = current_match['status'] == 'FINISHED'
        score_text = f"{int(current_match['barca_score'])} - {int(current_match['opp_score'])}" if is_finished else "VS"
        
        home_color = "#EDBB00" if current_match['is_barca_home'] else "#FFFFFF"
        away_color = "#FFFFFF" if current_match['is_barca_home'] else "#EDBB00"
        
        venue_display = str(current_match['venue']) if (pd.notna(current_match['venue']) and str(current_match['venue']).lower() not in ['nan', 'none', '']) else 'Estadio Oficial'
        referee_display = str(current_match['referee']) if (pd.notna(current_match['referee']) and str(current_match['referee']).lower() not in ['nan', 'none', '']) else 'Árbitro Oficial'
        time_display = f" • ⏰ {current_match['time']}" if (pd.notna(current_match['time']) and str(current_match['time']).lower() not in ['nan', 'none', '']) else ""
        
        st.markdown(f"""
            <div class="match-score-card">
                <div style="display: flex; justify-content: space-between; align-items: center; text-align: center; flex-wrap: wrap;">
                    <div style="flex: 1; min-width: 160px;">
                        <h3 style="color: {home_color}; margin: 0; font-size: 1.4rem;">{home_name}</h3>
                        <span style="color: #94A3B8; font-size: 0.85rem; font-weight: 700;">LOCAL</span>
                    </div>
                    <div style="flex: 1; min-width: 200px; padding: 10px 20px;">
                        <div style="font-size: 2.5rem; font-weight: 900; color: #EDBB00; letter-spacing: 2px;">{score_text}</div>
                        <div style="color: #94A3B8; font-size: 0.85rem; margin-top: 4px;">📅 {current_match['date']}{time_display}</div>
                        <div style="color: #64748B; font-size: 0.8rem;">🏟️ {venue_display} • 👨‍⚖️ {referee_display}</div>
                    </div>
                    <div style="flex: 1; min-width: 160px;">
                        <h3 style="color: {away_color}; margin: 0; font-size: 1.4rem;">{away_name}</h3>
                        <span style="color: #94A3B8; font-size: 0.85rem; font-weight: 700;">VISITANTE</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # -------------------------------------------------------------
        # ROW 1: RIVAL PERFORMANCE / FORM (LEFT) + GOALS/xG HISTORICAL (RIGHT)
        # -------------------------------------------------------------
        h2h = calculate_h2h_summary(df_all[df_all['status'] == 'FINISHED'], opponent_name)
        opp_form = compute_opponent_recent_form(df_opp_matches, opponent_name, competition=match_comp, limit=5)
        
        col_row1_left, col_row1_right = st.columns([0.48, 0.52])
        
        with col_row1_left:
            st.markdown(f"#### ⚔️ Rendimiento y Forma de {opponent_name}")
            
            scout_choice = st.radio(
                "Selecciona perspectiva de scouting:",
                ["🔵🔴 Historial vs Barça", f"⚡ Últimos 5 de {opponent_name} en {match_comp}"],
                horizontal=True,
                label_visibility="collapsed",
                key=f"scout_toggle_{selected_match_id}"
            )
            
            # SUBTAB 1: H2H VS BARÇA
            if scout_choice == "🔵🔴 Historial vs Barça":
                if h2h['total_matches'] > 0:
                    recent_opp_matches = h2h['matches_df'].head(5)
                    form_pills = []
                    for _, rm in recent_opp_matches.iterrows():
                        if rm['result'] == 'W':
                            form_pills.append("<span class='badge-win'>V</span>")
                        elif rm['result'] == 'D':
                            form_pills.append("<span class='badge-draw'>E</span>")
                        else:
                            form_pills.append("<span class='badge-loss'>D</span>")
                    
                    match_items_html = []
                    for _, mm in h2h['matches_df'].head(5).iterrows():
                        badge = "🟢" if mm['result']=='W' else ("🟡" if mm['result']=='D' else "🔴")
                        m_stg = str(mm['stage']) if pd.notna(mm['stage']) else 'Oficial'
                        b_sc = int(mm['barca_score']) if pd.notna(mm['barca_score']) else 0
                        o_sc = int(mm['opp_score']) if pd.notna(mm['opp_score']) else 0
                        b_xg = f"{float(mm['barca_xg']):.2f}" if pd.notna(mm.get('barca_xg')) else "0.00"
                        o_xg = f"{float(mm['opp_xg']):.2f}" if pd.notna(mm.get('opp_xg')) else "0.00"
                        match_items_html.append(f'<div style="display:flex; justify-content:space-between; align-items:center; padding:6px 0; border-bottom:1px solid rgba(255,255,255,0.06); font-size:0.85rem;"><span>{badge} <b>{mm["date"]}</b> ({mm["competition"][:3]} - {m_stg})</span><span style="font-weight:800; color:#EDBB00; font-size:0.95rem;">{b_sc} - {o_sc}</span><span style="color:#94A3B8; font-size:0.75rem;">xG: {b_xg} - {o_xg}</span></div>')

                    matches_block = "".join(match_items_html)
                    pills_block = " ".join(form_pills)

                    st.markdown(f"""
                        <div style="background: rgba(18, 26, 44, 0.7); padding: 14px; border-radius: 14px; border: 1px solid rgba(237, 187, 0, 0.25); margin-bottom: 8px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                                <span style="color: #94A3B8; font-size: 0.85rem; font-weight: 600;">Racha del Barça vs Rival ({len(form_pills)} últimos):</span>
                                <div style="display: flex; gap: 6px;">{pills_block}</div>
                            </div>
                            <div style="display: flex; justify-content: space-around; text-align: center; margin: 10px 0;">
                                <div>
                                    <div style="font-size: 1.3rem; font-weight: 800; color: #10B981;">{h2h['wins']}</div>
                                    <div style="color: #94A3B8; font-size: 0.75rem;">VICTORIAS BARÇA</div>
                                </div>
                                <div>
                                    <div style="font-size: 1.3rem; font-weight: 800; color: #F59E0B;">{h2h['draws']}</div>
                                    <div style="color: #94A3B8; font-size: 0.75rem;">EMPATES</div>
                                </div>
                                <div>
                                    <div style="font-size: 1.3rem; font-weight: 800; color: #EF4444;">{h2h['losses']}</div>
                                    <div style="color: #94A3B8; font-size: 0.75rem;">DERROTAS</div>
                                </div>
                            </div>
                            <hr style="border-color: rgba(255,255,255,0.06); margin: 8px 0;">
                            <div style="font-size: 0.8rem; font-weight: 600; color: #94A3B8; margin-bottom: 6px;">Últimos Duelos Directos:</div>
                            {matches_block}
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.info(f"Sin enfrentamientos oficiales previos registrados contra {opponent_name}.")

            # SUBTAB 2: ÚLTIMOS 5 PARTIDOS DEL RIVAL EN LA COMPETICIÓN
            else:
                if opp_form['total_matches'] > 0:
                    s = opp_form['summary']
                    pills_str = " ".join(opp_form['form_pills'])
                    
                    st.markdown(f"""
                        <div style="background: rgba(18, 26, 44, 0.7); padding: 14px; border-radius: 14px; border: 1px solid rgba(56, 189, 248, 0.25); margin-bottom: 8px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                                <span style="color: #94A3B8; font-size: 0.85rem; font-weight: 600;">Racha en {match_comp} (5 últimos):</span>
                                <div style="display: flex; gap: 6px;">{pills_str}</div>
                            </div>
                            <div style="display: flex; justify-content: space-around; text-align: center; margin: 8px 0;">
                                <div>
                                    <div style="font-size: 1.2rem; font-weight: 800; color: #10B981;">{opp_form['wins']}V</div>
                                    <div style="color: #94A3B8; font-size: 0.7rem;">VICTORIAS</div>
                                </div>
                                <div>
                                    <div style="font-size: 1.2rem; font-weight: 800; color: #F59E0B;">{opp_form['draws']}E</div>
                                    <div style="color: #94A3B8; font-size: 0.7rem;">EMPATES</div>
                                </div>
                                <div>
                                    <div style="font-size: 1.2rem; font-weight: 800; color: #EF4444;">{opp_form['losses']}D</div>
                                    <div style="color: #94A3B8; font-size: 0.7rem;">DERROTAS</div>
                                </div>
                            </div>
                            <hr style="border-color: rgba(255,255,255,0.06); margin: 6px 0;">
                            <div style="font-size: 0.8rem; font-weight: 700; color: #38BDF8; margin-bottom: 6px;">📊 Balance Resumido (Últimos 5 PJ):</div>
                            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; font-size: 0.8rem; line-height: 1.5;">
                                <div>⚽ <b>Goles (F / C):</b> {s['gf_total']} ({s['gf_avg']}/PJ) / {s['ga_total']} ({s['ga_avg']}/PJ)</div>
                                <div>🎯 <b>xG (F / C):</b> {s['xg_for_avg']} / {s['xg_against_avg']} xGA</div>
                                <div>✨ <b>Posesión Media:</b> {s['possession_avg']}%</div>
                                <div>🥅 <b>Tiros Puerta (F / C):</b> {s['sot_for_total']} ({s['sot_for_avg']}/PJ) / {s['sot_against_total']} ({s['sot_against_avg']}/PJ)</div>
                                <div>🚩 <b>Córners (F / C):</b> {s['corners_for_total']} ({s['corners_for_avg']}/PJ) / {s['corners_against_total']} ({s['corners_against_avg']}/PJ)</div>
                                <div>🛑 <b>Faltas (Prov / Com):</b> {s['fouls_for_avg']}/PJ / {s['fouls_against_avg']}/PJ</div>
                                <div>🟨 <b>Tarjetas Amarillas (Prov / Rec):</b> {s['yc_against_total']} ({s['yc_against_avg']}/PJ) / {s['yc_for_total']} ({s['yc_for_avg']}/PJ)</div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Expandable breakdown of individual 5 opponent matches
                    st.markdown("##### 📌 Desglose Partido a Partido del Rival")
                    for _, opp_m in opp_form['matches_df'].iterrows():
                        r_badge = "🟢 Victoria" if opp_m['result'] == 'W' else ("🟡 Empate" if opp_m['result'] == 'D' else "🔴 Derrota")
                        cond_str = "Local" if opp_m['is_home'] else "Visitante"
                        with st.expander(f"📅 {opp_m['date']} | vs {opp_m['rival']} ({cond_str}): {opp_m['team_score']} - {opp_m['rival_score']} ({r_badge})"):
                            col_sub1, col_sub2 = st.columns(2)
                            with col_sub1:
                                st.markdown(f"""
                                    • <b>Marcador:</b> {opp_m['team_score']} - {opp_m['rival_score']}<br>
                                    • <b>Expected Goals (xG):</b> {opp_m.get('xg_for', 0)} vs {opp_m.get('xg_against', 0)}<br>
                                    • <b>Posesión:</b> {opp_m.get('possession', 50)}%<br>
                                    • <b>Tiros Totales:</b> {opp_m.get('shots_for', 0)} vs {opp_m.get('shots_against', 0)}
                                """, unsafe_allow_html=True)
                            with col_sub2:
                                st.markdown(f"""
                                    • <b>Tiros a Puerta:</b> {opp_m.get('sot_for', 0)} vs {opp_m.get('sot_against', 0)}<br>
                                    • <b>Córners:</b> {opp_m.get('corners_for', 0)} vs {opp_m.get('corners_against', 0)}<br>
                                    • <b>Faltas (Prov / Com):</b> {opp_m.get('fouls_for', 0)} vs {opp_m.get('fouls_against', 0)}<br>
                                    • <b>Tarjetas Amarillas (Prov / Rec):</b> {opp_m.get('yellow_cards_against', 0)} vs {opp_m.get('yellow_cards_for', 0)}
                                """, unsafe_allow_html=True)
                else:
                    st.info(f"Sin registros recientes de {opponent_name} en {match_comp}.")

        with col_row1_right:
            if h2h['total_matches'] > 0:
                st.plotly_chart(create_opponent_form_chart(h2h['matches_df'], opponent_name), use_container_width=True)
            else:
                st.info(f"Gráfica de histórico vs {opponent_name} disponible una vez disputado al menos un encuentro.")

        # -------------------------------------------------------------
        # ROW 2: ESTADÍSTICAS COMPARATIVAS DEL ENCUENTRO (POR PARTIDO)
        # -------------------------------------------------------------
        st.markdown("---")
        st.markdown(f"### 📊 Estadísticas Comparativas por Partido: Barça vs {opponent_name}")
        
        # PRESET SELECTION TOOLBAR WITH DIRECT STATE CALLBACKS
        DEFAULT_METRICS = ["xg", "shots", "sot", "possession", "corners", "fouls", "pass_acc", "big_chances"]
        if "mc_dynamic_metrics_selector" not in st.session_state:
            st.session_state["mc_dynamic_metrics_selector"] = DEFAULT_METRICS

        def set_metrics(preset_list):
            st.session_state["mc_dynamic_metrics_selector"] = preset_list

        st.markdown("##### 🎛️ Panel de Control de Estadísticas (Prender / Apagar)")
        
        preset_c1, preset_c2, preset_c3, preset_c4, preset_c5 = st.columns(5)
        with preset_c1:
            st.button("⭐ Básicas", on_click=set_metrics, args=(["xg", "shots", "sot", "possession", "corners", "fouls"],), use_container_width=True)
        with preset_c2:
            st.button("⚔️ Ataque & Ocasiones", on_click=set_metrics, args=(["xg", "shots", "sot", "shots_off", "big_chances"],), use_container_width=True)
        with preset_c3:
            st.button("🛡️ Defensa & Disciplina", on_click=set_metrics, args=(["fouls", "yellow_cards", "red_cards", "offsides", "saves"],), use_container_width=True)
        with preset_c4:
            st.button("✨ Control & Pases", on_click=set_metrics, args=(["possession", "pass_acc", "blocked_shots", "shots"],), use_container_width=True)
        with preset_c5:
            st.button("🔍 Todas las Métricas (14)", on_click=set_metrics, args=(list(ALL_COMPARISON_METRICS.keys()),), use_container_width=True)

        metric_display_names = {k: f"{v[3]} | {v[0]}" for k, v in ALL_COMPARISON_METRICS.items()}
        selected_metric_keys = st.multiselect(
            "Selecciona o modifica las estadísticas individuales que deseas ver:",
            options=list(ALL_COMPARISON_METRICS.keys()),
            format_func=lambda k: metric_display_names[k],
            key="mc_dynamic_metrics_selector"
        )
        
        # Determine which specific match stats to plot (per-match data, zero sums/averages)
        if is_finished:
            match_data_for_chart = current_match
            st.caption(f"✅ Mostrando estadísticas oficiales individuales del partido: {current_match['date']} ({current_match['home_team']} {int(current_match['barca_score'])}-{int(current_match['opp_score'])} {current_match['away_team']})")
        else:
            # If match is scheduled, let user pick which specific past duel to inspect
            if h2h['total_matches'] > 0:
                past_match_options = []
                for _, pm in h2h['matches_df'].iterrows():
                    stg = str(pm['stage']) if pd.notna(pm['stage']) else 'Oficial'
                    h_sc = int(pm['barca_score'] if pm['is_barca_home'] else pm['opp_score'])
                    a_sc = int(pm['opp_score'] if pm['is_barca_home'] else pm['barca_score'])
                    past_match_options.append((pm['match_id'], f"📅 {pm['date']} | {pm['competition']} ({stg}): {pm['home_team']} {h_sc} - {a_sc} {pm['away_team']}"))
                
                sel_past_match_tuple = st.selectbox(
                    f"⏳ Este partido está programado ({current_match['date']}). Selecciona un duelo previo específico para ver sus estadísticas individuales:",
                    past_match_options,
                    format_func=lambda x: x[1],
                    key=f"mc_scheduled_picker_{selected_match_id}"
                )
                match_data_for_chart = h2h['matches_df'][h2h['matches_df']['match_id'] == sel_past_match_tuple[0]].iloc[0]
            else:
                st.info(f"⏳ Encuentro programado para el {current_match['date']} sin enfrentamientos previos en la base de datos.")
                match_data_for_chart = current_match

        if selected_metric_keys and not match_data_for_chart.empty:
            # Comparative Bars (Individual Match Stats)
            st.plotly_chart(create_match_comparison_bars(match_data_for_chart, selected_metric_keys), use_container_width=True)
            
            # Active Stat Metric Chips
            st.markdown("##### 📌 Desglose de Estadísticas de este Partido")
            chips_cols = st.columns(min(4, max(2, len(selected_metric_keys))))
            for idx, k in enumerate(selected_metric_keys):
                col_idx = idx % len(chips_cols)
                meta = ALL_COMPARISON_METRICS[k]
                m_label, b_field, o_field = meta[0], meta[1], meta[2]
                b_val = match_data_for_chart.get(b_field, 0)
                o_val = match_data_for_chart.get(o_field, 0)
                b_val_str = "0" if pd.isna(b_val) else str(b_val)
                o_val_str = "0" if pd.isna(o_val) else str(o_val)
                
                with chips_cols[col_idx]:
                    st.markdown(f"""
                        <div class="metric-card" style="padding: 10px 14px; margin-bottom: 8px;">
                            <div class="metric-title" style="font-size: 0.8rem;">{m_label}</div>
                            <div style="display: flex; justify-content: space-between; align-items: baseline; margin-top: 4px;">
                                <span style="color: #EDBB00; font-size: 1.2rem; font-weight: 800;">{b_val_str}</span>
                                <span style="color: #94A3B8; font-size: 0.75rem;">vs</span>
                                <span style="color: #94A3B8; font-size: 1.1rem; font-weight: 700;">{o_val_str}</span>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Selecciona al menos una estadística para generar la comparativa.")

        # -------------------------------------------------------------
        # ROW 3: INFORMACIÓN DESGLOSADA PARTIDO POR PARTIDO
        # -------------------------------------------------------------
        st.markdown("---")
        st.markdown(f"### 🔍 Información Desglosada Partido por Partido vs {opponent_name}")
        st.markdown("Historial individualizado con todas las métricas tácticas y arbitrales de cada enfrentamiento disputado:")
        
        if h2h['total_matches'] > 0:
            for idx, h_match in h2h['matches_df'].iterrows():
                res_badge = "🟢 Victoria" if h_match['result'] == 'W' else ("🟡 Empate" if h_match['result'] == 'D' else "🔴 Derrota")
                stage_label = f"{h_match['season']} - {h_match['competition']} ({h_match['stage'] or 'Jornada'})"
                v_name = str(h_match['venue']) if pd.notna(h_match['venue']) and str(h_match['venue']).lower() not in ['nan', 'none', ''] else 'Estadio Oficial'
                ref_name = str(h_match['referee']) if pd.notna(h_match['referee']) and str(h_match['referee']).lower() not in ['nan', 'none', ''] else 'Árbitro Oficial'
                notes_name = str(h_match['notes']) if pd.notna(h_match['notes']) and str(h_match['notes']).lower() not in ['nan', 'none', ''] else 'Sin incidencias'
                
                with st.expander(f"📅 {h_match['date']} | {stage_label} | Marcador: {int(h_match['barca_score'])} - {int(h_match['opp_score'])} ({res_badge})"):
                    col_d1, col_d2, col_d3 = st.columns(3)
                    with col_d1:
                        st.markdown(f"""
                            <b>📌 Datos Generales:</b><br>
                            • <b>Estadio:</b> {v_name}<br>
                            • <b>Condición:</b> {'Local (Camp Nou/Montjuïc)' if h_match['is_barca_home'] else 'Visitante'}<br>
                            • <b>Árbitro:</b> {ref_name}<br>
                            • <b>Notas:</b> {notes_name}
                        """, unsafe_allow_html=True)
                    with col_d2:
                        st.markdown(f"""
                            <b>⚽ Ataque y Posesión:</b><br>
                            • <b>Posesión:</b> {h_match.get('barca_possession', 50)}% vs {h_match.get('opp_possession', 50)}%<br>
                            • <b>Expected Goals (xG):</b> {h_match.get('barca_xg', 0)} vs {h_match.get('opp_xg', 0)}<br>
                            • <b>Tiros Totales:</b> {h_match.get('barca_shots', 0)} vs {h_match.get('opp_shots', 0)}<br>
                            • <b>Tiros a Puerta:</b> {h_match.get('barca_shots_on_target', 0)} vs {h_match.get('opp_shots_on_target', 0)}<br>
                            • <b>Grandes Ocasiones:</b> {h_match.get('barca_big_chances', 0)} vs {h_match.get('opp_big_chances', 0)}
                        """, unsafe_allow_html=True)
                    with col_d3:
                        st.markdown(f"""
                            <b>🛡️ Defensa, Faltas y Disciplina:</b><br>
                            • <b>Faltas Cometidas:</b> {h_match.get('barca_fouls', 0)} vs {h_match.get('opp_fouls', 0)}<br>
                            • <b>Tarjetas (A/R):</b> {h_match.get('barca_yellow_cards', 0)}/{h_match.get('barca_red_cards', 0)} vs {h_match.get('opp_yellow_cards', 0)}/{h_match.get('opp_red_cards', 0)}<br>
                            • <b>Córners:</b> {h_match.get('barca_corners', 0)} vs {h_match.get('opp_corners', 0)}<br>
                            • <b>Fueras de Juego:</b> {h_match.get('barca_offsides', 0)} vs {h_match.get('opp_offsides', 0)}<br>
                            • <b>Paradas:</b> {h_match.get('barca_saves', 0)} vs {h_match.get('opp_saves', 0)}
                        """, unsafe_allow_html=True)

# =====================================================================
# TAB 2: MOMENTUM & PROGRESIÓN DE TEMPORADAS (SLIDER DINÁMICO ARRIBA)
# =====================================================================
with tab2:
    st.subheader("📈 Comparativas de Momentum & Trayectoria Multi-Temporada")
    st.markdown("Compara la trayectoria y el momentum jornada a jornada entre las temporadas **2024/25** (88 pts), **2025/26** (94 pts) y **2026/27**.")
    
    col_mom_top1, col_mom_top2 = st.columns([1.2, 2.8])
    with col_mom_top1:
        comp_for_momentum = st.selectbox("Torneo para Análisis", ["LaLiga", "Champions League"], key="mom_comp")
    
    jornada_max = 38 if comp_for_momentum == "LaLiga" else 8
    
    with col_mom_top2:
        selected_jornada = st.slider(
            "🔍 Filtrar Evolución hasta la Jornada / Matchday:",
            min_value=1,
            max_value=jornada_max,
            value=jornada_max,
            key="mom_slider",
            help="Mueve el deslizador para actualizar las gráficas y comparar el rendimiento acumulado hasta esa jornada específica."
        )
    
    # Calculate progression and slice up to selected_jornada
    prog_dict_full = get_multi_season_progression(df_all, competition=comp_for_momentum)
    prog_dict_filtered = {}
    
    for s_k, df_s in prog_dict_full.items():
        if df_s is not None and not df_s.empty:
            prog_dict_filtered[s_k] = df_s[df_s['jornada'] <= selected_jornada].copy()
        else:
            prog_dict_filtered[s_k] = pd.DataFrame()
    
    st.caption(f"📊 Mostrando datos y evolución acumulada desde la **Jornada 1 hasta la Jornada {selected_jornada}**.")
    
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.plotly_chart(create_multi_season_points_chart(prog_dict_filtered, max_jornada=selected_jornada), use_container_width=True)
    with col_chart2:
        st.plotly_chart(create_xg_differential_chart(prog_dict_filtered, max_jornada=selected_jornada), use_container_width=True)
        
    st.plotly_chart(create_momentum_chart(prog_dict_filtered, max_jornada=selected_jornada), use_container_width=True)
    
    # Comparison snapshot at exact Matchday N
    st.markdown("---")
    st.markdown(f"#### 📌 Foto Fija del Rendimiento en la Jornada {selected_jornada}")
    
    col_j1, col_j2, col_j3 = st.columns(3)
    
    for idx, (s_name, s_col) in enumerate([("2024-25", col_j1), ("2025-26", col_j2), ("2026-27", col_j3)]):
        df_s = prog_dict_full.get(s_name)
        with s_col:
            st.markdown(f"##### Temporada {s_name}")
            if df_s is not None and not df_s.empty:
                row_j = df_s[df_s['jornada'] == selected_jornada]
                if not row_j.empty:
                    r = row_j.iloc[0]
                    st.markdown(f"""
                        <div class="metric-card">
                            <div style="font-size: 1.1rem; font-weight: 700; color: #EDBB00;">Jornada {selected_jornada}: vs {r['opponent']}</div>
                            <div style="font-size: 0.85rem; color: #94A3B8; margin-bottom: 8px;">Resultado: <b>{r['barca_score']} - {r['opp_score']}</b> ({r['result']})</div>
                            <hr style="border-color: rgba(255,255,255,0.05); margin: 6px 0;">
                            <div style="font-size: 0.85rem; line-height: 1.7;">
                                <div><b>Puntos Acumulados:</b> <span style="color: #10B981; font-weight: 800;">{r['cum_points']} pts</span></div>
                                <div><b>Goles (F / C):</b> {r['cum_goals_for']} / {r['cum_goals_against']}</div>
                                <div><b>xG Acumulado (F / C):</b> {r['cum_xg_for']:.2f} / {r['cum_xg_against']:.2f}</div>
                                <div><b>Δ xG Acumulado:</b> +{r['cum_xg_diff']:.2f}</div>
                                <div><b>Momentum Score:</b> {r['momentum_score']}/100</div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown(f"""
                        <div class="metric-card" style="opacity: 0.7;">
                            <div style="color: #94A3B8;">Jornada {selected_jornada} no disputada o fuera de rango.</div>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div class="metric-card" style="opacity: 0.7;">
                        <div style="color: #94A3B8;">Sin datos registrados aún.</div>
                    </div>
                """, unsafe_allow_html=True)

# =====================================================================
# TAB 3: PERFIL TÁCTICO & RADAR (CON PUNTOS TOTALES Y PUNTOS/PARTIDO)
# =====================================================================
with tab3:
    st.subheader("🎯 Perfil Táctico Multivariante & Comparativa Radar 360°")
    st.markdown("Evalúa los pilares futbolísticos del Barça (Ataque, Control, Solidez Defensiva, Balón Parado e Intensidad) contrastando puntos y métricas por temporada.")
    
    radar_2425 = compute_team_radar_metrics(df_all, season="2024-25", competition=selected_comp)
    radar_2526 = compute_team_radar_metrics(df_all, season="2025-26", competition=selected_comp)
    radar_2627 = compute_team_radar_metrics(df_all, season="2026-27", competition=selected_comp)
    
    # Prominent Season Points Cards at Top
    st.markdown("#### 🏆 Puntos y Rendimiento General por Temporada")
    pts_c1, pts_c2, pts_c3 = st.columns(3)
    
    with pts_c1:
        pts_24 = radar_2425.get('raw_stats', {}).get('total_points', 88)
        ppg_24 = radar_2425.get('raw_stats', {}).get('points_per_match', 2.32)
        pj_24 = radar_2425.get('raw_stats', {}).get('matches_count', 38)
        st.markdown(f"""
            <div class="metric-card" style="border-top: 4px solid #004D98;">
                <div class="metric-title">TEMPORADA 2024/25 (CAMPEÓN)</div>
                <div style="display: flex; justify-content: space-between; align-items: baseline; margin-top: 8px;">
                    <div>
                        <div style="font-size: 2rem; font-weight: 900; color: #00D2FF;">{pts_24} <span style="font-size: 1rem; color: #94A3B8;">PTS</span></div>
                        <div style="color: #94A3B8; font-size: 0.8rem;">{pj_24} Partidos Disputados</div>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 1.4rem; font-weight: 800; color: #EDBB00;">{ppg_24}</div>
                        <div style="color: #94A3B8; font-size: 0.75rem;">PTS / PARTIDO</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with pts_c2:
        pts_25 = radar_2526.get('raw_stats', {}).get('total_points', 94)
        ppg_25 = radar_2526.get('raw_stats', {}).get('points_per_match', 2.47)
        pj_25 = radar_2526.get('raw_stats', {}).get('matches_count', 38)
        st.markdown(f"""
            <div class="metric-card" style="border-top: 4px solid #EDBB00;">
                <div class="metric-title">TEMPORADA 2025/26 (CAMPEÓN)</div>
                <div style="display: flex; justify-content: space-between; align-items: baseline; margin-top: 8px;">
                    <div>
                        <div style="font-size: 2rem; font-weight: 900; color: #EDBB00;">{pts_25} <span style="font-size: 1rem; color: #94A3B8;">PTS</span></div>
                        <div style="color: #94A3B8; font-size: 0.8rem;">{pj_25} Partidos Disputados</div>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 1.4rem; font-weight: 800; color: #10B981;">{ppg_25}</div>
                        <div style="color: #94A3B8; font-size: 0.75rem;">PTS / PARTIDO</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with pts_c3:
        pts_26 = radar_2627.get('raw_stats', {}).get('total_points', 0)
        ppg_26 = radar_2627.get('raw_stats', {}).get('points_per_match', 0.0)
        pj_26 = radar_2627.get('raw_stats', {}).get('matches_count', 0)
        st.markdown(f"""
            <div class="metric-card" style="border-top: 4px solid #A50044;">
                <div class="metric-title">TEMPORADA 2026/27 (EN CURSO)</div>
                <div style="display: flex; justify-content: space-between; align-items: baseline; margin-top: 8px;">
                    <div>
                        <div style="font-size: 2rem; font-weight: 900; color: #A50044;">{pts_26} <span style="font-size: 1rem; color: #94A3B8;">PTS</span></div>
                        <div style="color: #94A3B8; font-size: 0.8rem;">{pj_26} Partidos Disputados</div>
                    </div>
                    <div style="text-align: right;">
                        <div style="font-size: 1.4rem; font-weight: 800; color: #EDBB00;">{ppg_26}</div>
                        <div style="color: #94A3B8; font-size: 0.75rem;">PTS / PARTIDO</div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    col_rad1, col_rad2 = st.columns([1.05, 0.95])
    
    radar_list = [
        ("Temporada 2024-25 (88 pts)", COLOR_BARCA_BLUE, radar_2425),
        ("Temporada 2025-26 (94 pts)", COLOR_BARCA_GOLD, radar_2526),
        ("Temporada 2026-27 (En Curso)", COLOR_BARCA_GARNET, radar_2627)
    ]
    
    with col_rad1:
        st.plotly_chart(create_radar_comparison_chart(radar_list), use_container_width=True)
        
    with col_rad2:
        st.markdown("#### 📋 Métricas y Puntos por Temporada")
        
        stat_rows = []
        for s_label, _, rdata in radar_list:
            if rdata and 'raw_stats' in rdata and rdata['raw_stats']['matches_count'] > 0:
                raw = rdata['raw_stats']
                stat_rows.append({
                    "Temporada": s_label,
                    "Partidos": int(raw.get('matches_count', 0)),
                    "Puntos Totales": int(raw.get('total_points', 0)),
                    "Pts / PJ": float(raw.get('points_per_match', 0.0)),
                    "Goles / PJ": float(raw.get('goals_per_match', 0.0)),
                    "xG / PJ": float(raw.get('xg_per_match', 0.0)),
                    "Tiros Puerta": float(raw.get('sot_per_match', 0.0)),
                    "Posesión %": f"{raw.get('possession', 0.0)}%",
                    "xGA (concedido)": float(raw.get('xga_per_match', 0.0)),
                    "Córners": float(raw.get('corners_per_match', 0.0))
                })
            else:
                stat_rows.append({
                    "Temporada": s_label,
                    "Partidos": 0,
                    "Puntos Totales": 0,
                    "Pts / PJ": 0.0,
                    "Goles / PJ": 0.0,
                    "xG / PJ": 0.0,
                    "Tiros Puerta": 0.0,
                    "Posesión %": "0.0%",
                    "xGA (concedido)": 0.0,
                    "Córners": 0.0
                })
                
        if stat_rows:
            df_radar_table = pd.DataFrame(stat_rows).set_index("Temporada")
            st.dataframe(df_radar_table, use_container_width=True)
        else:
            st.info("Sin datos para calcular el perfil táctico.")

# =====================================================================
# TAB 4: HISTORIAL DE PARTIDOS COMPLETO
# =====================================================================
with tab4:
    st.subheader("📋 Base de Datos de Encuentros (24/25, 25/26 & 26/27)")
    
    col_f1, col_f2, col_f3, col_f4 = st.columns(4)
    with col_f1:
        f_season = st.selectbox("Filtrar Temporada", ["Todas", "2026-27", "2025-26", "2024-25"], key="hist_s")
    with col_f2:
        f_comp = st.selectbox("Filtrar Competición", ["Todas", "LaLiga", "Champions League", "Copa del Rey", "Supercopa"], key="hist_c")
    with col_f3:
        f_res = st.selectbox("Filtrar Resultado", ["Todos", "Victorias (W)", "Empates (D)", "Derrotas (L)"], key="hist_r")
    with col_f4:
        f_opp = st.selectbox("Filtrar Rival", ["Todos"] + db.get_opponents(), key="hist_opp")
        
    df_table = df_all.copy()
    if f_season != "Todas":
        df_table = df_table[df_table['season'] == f_season]
    if f_comp != "Todas":
        df_table = df_table[df_table['competition'] == f_comp]
    if f_res != "Todos":
        code = f_res.split("(")[1][0]
        df_table = df_table[df_table['result'] == code]
    if f_opp != "Todos":
        df_table = df_table[df_table['opponent'] == f_opp]
        
    display_cols = [
        'date', 'season', 'competition', 'stage', 'opponent', 'is_barca_home', 
        'barca_score', 'opp_score', 'result', 'barca_xg', 'opp_xg', 
        'barca_possession', 'barca_shots_on_target', 'barca_corners', 'barca_fouls'
    ]
    
    st.dataframe(
        df_table[display_cols].rename(columns={
            'date': 'Fecha',
            'season': 'Temporada',
            'competition': 'Torneo',
            'stage': 'Fase/Jornada',
            'opponent': 'Rival',
            'is_barca_home': 'Local',
            'barca_score': 'Goles Barça',
            'opp_score': 'Goles Rival',
            'result': 'Res.',
            'barca_xg': 'xG Barça',
            'opp_xg': 'xG Rival',
            'barca_possession': 'Posesión %',
            'barca_shots_on_target': 'Tiros Puerta',
            'barca_corners': 'Córners',
            'barca_fouls': 'Faltas'
        }),
        use_container_width=True,
        height=450
    )
    
    csv_data = df_table.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Descargar Datos en CSV",
        data=csv_data,
        file_name="barca_matches_analytics.csv",
        mime="text/csv"
    )

# =====================================================================
# TAB 5: AGENTE DE SINCRONIZACIÓN AUTOMÁTICA & LIMPIEZA (ROLE PROTECTED)
# =====================================================================
with tab5:
    st.subheader("🤖 Agente de Sincronización Automática & Limpieza de Datos")
    
    if user_role != "ADMIN":
        render_tab5_admin_prompt()
    else:
        st.markdown("""
            Este módulo mantiene la base de datos sincronizada y validada automáticamente sin captura manual.
            Como **Administrador**, puedes sincronizar la próxima jornada o ejecutar una auditoría completa de datos oficiales.
        """)
        
        col_ag1, col_ag2 = st.columns([1.15, 0.85])
        
        with col_ag1:
            st.markdown("#### ⚡ Acciones del Agente de Sincronización")
            
            pending_matches = sync_agent.get_pending_matches("2026-27")
            
            if pending_matches.empty:
                st.success("🎉 Todos los partidos programados de la temporada 2026/27 han sido sincronizados.")
            else:
                next_m = pending_matches.iloc[0]
                st.info(f"⏳ **Próximo Partido a Sincronizar**: {next_m['stage']} vs **{next_m['opponent']}** ({'Local' if next_m['is_barca_home'] else 'Visitante'}) - 📅 {next_m['date']}")
                
                col_b1, col_b2 = st.columns(2)
                with col_b1:
                    if st.button("🚀 Sincronizar Próxima Jornada Ahora", use_container_width=True):
                        with st.spinner("Agente extrayendo estadísticas oficiales..."):
                            sync_res = sync_agent.sync_next_matchday("2026-27")
                            if sync_res:
                                st.success(f"✅ ¡Partido vs {sync_res['opponent']} sincronizado! Marcador: {sync_res['score']} (xG: {sync_res['xg']})")
                                st.rerun()
                with col_b2:
                    if st.button("⏩ Sincronizar Primeras 5 Jornadas", use_container_width=True):
                        with st.spinner("Sincronizando lote de jornadas con el agente..."):
                            for _ in range(5):
                                sync_agent.sync_next_matchday("2026-27")
                            st.success("✅ ¡5 Jornadas sincronizadas exitosamente en la base de datos!")
                            st.rerun()

            st.markdown("---")
            st.markdown("#### 🧹 Auditoría y Limpieza Completa de Datos")
            st.markdown("Vuelve a ejecutar la auditoría de fuentes oficiales (LaLiga, UEFA, Wikipedia, Transfermarkt) para verificar y limpiar todos los partidos de 2024/25, 2025/26 y 2026/27.")
            if st.button("🔄 Ejecutar Auditoría y Limpieza de Base de Datos"):
                with st.spinner("Limpiando y validando integridad de datos..."):
                    cleaner = DataCleanerEngine("barca_analytics.db")
                    res = cleaner.audit_and_clean_all()
                    st.success(f"✅ ¡Base de datos limpia y verificada! Total: {res['total_matches']} partidos auditados.")
                    st.rerun()

        with col_ag2:
            st.markdown("#### 📋 Partidos Sincronizados de la Temporada 26/27")
            synced_2627 = df_all[(df_all['season'] == '2026-27') & (df_all['status'] == 'FINISHED')].sort_values('date', ascending=False)
            
            if synced_2627.empty:
                st.info("Aún no hay partidos finalizados en 2026/27. Pulsa en 'Sincronizar Próxima Jornada' para registrar el primer encuentro.")
            else:
                for _, s_m in synced_2627.iterrows():
                    res_class = "badge-win" if s_m['result'] == 'W' else ("badge-draw" if s_m['result'] == 'D' else "badge-loss")
                    st.markdown(f"""
                        <div style="background: rgba(18, 26, 44, 0.7); padding: 12px; border-radius: 10px; margin-bottom: 8px; border: 1px solid rgba(255,255,255,0.05);">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <div>
                                    <b>{s_m['stage']} vs {s_m['opponent']}</b><br>
                                    <span style="font-size: 0.8rem; color: #94A3B8;">📅 {s_m['date']} • xG: {s_m.get('barca_xg', 0)} - {s_m.get('opp_xg', 0)}</span>
                                </div>
                                <div style="text-align: right;">
                                    <span style="font-size: 1.2rem; font-weight: 800; color: #EDBB00;">{s_m['barca_score']} - {s_m['opp_score']}</span>
                                    <div><span class="{res_class}">{s_m['result']}</span></div>
                                </div>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
