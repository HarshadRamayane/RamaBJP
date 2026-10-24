"""
RamaBJP — Predictive Maintenance for Defence Equipment
Main application entry point (Login Removed).
"""

import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="RAMEDOX | Predictive Maintenance",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# SIDEBAR
# ============================================================
from components.sidebar import render_sidebar
page = render_sidebar()

# ============================================================
# ROUTING
# ============================================================
if page == "🏠 Dashboard":
    from pages.dashboard_overview import render_dashboard_overview
    render_dashboard_overview()

elif page == "🚜 Equipment Management":
    from pages.equipment import render_equipment
    render_equipment()

elif page == "📡 Sensor Monitoring":
    from config.theme import get_custom_css
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    from pages.sensors import render_sensors
    render_sensors()

elif page == "📥 Data Import & Ingestion":
    from config.theme import get_custom_css
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    from pages.import_data import render_import
    render_import()

elif page == "⚙️ Rules & Analysis":
    st.info("Rules & Analysis page coming soon...")

elif page == "🔔 Alerts & Notifications":
    from config.theme import get_custom_css
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    from pages.alerts import render_alerts
    render_alerts()

elif page == "🛠️ Maintenance Management":
    from config.theme import get_custom_css
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    from pages.maintenance import render_maintenance
    render_maintenance()

elif page == "📈 Analytics & Trends":
    from config.theme import get_custom_css
    st.markdown(get_custom_css(), unsafe_allow_html=True)
    from pages.analytics import render_analytics
    render_analytics()

elif page == "📄 Reports":
    from pages.reports import render_reports
    render_reports()
    
elif page == "⚙️ Settings":
    st.info("Settings page coming soon...")

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6C757D; font-size: 12px; padding: 10px;">
    RAMEDOX | Predictive Maintenance for Defence Equipment | Software Proof of Concept | 2026
</div>
""", unsafe_allow_html=True)