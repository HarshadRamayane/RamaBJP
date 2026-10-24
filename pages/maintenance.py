import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def render_maintenance():
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
        
        /* Calendar (Mock) */
        .calendar-grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 5px; text-align: center; font-size: 11px; margin-top: 10px; }
        .calendar-header { font-weight: bold; color: #6C757D; margin-bottom: 5px; }
        .calendar-cell { padding: 8px 0; border-radius: 4px; background: #F8F9FA; border: 1px solid #DEE2E6; position: relative; }
        .calendar-event { position: absolute; bottom: 2px; left: 50%; transform: translateX(-50%); width: 4px; height: 4px; border-radius: 50%; }
    </style>
    """, unsafe_allow_html=True)

    # ============================================================
    # 1. HEADER
    # ============================================================
    col_h1, col_h2 = st.columns([2, 1.2])
    with col_h1:
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
            <div style="background: #0D6EFD; color: white; padding: 8px; border-radius: 8px; font-size: 20px;">🔧</div>
            <div>
                <h3 style="margin: 0; font-size: 22px; font-weight: 700; color: #1A1D21;">Maintenance Management</h3>
                <p style="margin: 0; font-size: 12px; color: #6C757D;">Plan, track and manage maintenance activities for optimal equipment performance.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_h2:
        c1, c2, c3 = st.columns([1.2, 1.2, 1])
        with c1: st.selectbox("Equip", ["All Equipment"], label_visibility="collapsed")
        with c2: st.selectbox("Loc", ["All Locations"], label_visibility="collapsed")
        with c3: st.button("➕ Schedule Maintenance", use_container_width=True)

    # ============================================================
    # 2. KPI CARDS (5)
    # ============================================================
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.markdown('<div class="kpi-card" style="border-left: 3px solid #0D6EFD;"><div style="background: #E7F1FF; color: #0D6EFD; padding: 8px; border-radius: 50%; margin-right: 10px; font-size: 16px;">📋</div><div><div style="color: #6C757D; font-size: 11px;">Total Maintenance</div><div style="color: #0D6EFD; font-size: 20px; font-weight: bold;">24</div><div style="color: #198754; font-size: 10px;">↑ 3 this week</div></div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="kpi-card" style="border-left: 3px solid #198754;"><div style="background: #D1E7DD; color: #198754; padding: 8px; border-radius: 50%; margin-right: 10px; font-size: 16px;">✅</div><div><div style="color: #6C757D; font-size: 11px;">Completed</div><div style="color: #198754; font-size: 20px; font-weight: bold;">12</div><div style="color: #6C757D; font-size: 10px;">50% of total</div></div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="kpi-card" style="border-left: 3px solid #FFC107;"><div style="background: #FFF3CD; color: #FFC107; padding: 8px; border-radius: 50%; margin-right: 10px; font-size: 16px;">⏳</div><div><div style="color: #6C757D; font-size: 11px;">In Progress</div><div style="color: #FFC107; font-size: 20px; font-weight: bold;">7</div><div style="color: #6C757D; font-size: 10px;">29% of total</div></div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="kpi-card" style="border-left: 3px solid #DC3545;"><div style="background: #F8D7DA; color: #DC3545; padding: 8px; border-radius: 50%; margin-right: 10px; font-size: 16px;">🚨</div><div><div style="color: #6C757D; font-size: 11px;">Overdue</div><div style="color: #DC3545; font-size: 20px; font-weight: bold;">3</div><div style="color: #6C757D; font-size: 10px;">12% of total</div></div></div>', unsafe_allow_html=True)
    with c5:
        st.markdown('<div class="kpi-card" style="border-left: 3px solid #0DCAF0;"><div style="background: #CFF4FC; color: #0DCAF0; padding: 8px; border-radius: 50%; margin-right: 10px; font-size: 16px;">📅</div><div><div style="color: #6C757D; font-size: 11px;">Upcoming (Next 7 Days)</div><div style="color: #0DCAF0; font-size: 20px; font-weight: bold;">5</div><div style="color: #6C757D; font-size: 10px;">21% of total</div></div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ============================================================
    # 3. MAIN LAYOUT
    # ============================================================
    col_left, col_right = st.columns([2, 1])

    # --- LEFT: Maintenance Schedule Table ---
    with col_left:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown('<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;"><div style="font-size:15px; font-weight:600;">📋 Maintenance Schedule</div><div style="font-size:11px; color:#6C757D; border:1px solid #DEE2E6; padding:2px 8px; border-radius:4px;">Search by equipment, task or ID... 🔍</div></div>', unsafe_allow_html=True)
        
        table_html = """
        <table class="custom-table">
            <tr><th>ID</th><th>Equipment Name</th><th>Task Type</th><th>Scheduled</th><th>Priority</th><th>Status</th><th>Assigned To</th></tr>
            <tr><td>MT-001</td><td>T-90 Main Battle Tank</td><td>Inspection</td><td>May 5, 2025</td><td><span class="badge badge-red">High</span></td><td><span class="badge badge-blue">Scheduled</span></td><td>Team Alpha</td></tr>
            <tr><td>MT-002</td><td>APC Vehicle</td><td>Oil Change</td><td>May 7, 2025</td><td><span class="badge badge-yellow">Medium</span></td><td><span class="badge badge-yellow">In Progress</span></td><td>Team Bravo</td></tr>
            <tr><td>MT-003</td><td>Artillery Gun</td><td>Calibration</td><td>May 8, 2025</td><td><span class="badge badge-red">High</span></td><td><span class="badge badge-blue">Scheduled</span></td><td>Team Charlie</td></tr>
            <tr><td>MT-004</td><td>Radar System</td><td>Software Update</td><td>May 9, 2025</td><td><span class="badge badge-green">Low</span></td><td><span class="badge badge-green">Completed</span></td><td>Tech Engineer</td></tr>
            <tr><td>MT-005</td><td>Transport Truck</td><td>General Checkup</td><td>May 10, 2025</td><td><span class="badge badge-yellow">Medium</span></td><td><span class="badge badge-blue">Scheduled</span></td><td>Team Alpha</td></tr>
            <tr><td>MT-006</td><td>Communication Unit</td><td>Battery Check</td><td>May 12, 2025</td><td><span class="badge badge-green">Low</span></td><td><span class="badge badge-red">Overdue</span></td><td>Team Bravo</td></tr>
            <tr><td>MT-007</td><td>Helicopter</td><td>Engine Inspection</td><td>May 15, 2025</td><td><span class="badge badge-red">High</span></td><td><span class="badge badge-yellow">In Progress</span></td><td>Team Charlie</td></tr>
        </table>
        """
        st.markdown(table_html, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- RIGHT: Status Chart & Upcoming ---
    with col_right:
        # Chart
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:15px; font-weight:600; margin-bottom:10px;">🛡️ Maintenance Status</div>', unsafe_allow_html=True)
        
        fig = go.Figure(data=[go.Pie(
            labels=["Completed", "In Progress", "Scheduled", "Overdue"],
            values=[12, 7, 2, 3],
            hole=0.6,
            marker=dict(colors=["#198754", "#FFC107", "#0D6EFD", "#DC3545"]),
            textinfo='none'
        )])
        fig.add_annotation(text="24<br><span style='font-size:10px;color:#6C757D'>Total</span>", x=0.5, y=0.5, font=dict(size=20, color="#1A1D21"), showarrow=False)
        
        fig.update_layout(template="plotly_white", height=200, margin=dict(l=0, r=0, t=0, b=0), showlegend=True, legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.0, font=dict(size=10)))
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div style="background:#F0FDF4; border:1px solid #198754; padding:8px; border-radius:6px; font-size:10px; color:#198754; margin-top:10px;">
            🟢 Maintenance is on track.<br>All tasks are planned, scheduled and executed.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Upcoming Maintenance
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:15px; font-weight:600; margin-bottom:10px;">📅 Upcoming Maintenance</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="font-size:11px; line-height: 2;">
            <div style="display:flex; justify-content:space-between; border-bottom:1px solid #F1F3F5; padding-bottom:5px; margin-bottom:5px;"><span>May 5, 2025 - T-90 Tank</span><span style="color:#DC3545; font-weight:bold;">High</span></div>
            <div style="display:flex; justify-content:space-between; border-bottom:1px solid #F1F3F5; padding-bottom:5px; margin-bottom:5px;"><span>May 7, 2025 - APC</span><span style="color:#FFC107; font-weight:bold;">Med</span></div>
            <div style="display:flex; justify-content:space-between; border-bottom:1px solid #F1F3F5; padding-bottom:5px; margin-bottom:5px;"><span>May 8, 2025 - Artillery</span><span style="color:#DC3545; font-weight:bold;">High</span></div>
            <div style="display:flex; justify-content:space-between;"><span>May 9, 2025 - Radar</span><span style="color:#198754; font-weight:bold;">Low</span></div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ============================================================
    # 4. BOTTOM ROW (Calendar + Tasks + Quick Actions)
    # ============================================================
    col_b1, col_b2, col_b3 = st.columns([1.2, 1.5, 1])

    # --- BOTTOM LEFT: Calendar (Mock) ---
    with col_b1:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;"><div style="font-size:14px; font-weight:600;">📅 Maintenance Calendar</div><div style="font-size:11px; color:#6C757D;">May 2025 ▼</div></div>', unsafe_allow_html=True)
        
        # Mock Calendar
        calendar_html = """
        <div style="display:grid; grid-template-columns: repeat(7, 1fr); gap: 2px; text-align:center; font-size:10px;">
            <div class="calendar-header" style="color:#DC3545;">Sun</div><div class="calendar-header">Mon</div><div class="calendar-header">Tue</div><div class="calendar-header">Wed</div><div class="calendar-header">Thu</div><div class="calendar-header">Fri</div><div class="calendar-header" style="color:#0D6EFD;">Sat</div>
            <!-- Row 1 -->
            <div style="padding:5px; background:#F8F9FA; border-radius:4px; color:#ADB5BD;">27</div><div style="padding:5px; background:#F8F9FA; border-radius:4px; color:#ADB5BD;">28</div><div style="padding:5px; background:#F8F9FA; border-radius:4px; color:#ADB5BD;">29</div><div style="padding:5px; background:#F8F9FA; border-radius:4px; color:#ADB5BD;">30</div><div style="padding:5px; background:#F8F9FA; border-radius:4px; color:#ADB5BD;">1</div><div style="padding:5px; background:#F8F9FA; border-radius:4px; color:#ADB5BD;">2</div><div style="padding:5px; background:#E7F1FF; border-radius:4px; color:#0D6EFD; font-weight:bold;">3</div>
            <!-- Row 2 -->
            <div style="padding:5px; position:relative;">4<div class="calendar-event" style="background:#FFC107;"></div></div><div style="padding:5px; position:relative;">5<div class="calendar-event" style="background:#DC3545;"></div></div><div style="padding:5px; position:relative;">6<div class="calendar-event" style="background:#0D6EFD;"></div></div><div style="padding:5px;">7</div><div style="padding:5px; position:relative;">8<div class="calendar-event" style="background:#FFC107;"></div></div><div style="padding:5px;">9</div><div style="padding:5px;">10</div>
            <!-- Row 3 -->
            <div style="padding:5px;">11</div><div style="padding:5px; position:relative;">12<div class="calendar-event" style="background:#DC3545;"></div></div><div style="padding:5px;">13</div><div style="padding:5px;">14</div><div style="padding:5px; position:relative;">15<div class="calendar-event" style="background:#0D6EFD;"></div></div><div style="padding:5px;">16</div><div style="padding:5px;">17</div>
            <!-- Row 4 -->
            <div style="padding:5px;">18</div><div style="padding:5px;">19</div><div style="padding:5px;">20</div><div style="padding:5px; position:relative;">21<div class="calendar-event" style="background:#198754;"></div></div><div style="padding:5px;">22</div><div style="padding:5px;">23</div><div style="padding:5px;">24</div>
        </div>
        """
        st.markdown(calendar_html, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="display:flex; gap:10px; font-size:10px; margin-top:10px; color:#6C757D;">
            <span><span style="color:#DC3545;">●</span> High</span>
            <span><span style="color:#FFC107;">●</span> Medium</span>
            <span><span style="color:#198754;">●</span> Completed</span>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- BOTTOM CENTER: Maintenance Tasks ---
    with col_b2:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;"><div style="font-size:14px; font-weight:600;">🔧 Maintenance Tasks</div><div style="font-size:11px; color:#0D6EFD; cursor:pointer;">View All</div></div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="font-size:11px; display:flex; flex-direction:column; gap:8px;">
            <div style="background:#FFF5F5; border-left:3px solid #DC3545; padding:8px; border-radius:4px;"><b>T-90 Tank Inspection</b><br>May 5, 2025 - 10:00 AM</div>
            <div style="background:#FFF9E6; border-left:3px solid #FFC107; padding:8px; border-radius:4px;"><b>APC Oil Change</b><br>May 7, 2025 - 11:30 AM</div>
            <div style="background:#F8F9FA; border-left:3px solid #0D6EFD; padding:8px; border-radius:4px;"><b>Artillery Calibration</b><br>May 8, 2025 - 09:00 AM</div>
            <div style="background:#F0FDF4; border-left:3px solid #198754; padding:8px; border-radius:4px;"><b>Radar Software Update</b><br>May 9, 2025 - 02:00 PM</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- BOTTOM RIGHT: Quick Actions ---
    with col_b3:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:14px; font-weight:600; margin-bottom:10px;">⚡ Quick Actions</div>', unsafe_allow_html=True)
        
        st.button("📅 Schedule Maintenance", use_container_width=True)
        st.button("👁️ View Maintenance History", use_container_width=True)
        st.button("📄 Generate Work Order", use_container_width=True)
        st.button("👤 Assign Task", use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)