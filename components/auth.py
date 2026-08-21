"""
Authentication and Role-Based Access Control (RBAC) for Barca Analytics Hub.
Zero-friction architecture:
- Public/Guest access by default (Read-only Viewer mode).
- In-place Admin Login via sidebar or Tab 5 to unlock sync and database management tools.
"""

import streamlit as st
import os

# Default fallback credentials (can be overridden via .streamlit/secrets.toml)
DEFAULT_ADMIN_USER = "admin"
DEFAULT_ADMIN_PASS = "barca2026"

def get_admin_credentials():
    """Retrieves admin credentials from Streamlit secrets or default fallback."""
    admin_user = DEFAULT_ADMIN_USER
    admin_pass = DEFAULT_ADMIN_PASS

    if hasattr(st, "secrets") and "auth" in st.secrets:
        admin_user = st.secrets["auth"].get("admin_user", DEFAULT_ADMIN_USER)
        admin_pass = st.secrets["auth"].get("admin_pass", DEFAULT_ADMIN_PASS)

    return admin_user, admin_pass


def render_auth_sidebar() -> str:
    """
    Renders user status and admin login in the sidebar.
    Returns: 'ADMIN' if authenticated as admin, otherwise 'VIEWER'.
    """
    if "user_role" not in st.session_state:
        st.session_state["user_role"] = "VIEWER"

    admin_user, admin_pass = get_admin_credentials()
    is_admin = (st.session_state.get("user_role") == "ADMIN")

    with st.sidebar:
        st.markdown("---")
        if is_admin:
            st.markdown("""
                <div style="background: rgba(237, 187, 0, 0.15); border: 1px solid #EDBB00; padding: 10px 12px; border-radius: 10px; margin-bottom: 10px; text-align: center;">
                    <div style="font-size: 0.75rem; color: #94A3B8; font-weight: 600;">SESIÓN ACTIVA</div>
                    <div style="font-size: 0.85rem; font-weight: 800; color: #EDBB00; margin-top: 2px;">⚡ ADMINISTRADOR</div>
                    <div style="font-size: 0.7rem; color: #10B981; margin-top: 2px;">Control Total & Sync Habilitado</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("🚪 Cerrar Sesión de Admin", use_container_width=True, key="sb_btn_logout"):
                st.session_state["user_role"] = "VIEWER"
                st.rerun()
        else:
            st.markdown("""
                <div style="background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.3); padding: 8px 12px; border-radius: 10px; margin-bottom: 10px; text-align: center;">
                    <div style="font-size: 0.75rem; color: #94A3B8; font-weight: 600;">MODO ACTUAL</div>
                    <div style="font-size: 0.85rem; font-weight: 700; color: #38BDF8; margin-top: 1px;">👥 Modo Visualización</div>
                </div>
            """, unsafe_allow_html=True)
            
            with st.expander("🔐 Iniciar Sesión como Admin", expanded=False):
                inp_user = st.text_input("Usuario", key="sb_admin_user", placeholder="admin")
                inp_pass = st.text_input("Contraseña", type="password", key="sb_admin_pass", placeholder="Contraseña...")
                if st.button("⚡ Ingresar como Admin", use_container_width=True, key="sb_btn_login"):
                    if inp_user == admin_user and inp_pass == admin_pass:
                        st.session_state["user_role"] = "ADMIN"
                        st.success("¡Sesión de Administrador iniciada!")
                        st.rerun()
                    else:
                        st.error("Credenciales inválidas.")

    return st.session_state["user_role"]


def render_tab5_admin_prompt():
    """Renders an inline login prompt on Tab 5 when accessed by a viewer."""
    admin_user, admin_pass = get_admin_credentials()
    
    st.markdown("""
        <div style="background: rgba(237, 187, 0, 0.1); border: 1px solid rgba(237, 187, 0, 0.3); padding: 20px; border-radius: 14px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 12px;">
                <div style="font-size: 2.2rem;">🔒</div>
                <div>
                    <h4 style="color: #EDBB00; margin: 0 0 4px 0;">Acceso Restringido para Administrador</h4>
                    <p style="color: #94A3B8; margin: 0; font-size: 0.88rem;">
                        La sincronización automática de partidos y las herramientas de auditoría requieren permisos de Administrador. 
                        Inicia sesión a continuación para habilitar estas funciones:
                    </p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    col_c1, col_c2, col_c3 = st.columns([1, 1.8, 1])
    with col_c2:
        st.markdown("<div style='background: rgba(18, 26, 44, 0.7); padding: 18px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.08);'>", unsafe_allow_html=True)
        inp_u = st.text_input("Usuario Administrador", key="tab5_admin_user", placeholder="admin")
        inp_p = st.text_input("Contraseña de Administrador", type="password", key="tab5_admin_pass", placeholder="Contraseña...")
        if st.button("🚀 Iniciar Sesión y Desbloquear Sync", use_container_width=True, key="tab5_btn_login"):
            if inp_u == admin_user and inp_p == admin_pass:
                st.session_state["user_role"] = "ADMIN"
                st.success("¡Acceso de Administrador concedido!")
                st.rerun()
            else:
                st.error("❌ Credenciales inválidas.")
        st.markdown("</div>", unsafe_allow_html=True)
