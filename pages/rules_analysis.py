import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def render_rules_analysis():
    # ============================================================
    # LIGHT THEME & CUSTOM CSS
    # ============================================================
    st.markdown("""
    <style>
        .stApp { background-color: #F8F9FA !important; }
        .block-container { padding-top: 1rem !important; }
        header[data-testid="stHeader"] { background: transparent !important; }
        
        /* Cards */
        .kpi-card { background-color: #FFFFFF; border: 1px solid #DEE2E6; border-radius: 8px; padding: 15px; display: flex; align-items: center; box-shadow: 0 1px 3px rgba(0,0,0,0.02); height: 100%; }
        .main-card { background-color: #FFFFFF; border: 1px solid #DEE2E6; border-radius: 8px; padding: 20px; margin-bottom: 20px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); }
        
        /* Tables */
        .custom-table { width: 100%; border-collapse: collapse; font-size: 12px; }
        .custom-table th { color: #6C757D; text-align: left; padding: 10px 8px; border-bottom: 1px solid #DEE2E6; font-weight: 600; }
        .custom-table td { padding: 10px 8px; border-bottom: 1px solid #F8F9FA; color: #1A1D21; vertical-align: middle; }
        
        /* Badges */
        .badge { padding: 3px 8px; border-radius: 12px; font-size: 10px; font-weight: 600; display: inline-block;}
        .badge-green { background: #D1E7DD; color: #0F5132; }
        .badge-yellow { background: #FFF3CD; color: #664D03; }
        .badge-red { background: #F8D7DA; color: #842029; }
        .badge-blue { background: #CFE2FF; color: #084298; }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] { gap: 8px; }
        .stTabs [data-baseweb="tab"] { background-color: #F8F9FA; border-radius: 4px; padding: 5px 15px; border: 1px solid #DEE2E6; }
        .stTabs [aria-selected="true"] { background-color: #0D6EFD !important; color: white !important; border: 1px solid #0D6EFD; }
    </style>
    """, unsafe_allow_html=True)

    # ============================================================
    # 1. HEADER
    # ============================================================
    col_h1, col_h2 = st.columns([2, 1.2])
    with col_h1:
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 5px;">
            <div style="background: #0D6EFD; color: white; padding: 6px; border-radius: 8px; font-size: 20px;">⚙️</div>
            <div>
                <h3 style="margin: 0; font-size: 22px; font-weight: 700; color: #1A1D21;">Rules & Analysis</h3>
                <p style="margin: 0; font-size: 12px; color: #6C757D;">Configure rules, analyze sensor data, and get actionable insights for better decision making.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_h2:
        st.info("💡 This is a quick-read Proof of Concept. You can build your final solution in one day or less.")
    
    st.markdown("<hr style='margin: 10px 0 20px 0; border-color: #DEE2E6;'>", unsafe_allow_html=True)

    # ============================================================
    # 2. KPI CARDS (5 Cards)
    # ============================================================
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.markdown('<div class="kpi-card" style="border-left: 3px solid #0D6EFD;"><div><div style="color: #6C757D; font-size: 11px;">Total Rules</div><div style="color: #0D6EFD; font-size: 22px; font-weight: bold;">12</div><div style="color: #198754; font-size: 10px;">↑ 2 new rules</div></div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="kpi-card" style="border-left: 3px solid #198754;"><div><div style="color: #6C757D; font-size: 11px;">Active Rules</div><div style="color: #198754; font-size: 22px; font-weight: bold;">10</div><div style="color: #6C757D; font-size: 10px;">83% of total</div></div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="kpi-card" style="border-left: 3px solid #FFC107;"><div><div style="color: #6C757D; font-size: 11px;">Triggered Rules</div><div style="color: #FFC107; font-size: 22px; font-weight: bold;">3</div><div style="color: #6C757D; font-size: 10px;">Needs attention</div></div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="kpi-card" style="border-left: 3px solid #6F42C1;"><div><div style="color: #6C757D; font-size: 11px;">Analysis Runs</div><div style="color: #6F42C1; font-size: 22px; font-weight: bold;">24</div><div style="color: #6C757D; font-size: 10px;">Last 7 days</div></div></div>', unsafe_allow_html=True)
    with c5:
        st.markdown('<div class="kpi-card" style="border-left: 3px solid #0DCAF0;"><div><div style="color: #6C757D; font-size: 11px;">Recommendations</div><div style="color: #0DCAF0; font-size: 22px; font-weight: bold;">7</div><div style="color: #6C757D; font-size: 10px;">Based on rule analysis</div></div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ============================================================
    # 3. MAIN LAYOUT (Rules + Analysis)
    # ============================================================
    col_left, col_right = st.columns([1.3, 1])

    # --- LEFT: Rule Management ---
    with col_left:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown('<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;"><div style="font-size:15px; font-weight:600;">🛡️ Rule Management</div><div style="background:#0D6EFD; color:white; padding:4px 10px; border-radius:6px; font-size:11px; cursor:pointer;">+ New Rule</div></div>', unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["All Rules (12)", "Active (10)", "Inactive (2)"])
        
        with tab1:
            # Rule Table
            table_html = """
            <table class="custom-table">
                <tr><th>Rule Name</th><th>Condition</th><th>Action</th><th>Status</th><th></th></tr>
                <tr><td>High Vibration</td><td>Vibration > 10 mm/s</td><td>Raise Alert</td><td><span class="badge badge-green">Active</span></td><td>⋮</td></tr>
                <tr><td>High Temperature</td><td>Temperature > 85 °C</td><td>Raise Alert</td><td><span class="badge badge-green">Active</span></td><td>⋮</td></tr>
                <tr><td>Low Oil Quality</td><td>Oil Quality < 40%</td><td>Schedule Maintenance</td><td><span class="badge badge-green">Active</span></td><td>⋮</td></tr>
                <tr><td>High Pressure</td><td>Pressure > 3.5 bar</td><td>Raise Alert</td><td><span class="badge badge-yellow">Warning</span></td><td>⋮</td></tr>
                <tr><td>Excessive RPM</td><td>RPM > 2200</td><td>Raise Alert</td><td><span class="badge badge-green">Active</span></td><td>⋮</td></tr>
                <tr><td>Sensor Offline</td><td>No data for > 5 min</td><td>Create Maintenance Task</td><td><span class="badge badge-red">Inactive</span></td><td>⋮</td></tr>
                <tr><td>Trend Degradation</td><td>25% drop in 7 days</td><td>Create Maintenance Task</td><td><span class="badge badge-green">Active</span></td><td>⋮</td></tr>
                <tr><td>Critical Fault</td><td>Multiple issues</td><td>Auto Create</td><td><span class="badge badge-green">Active</span></td><td>⋮</td></tr>
                <tr><td>Fuel Low</td><td>Fuel < 10%</td><td>Notify & Log</td><td><span class="badge badge-green">Active</span></td><td>⋮</td></tr>
                <tr><td>Battery Voltage Low</td><td>Voltage < 11.5V</td><td>Raise Alert</td><td><span class="badge badge-green">Active</span></td><td>⋮</td></tr>
            </table>
            """
            st.markdown(table_html, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- RIGHT: Sensor Analysis ---
    with col_right:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;"><div style="font-size:15px; font-weight:600;">📊 Sensor Analysis</div><div style="font-size:11px; color:#6C757D; border:1px solid #DEE2E6; padding:2px 8px; border-radius:4px;">Last 7 Days ▼</div></div>', unsafe_allow_html=True)
        
        # Fake Tabs for Sensors
        st.markdown("""
        <div style="display:flex; gap:10px; font-size:11px; margin-bottom:15px; flex-wrap:wrap;">
            <span style="background:#F8F9FA; padding:4px 10px; border-radius:4px; border:1px solid #DEE2E6; cursor:pointer;">Vibration</span>
            <span style="background:#0D6EFD; color:white; padding:4px 10px; border-radius:4px; cursor:pointer;">Temperature</span>
            <span style="background:#F8F9FA; padding:4px 10px; border-radius:4px; border:1px solid #DEE2E6; cursor:pointer;">Oil Quality</span>
            <span style="background:#F8F9FA; padding:4px 10px; border-radius:4px; border:1px solid #DEE2E6; cursor:pointer;">Pressure</span>
        </div>
        """, unsafe_allow_html=True)

        # Chart Layout
        col_chart, col_stats = st.columns([2, 1])
        
        with col_chart:
            fig = go.Figure()
            # Normal line
            fig.add_trace(go.Scatter(x=["Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", "Apr 27", "Apr 28"], 
                                     y=[60, 62, 65, 64, 68, 70, 72], mode='lines', name='Normal',
                                     line=dict(color='#0D6EFD', width=2)))
            # Trigger line
            fig.add_trace(go.Scatter(x=["Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", "Apr 27", "Apr 28"], 
                                     y=[70, 72, 75, 74, 78, 82, 85], mode='lines', name='Triggered',
                                     line=dict(color='#DC3545', width=2)))
            # Threshold line
            fig.add_hline(y=80, line_dash="dash", line_color="#DC3545", annotation_text="High Threshold")
            
            fig.update_layout(template="plotly_white", height=200, margin=dict(l=0, r=0, t=10, b=0), 
                              legend=dict(orientation="h", yanchor="bottom", y=-0.4, xanchor="center", x=0.5, font=dict(size=9)),
                              xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor="#F1F3F5"))
            st.plotly_chart(fig, use_container_width=True)

        with col_stats:
            st.markdown("""
            <div style="background:#F8F9FA; padding:10px; border-radius:8px; border:1px solid #DEE2E6; text-align:center;">
                <div style="color:#6C757D; font-size:10px;">Current Value</div>
                <div style="color:#198754; font-size:20px; font-weight:bold;">4.2 mm/s</div>
                <div style="color:#198754; font-size:10px; font-weight:600;">Normal</div>
            </div>
            <div style="background:#F8F9FA; padding:10px; border-radius:8px; border:1px solid #DEE2E6; text-align:center; margin-top:10px;">
                <div style="color:#6C757D; font-size:10px;">Threshold Range</div>
                <div style="color:#1A1D21; font-size:14px; font-weight:bold;">2.0 - 7.0 mm/s</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ============================================================
    # 4. BOTTOM ROW (Run Analysis + Insights)
    # ============================================================
    col_b1, col_b2 = st.columns([1.3, 1])

    # --- BOTTOM LEFT: Run Analysis ---
    with col_b1:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown('<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;"><div style="font-size:15px; font-weight:600;">⚙️ Rule Analysis</div><div style="font-size:11px; color:#0D6EFD; cursor:pointer;">View All</div></div>', unsafe_allow_html=True)
        
        table_html_2 = """
        <table class="custom-table">
            <tr><th>Rule Name</th><th>Equipment</th><th>Status</th><th>Severity</th></tr>
            <tr><td>High Vibration</td><td>EQ-001</td><td><span class="badge badge-red">Triggered</span></td><td style="color:#DC3545;">Critical</td></tr>
            <tr><td>High Temp</td><td>EQ-002</td><td><span class="badge badge-red">Triggered</span></td><td style="color:#DC3545;">Critical</td></tr>
            <tr><td>Low Oil Quality</td><td>EQ-003</td><td><span class="badge badge-yellow">Warning</span></td><td style="color:#FFC107;">High</td></tr>
            <tr><td>High Pressure</td><td>EQ-004</td><td><span class="badge badge-yellow">Warning</span></td><td style="color:#FFC107;">Medium</td></tr>
            <tr><td>Excessive RPM</td><td>EQ-005</td><td><span class="badge badge-green">Normal</span></td><td style="color:#198754;">Low</td></tr>
        </table>
        """
        st.markdown(table_html_2, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- BOTTOM RIGHT: Insights ---
    with col_b2:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:15px; font-weight:600; margin-bottom:15px;">💡 Insights & Recommendations</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="display:flex; flex-direction:column; gap:10px;">
            <div style="background:#FFF5F5; border-left:3px solid #DC3545; padding:10px; border-radius:4px;">
                <div style="font-size:12px; font-weight:600; color:#DC3545;">High Vibration Detected</div>
                <div style="font-size:11px; color:#6C757D;">EQ-001 is showing vibration levels above threshold. Schedule inspection immediately.</div>
            </div>
            <div style="background:#FFF9E6; border-left:3px solid #FFC107; padding:10px; border-radius:4px;">
                <div style="font-size:12px; font-weight:600; color:#FFC107;">Oil Quality Degradation</div>
                <div style="font-size:11px; color:#6C757D;">EQ-003 oil quality has dropped below 40%. Plan oil change within 5 days.</div>
            </div>
            <div style="background:#F0FDF4; border-left:3px solid #198754; padding:10px; border-radius:4px;">
                <div style="font-size:12px; font-weight:600; color:#198754;">Generator Health Stable</div>
                <div style="font-size:11px; color:#6C757D;">EQ-005 is operating normally. No action required.</div>
            </div>
            <div style="background:#F0FDF4; border-left:3px solid #198754; padding:10px; border-radius:4px;">
                <div style="font-size:12px; font-weight:600; color:#198754;">Vehicle-1 Temperature Stable</div>
                <div style="font-size:11px; color:#6C757D;">EQ-006 is within normal range. Continue monitoring.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)