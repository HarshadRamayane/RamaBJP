"""
RamaBJP Alerts Management Page
"""

import streamlit as st
import pandas as pd
from repositories.alert_repo import (
    get_all_alerts, get_alerts_by_status, get_alerts_by_severity,
    acknowledge_alert, resolve_alert, get_alert_stats
)
from config.theme import COLORS, get_status_badge


def render_alerts():
    """Render the alerts management page."""
    st.markdown("## 🚨 Alerts Management")
    st.markdown("View, acknowledge and resolve maintenance alerts")
    st.markdown("---")
    
    # ============================================================
    # STATS
    # ============================================================
    stats = get_alert_stats()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Alerts", stats["total"])
    with col2:
        st.metric("Open", stats["open"])
    with col3:
        st.metric("Acknowledged", stats["acknowledged"])
    with col4:
        st.metric("Resolved", stats["resolved"])
    
    st.markdown("---")
    
    # ============================================================
    # FILTERS
    # ============================================================
    col1, col2 = st.columns(2)
    with col1:
        status_filter = st.selectbox("Filter by Status", ["All", "OPEN", "ACKNOWLEDGED", "RESOLVED"])
    with col2:
        severity_filter = st.selectbox("Filter by Severity", ["All", "Critical", "Warning"])
    
    # Apply filters
    if status_filter != "All":
        alerts = get_alerts_by_status(status_filter)
    elif severity_filter != "All":
        alerts = get_alerts_by_severity(severity_filter)
    else:
        alerts = get_all_alerts()
    
    st.markdown("---")
    
    # ============================================================
    # ALERTS LIST
    # ============================================================
    if not alerts:
        st.info("No alerts found.")
        return
    
    for alert in alerts:
        severity = alert["severity"]
        status = alert["status"]
        
        severity_color = COLORS["critical"] if severity == "Critical" else COLORS["warning_status"]
        status_color = {
            "OPEN": COLORS["danger"],
            "ACKNOWLEDGED": COLORS["info"],
            "RESOLVED": COLORS["success"]
        }.get(status, COLORS["unknown"])
        
        with st.expander(f"{severity} — {alert.get('equipment_name', alert['equipment_id'])} — {status}"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**Message:** {alert['message']}")
                st.markdown(f"**Equipment:** {alert['equipment_id']} ({alert.get('equipment_name', 'N/A')})")
                st.markdown(f"**Sensor:** {alert.get('sensor_id', 'N/A')}")
                st.markdown(f"**Reading:** {alert.get('reading_value', 'N/A')}")
                st.markdown(f"**Threshold:** {alert.get('threshold_value', 'N/A')}")
                st.markdown(f"**Created:** {alert['created_at'][:19]}")
                
                if alert.get('acknowledged_at'):
                    st.markdown(f"**Acknowledged:** {alert['acknowledged_at'][:19]} by {alert.get('acknowledged_by', 'N/A')}")
                if alert.get('resolved_at'):
                    st.markdown(f"**Resolved:** {alert['resolved_at'][:19]} by {alert.get('resolved_by', 'N/A')}")
                    st.markdown(f"**Notes:** {alert.get('resolution_notes', 'N/A')}")
            
            with col2:
                st.markdown(f"**Severity:** {get_status_badge(severity)}", unsafe_allow_html=True)
                st.markdown(f"**Status:** {get_status_badge(status)}", unsafe_allow_html=True)
                
                st.markdown("---")
                
                if status == "OPEN":
                    if st.button(f"✅ Acknowledge", key=f"ack_{alert['alert_id']}"):
                        acknowledge_alert(alert['alert_id'], "current_user")
                        st.success("Acknowledged!")
                        st.rerun()
                
                if status in ["OPEN", "ACKNOWLEDGED"]:
                    notes = st.text_input("Resolution notes", key=f"notes_{alert['alert_id']}")
                    if st.button(f"✔️ Resolve", key=f"res_{alert['alert_id']}"):
                        resolve_alert(alert['alert_id'], notes, "current_user")
                        st.success("Resolved!")
                        st.rerun()