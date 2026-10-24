import streamlit as st
import pandas as pd

def render_alerts():
    # ============================================================
    # LIGHT THEME & CUSTOM CSS
    # ============================================================
    st.markdown("""
    <style>
        .stApp { background-color: #F8F9FA !important; }
        .block-container { padding-top: 1rem !important; }
        header[data-testid="stHeader"] { background: transparent !important; }
        
        /* KPI Cards */
        .kpi-card { background-color: #FFFFFF; border: 1px solid #DEE2E6; border-radius: 8px; padding: 15px; display: flex; align-items: center; box-shadow: 0 1px 3px rgba(0,0,0,0.02); }
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
        
        /* Timeline Notifications */
        .notif-item { display: flex; gap: 10px; margin-bottom: 15px; }
        .notif-icon { width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 12px; color: white; flex-shrink: 0;}
        .notif-content { flex: 1; border-bottom: 1px solid #F1F3F5; padding-bottom: 10px; }
        .notif-title { font-weight: 600; font-size: 12px; color: #1A1D21; }
        .notif-desc { font-size: 11px; color: #6C757D; margin: 2px 0; }
        .notif-time { font-size: 10px; color: #ADB5BD; }
        
        /* Quick Actions */
        .action-box { background: #F8F9FA; border: 1px solid #DEE2E6; padding: 15px; border-radius: 8px; text-align: center; cursor: pointer; transition: 0.2s; }
        .action-box:hover { background: #E7F1FF; border-color: #0D6EFD; }
        
        /* Tabs */
        .stTabs [data-baseweb="tab-list"] { gap: 8px; }
        .stTabs [data-baseweb="tab"] { background-color: #F8F9FA; border-radius: 4px; padding: 5px 15px; border: 1px solid #DEE2E6; }
        .stTabs [aria-selected="true"] { background-color: #0D6EFD !important; color: white !important; border: 1px solid #0D6EFD; }
    </style>
    """, unsafe_allow_html=True)

    # ============================================================
    # 1. HEADER
    # ============================================================
    col_h1, col_h2 = st.columns([2, 1])
    with col_h1:
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
            <div style="background: #0D6EFD; color: white; padding: 8px; border-radius: 8px; font-size: 20px;">🔔</div>
            <div>
                <h3 style="margin: 0; font-size: 22px; font-weight: 700; color: #1A1D21;">Alerts & Notifications</h3>
                <p style="margin: 0; font-size: 12px; color: #6C757D;">Stay informed about critical issues, system alerts and important updates.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_h2:
        st.markdown("""
        <div style="display: flex; justify-content: flex-end; align-items: center; gap: 10px; height: 100%;">
            <div style="background: #F0FDF4; border: 1px solid #198754; color: #198754; padding: 5px 12px; border-radius: 20px; font-size: 11px; font-weight: 600;">🟢 System Online</div>
            <div style="font-size: 11px; color: #6C757D;">All systems operational</div>
        </div>
        """, unsafe_allow_html=True)

    # ============================================================
    # 2. KPI CARDS (4)
    # ============================================================
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("""
        <div class="kpi-card" style="border-left: 4px solid #DC3545;">
            <div style="background: #F8D7DA; color: #DC3545; padding: 10px; border-radius: 50%; margin-right: 15px; font-size: 18px;">🚨</div>
            <div><div style="color: #DC3545; font-size: 12px; font-weight: 600;">Critical Alerts</div><div style="font-size: 24px; font-weight: bold; color: #1A1D21;">3</div><div style="color: #6C757D; font-size: 10px;">Requires immediate attention</div></div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="kpi-card" style="border-left: 4px solid #FFC107;">
            <div style="background: #FFF3CD; color: #FFC107; padding: 10px; border-radius: 50%; margin-right: 15px; font-size: 18px;">⚠️</div>
            <div><div style="color: #FFC107; font-size: 12px; font-weight: 600;">Warning Alerts</div><div style="font-size: 24px; font-weight: bold; color: #1A1D21;">6</div><div style="color: #6C757D; font-size: 10px;">Requires attention</div></div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="kpi-card" style="border-left: 4px solid #0D6EFD;">
            <div style="background: #CFE2FF; color: #0D6EFD; padding: 10px; border-radius: 50%; margin-right: 15px; font-size: 18px;">ℹ️</div>
            <div><div style="color: #0D6EFD; font-size: 12px; font-weight: 600;">Info Notifications</div><div style="font-size: 24px; font-weight: bold; color: #1A1D21;">12</div><div style="color: #6C757D; font-size: 10px;">General information</div></div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown("""
        <div class="kpi-card" style="border-left: 4px solid #198754;">
            <div style="background: #D1E7DD; color: #198754; padding: 10px; border-radius: 50%; margin-right: 15px; font-size: 18px;">✅</div>
            <div><div style="color: #198754; font-size: 12px; font-weight: 600;">Resolved (Last 7 Days)</div><div style="font-size: 24px; font-weight: bold; color: #1A1D21;">18</div><div style="color: #6C757D; font-size: 10px;">No action required</div></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ============================================================
    # 3. MAIN LAYOUT
    # ============================================================
    col_left, col_right = st.columns([1.5, 1])

    # --- LEFT: Alerts Feed ---
    with col_left:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown('<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;"><div style="font-size:15px; font-weight:600;">🔔 Alerts Feed</div><div style="font-size:11px; color:#0D6EFD; cursor:pointer;">Mark all as Read</div></div>', unsafe_allow_html=True)
        tab1, tab2, tab3, tab4 = st.tabs(["All (21)", "Critical (3)", "Warning (6)", "Info (12)"])
        
        
        with tab1:
            table_html = """
            <table class="custom-table">
                <tr><th>Time</th><th>Equipment</th><th>Alert Message</th><th>Severity</th><th>Status</th><th>Actions</th></tr>
                <tr><td>Apr 28, 10:45</td><td>EQ-001 T-90 Tank</td><td>Vibration level exceeded threshold (10 mm/s)</td><td><span class="badge badge-red">Critical</span></td><td>Open</td><td>⋯</td></tr>
                <tr><td>Apr 28, 10:30</td><td>EQ-002 APC Vehicle</td><td>Temperature above normal (90 °C)</td><td><span class="badge badge-red">Critical</span></td><td>Open</td><td>⋯</td></tr>
                <tr><td>Apr 28, 09:45</td><td>EQ-003 Artillery Gun</td><td>Oil quality below threshold (40%)</td><td><span class="badge badge-yellow">Warning</span></td><td>In Progress</td><td>⋯</td></tr>
                <tr><td>Apr 28, 09:15</td><td>EQ-004 Radar System</td><td>Sensor data delayed (> 5 min)</td><td><span class="badge badge-red">Critical</span></td><td>Open</td><td>⋯</td></tr>
                <tr><td>Apr 28, 08:30</td><td>EQ-005 Transport Truck</td><td>Maintenance due in 5 days</td><td><span class="badge badge-blue">Info</span></td><td>New</td><td>⋯</td></tr>
                <tr><td>Apr 28, 07:50</td><td>EQ-006 Communication Unit</td><td>Network connectivity issue</td><td><span class="badge badge-blue">Info</span></td><td>Resolved</td><td>⋯</td></tr>
                <tr><td>Apr 28, 07:15</td><td>EQ-007 Helicopter</td><td>Battery voltage low (11.8 V)</td><td><span class="badge badge-yellow">Warning</span></td><td>Open</td><td>⋯</td></tr>
                <tr><td>Apr 28, 06:30</td><td>EQ-008 Generator</td><td>Overheating detected (85 °C)</td><td><span class="badge badge-red">Critical</span></td><td>Open</td><td>⋯</td></tr>
            </table>
            """
            st.markdown(table_html, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- RIGHT: Notifications & Quick Actions ---
    with col_right:
        # Recent Notifications
        st.markdown('<div class="main-card" style="height: auto;">', unsafe_allow_html=True)
        st.markdown('<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;"><div style="font-size:15px; font-weight:600;">🔔 Recent Notifications</div><div style="font-size:11px; color:#0D6EFD; cursor:pointer;">View All</div></div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="font-size:12px;">
            <div class="notif-item">
                <div class="notif-icon" style="background:#DC3545;">🚨</div>
                <div class="notif-content">
                    <div class="notif-title">Critical: Vibration level exceeded (EQ-001)</div>
                    <div class="notif-desc">Tank T-90 - Vibration level crossed 10 mm/s.</div>
                    <div class="notif-time">Apr 28, 10:45</div>
                </div>
            </div>
            <div class="notif-item">
                <div class="notif-icon" style="background:#FFC107;">⚠️</div>
                <div class="notif-content">
                    <div class="notif-title">Warning: Temperature above normal (EQ-002)</div>
                    <div class="notif-desc">APC Vehicle - Temperature above 90 °C.</div>
                    <div class="notif-time">Apr 28, 10:30</div>
                </div>
            </div>
            <div class="notif-item">
                <div class="notif-icon" style="background:#FFC107;">⚠️</div>
                <div class="notif-content">
                    <div class="notif-title">Warning: Oil quality below threshold (EQ-003)</div>
                    <div class="notif-desc">Artillery Gun - Oil quality dropped below 40%.</div>
                    <div class="notif-time">Apr 28, 09:45</div>
                </div>
            </div>
            <div class="notif-item">
                <div class="notif-icon" style="background:#0D6EFD;">ℹ️</div>
                <div class="notif-content">
                    <div class="notif-title">Info: Maintenance reminder (EQ-005)</div>
                    <div class="notif-desc">Transport Truck - Scheduled maintenance due in 5 days.</div>
                    <div class="notif-time">Apr 28, 08:30</div>
                </div>
            </div>
            <div class="notif-item">
                <div class="notif-icon" style="background:#198754;">✅</div>
                <div class="notif-content">
                    <div class="notif-title">Resolved: Network issue (EQ-006)</div>
                    <div class="notif-desc">Communication Unit - Network connectivity restored.</div>
                    <div class="notif-time">Apr 28, 07:50</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Quick Actions
        st.markdown('<div class="main-card" style="margin-top: 20px;">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:15px; font-weight:600; margin-bottom:15px;">⚡ Quick Actions</div>', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="action-box"><div style="font-size:20px; color:#0D6EFD;">👁️</div><div style="font-size:12px; font-weight:600; margin-top:5px;">View All Alerts</div><div style="font-size:10px; color:#6C757D;">See complete alert history</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="action-box"><div style="font-size:20px; color:#198754;">🛠️</div><div style="font-size:12px; font-weight:600; margin-top:5px;">Manage Rules</div><div style="font-size:10px; color:#6C757D;">Configure alert rules</div></div>', unsafe_allow_html=True)
            
        c3, c4 = st.columns(2)
        with c3:
            st.markdown('<div class="action-box" style="margin-top:10px;"><div style="font-size:20px; color:#FFC107;">🔔</div><div style="font-size:12px; font-weight:600; margin-top:5px;">Send Notification</div><div style="font-size:10px; color:#6C757D;">Notify team members</div></div>', unsafe_allow_html=True)
        with c4:
            st.markdown('<div class="action-box" style="margin-top:10px;"><div style="font-size:20px; color:#6C757D;">⚙️</div><div style="font-size:12px; font-weight:600; margin-top:5px;">Notification Settings</div><div style="font-size:10px; color:#6C757D;">Email, SMS & in-app</div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Notification Preferences (Checkboxes)
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:15px; font-weight:600; margin-bottom:15px;">🔔 Notification Preferences</div>', unsafe_allow_html=True)
        
        st.checkbox("Email Notifications", value=True, help="Receive email alerts for critical issues.")
        st.checkbox("SMS Notifications", value=False, help="Receive SMS alerts for critical issues.")
        st.checkbox("In-App Notifications", value=True, help="Receive in-app alerts for critical issues.")
        
        st.markdown('<div style="font-size:11px; color:#0D6EFD; cursor:pointer; margin-top:10px;">Manage Preferences →</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)