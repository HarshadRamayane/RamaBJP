import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def render_reports():
    # ============================================================
    # CUSTOM CSS (Light Theme)
    # ============================================================
    st.markdown("""
    <style>
        .stApp { background-color: #F8F9FA !important; }
        .block-container { padding-top: 1rem !important; padding-bottom: 1rem !important; }
        header[data-testid="stHeader"] { background: transparent !important; }

        .kpi-card { 
            background-color: #FFFFFF; border: 1px solid #DEE2E6; border-radius: 8px; 
            padding: 12px 15px; display: flex; align-items: center; gap: 12px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02); height: 100%; 
        }
        .main-card { 
            background-color: #FFFFFF; border: 1px solid #DEE2E6; border-radius: 8px; 
            padding: 15px; margin-bottom: 15px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); height: 100%;
        }
        .custom-table { width: 100%; border-collapse: collapse; font-size: 11px; }
        .custom-table th { color: #6C757D; text-align: left; padding: 10px 6px; border-bottom: 1px solid #DEE2E6; font-weight: 600; font-size: 10px; }
        .custom-table td { padding: 10px 6px; border-bottom: 1px solid #F8F9FA; color: #1A1D21; vertical-align: middle; }
        .badge { padding: 3px 8px; border-radius: 12px; font-size: 9px; font-weight: 600; display: inline-block;}
        .badge-green { background: #D1E7DD; color: #0F5132; }
        .badge-yellow { background: #FFF3CD; color: #664D03; }
        .badge-red { background: #F8D7DA; color: #842029; }
        .badge-blue { background: #CFE2FF; color: #084298; }
        .badge-purple { background: #E2D9F3; color: #432874; }
        .filter-bar { background: #F8F9FA; border: 1px solid #DEE2E6; border-radius: 4px; padding: 4px 8px; font-size: 11px; color: #6C757D; display: inline-block; }
    </style>
    """, unsafe_allow_html=True)

    # 1. HEADER & FILTERS
    col_h1, col_h2 = st.columns([1.5, 2])
    with col_h1:
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 20px;">
            <div style="background: #0D6EFD; color: white; padding: 8px 10px; border-radius: 8px; font-size: 18px;">📄</div>
            <div>
                <h3 style="margin: 0; font-size: 22px; font-weight: 700; color: #1A1D21;">Reports</h3>
                <p style="margin: 0; font-size: 12px; color: #6C757D;">Create and view detailed reports for equipment, maintenance, alerts and performance.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_h2:
        c1, c2, c3, c4 = st.columns([1.5, 1.2, 1.2, 1])
        with c1: st.markdown('<div class="filter-bar" style="width:100%; text-align:center;">📅 Apr 11, 2025 - Apr 20, 2025 ▼</div>', unsafe_allow_html=True)
        with c2: st.selectbox("Equip", ["All Equipment"], label_visibility="collapsed")
        with c3: st.selectbox("Loc", ["All Locations"], label_visibility="collapsed")
        with c4: st.button("+ Generate Report", use_container_width=True)

    # 2. KPI CARDS (5)
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.markdown('<div class="kpi-card"><div style="background:#E7F1FF; padding:10px; border-radius:8px; font-size:18px;">📄</div><div><div style="color: #6C757D; font-size: 11px; font-weight: 600;">Total Reports</div><div style="font-size: 22px; font-weight: bold; color: #1A1D21;">37</div><div style="color: #198754; font-size: 10px;">↑ 12% vs last week</div></div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="kpi-card"><div style="background:#E8F5E9; padding:10px; border-radius:8px; font-size:18px;">🔧</div><div><div style="color: #6C757D; font-size: 11px; font-weight: 600;">Maintenance Reports</div><div style="font-size: 22px; font-weight: bold; color: #1A1D21;">14</div><div style="color: #198754; font-size: 10px;">↑ 27% vs last week</div></div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="kpi-card"><div style="background:#FFF3E0; padding:10px; border-radius:8px; font-size:18px;">⚠️</div><div><div style="color: #6C757D; font-size: 11px; font-weight: 600;">Alert Reports</div><div style="font-size: 22px; font-weight: bold; color: #1A1D21;">8</div><div style="color: #DC3545; font-size: 10px;">↓ 5% vs last week</div></div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="kpi-card"><div style="background:#F3E8FF; padding:10px; border-radius:8px; font-size:18px;">📊</div><div><div style="color: #6C757D; font-size: 11px; font-weight: 600;">Performance Reports</div><div style="font-size: 22px; font-weight: bold; color: #1A1D21;">10</div><div style="color: #198754; font-size: 10px;">↑ 10% vs last week</div></div></div>', unsafe_allow_html=True)
    with c5:
        st.markdown('<div class="kpi-card"><div style="background:#E0F7FA; padding:10px; border-radius:8px; font-size:18px;">💾</div><div><div style="color: #6C757D; font-size: 11px; font-weight: 600;">Data & Sensor Reports</div><div style="font-size: 22px; font-weight: bold; color: #1A1D21;">5</div><div style="color: #198754; font-size: 10px;">↑ 25% vs last week</div></div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. ROW 1 (Charts & Quick Actions)
    col_r1_left, col_r1_mid, col_r1_right = st.columns([1.5, 1, 1])
    with col_r1_left:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:13px; font-weight:600; margin-bottom:10px;">Report Overview</div>', unsafe_allow_html=True)
        fig_bar = go.Figure()
        days = ['Apr 11', 'Apr 12', 'Apr 13', 'Apr 14', 'Apr 15', 'Apr 16', 'Apr 17']
        fig_bar.add_trace(go.Bar(x=days, y=[3, 4, 3, 5, 4, 3, 4], name='Maintenance', marker_color='#0D6EFD'))
        fig_bar.add_trace(go.Bar(x=days, y=[2, 2, 2, 3, 2, 2, 3], name='Alerts', marker_color='#FFC107'))
        fig_bar.add_trace(go.Bar(x=days, y=[1, 2, 1, 2, 1, 2, 2], name='Performance', marker_color='#6F42C1'))
        fig_bar.add_trace(go.Bar(x=days, y=[1, 1, 1, 1, 1, 1, 1], name='Data', marker_color='#0DCAF0'))
        fig_bar.update_layout(template="plotly_white", height=220, margin=dict(l=0, r=0, t=0, b=0), barmode='stack', legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5, font=dict(size=9)))
        st.plotly_chart(fig_bar, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_r1_mid:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:13px; font-weight:600; margin-bottom:10px;">Report Types</div>', unsafe_allow_html=True)
        fig_pie = go.Figure(data=[go.Pie(labels=["Maintenance", "Alerts", "Performance", "Data & Sensors"], values=[14, 8, 10, 5], hole=0.65, marker=dict(colors=["#0D6EFD", "#FFC107", "#6F42C1", "#0DCAF0"]), textinfo='none')])
        fig_pie.add_annotation(text="<b>37</b><br><span style='font-size:10px;color:#6C757D'>Total Reports</span>", x=0.5, y=0.5, font=dict(size=16, color="#1A1D21"), showarrow=False)
        fig_pie.update_layout(template="plotly_white", height=220, margin=dict(l=0, r=0, t=0, b=0), showlegend=True, legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.0, font=dict(size=9)))
        st.plotly_chart(fig_pie, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_r1_right:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:13px; font-weight:600; margin-bottom:10px;">Quick Actions</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="display:flex; flex-direction:column; gap:6px; font-size:11px;">
            <div style="border:1px solid #DEE2E6; border-radius:6px; padding:8px; display:flex; justify-content:space-between;"><div>🔧 Generate Maintenance Report</div><div style="color:#6C757D;">›</div></div>
            <div style="border:1px solid #DEE2E6; border-radius:6px; padding:8px; display:flex; justify-content:space-between;"><div>⚠️ Generate Alert Report</div><div style="color:#6C757D;">›</div></div>
            <div style="border:1px solid #DEE2E6; border-radius:6px; padding:8px; display:flex; justify-content:space-between;"><div>📊 Generate Performance Report</div><div style="color:#6C757D;">›</div></div>
            <div style="border:1px solid #DEE2E6; border-radius:6px; padding:8px; display:flex; justify-content:space-between;"><div>📄 Export All Reports</div><div style="color:#6C757D;">›</div></div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # 4. ROW 2 (Table & Summary)
    col_r2_left, col_r2_right = st.columns([2, 1])
    with col_r2_left:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:13px; font-weight:600; margin-bottom:10px;">Recent Reports</div>', unsafe_allow_html=True)
        st.markdown("""
        <table class="custom-table">
            <thead><tr><th>#</th><th>Report Name</th><th>Type</th><th>Generated On</th><th>Status</th></tr></thead>
            <tbody>
                <tr><td>1</td><td>RPT-0016 - Weekly Maintenance</td><td><span class="badge badge-blue">Maintenance</span></td><td>Apr 20, 2025</td><td><span class="badge badge-green">Completed</span></td></tr>
                <tr><td>2</td><td>RPT-0015 - Critical Alert</td><td><span class="badge badge-red">Alert</span></td><td>Apr 20, 2025</td><td><span class="badge badge-green">Completed</span></td></tr>
                <tr><td>3</td><td>RPT-0014 - Performance</td><td><span class="badge badge-purple">Performance</span></td><td>Apr 19, 2025</td><td><span class="badge badge-green">Completed</span></td></tr>
            </tbody>
        </table>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_r2_right:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:13px; font-weight:600; margin-bottom:10px;">Top Report Summary</div>', unsafe_allow_html=True)
        st.markdown("""
        <table class="custom-table">
            <tr><td>🔧 Maintenance</td><td style="text-align:right; font-weight:bold;">14</td><td style="text-align:right; color:#198754; font-size:10px;">↑ 27%</td></tr>
            <tr><td>⚠️ Alerts</td><td style="text-align:right; font-weight:bold;">8</td><td style="text-align:right; color:#DC3545; font-size:10px;">↓ 5%</td></tr>
            <tr><td>📊 Performance</td><td style="text-align:right; font-weight:bold;">10</td><td style="text-align:right; color:#198754; font-size:10px;">↑ 10%</td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)