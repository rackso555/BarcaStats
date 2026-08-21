"""
Plotly Chart Generators for Barça Analytics Hub.
All charts are 100% interactive, responsive, and follow the Blaugrana color palette.
Supports customizable metric toggles, dynamic slider constraints, and non-overlapping layouts.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# Blaugrana Color Palette Constants
COLOR_BARCA_GARNET = "#A50044"
COLOR_BARCA_BLUE = "#004D98"
COLOR_BARCA_GOLD = "#EDBB00"
COLOR_BARCA_CYAN = "#00D2FF"
COLOR_OPPONENT = "#64748B"
COLOR_OPPONENT_BORDER = "#94A3B8"
COLOR_DARK_BG = "#0c1322"
COLOR_CARD_BG = "#131c2e"
COLOR_GRID = "rgba(255, 255, 255, 0.08)"

# All 14 available comparison metrics with display metadata
ALL_COMPARISON_METRICS = {
    "xg": ("Expected Goals (xG)", "barca_xg", "opp_xg", "🎯 Ataque"),
    "shots": ("Tiros Totales", "barca_shots", "opp_shots", "🎯 Ataque"),
    "sot": ("Tiros a Puerta", "barca_shots_on_target", "opp_shots_on_target", "🎯 Ataque"),
    "shots_off": ("Tiros Fuera", "barca_shots_off_target", "opp_shots_off_target", "🎯 Ataque"),
    "big_chances": ("Grandes Ocasiones", "barca_big_chances", "opp_big_chances", "🎯 Ataque"),
    "possession": ("Posesión (%)", "barca_possession", "opp_possession", "✨ Control"),
    "pass_acc": ("Precisión de Pase (%)", "barca_pass_acc", "opp_pass_acc", "✨ Control"),
    "blocked_shots": ("Tiros Bloqueados", "barca_blocked_shots", "opp_blocked_shots", "✨ Control"),
    "corners": ("Córners", "barca_corners", "opp_corners", "🛡️ Balón Parado"),
    "fouls": ("Faltas Cometidas", "barca_fouls", "opp_fouls", "🛡️ Disciplina"),
    "yellow_cards": ("Tarjetas Amarillas", "barca_yellow_cards", "opp_yellow_cards", "🛡️ Disciplina"),
    "red_cards": ("Tarjetas Rojas", "barca_red_cards", "opp_red_cards", "🛡️ Disciplina"),
    "offsides": ("Fueras de Juego Provocados", "opp_offsides", "barca_offsides", "🛡️ Defensa"),
    "saves": ("Paradas de Portero", "barca_saves", "opp_saves", "🛡️ Portería")
}

def get_base_layout(title: str = "", height: int = 420):
    return go.Layout(
        title=dict(
            text=title,
            font=dict(color="#F8FAFC", size=15, family="Outfit, sans-serif"),
            x=0.01,
            y=0.98
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=height,
        margin=dict(l=45, r=30, t=55, b=55),
        legend=dict(
            font=dict(color="#CBD5E1", size=11),
            bgcolor="rgba(18, 26, 44, 0.85)",
            bordercolor="rgba(255, 255, 255, 0.12)",
            borderwidth=1,
            orientation="h",
            yanchor="top",
            y=-0.22,
            xanchor="center",
            x=0.5
        ),
        xaxis=dict(
            gridcolor=COLOR_GRID,
            zerolinecolor=COLOR_GRID,
            tickfont=dict(color="#94A3B8", size=11),
            automargin=True
        ),
        yaxis=dict(
            gridcolor=COLOR_GRID,
            zerolinecolor=COLOR_GRID,
            tickfont=dict(color="#94A3B8", size=11),
            automargin=True
        )
    )


def create_match_comparison_bars(match_row: pd.Series, selected_metric_keys: list = None) -> go.Figure:
    """
    Horizontal comparison bars for a single match with customizable metric filters.
    Labels and numbers are strictly non-overlapping and highly legible.
    """
    if not selected_metric_keys:
        selected_metric_keys = ["xg", "shots", "sot", "possession", "corners", "fouls", "pass_acc", "big_chances"]

    labels = []
    barca_vals = []
    opp_vals = []
    
    for k in selected_metric_keys:
        if k in ALL_COMPARISON_METRICS:
            meta = ALL_COMPARISON_METRICS[k]
            name, b_col, o_col = meta[0], meta[1], meta[2]
            labels.append(name)
            b_val = match_row.get(b_col, 0)
            o_val = match_row.get(o_col, 0)
            barca_vals.append(0.0 if pd.isna(b_val) else round(float(b_val), 2))
            opp_vals.append(0.0 if pd.isna(o_val) else round(float(o_val), 2))

    opp_name = match_row.get('opponent', 'Rival')

    fig = go.Figure()
    
    # Trace for FC Barcelona
    fig.add_trace(go.Bar(
        y=labels,
        x=barca_vals,
        name="FC Barcelona",
        orientation='h',
        marker=dict(
            color=COLOR_BARCA_GARNET,
            line=dict(color=COLOR_BARCA_GOLD, width=1.5)
        ),
        text=[f" {v}" for v in barca_vals],
        textposition='auto',
        textfont=dict(color="#FFFFFF", size=12, family="Outfit, sans-serif")
    ))
    
    # Trace for Opponent
    fig.add_trace(go.Bar(
        y=labels,
        x=opp_vals,
        name=str(opp_name),
        orientation='h',
        marker=dict(
            color=COLOR_OPPONENT,
            line=dict(color=COLOR_OPPONENT_BORDER, width=1.5)
        ),
        text=[f" {v}" for v in opp_vals],
        textposition='auto',
        textfont=dict(color="#FFFFFF", size=12, family="Outfit, sans-serif")
    ))
    
    calc_height = max(340, len(labels) * 46 + 100)

    fig.update_layout(
        title=dict(
            text=f"📊 Comparativa Lado a Lado: FC Barcelona vs {opp_name}",
            font=dict(color="#F8FAFC", size=15, family="Outfit, sans-serif"),
            x=0.01,
            y=0.98
        ),
        barmode='group',
        bargap=0.25,
        bargroupgap=0.1,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=calc_height,
        margin=dict(l=190, r=40, t=50, b=75),
        legend=dict(
            font=dict(color="#CBD5E1", size=11),
            bgcolor="rgba(18, 26, 44, 0.85)",
            bordercolor="rgba(255, 255, 255, 0.1)",
            borderwidth=1,
            orientation="h",
            yanchor="top",
            y=-0.14,
            xanchor="center",
            x=0.5
        ),
        xaxis=dict(
            gridcolor=COLOR_GRID,
            zerolinecolor=COLOR_GRID,
            tickfont=dict(color="#94A3B8", size=11),
            automargin=True
        ),
        yaxis=dict(
            autorange="reversed",
            tickfont=dict(color="#F1F5F9", size=12, family="Outfit, sans-serif"),
            gridcolor='rgba(0,0,0,0)',
            automargin=True
        )
    )
    return fig


def create_opponent_form_chart(opponent_matches: pd.DataFrame, opponent_name: str) -> go.Figure:
    """Visualizes recent goals and xG evolution against this opponent with legend placed cleanly below."""
    if opponent_matches.empty:
        return go.Figure()

    df = opponent_matches.sort_values('date').tail(6).copy()
    df['match_label'] = df['date'].str[5:] + " (" + df['competition'].str[:3] + ")"
    
    fig = go.Figure()
    
    # Goles Barça
    fig.add_trace(go.Bar(
        x=df['match_label'],
        y=df['barca_score'],
        name="Goles Barça",
        marker=dict(color=COLOR_BARCA_GARNET, line=dict(color=COLOR_BARCA_GOLD, width=1))
    ))
    
    # Goles Rival
    fig.add_trace(go.Bar(
        x=df['match_label'],
        y=df['opp_score'],
        name=f"Goles {opponent_name}",
        marker=dict(color=COLOR_OPPONENT, line=dict(color=COLOR_OPPONENT_BORDER, width=1))
    ))
    
    # xG Barça
    fig.add_trace(go.Scatter(
        x=df['match_label'],
        y=df['barca_xg'],
        name="xG Barça",
        mode="lines+markers",
        line=dict(color=COLOR_BARCA_GOLD, width=2.5),
        marker=dict(size=7, color=COLOR_BARCA_GOLD)
    ))
    
    # xG Rival
    fig.add_trace(go.Scatter(
        x=df['match_label'],
        y=df['opp_xg'],
        name=f"xG {opponent_name}",
        mode="lines+markers",
        line=dict(color="#38BDF8", width=2.5, dash="dot"),
        marker=dict(size=7, color="#38BDF8")
    ))

    fig.update_layout(
        title=dict(
            text=f"📉 Histórico de Goles y xG vs {opponent_name}",
            font=dict(color="#F8FAFC", size=15, family="Outfit, sans-serif"),
            x=0.01,
            y=0.98
        ),
        barmode='group',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=360,
        margin=dict(l=40, r=25, t=45, b=75),
        legend=dict(
            font=dict(color="#CBD5E1", size=10),
            bgcolor="rgba(18, 26, 44, 0.85)",
            bordercolor="rgba(255, 255, 255, 0.1)",
            borderwidth=1,
            orientation="h",
            yanchor="top",
            y=-0.26,
            xanchor="center",
            x=0.5
        ),
        xaxis=dict(
            gridcolor=COLOR_GRID,
            zerolinecolor=COLOR_GRID,
            tickfont=dict(color="#94A3B8", size=10),
            automargin=True
        ),
        yaxis=dict(
            gridcolor=COLOR_GRID,
            zerolinecolor=COLOR_GRID,
            tickfont=dict(color="#94A3B8", size=10),
            automargin=True
        )
    )
    return fig


def create_multi_season_points_chart(progression_dict: dict, max_jornada: int = None) -> go.Figure:
    """Line chart comparing points accumulation across seasons, cropped dynamically by max_jornada."""
    fig = go.Figure(layout=get_base_layout("📈 Trayectoria de Puntos Acumulados por Jornada", height=400))
    
    season_styles = {
        "2024-25": dict(color=COLOR_BARCA_BLUE, width=2.5, dash="dash", name="2024-25 (88 pts - Campeón)"),
        "2025-26": dict(color=COLOR_BARCA_GOLD, width=3, dash="solid", name="2025-26 (94 pts - Campeón)"),
        "2026-27": dict(color=COLOR_BARCA_GARNET, width=4, dash="solid", name="2026-27 (Actual)")
    }
    
    for s, style in season_styles.items():
        df = progression_dict.get(s)
        if df is not None and not df.empty:
            fig.add_trace(go.Scatter(
                x=df['jornada'],
                y=df['cum_points'],
                mode='lines+markers',
                name=style['name'],
                line=dict(color=style['color'], width=style['width'], dash=style['dash']),
                marker=dict(size=6, color=style['color']),
                hovertemplate="<b>Jornada %{x}</b><br>Puntos acumulados: %{y}<br>Rival: " + df['opponent'] + "<extra></extra>"
            ))
            
    x_range = [0.5, max_jornada + 0.5] if max_jornada is not None else None
    dt = 1 if (max_jornada and max_jornada <= 10) else (2 if (max_jornada and max_jornada <= 20) else 4)
    fig.update_xaxes(title_text="Jornada de Liga", range=x_range, dtick=dt)
    fig.update_yaxes(title_text="Puntos Totales")
    return fig


def create_momentum_chart(progression_dict: dict, max_jornada: int = None) -> go.Figure:
    """Momentum Index across matchdays, updating dynamically based on max_jornada slider."""
    fig = go.Figure(layout=get_base_layout("🔥 Índice de Momentum & Forma (Media Móvil 3 Partidos)", height=380))
    
    colors = {"2024-25": "#64748B", "2025-26": COLOR_BARCA_GOLD, "2026-27": "#38BDF8"}
    
    for s, col in colors.items():
        df = progression_dict.get(s)
        if df is not None and not df.empty and 'rolling_momentum_3' in df:
            fig.add_trace(go.Scatter(
                x=df['jornada'],
                y=df['rolling_momentum_3'],
                mode='lines+markers',
                name=f"Temporada {s}",
                line=dict(color=col, width=3),
                marker=dict(size=6, color=col),
                fill='tozeroy' if s == "2026-27" else 'none',
                fillcolor='rgba(56, 189, 248, 0.1)' if s == "2026-27" else None,
                hovertemplate="<b>Jornada %{x}</b><br>Momentum Index: %{y:.1f}/100<extra></extra>"
            ))
            
    x_range = [0.5, max_jornada + 0.5] if max_jornada is not None else None
    dt = 1 if (max_jornada and max_jornada <= 10) else (2 if (max_jornada and max_jornada <= 20) else 4)
    fig.update_xaxes(title_text="Jornada", range=x_range, dtick=dt)
    fig.update_yaxes(title_text="Momentum Score (0-100)", range=[0, 100])
    return fig


def create_xg_differential_chart(progression_dict: dict, max_jornada: int = None) -> go.Figure:
    """Cumulative xG Differential chart, updating dynamically based on max_jornada slider."""
    fig = go.Figure(layout=get_base_layout("🎯 Dominancia de Ocasiones: xG Diferencial Acumulado (xG - xGA)", height=400))
    
    season_styles = {
        "2024-25": dict(color="#94A3B8", name="2024-25"),
        "2025-26": dict(color=COLOR_BARCA_GOLD, name="2025-26"),
        "2026-27": dict(color="#10B981", name="2026-27")
    }
    
    for s, style in season_styles.items():
        df = progression_dict.get(s)
        if df is not None and not df.empty and 'cum_xg_diff' in df:
            fig.add_trace(go.Scatter(
                x=df['jornada'],
                y=df['cum_xg_diff'].round(2),
                mode='lines+markers',
                name=style['name'],
                line=dict(color=style['color'], width=3),
                marker=dict(size=6, color=style['color']),
                hovertemplate="<b>Jornada %{x}</b><br>Δ xG Acumulado: +%{y:.2f}<extra></extra>"
            ))
            
    x_range = [0.5, max_jornada + 0.5] if max_jornada is not None else None
    dt = 1 if (max_jornada and max_jornada <= 10) else (2 if (max_jornada and max_jornada <= 20) else 4)
    fig.update_xaxes(title_text="Jornada", range=x_range, dtick=dt)
    fig.update_yaxes(title_text="Δ xG Acumulado (xG a favor - xG en contra)")
    return fig


def create_radar_comparison_chart(radar_data_list: list) -> go.Figure:
    """
    Radar Chart overlaying multiple profiles.
    radar_data_list: list of tuples (label, color, radar_dict)
    """
    fig = go.Figure()
    
    for label, color, rdata in radar_data_list:
        if not rdata:
            continue
        cats = rdata['categories'] + [rdata['categories'][0]]
        vals = rdata['values'] + [rdata['values'][0]]
        
        fig.add_trace(go.Scatterpolar(
            r=vals,
            theta=cats,
            name=label,
            line=dict(color=color, width=2.5),
            fill='toself',
            fillcolor=f"rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.2)" if color.startswith('#') and len(color)==7 else "rgba(100,100,100,0.2)"
        ))
        
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                gridcolor=COLOR_GRID,
                tickfont=dict(color="#64748B", size=9)
            ),
            angularaxis=dict(
                gridcolor=COLOR_GRID,
                tickfont=dict(color="#F1F5F9", size=11, family="Outfit, sans-serif")
            ),
            bgcolor="rgba(0,0,0,0)"
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        height=450,
        margin=dict(l=50, r=50, t=40, b=40),
        legend=dict(
            font=dict(color="#CBD5E1"),
            orientation="h",
            yanchor="top",
            y=-0.15,
            xanchor="center",
            x=0.5
        )
    )
    return fig
