"""
Barça Custom UI Theme & CSS Styler.
Provides Blaugrana styling, glowing cards, glassmorphism, and responsive badges.
"""

import streamlit as st

def apply_barca_theme():
    """Injects custom CSS styling for FC Barcelona aesthetic."""
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;900&display=swap');

        html, body, [class*="css"] {
            font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
        }

        /* Main background & container */
        .stApp {
            background: linear-gradient(145deg, #090e17 0%, #0d1527 50%, #150914 100%);
            color: #E2E8F0;
        }

        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #080c14 !important;
            border-right: 1px solid rgba(165, 0, 68, 0.25);
        }

        /* Custom Header Banner */
        .barca-banner {
            background: linear-gradient(90deg, #A50044 0%, #004D98 100%);
            padding: 22px 28px;
            border-radius: 16px;
            box-shadow: 0 8px 32px rgba(165, 0, 68, 0.25);
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border: 1px solid rgba(237, 187, 0, 0.3);
        }
        
        .barca-banner h1 {
            color: #FFFFFF;
            font-weight: 900;
            font-size: 2.2rem;
            margin: 0;
            letter-spacing: -0.5px;
            text-shadow: 0 2px 10px rgba(0,0,0,0.5);
        }
        
        .barca-banner p {
            color: #EDBB00;
            margin: 4px 0 0 0;
            font-size: 1.05rem;
            font-weight: 600;
            letter-spacing: 0.5px;
        }

        /* Metric Cards */
        .metric-card {
            background: rgba(18, 26, 44, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 16px 20px;
            backdrop-filter: blur(12px);
            transition: all 0.2s ease-in-out;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
        }
        .metric-card:hover {
            border-color: rgba(237, 187, 0, 0.5);
            transform: translateY(-2px);
        }
        .metric-title {
            color: #94A3B8;
            font-size: 0.85rem;
            text-transform: uppercase;
            font-weight: 600;
            letter-spacing: 1px;
        }
        .metric-value {
            color: #F8FAFC;
            font-size: 1.8rem;
            font-weight: 800;
            margin-top: 4px;
        }
        .metric-delta {
            font-size: 0.85rem;
            font-weight: 600;
        }
        .delta-pos { color: #10B981; }
        .delta-neg { color: #EF4444; }

        /* Match Score Banner */
        .match-score-card {
            background: linear-gradient(135deg, rgba(13, 22, 40, 0.9) 0%, rgba(26, 12, 28, 0.9) 100%);
            border: 1px solid rgba(237, 187, 0, 0.2);
            border-radius: 16px;
            padding: 24px;
            margin: 15px 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        /* Badges */
        .badge-win {
            background-color: #059669;
            color: #FFFFFF;
            padding: 4px 10px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 0.85rem;
        }
        .badge-draw {
            background-color: #D97706;
            color: #FFFFFF;
            padding: 4px 10px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 0.85rem;
        }
        .badge-loss {
            background-color: #DC2626;
            color: #FFFFFF;
            padding: 4px 10px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 0.85rem;
        }

        /* Tabs styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px;
        }
        .stTabs [data-baseweb="tab"] {
            background-color: rgba(18, 26, 44, 0.6);
            border-radius: 10px;
            padding: 10px 20px;
            border: 1px solid rgba(255, 255, 255, 0.05);
            color: #94A3B8;
            font-weight: 600;
        }
        .stTabs [aria-selected="true"] {
            background: linear-gradient(90deg, #A50044 0%, #004D98 100%) !important;
            color: #FFFFFF !important;
            border: 1px solid #EDBB00 !important;
        }

        /* Custom buttons */
        .stButton>button {
            border-radius: 10px;
            font-weight: 700;
            border: none;
            transition: all 0.2s;
        }
        .stButton>button:hover {
            box-shadow: 0 0 15px rgba(237, 187, 0, 0.4);
        }
        </style>
    """, unsafe_allow_html=True)
