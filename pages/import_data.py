import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def render_import():
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
        
        /* KPI Cards */
        .kpi-card {
            background-color: #FFFFFF; border: 1px solid #DEE2E6;
            border-radius: 8px; padding: 15px; display: flex; align-items: center;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        }
        
        /* Main Cards */
        .main-card {
            background-color: #FFFFFF; border: 1px solid #DEE2E6;
            border-radius: 8px; padding: 15px; margin-bottom: 15px;
            box-shadow: 0 1px 3px rgba(0,0,0,0.02);
        }
        
        /* Source Cards */
        .source-card {
            background-color: #F8F9FA; border: 1px solid #DEE2E6;
            border-radius: 8px; padding: 15px; text-align: center;
            cursor: pointer; transition: 0.2s;
        }
        .source-card:hover { background-color: #E7F1FF; border-color: #0D6EFD; }
        
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
            <span>🔔 <span style="background: #DC3545; color: white; border-radius: 50%; padding: 2px 5px; font-size: 9px;">3</span></span>
            <div style="display: flex; align-items: center; gap: 8px;">
                <div style="background: #E7F1FF; color: #0D6EFD; width: 28px; height: 28px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 11px;">TE</div>
                <div style="line-height: 1.2;"><div style="font-weight: 600; color: #1A1D21;">Tech Engineer</div><div style="font-size: 10px; color: #6C757D;">Maintenance Team ▼</div></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ============================================================
    # 2. HEADER & FILTERS
    # ============================================================
    col_h1, col_h2 = st.columns([1, 1.2])
    with col_h1:
        st.markdown("""
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 15px;">
            <div style="background: #E7F1FF; color: #0D6EFD; padding: 8px; border-radius: 8px; font-size: 20px;">📥</div>
            <div>
                <h3 style="margin: 0; font-size: 18px; font-weight: 700; color: #1A1D21;">Data Import & Ingestion</h3>
                <p style="margin: 0; font-size: 11px; color: #6C757D;">Bring data from multiple sources, validate it and make it ready for analysis.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    with col_h2:
        c1, c2, c3, c4 = st.columns([1.5, 1, 1, 1])
        with c1: 
            st.markdown('<div style="background: #FFFFFF; border: 1px solid #DEE2E6; padding: 6px; border-radius: 4px; font-size: 11px; color: #6C757D;">📅 Apr 21, 2025 - Apr 28, 2025 ▼</div>', unsafe_allow_html=True)
        with c2: st.selectbox("Source", ["All Sources"], label_visibility="collapsed")
        with c3: st.selectbox("Status", ["All Status"], label_visibility="collapsed")
        with c4: st.button("+ Import Data", use_container_width=True)

    # ============================================================
    # 3. KPI CARDS (4)
    # ============================================================
    st.markdown("""
    <div style="display: flex; gap: 15px; margin-bottom: 20px;">
        <div class="kpi-card" style="flex: 1; border-left: 4px solid #0D6EFD;">
            <div style="background: #E7F1FF; color: #0D6EFD; padding: 12px; border-radius: 50%; margin-right: 15px; font-size: 20px;">🗄️</div>
            <div>
                <div style="color: #0D6EFD; font-size: 12px; font-weight: 600;">Total Files Imported</div>
                <div style="font-size: 24px; font-weight: bold; color: #1A1D21; line-height: 1.2;">12</div>
                <div style="color: #198754; font-size: 10px;">↑ 3 new today</div>
            </div>
        </div>
        <div class="kpi-card" style="flex: 1; border-left: 4px solid #198754;">
            <div style="background: #D1E7DD; color: #198754; padding: 12px; border-radius: 50%; margin-right: 15px; font-size: 20px;">✅</div>
            <div>
                <div style="color: #198754; font-size: 12px; font-weight: 600;">Successfully Processed</div>
                <div style="font-size: 24px; font-weight: bold; color: #1A1D21; line-height: 1.2;">11</div>
                <div style="color: #6C757D; font-size: 10px;">92% success rate</div>
            </div>
        </div>
        <div class="kpi-card" style="flex: 1; border-left: 4px solid #DC3545;">
            <div style="background: #F8D7DA; color: #DC3545; padding: 12px; border-radius: 50%; margin-right: 15px; font-size: 20px;">🚨</div>
            <div>
                <div style="color: #DC3545; font-size: 12px; font-weight: 600;">Failed Imports</div>
                <div style="font-size: 24px; font-weight: bold; color: #1A1D21; line-height: 1.2;">1</div>
                <div style="color: #6C757D; font-size: 10px;">Needs attention</div>
            </div>
        </div>
        <div class="kpi-card" style="flex: 1; border-left: 4px solid #6F42C1;">
            <div style="background: #E2D9F3; color: #6F42C1; padding: 12px; border-radius: 50%; margin-right: 15px; font-size: 20px;">⏳</div>
            <div>
                <div style="color: #6F42C1; font-size: 12px; font-weight: 600;">Pending Processing</div>
                <div style="font-size: 24px; font-weight: bold; color: #1A1D21; line-height: 1.2;">0</div>
                <div style="color: #6C757D; font-size: 10px;">All up to date</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ============================================================
    # 4. MIDDLE ROW (Data Sources + Recent Imports)
    # ============================================================
    col_mid_left, col_mid_right = st.columns([1, 1.8])

    # --- Left: Data Sources ---
    with col_mid_left:
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        st.markdown('<div style="font-size: 13px; font-weight: 600; margin-bottom: 5px;">📂 Data Sources</div>', unsafe_allow_html=True)
        st.markdown('<div style="font-size: 10px; color: #6C757D; margin-bottom: 15px;">Import data from different sources including files, databases and APIs.</div>', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            <div class="source-card">
                <div style="font-size: 24px; color: #198754;">📗</div>
                <div style="font-size: 12px; font-weight: 600; color: #1A1D21; margin-top: 5px;">CSV / Excel</div>
                <div style="font-size: 10px; color: #0D6EFD; margin-top: 5px;">Upload files →</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
            <div class="source-card">
                <div style="font-size: 24px; color: #0D6EFD;">☁️</div>
                <div style="font-size: 12px; font-weight: 600; color: #1A1D21; margin-top: 5px;">API</div>
                <div style="font-size: 10px; color: #0D6EFD; margin-top: 5px;">API Integration →</div>
            </div>
            """, unsafe_allow_html=True)
        with c2:
            st.markdown("""
            <div class="source-card">
                <div style="font-size: 24px; color: #0D6EFD;">🗄️</div>
                <div style="font-size: 12px; font-weight: 600; color: #1A1D21; margin-top: 5px;">Database</div>
                <div style="font-size: 10px; color: #0D6EFD; margin-top: 5px;">Connect DB →</div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("""
            <div class="source-card">
                <div style="font-size: 24px; color: #6C757D;">📄</div>
                <div style="font-size: 12px; font-weight: 600; color: #1A1D21; margin-top: 5px;">Manual Entry</div>
                <div style="font-size: 10px; color: #0D6EFD; margin-top: 5px;">Add Manually →</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Right: Recent Imports Table ---
    with col_mid_right:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="font-size: 13px; font-weight: 600;">📋 Recent Imports</div>
            <div style="color: #0D6EFD; font-size: 11px; cursor: pointer;">View All</div>
        </div>
        <table class="custom-table">
            <tr><th>Name</th><th>Source</th><th>Type</th><th>Records</th><th>Status</th><th>Time</th></tr>
            <tr><td>equipment_sensor_data.csv</td><td>CSV File</td><td>Sensor</td><td>4,892</td><td><span class="badge badge-green">● Success</span></td><td>Apr 28, 09:42</td></tr>
            <tr><td>maintenance_log.db</td><td>Database</td><td>Maintenance</td><td>1,245</td><td><span class="badge badge-green">● Success</span></td><td>Apr 28, 08:17</td></tr>
            <tr><td>equipment_master.xlsx</td><td>Excel File</td><td>Equipment</td><td>320</td><td><span class="badge badge-green">● Success</span></td><td>Apr 27, 16:35</td></tr>
            <tr><td>vibration_api_data</td><td>API</td><td>Sensor</td><td>2,410</td><td><span class="badge badge-yellow">● Processing</span></td><td>Apr 27, 14:20</td></tr>
            <tr><td>fault_records.csv</td><td>CSV File</td><td>Fault</td><td>0</td><td><span class="badge badge-red">● Failed</span></td><td>Apr 27, 11:03</td></tr>
        </table>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ============================================================
    # 5. BOTTOM ROW (Ingestion Status, Data Volume, Data Quality)
    # ============================================================
    st.markdown("<br>", unsafe_allow_html=True)
    col_b1, col_b2, col_b3 = st.columns([1.2, 1.5, 1])

    # --- Bottom 1: Ingestion Status ---
    with col_b1:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div style="font-size: 13px; font-weight: 600; margin-bottom: 15px;">⏳ Ingestion Status</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px; text-align: center; font-size: 10px; color: #6C757D;">
            <div><div style="background: #D1E7DD; color: #198754; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 5px auto;">✓</div>File Received</div>
            <div style="flex: 1; height: 2px; background: #198754; margin: 0 5px; margin-bottom: 15px;"></div>
            <div><div style="background: #D1E7DD; color: #198754; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 5px auto;">✓</div>Validation</div>
            <div style="flex: 1; height: 2px; background: #198754; margin: 0 5px; margin-bottom: 15px;"></div>
            <div><div style="background: #D1E7DD; color: #198754; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 5px auto;">✓</div>Transformation</div>
            <div style="flex: 1; height: 2px; background: #198754; margin: 0 5px; margin-bottom: 15px;"></div>
            <div><div style="background: #E7F1FF; color: #0D6EFD; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 5px auto; border: 2px solid #0D6EFD;">●</div>Loading</div>
            <div style="flex: 1; height: 2px; background: #E9ECEF; margin: 0 5px; margin-bottom: 15px;"></div>
            <div><div style="background: #E9ECEF; color: #6C757D; width: 24px; height: 24px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 5px auto;">○</div>Complete</div>
        </div>
        
        <div style="font-size: 11px; color: #6C757D; margin-top: 15px; margin-bottom: 5px;">Processing: vibration_api_data <span style="float: right; color: #198754; font-weight: 600;">75%</span></div>
        <div style="background: #E9ECEF; border-radius: 4px; height: 6px; width: 100%;">
            <div style="background: #198754; width: 75%; height: 6px; border-radius: 4px;"></div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Bottom 2: Data Volume Chart ---
    with col_b2:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div style="font-size: 13px; font-weight: 600;">📊 Data Volume</div>
            <div style="font-size: 10px; color: #6C757D; border: 1px solid #DEE2E6; padding: 2px 8px; border-radius: 4px;">Last 7 Days ▼</div>
        </div>
        """, unsafe_allow_html=True)
        
        fig_vol = go.Figure(data=[
            go.Bar(name='Imported Records', x=["Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", "Apr 27", "Apr 28"], y=[2500, 2800, 3500, 3800, 4000, 4200, 4500], marker_color='#0D6EFD'),
            go.Bar(name='Processed Records', x=["Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", "Apr 27", "Apr 28"], y=[2400, 2700, 3400, 3700, 3900, 4100, 4400], marker_color='#198754')
        ])
        fig_vol.update_layout(
            template="plotly_white", height=180, margin=dict(l=0, r=0, t=10, b=0),
            barmode='group', bargap=0.2, bargroupgap=0.1,
            legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5, font=dict(size=9)),
            xaxis=dict(showgrid=False, tickfont=dict(size=9)),
            yaxis=dict(showgrid=True, gridcolor="#F1F3F5", tickfont=dict(size=9))
        )
        st.plotly_chart(fig_vol, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- Bottom 3: Data Quality Gauge ---
    with col_b3:
        st.markdown('<div class="main-card" style="height: 100%;">', unsafe_allow_html=True)
        st.markdown('<div style="font-size: 13px; font-weight: 600; margin-bottom: 10px;">📉 Data Quality</div>', unsafe_allow_html=True)
        
        fig_qual = go.Figure(data=[go.Pie(
            labels=["Valid", "Warnings", "Errors"], 
            values=[92, 6, 2], 
            hole=0.7,
            marker=dict(colors=["#198754", "#FFC107", "#DC3545"]),
            textinfo='none'
        )])
        fig_qual.add_annotation(text="<b>92%</b><br><span style='font-size:10px;color:#6C757D'>Overall Quality</span>", x=0.5, y=0.5, showarrow=False, font=dict(size=20))
        fig_qual.update_layout(
            template="plotly_white", height=180, margin=dict(l=0, r=0, t=10, b=10),
            showlegend=True, legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.0, font=dict(size=9))
        )
        st.plotly_chart(fig_qual, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # ============================================================
    # 6. BOTTOM FOOTER FEATURES
    # ============================================================
    st.markdown("""
    <div style="background: #FFFFFF; border: 1px solid #DEE2E6; border-radius: 8px; padding: 15px; display: flex; justify-content: space-between; text-align: center; font-size: 10px; color: #6C757D;">
        <div style="flex: 1; border-right: 1px solid #DEE2E6;">
            <div style="font-size: 16px; margin-bottom: 5px;">🛡️</div>
            <b style="color: #1A1D21;">Secure & Compliant</b><br>Your data is encrypted and follows defence data handling standards.
        </div>
        <div style="flex: 1; border-right: 1px solid #DEE2E6;">
            <div style="font-size: 16px; margin-bottom: 5px;">📄</div>
            <b style="color: #1A1D21;">Multi-format Support</b><br>CSV, Excel, JSON, XML, etc.
        </div>
        <div style="flex: 1; border-right: 1px solid #DEE2E6;">
            <div style="font-size: 16px; margin-bottom: 5px;">🛡️</div>
            <b style="color: #1A1D21;">Automated Validation</b><br>Checks for data accuracy.
        </div>
        <div style="flex: 1;">
            <div style="font-size: 16px; margin-bottom: 5px;">⚡</div>
            <b style="color: #1A1D21;">Real-time Processing</b><br>Faster insights, better decisions.
        </div>
    </div>
    """, unsafe_allow_html=True)