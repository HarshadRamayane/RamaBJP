"""
RamaBJP Analytics Page
"""

import streamlit as st
import plotly.graph_objects as go
from config.theme import COLORS
from analytics.trends import (
    get_equipment_status_distribution, get_alert_frequency,
    get_maintenance_status_distribution, get_data_completeness,
    get_summary_stats
)


def render_analytics():
    """Render the analytics page."""
    st.markdown("## 📈 Analytics & Trends")
    st.markdown("Data completeness, trends and insights")
    st.markdown("---")
    
    # ============================================================
    # SUMMARY
    # ============================================================
    summary = get_summary_stats()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Equipment", summary["total_equipment"])
    with col2:
        st.metric("Total Readings", summary["total_readings"])
    with col3:
        st.metric("Open Alerts", summary["open_alerts"])
    with col4:
        st.metric("Open Work Orders", summary["open_work_orders"])
    
    st.markdown("---")
    
    # ============================================================
    # CHARTS
    # ============================================================
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Equipment Status Distribution")
        dist = get_equipment_status_distribution()
        
        if dist:
            fig = go.Figure(data=[go.Bar(
                x=list(dist.keys()),
                y=list(dist.values()),
                marker_color=[
                    COLORS["normal"] if k == "Normal" else
                    COLORS["warning_status"] if k == "Warning" else
                    COLORS["critical"] if k == "Critical" else
                    COLORS["unknown"]
                    for k in dist.keys()
                ]
            )])
            fig.update_layout(
                template="plotly_white",
                height=350,
                margin=dict(l=20, r=20, t=20, b=20),
                xaxis_title="Status",
                yaxis_title="Count"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### Maintenance Status Distribution")
        dist = get_maintenance_status_distribution()
        
        if dist:
            fig = go.Figure(data=[go.Pie(
                labels=list(dist.keys()),
                values=list(dist.values()),
                hole=0.5
            )])
            fig.update_layout(
                template="plotly_white",
                height=350,
                margin=dict(l=20, r=20, t=20, b=20)
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No maintenance data yet.")
    
    st.markdown("---")
    
    # ============================================================
    # DATA COMPLETENESS
    # ============================================================
    st.markdown("### Data Completeness")
    
    completeness = get_data_completeness()
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Equipment", completeness["total_equipment"])
    with col2:
        st.metric("Sensor Mappings", completeness["total_mappings"])
    with col3:
        st.metric("Total Readings", completeness["total_readings"])
    with col4:
        st.metric("Avg per Equipment", completeness["avg_readings_per_equipment"])