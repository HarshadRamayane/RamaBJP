import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

def render_analytics():
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
        .main-card { background-color: #FFFFFF; border: 1px solid #DEE2E6; border-radius: 8px; padding: 15px; margin-bottom: 15px; box-shadow: 0 1px 3px rgba(0,0,0,0.02); }
        
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
        
        /* Mini Sensor Cards */
        .sensor-card { background: #F8F9FA; border: 1px solid #DEE2E6; padding: 10px; border-radius: 6px; text-align: center; }
        .sensor-val { font-size: 16px; font-weight: bold; color: #1A1D21; }
        .sensor-label { font-size: 10px; color: #6C757D; margin-bottom: 5px;}
    </style>
    """, unsafe_allow_html=True)

    # ============================================================
    # 1. HEADER & FILTERS
    # ============================================================
    col_h1, col_h2 = st.columns([1.5, 1.5])
    with col_h1:
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
            <div style="background: #0D6EFD; color: white; padding: 8px; border-radius: 8px; font-size: 20px;">📈</div>
            <div>
                <h3 style="margin: 0; font-size: 22px; font-weight: 700; color: #1A1D21;">Analytics & Trends</h3>
                <p style="margin: 0; font-size: 12px; color: #6C757D;">Explore trends, patterns and performance insights across your equipment and sensor data.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_h2:
        c1, c2, c3, c4 = st.columns([1.2, 1.2, 1.2, 1])
        with c1: st.markdown('<div style="background:#F8F9FA; border:1px solid #DEE2E6; padding:6px; border-radius:4px; font-size:11px; color:#6C757D;">📅 Apr 21, 2025 - Apr 28, 2025 ▼</div>', unsafe_allow_html=True)
        with c2: st.selectbox("Equip", ["All Equipment"], label_visibility="collapsed")
        with c3: st.selectbox("Loc", ["All Locations"], label_visibility="collapsed")
        with c4: st.button("⬇️ Export Report", use_container_width=True)

    # ============================================================
    # 2. KPI CARDS (5)
    # ============================================================
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.markdown('<div class="kpi-card" style="border-left: 3px solid #0D6EFD;"><div><div style="color: #0D6EFD; font-size: 11px; font-weight: 600;">Total Equipment</div><div style="font-size: 20px; font-weight: bold; color: #1A1D21;">24</div><div style="color: #198754; font-size: 10px;">↑ 3 since last week</div></div></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="kpi-card" style="border-left: 3px solid #198754;"><div><div style="color: #198754; font-size: 11px; font-weight: 600;">Healthy Equipment</div><div style="font-size: 20px; font-weight: bold; color: #1A1D21;">18</div><div style="color: #198754; font-size: 10px;">75% of total</div></div></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="kpi-card" style="border-left: 3px solid #FFC107;"><div><div style="color: #FFC107; font-size: 11px; font-weight: 600;">At Risk</div><div style="font-size: 20px; font-weight: bold; color: #1A1D21;">4</div><div style="color: #198754; font-size: 10px;">17% of total</div></div></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="kpi-card" style="border-left: 3px solid #DC3545;"><div><div style="color: #DC3545; font-size: 11px; font-weight: 600;">Critical</div><div style="font-size: 20px; font-weight: bold; color: #1A1D21;">2</div><div style="color: #198754; font-size: 10px;">8% of total</div></div></div>', unsafe_allow_html=True)
    with c5:
        st.markdown('<div class="kpi-card" style="border-left: 3px solid #6F42C1;"><div><div style="color: #6F42C1; font-size: 11px; font-weight: 600;">Avg. MTBF</div><div style="font-size: 20px; font-weight: bold; color: #1A1D21;">312 hrs</div><div style="color: #198754; font-size: 10px;">↑ 12% vs last week</div></div></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ============================================================
    # 3. ROW 1 (Health Trend + Performance)
    # ============================================================
    col_r1_left, col_r1_right = st.columns([1.5, 1])

    with col_r1_left:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;"><div style="font-size:14px; font-weight:600;">📈 Equipment Health Trend</div><div style="font-size:10px; color:#6C757D;">Last 7 Days ▼</div></div>', unsafe_allow_html=True)
        
        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(x=["Apr 21", "Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", "Apr 27", "Apr 28"], y=[60, 62, 65, 63, 68, 70, 72, 75], mode='lines', name='Health Score', line=dict(color='#0D6EFD', width=2)))
        fig_line.add_trace(go.Scatter(x=["Apr 21", "Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", "Apr 27", "Apr 28"], y=[40, 42, 45, 44, 48, 50, 52, 55], mode='lines', name='Risk Score', line=dict(color='#FFC107', width=2)))
        fig_line.add_trace(go.Scatter(x=["Apr 21", "Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", "Apr 27", "Apr 28"], y=[20, 22, 25, 23, 28, 30, 32, 35], mode='lines', name='Critical', line=dict(color='#DC3545', width=2)))
        
        fig_line.update_layout(template="plotly_white", height=220, margin=dict(l=0, r=0, t=0, b=0), legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5, font=dict(size=9)), xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor="#F1F3F5"))
        st.plotly_chart(fig_line, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_r1_right:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:14px; font-weight:600; margin-bottom:10px;">⏱️ Performance by Equipment Type</div>', unsafe_allow_html=True)
        
        fig_pie = go.Figure(data=[go.Pie(
            labels=["Tanks", "Vehicles", "Artillery", "Aircraft", "Radar Systems", "Communication"],
            values=[30, 25, 15, 15, 10, 5],
            hole=0.6,
            marker=dict(colors=["#0D6EFD", "#198754", "#FFC107", "#DC3545", "#6F42C1", "#0DCAF0"]),
            textinfo='none'
        )])
        fig_pie.add_annotation(text="24<br><span style='font-size:10px;color:#6C757D'>Total</span>", x=0.5, y=0.5, font=dict(size=16, color="#1A1D21"), showarrow=False)
        fig_pie.update_layout(template="plotly_white", height=220, margin=dict(l=0, r=0, t=0, b=0), showlegend=True, legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.0, font=dict(size=9)))
        st.plotly_chart(fig_pie, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ============================================================
    # 4. ROW 2 (Sensor Trend + Top Risk + Key Insights)
    # ============================================================
    col_r2_left, col_r2_mid, col_r2_right = st.columns([1, 1.2, 1])

    # --- Left: Sensor Trend (Mini Cards) ---
    with col_r2_left:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:14px; font-weight:600; margin-bottom:10px;">📊 Sensor Trend (Last 7 Days)</div>', unsafe_allow_html=True)
        
        # Mini Grid
        st.markdown("""
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 8px;">
            <div class="sensor-card"><div class="sensor-label">Temperature</div><div class="sensor-val" style="color:#198754;">↓ 72.3 °C</div></div>
            <div class="sensor-card"><div class="sensor-label">Oil Quality</div><div class="sensor-val" style="color:#198754;">↑ 86.7 %</div></div>
            <div class="sensor-card"><div class="sensor-label">Pressure</div><div class="sensor-val" style="color:#198754;">↑ 4.8 bar</div></div>
            <div class="sensor-card"><div class="sensor-label">Current</div><div class="sensor-val" style="color:#198754;">↓ 12.4 A</div></div>
            <div class="sensor-card"><div class="sensor-label">RPM</div><div class="sensor-val" style="color:#198754;">↑ 1760</div></div>
            <div class="sensor-card"><div class="sensor-label">Fuel Level</div><div class="sensor-val" style="color:#FFC107;">↓ 68.5 %</div></div>
            <div class="sensor-card"><div class="sensor-label">Battery Voltage</div><div class="sensor-val" style="color:#DC3545;">↓ 11.8 V</div></div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Middle: Top Risk Equipment ---
    with col_r2_mid:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:14px; font-weight:600; margin-bottom:10px;">⚠️ Top 5 Risk Equipment</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <table class="custom-table">
            <tr><th>Equipment</th><th>Health Score</th><th>Risk Level</th><th>Trend</th></tr>
            <tr><td>EQ-006 Communication Unit</td><td>41</td><td><span class="badge badge-red">Critical</span></td><td>↓</td></tr>
            <tr><td>EQ-003 Artillery Gun</td><td>65</td><td><span class="badge badge-red">High</span></td><td>↓</td></tr>
            <tr><td>EQ-001 T-90 Tank</td><td>92</td><td><span class="badge badge-red">Critical</span></td><td>↓</td></tr>
            <tr><td>EQ-007 Helicopter</td><td>70</td><td><span class="badge badge-yellow">Medium</span></td><td>→</td></tr>
            <tr><td>EQ-002 APC Vehicle</td><td>87</td><td><span class="badge badge-green">Low</span></td><td>↑</td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Right: Key Insights ---
    with col_r2_right:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:14px; font-weight:600; margin-bottom:10px;">💡 Key Insights</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="font-size:10px; display:flex; flex-direction:column; gap:10px; color:#6C757D;">
            <div><span style="color:#0D6EFD;">●</span> <b>Overall health improved by 28%</b> compared to last month.</div>
            <div><span style="color:#DC3545;">●</span> <b>Communication Unit</b> requires immediate maintenance.</div>
            <div><span style="color:#FFC107;">●</span> <b>Battery voltage</b> levels are declining in 4 devices.</div>
            <div><span style="color:#198754;">●</span> <b>T-90 Tank</b> showed a 15% health score increase.</div>
            <div><span style="color:#6C757D;">●</span> <b>Average fuel efficiency</b> improved by 12%.</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ============================================================
    # 5. ROW 3 (Predictive Chart + Report Summary + Image Banner)
    # ============================================================
    col_r3_left, col_r3_mid, col_r3_right = st.columns([1.5, 1, 1])

    # --- Left: Predictive Trend ---
    with col_r3_left:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;"><div style="font-size:14px; font-weight:600;">📉 Predictive Trend (Next 7 Days)</div><div style="font-size:10px; color:#6C757D;">Next 7 Days ▼</div></div>', unsafe_allow_html=True)
        
        fig_pred = go.Figure()
        fig_pred.add_trace(go.Scatter(x=["May 1", "May 2", "May 3", "May 4", "May 5", "May 6", "May 7"], y=[75, 74, 72, 70, 68, 65, 62], mode='lines+markers', name='Healthy', line=dict(color='#198754', width=2)))
        fig_pred.add_trace(go.Scatter(x=["May 1", "May 2", "May 3", "May 4", "May 5", "May 6", "May 7"], y=[55, 54, 52, 50, 48, 46, 45], mode='lines+markers', name='At Risk', line=dict(color='#FFC107', width=2)))
        fig_pred.add_trace(go.Scatter(x=["May 1", "May 2", "May 3", "May 4", "May 5", "May 6", "May 7"], y=[35, 34, 33, 32, 30, 28, 26], mode='lines+markers', name='Critical', line=dict(color='#DC3545', width=2)))
        
        fig_pred.update_layout(template="plotly_white", height=200, margin=dict(l=0, r=0, t=0, b=0), legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5, font=dict(size=9)), xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor="#F1F3F5"))
        st.plotly_chart(fig_pred, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Middle: Report Summary ---
    with col_r3_mid:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div style="font-size:14px; font-weight:600; margin-bottom:10px;">📋 Report Summary</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <table class="custom-table">
            <tr><td>Total Data Points</td><td style="text-align:right; font-weight:bold;">1,248,320</td><td style="text-align:right; color:#198754; font-size:10px;">↑ 12%</td></tr>
            <tr><td>Alerts Generated</td><td style="text-align:right; font-weight:bold;">37</td><td style="text-align:right; color:#DC3545; font-size:10px;">↑ 5%</td></tr>
            <tr><td>Maintenance Actions</td><td style="text-align:right; font-weight:bold;">12</td><td style="text-align:right; color:#198754; font-size:10px;">↓ 8%</td></tr>
            <tr><td>Analysis Completed</td><td style="text-align:right; font-weight:bold;">24</td><td style="text-align:right; color:#198754; font-size:10px;">↑ 10%</td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Right: Image Banner ---
    with col_r3_right:
        st.markdown('<div class="main-card" style="height: 100%; padding: 0; overflow: hidden; border-radius: 8px; position: relative;">', unsafe_allow_html=True)
        # Banner Image
        st.markdown("""
        <div style="width: 100%; height: 200px; background: url('https://images.unsplash.com/photo-1579912268200-5e4b4d9c5c1e?q=80&w=400&auto=format&fit=crop') center/cover no-repeat; position: relative;">
            <div style="position: absolute; bottom: 0; left: 0; right: 0; background: linear-gradient(to top, rgba(10,25,41,0.9), transparent); padding: 15px;">
                <div style="font-weight: bold; color: white; font-size: 14px;">STRONGER DEFENCE</div>
                <div style="color: #64FFDA; font-size: 18px; font-weight: bold;">WITH DATA</div>
                <div style="color: #A0ABC0; font-size: 10px; margin-top: 5px;">RAMEDOX Defence. Predictive. Reliable. Mission Ready.</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)