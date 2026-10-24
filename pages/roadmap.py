"""
RamaBJP Implementation Roadmap Page
"""

import streamlit as st
import pandas as pd
from config.theme import COLORS


def render_roadmap():
    """Render the roadmap page."""
    st.markdown("## 🗺️ Implementation Roadmap")
    st.markdown("From proof of concept to deployment")
    st.markdown("---")
    
    # ============================================================
    # PHASES TABLE
    # ============================================================
    phases = pd.DataFrame({
        "Phase": ["Phase 1", "Phase 2", "Phase 3", "Phase 4", "Phase 5", "Phase 6"],
        "Title": [
            "Software Proof of Concept",
            "Validated CSV Data Ingestion",
            "Hardware/Controller Integration",
            "Secure User Roles & Audit",
            "Historical Data & Predictive Modelling",
            "Controlled Pilot Testing"
        ],
        "Status": ["✅ COMPLETE", "📅 PLANNED", "📅 PLANNED", "📅 PLANNED", "📅 PLANNED", "📅 PLANNED"],
        "Description": [
            "Local software prototype with synthetic data and rule-based logic",
            "Import and validate real CSV sensor data",
            "Connect to real hardware controllers and sensors",
            "Add authentication, role-based access, and audit logging",
            "Collect historical data and train validated prediction models",
            "Controlled pilot with expert review and safety controls"
        ]
    })
    st.dataframe(phases, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # ============================================================
    # VISUAL TIMELINE
    # ============================================================
    st.markdown("### Visual Timeline")
    
    st.markdown("""
    <div style="background-color: #F8F9FA; padding: 25px; border-radius: 12px; border: 1px solid #DEE2E6;">
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <div style="text-align: center; flex: 1;">
                <div style="width: 50px; height: 50px; border-radius: 50%; background-color: #198754; margin: 0 auto; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 20px;">✓</div>
                <div style="color: #198754; font-weight: bold; margin-top: 10px; font-size: 12px;">PHASE 1</div>
                <div style="color: #1A1D21; font-size: 11px; margin-top: 5px;">Software PoC</div>
                <div style="color: #6C757D; font-size: 10px; margin-top: 3px;">Completed</div>
            </div>
            <div style="text-align: center; flex: 1;">
                <div style="width: 50px; height: 50px; border-radius: 50%; background-color: #F8F9FA; margin: 0 auto; border: 3px solid #0D6EFD; display: flex; align-items: center; justify-content: center; color: #0D6EFD; font-weight: bold; font-size: 18px;">2</div>
                <div style="color: #0D6EFD; font-weight: bold; margin-top: 10px; font-size: 12px;">PHASE 2</div>
                <div style="color: #1A1D21; font-size: 11px; margin-top: 5px;">CSV Ingestion</div>
                <div style="color: #6C757D; font-size: 10px; margin-top: 3px;">Planned</div>
            </div>
            <div style="text-align: center; flex: 1;">
                <div style="width: 50px; height: 50px; border-radius: 50%; background-color: #F8F9FA; margin: 0 auto; border: 3px solid #FFC107; display: flex; align-items: center; justify-content: center; color: #FFC107; font-weight: bold; font-size: 18px;">3</div>
                <div style="color: #FFC107; font-weight: bold; margin-top: 10px; font-size: 12px;">PHASE 3</div>
                <div style="color: #1A1D21; font-size: 11px; margin-top: 5px;">Hardware</div>
                <div style="color: #6C757D; font-size: 10px; margin-top: 3px;">Planned</div>
            </div>
            <div style="text-align: center; flex: 1;">
                <div style="width: 50px; height: 50px; border-radius: 50%; background-color: #F8F9FA; margin: 0 auto; border: 3px solid #0DCAF0; display: flex; align-items: center; justify-content: center; color: #0DCAF0; font-weight: bold; font-size: 18px;">4</div>
                <div style="color: #0DCAF0; font-weight: bold; margin-top: 10px; font-size: 12px;">PHASE 4</div>
                <div style="color: #1A1D21; font-size: 11px; margin-top: 5px;">Security</div>
                <div style="color: #6C757D; font-size: 10px; margin-top: 3px;">Planned</div>
            </div>
            <div style="text-align: center; flex: 1;">
                <div style="width: 50px; height: 50px; border-radius: 50%; background-color: #F8F9FA; margin: 0 auto; border: 3px solid #6C757D; display: flex; align-items: center; justify-content: center; color: #6C757D; font-weight: bold; font-size: 18px;">5</div>
                <div style="color: #6C757D; font-weight: bold; margin-top: 10px; font-size: 12px;">PHASE 5</div>
                <div style="color: #1A1D21; font-size: 11px; margin-top: 5px;">Historical Data</div>
                <div style="color: #6C757D; font-size: 10px; margin-top: 3px;">Planned</div>
            </div>
            <div style="text-align: center; flex: 1;">
                <div style="width: 50px; height: 50px; border-radius: 50%; background-color: #F8F9FA; margin: 0 auto; border: 3px solid #6C757D; display: flex; align-items: center; justify-content: center; color: #6C757D; font-weight: bold; font-size: 18px;">6</div>
                <div style="color: #6C757D; font-weight: bold; margin-top: 10px; font-size: 12px;">PHASE 6</div>
                <div style="color: #1A1D21; font-size: 11px; margin-top: 5px;">Pilot Testing</div>
                <div style="color: #6C757D; font-size: 10px; margin-top: 3px;">Planned</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # ============================================================
    # RISKS & DEPENDENCIES
    # ============================================================
    col1, col2 = st.columns(2)
    
    with col1:
        st.error("""
        **⚠️ RISKS**
        
        - Data access requires authorisation
        - Expert validation needed before deployment
        - Sensor hardware not yet integrated
        - Compliance with defence regulations
        - Cybersecurity requirements
        """)
    
    with col2:
        st.info("""
        **🔗 DEPENDENCIES**
        
        - Government approval for pilot
        - MRO unit partnership
        - Real sensor procurement
        - Expert review completion
        - Funding / grant support
        """)