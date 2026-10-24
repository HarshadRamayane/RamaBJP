import streamlit as st
import plotly.graph_objects as go

def render_sensors():
    # ============================================================
    # EXACT LIGHT THEME CSS
    # ============================================================
    st.markdown("""
    <style>
        /* Main Background */
        .stApp { background-color: #F8F9FA !important; }
        .block-container { padding-top: 1.5rem !important; }
        
        /* Hide Streamlit Default Header */
        header[data-testid="stHeader"] { display: none !important; }
        
        /* Top Bar */
        .top-bar {
            display: flex; justify-content: space-between; align-items: center;
            background-color: #FFFFFF; padding: 10px 20px; border-radius: 8px;
            border: 1px solid #DEE2E6; margin-bottom: 20px;
        }
        
        /* Sensor Small Cards */
        .sensor-card {
            background-color: #FFFFFF; border: 1px solid #DEE2E6;
            border-radius: 8px; padding: 12px; text-align: center;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        }
        .sensor-title { color: #6C757D; font-size: 11px; margin-bottom: 4px; }
        .sensor-value { color: #1A1D21; font-size: 18px; font-weight: 700; margin-bottom: 4px; }
        .sensor-status { font-size: 10px; font-weight: 600; }
        
        /* Main Cards */
        .main-card {
            background-color: #FFFFFF; border: 1px solid #DEE2E6;
            border-radius: 8px; padding: 15px; margin-bottom: 15px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        }
        
        /* Tables */
        .custom-table { width: 100%; border-collapse: collapse; font-size: 11px; }
        .custom-table th { color: #6C757D; text-align: left; padding: 8px 5px; border-bottom: 1px solid #DEE2E6; font-weight: 500; }
        .custom-table td { padding: 8px 5px; border-bottom: 1px solid #F8F9FA; color: #1A1D21; vertical-align: middle; }
        
        /* Badges */
        .badge { padding: 3px 8px; border-radius: 12px; font-size: 9px; font-weight: 600; }
        .badge-green { background: #D1E7DD; color: #0F5132; }
        .badge-yellow { background: #FFF3CD; color: #664D03; }
        .badge-red { background: #F8D7DA; color: #842029; }
    </style>
    """, unsafe_allow_html=True)

    # ============================================================
    # 1. TOP BAR
    # ============================================================
    st.markdown("""
    <div class="top-bar">
        <div style="color: #1A1D21; font-weight: 600; font-size: 14px;">RAMEDOX <span style="font-weight: normal; color: #6C757D; margin-left: 10px;">Predictive Maintenance for Defence Equipment</span></div>
        <div style="display: flex; gap: 15px; align-items: center; font-size: 12px;">
            <span style="color: #198754; font-weight: 600;">🟢 System Online</span>
            <span>🔔 <span style="background: #DC3545; color: white; border-radius: 50%; padding: 2px 5px; font-size: 9px;">3</span></span>
            <div style="display: flex; align-items: center; gap: 8px;">
                <div style="background: #E7F1FF; color: #0D6EFD; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 11px;">ME</div>
                <div style="line-height: 1.2;"><div style="font-weight: 600; color: #1A1D21;">Maintenance Engineer</div><div style="font-size: 10px; color: #6C757D;">Defence MRO ▼</div></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ============================================================
    # 2. HEADER & FILTERS
    # ============================================================
    col_h1, col_h2 = st.columns([1, 1.5])
    with col_h1:
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">
            <div style="background: #E7F1FF; color: #0D6EFD; padding: 8px; border-radius: 8px; font-size: 20px;">📡</div>
            <div>
                <h3 style="margin: 0; font-size: 18px; font-weight: 700; color: #1A1D21;">Sensor Monitoring</h3>
                <p style="margin: 0; font-size: 11px; color: #6C757D;">Real-time sensor data and equipment health status.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_h2:
        c1, c2, c3, c4, c5 = st.columns([1.5, 1, 1, 1, 0.8])
        with c1: st.selectbox("Equip", ["T-90 Main Battle Tank EQ-001"], label_visibility="collapsed")
        with c2: st.selectbox("Time", ["Last 7 Days"], label_visibility="collapsed")
        with c3: 
            st.markdown('<div style="background: #D1E7DD; color: #0F5132; text-align: center; padding: 6px; border-radius: 4px; font-size: 11px; font-weight: 600;">🟢 Live Data</div>', unsafe_allow_html=True)
        with c4:
            st.markdown('<div style="background: #E2E3E5; color: #41464B; text-align: center; padding: 6px; border-radius: 4px; font-size: 11px; font-weight: 600; cursor: pointer;">🔄 Refresh</div>', unsafe_allow_html=True)
        with c5:
            st.markdown('<div style="background: #D1E7DD; color: #0F5132; text-align: center; padding: 6px; border-radius: 4px; font-size: 11px; font-weight: 600;">Auto (30s)</div>', unsafe_allow_html=True)

    # ============================================================
    # 3. 6 SENSOR CARDS
    # ============================================================
    sensors = [
        ("📳 Vibration", "2.4 mm/s", "Normal", "#0D6EFD", "#E7F1FF"),
        ("🌡️ Temperature", "72 °C", "Normal", "#198754", "#D1E7DD"),
        ("🛢️ Oil Quality", "Good", "Normal", "#6F42C1", "#E2D9F3"),
        ("☁️ Pressure", "4.2 bar", "Normal", "#0D6EFD", "#E7F1FF"),
        ("⚡ Current", "12.5 A", "Normal", "#FFC107", "#FFF3CD"),
        ("🔄 RPM", "1800", "Normal", "#198754", "#D1E7DD"),
    ]

    cols = st.columns(6)
    for i, (title, val, status, color, bg) in enumerate(sensors):
        with cols[i]:
            st.markdown(f"""
            <div class="sensor-card">
                <div class="sensor-title" style="color: {color};">{title}</div>
                <div class="sensor-value">{val}</div>
                <div class="sensor-status" style="color: {color}; background: {bg}; padding: 2px 6px; border-radius: 4px; display: inline-block;">{status}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ============================================================
    # 4. CHARTS ROW (Line + Gauge)
    # ============================================================
    col_chart, col_gauge = st.columns([2.5, 1])

    with col_chart:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown('<div style="font-size: 13px; font-weight: 600; margin-bottom: 10px;">📈 Sensor Readings (Last 7 Days)</div>', unsafe_allow_html=True)
        
        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(x=["Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", "Apr 27", "Apr 28"], y=[60, 65, 62, 68, 70, 69, 72], mode='lines+markers', name='Temperature', line=dict(color='#0D6EFD')))
        fig_line.add_trace(go.Scatter(x=["Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", "Apr 27", "Apr 28"], y=[40, 45, 42, 48, 50, 48, 52], mode='lines+markers', name='Vibration', line=dict(color='#FFC107')))
        fig_line.add_trace(go.Scatter(x=["Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", "Apr 27", "Apr 28"], y=[25, 28, 26, 30, 32, 30, 35], mode='lines+markers', name='Pressure', line=dict(color='#6F42C1')))
        fig_line.add_trace(go.Scatter(x=["Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", "Apr 27", "Apr 28"], y=[15, 18, 16, 20, 22, 20, 25], mode='lines+markers', name='Current', line=dict(color='#198754')))
        fig_line.add_trace(go.Scatter(x=["Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", "Apr 27", "Apr 28"], y=[10, 12, 11, 14, 15, 14, 18], mode='lines+markers', name='RPM', line=dict(color='#DC3545')))
        
        fig_line.update_layout(
            template="plotly_white", height=260, margin=dict(l=10, r=10, t=10, b=10),
            legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5, font=dict(size=9)),
            xaxis=dict(showgrid=True, gridcolor="#F1F3F5"),
            yaxis=dict(showgrid=True, gridcolor="#F1F3F5")
        )
        st.plotly_chart(fig_line, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_gauge:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div style="font-size: 13px; font-weight: 600; margin-bottom: 10px;">🛡️ Equipment Health Status</div>', unsafe_allow_html=True)
        
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = 92,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "92%", 'font': {'size': 24, 'color': '#198754'}},
            gauge = {
                'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "#198754"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "#E9ECEF",
                'steps': [
                    {'range': [0, 50], 'color': '#F8D7DA'},
                    {'range': [50, 80], 'color': '#FFF3CD'},
                    {'range': [80, 100], 'color': '#D1E7DD'}
                ],
            }
        ))
        fig_gauge.update_layout(height=180, margin=dict(l=20, r=20, t=30, b=10))
        st.plotly_chart(fig_gauge, use_container_width=True)
        
        st.markdown("""
        <div style="font-size: 10px; color: #6C757D; line-height: 1.6; margin-top: -20px;">
            <span style="color: #198754;">●</span> Normal <b>5</b><br>
            <span style="color: #FFC107;">●</span> Warning <b>2</b><br>
            <span style="color: #DC3545;">●</span> Critical <b>1</b><br>
            <span style="color: #6C757D;">●</span> Offline <b>0</b>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: #D1E7DD; padding: 8px; border-radius: 6px; font-size: 10px; color: #0F5132; margin-top: 10px;">
            ✅ Equipment is operating within normal sensor limits.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ============================================================
    # 5. BOTTOM ROW (Details, Alerts, Live View)
    # ============================================================
    col_b1, col_b2, col_b3 = st.columns([1.2, 1.2, 1])

    # --- Bottom 1: Sensor Details ---
    with col_b1:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown('<div style="font-size: 13px; font-weight: 600; margin-bottom: 10px;">⚙️ Sensor Details</div>', unsafe_allow_html=True)
        st.markdown("""
        <table class="custom-table">
            <tr><th>Sensor</th><th>Current</th><th>Normal</th><th>Status</th></tr>
            <tr><td>📳 Vibration</td><td>2.4 mm/s</td><td>0 - 5 mm/s</td><td><span class="badge badge-green">Normal</span></td></tr>
            <tr><td>🌡️ Temperature</td><td>72 °C</td><td>50 - 90 °C</td><td><span class="badge badge-green">Normal</span></td></tr>
            <tr><td>🛢️ Oil Quality</td><td>Good</td><td>Normal</td><td><span class="badge badge-green">Normal</span></td></tr>
            <tr><td>☁️ Pressure</td><td>4.2 bar</td><td>3 - 6 bar</td><td><span class="badge badge-green">Normal</span></td></tr>
            <tr><td>⚡ Current</td><td>12.5 A</td><td>10 - 15 A</td><td><span class="badge badge-green">Normal</span></td></tr>
            <tr><td>🔄 RPM</td><td>1800</td><td>1500 - 2000</td><td><span class="badge badge-green">Normal</span></td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Bottom 2: Recent Alerts ---
    with col_b2:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown('<div style="font-size: 13px; font-weight: 600; margin-bottom: 10px;">🔔 Recent Alerts</div>', unsafe_allow_html=True)
        st.markdown("""
        <div style="font-size: 10px; line-height: 1.8;">
            <div style="border-bottom: 1px solid #F1F3F5; padding: 5px 0; display: flex; justify-content: space-between;">
                <div><span style="color: #FFC107;">⚠️</span> Apr 28, 10:24<br><b>High Temperature</b></div>
                <span class="badge badge-yellow">Warning</span>
            </div>
            <div style="border-bottom: 1px solid #F1F3F5; padding: 5px 0; display: flex; justify-content: space-between;">
                <div><span style="color: #198754;">ℹ️</span> Apr 28, 11:56<br><b>Sensor data normal</b></div>
                <span class="badge badge-green">Normal</span>
            </div>
            <div style="border-bottom: 1px solid #F1F3F5; padding: 5px 0; display: flex; justify-content: space-between;">
                <div><span style="color: #DC3545;">🚨</span> Apr 28, 10:24<br><b>Vibration limit close</b></div>
                <span class="badge badge-red">Critical</span>
            </div>
            <div style="padding: 5px 0; display: flex; justify-content: space-between;">
                <div><span style="color: #FFC107;">⚠️</span> Apr 28, 14:45<br><b>Oil quality reduced</b></div>
                <span class="badge badge-yellow">Warning</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Bottom 3: Live Sensor View ---
    with col_b3:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div style="font-size: 13px; font-weight: 600; margin-bottom: 10px;">📷 Live Sensor View</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="background: #E9ECEF; border-radius: 8px; height: 120px; display: flex; align-items: center; justify-content: center; margin-bottom: 10px; position: relative;">
            <span style="font-size: 40px;">🚜</span>
            <div style="position: absolute; top: 5px; left: 5px; background: #198754; color: white; padding: 2px 6px; border-radius: 4px; font-size: 9px;">● Live</div>
            <div style="position: absolute; bottom: 5px; right: 5px; background: rgba(0,0,0,0.6); color: white; padding: 2px 6px; border-radius: 4px; font-size: 9px;">EQ-001 - T-90 Main Battle Tank</div>
        </div>
        
        <div style="display: flex; justify-content: space-between; font-size: 10px; color: #6C757D; text-align: center;">
            <div>📳<br>Vibration</div>
            <div>🌡️<br>Temp</div>
            <div>🛢️<br>Oil</div>
            <div>☁️<br>Pressure</div>
            <div>⚡<br>Current</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)