import streamlit as st
import plotly.graph_objects as go
import base64
import os

# Image ko base64 mein convert karne ka function
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""

def render_dashboard_overview():
    # Tumhari images ke EXACT naam yahan daale hain
    img_tank = get_base64_image("assets/Tank.jpeg")
    img_eq1 = get_base64_image("assets/Engine-1.jpeg")
    img_eq2 = get_base64_image("assets/Engine-2.jpeg")
    img_gen1 = get_base64_image("assets/Generator-1.jpeg")
    img_gen2 = get_base64_image("assets/Generator-2.jpeg")
    img_veh1 = get_base64_image("assets/Vehicle-1.jpeg")
    img_veh2 = get_base64_image("assets/Vehicle-2.jpeg")

    # ============================================================
    # LIGHT THEME & DROPDOWN FIX CSS
    # ============================================================
    st.markdown("""
    <style>
        .stApp { background-color: #F8F9FA !important; }
        .block-container { padding-top: 1rem !important; }
        
        /* Dropdown Design Fix */
        div[data-baseweb="select"] > div {
            background-color: #F8F9FA !important;
            border: 1px solid #DEE2E6 !important;
            border-radius: 8px !important;
            color: #6C757D !important;
        }
        div[data-baseweb="select"] span { color: #6C757D !important; font-weight: 500; }
        div[data-baseweb="popover"] { background-color: #FFFFFF !important; }

        .kpi-card { background-color: #FFFFFF; border: 1px solid #DEE2E6; border-radius: 8px; padding: 15px; display: flex; align-items: center; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
        .chart-card { background-color: #FFFFFF; border: 1px solid #DEE2E6; border-radius: 8px; padding: 20px; margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.02); height: 100%; }
        
        .custom-table { width: 100%; font-size: 12px; border-collapse: collapse; }
        .custom-table th { color: #6C757D; text-align: left; padding: 10px 5px; border-bottom: 1px solid #DEE2E6; font-weight: 500; }
        .custom-table td { padding: 10px 5px; border-bottom: 1px solid #F1F3F5; color: #1A1D21; vertical-align: middle; }
        
        .badge { padding: 3px 8px; border-radius: 4px; font-size: 10px; font-weight: 600; display: inline-block; }
        .badge-normal { background: #D1E7DD; color: #0F5132; }
        .badge-warning { background: #FFF3CD; color: #664D03; }
        .badge-critical { background: #F8D7DA; color: #842029; }
        
        .alert-item { display: flex; justify-content: space-between; align-items: center; padding: 10px; border-radius: 6px; margin-bottom: 8px; }
        .eq-img { width: 28px; height: 28px; border-radius: 4px; object-fit: cover; }
    </style>
    """, unsafe_allow_html=True)

    # ============================================================
    # 1. CUSTOM TOP HEADER BAR
    # ============================================================
    st.markdown("""
    <div class="top-header" style="display: flex; justify-content: space-between; align-items: center; background-color: #FFFFFF; padding: 15px 25px; border-radius: 10px; border: 1px solid #DEE2E6; margin-bottom: 20px;">
        <div style="display: flex; align-items: center; gap: 20px;">
            <div style="color: #1A1D21; font-weight: 600; font-size: 16px;">🛡️ RAMEDOX <span style="font-weight: normal; font-size: 14px; margin-left: 10px; color: #6C757D;">Predictive Maintenance for Defence Equipment</span></div>
        </div>
        <div style="display: flex; align-items: center; gap: 25px; font-size: 13px;">
            <span style="color: #198754; display: flex; align-items: center; gap: 5px;">🟢 System Online</span>
            <span style="position: relative; cursor: pointer;">🔔 <span style="position: absolute; top: -5px; right: -5px; background: #DC3545; color: white; border-radius: 50%; padding: 2px 5px; font-size: 9px; font-weight: bold;">3</span></span>
            <div style="display: flex; align-items: center; gap: 8px;">
                <div style="background: #E7F1FF; color: #0D6EFD; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold;">TE</div>
                <div style="line-height: 1.2;"><div style="font-weight: 600; color: #1A1D21;">Tech Engineer</div><div style="font-size: 11px; color: #6C757D;">Maintenance Team</div></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ============================================================
    # 2. PAGE TITLE & FILTERS (WORKING LOGIC)
    # ============================================================
    col_title, col_filter = st.columns([1, 1.5])
    with col_title:
        st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="margin: 0; color: #1A1D21; font-weight: 700;">Good Morning, Team</h2>
            <p style="margin: 5px 0 0 0; color: #6C757D; font-size: 13px;">Here's the current health status of your defence equipment.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_filter:
        c1, c2, c3 = st.columns(3)
        with c1: sel_eq = st.selectbox("Equipment", ["All Equipment", "Engine-1", "Engine-2", "Generator-1", "Generator-2", "Vehicle-1", "Vehicle-2"], label_visibility="collapsed")
        with c2: sel_loc = st.selectbox("Location", ["All Locations", "Hangar A", "Hangar B", "Base Yard", "Workshop"], label_visibility="collapsed")
        with c3: sel_time = st.selectbox("Time Range", ["Last 7 Days", "Last 24 Hours", "Last 30 Days"], label_visibility="collapsed")

    # Filter logic check
    filter_active = (sel_eq != "All Equipment") or (sel_loc != "All Locations") or (sel_time != "Last 7 Days")
    
    if filter_active:
        st.success(f"Filter Applied: {sel_eq} | {sel_loc} | {sel_time} (Demo data filtered)")
        total_eq, normal, warning, critical, unknown = 1, 1, 0, 0, 0
    else:
        total_eq, normal, warning, critical, unknown = 8, 5, 2, 1, 0

    # ============================================================
    # 3. KPI CARDS
    # ============================================================
    kpi_html = f"""
    <div style="display: flex; gap: 15px; margin-bottom: 20px;">
        <div class="kpi-card" style="flex: 1; border-left: 4px solid #0D6EFD;">
            <div style="background: #E7F1FF; color: #0D6EFD; border-radius: 50%; padding: 10px; margin-right: 15px; font-size: 20px;">🏢</div>
            <div><div style="color: #0D6EFD; font-size: 12px; font-weight: 600;">Total Equipment</div><div style="color: #1A1D21; font-size: 24px; font-weight: bold; line-height: 1;">{total_eq}</div><div style="color: #6C757D; font-size: 10px; margin-top: 4px;">Registered equipment units</div></div>
        </div>
        <div class="kpi-card" style="flex: 1; border-left: 4px solid #198754;">
            <div style="background: #D1E7DD; color: #198754; border-radius: 50%; padding: 10px; margin-right: 15px; font-size: 20px;">✅</div>
            <div><div style="color: #198754; font-size: 12px; font-weight: 600;">Normal</div><div style="color: #1A1D21; font-size: 24px; font-weight: bold; line-height: 1;">{normal}</div><div style="color: #6C757D; font-size: 10px; margin-top: 4px;">Equipment working fine</div></div>
        </div>
        <div class="kpi-card" style="flex: 1; border-left: 4px solid #FFC107;">
            <div style="background: #FFF3CD; color: #FFC107; border-radius: 50%; padding: 10px; margin-right: 15px; font-size: 20px;">⚠️</div>
            <div><div style="color: #FFC107; font-size: 12px; font-weight: 600;">Warning</div><div style="color: #1A1D21; font-size: 24px; font-weight: bold; line-height: 1;">{warning}</div><div style="color: #6C757D; font-size: 10px; margin-top: 4px;">Needs attention</div></div>
        </div>
        <div class="kpi-card" style="flex: 1; border-left: 4px solid #DC3545;">
            <div style="background: #F8D7DA; color: #DC3545; border-radius: 50%; padding: 10px; margin-right: 15px; font-size: 20px;">🚨</div>
            <div><div style="color: #DC3545; font-size: 12px; font-weight: 600;">Critical</div><div style="color: #1A1D21; font-size: 24px; font-weight: bold; line-height: 1;">{critical}</div><div style="color: #6C757D; font-size: 10px; margin-top: 4px;">Immediate action required</div></div>
        </div>
        <div class="kpi-card" style="flex: 1; border-left: 4px solid #6C757D;">
            <div style="background: #E2E3E5; color: #6C757D; border-radius: 50%; padding: 10px; margin-right: 15px; font-size: 20px;">❓</div>
            <div><div style="color: #6C757D; font-size: 12px; font-weight: 600;">Unknown</div><div style="color: #1A1D21; font-size: 24px; font-weight: bold; line-height: 1;">{unknown}</div><div style="color: #6C757D; font-size: 10px; margin-top: 4px;">Data unavailable</div></div>
        </div>
    </div>
    """
    st.markdown(kpi_html, unsafe_allow_html=True)

    # ============================================================
    # 4. CHARTS & RIGHT ALERTS
    # ============================================================
    col_left, col_right = st.columns([2.8, 1.2])

    with col_left:
        c1, c2 = st.columns(2)
        
        with c1:
            with st.container():
                st.markdown('<div class="chart-card">', unsafe_allow_html=True)
                st.markdown('<div style="font-size: 14px; font-weight: 600; margin-bottom: 15px;">📈 Equipment Health Trend</div>', unsafe_allow_html=True)
                
                fig_line = go.Figure()
                fig_line.add_trace(go.Scatter(x=["Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", "Apr 27", "Apr 28"], y=[50, 55, 60, 58, 62, 60, 65], mode='lines+markers', name='Engine-1', line=dict(color='#0D6EFD')))
                fig_line.add_trace(go.Scatter(x=["Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", "Apr 27", "Apr 28"], y=[55, 60, 65, 62, 68, 65, 70], mode='lines+markers', name='Engine-2', line=dict(color='#FFC107')))
                fig_line.add_trace(go.Scatter(x=["Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", "Apr 27", "Apr 28"], y=[65, 70, 75, 72, 78, 75, 80], mode='lines+markers', name='Generator-1', line=dict(color='#198754')))
                fig_line.add_trace(go.Scatter(x=["Apr 22", "Apr 23", "Apr 24", "Apr 25", "Apr 26", "Apr 27", "Apr 28"], y=[60, 65, 70, 68, 72, 70, 75], mode='lines+markers', name='Generator-2', line=dict(color='#6F42C1')))
                
                fig_line.update_layout(template="plotly_white", height=260, margin=dict(l=10, r=10, t=10, b=10), legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5, font=dict(size=10)), xaxis=dict(showgrid=True, gridcolor="#F1F3F5"), yaxis=dict(showgrid=True, gridcolor="#F1F3F5", range=[0, 100]))
                st.plotly_chart(fig_line, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

        with c2:
            with st.container():
                st.markdown('<div class="chart-card">', unsafe_allow_html=True)
                st.markdown('<div style="font-size: 14px; font-weight: 600; margin-bottom: 15px;">🛡️ Equipment Status</div>', unsafe_allow_html=True)
                
                fig_pie = go.Figure(data=[go.Pie(labels=["Normal", "Warning", "Critical", "Unknown"], values=[normal, warning, critical, unknown], hole=0.6, marker=dict(colors=["#198754", "#FFC107", "#DC3545", "#6C757D"]), textinfo='none')])
                fig_pie.add_annotation(text=f"{total_eq}<br><span style='font-size:12px;color:#6C757D'>Total</span>", x=0.5, y=0.5, font=dict(size=20, color="#1A1D21"), showarrow=False)
                fig_pie.update_layout(template="plotly_white", height=260, margin=dict(l=10, r=10, t=10, b=10), showlegend=True, legend=dict(orientation="v", yanchor="middle", y=0.5, xanchor="left", x=1.0, font=dict(size=11)))
                st.plotly_chart(fig_pie, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)

    with col_right:
        with st.container():
            st.markdown('<div class="chart-card" style="height: 100%;">', unsafe_allow_html=True)
            st.markdown("""
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                <div style="font-size: 14px; font-weight: 600;">🔔 Recent Alerts</div>
                <div style="color: #0D6EFD; font-size: 11px; cursor: pointer;">View All</div>
            </div>
            <div class="alert-item" style="background: #FFF5F5;"><div><span class="badge badge-critical" style="margin-bottom: 5px;">Critical</span><div style="font-weight: 600; font-size: 12px; margin-top: 5px;">Generator-1</div><div style="font-size: 11px; color: #6C757D;">Oil Quality below normal</div><div style="font-size: 10px; color: #ADB5BD; margin-top: 2px;">Apr 28, 09:15</div></div><div style="color: #6C757D;">›</div></div>
            <div class="alert-item" style="background: #FFF9E6;"><div><span class="badge badge-warning" style="margin-bottom: 5px;">Warning</span><div style="font-weight: 600; font-size: 12px; margin-top: 5px;">Engine-2</div><div style="font-size: 11px; color: #6C757D;">Vibration level increasing</div><div style="font-size: 10px; color: #ADB5BD; margin-top: 2px;">Apr 28, 10:24</div></div><div style="color: #6C757D;">›</div></div>
            <div class="alert-item" style="background: #FFF9E6;"><div><span class="badge badge-warning" style="margin-bottom: 5px;">Warning</span><div style="font-weight: 600; font-size: 12px; margin-top: 5px;">Engine-1</div><div style="font-size: 11px; color: #6C757D;">Temperature above threshold</div><div style="font-size: 10px; color: #ADB5BD; margin-top: 2px;">Apr 28, 10:20</div></div><div style="color: #6C757D;">›</div></div>
            <div class="alert-item" style="background: #F0FDF4;"><div><span class="badge badge-normal" style="margin-bottom: 5px;">Normal</span><div style="font-weight: 600; font-size: 12px; margin-top: 5px;">Generator-2</div><div style="font-size: 11px; color: #6C757D;">All parameters normal</div><div style="font-size: 10px; color: #ADB5BD; margin-top: 2px;">Apr 28, 09:10</div></div><div style="color: #6C757D;">›</div></div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ============================================================
    # 5. BOTTOM ROW (Live Data, Equipment, Health Overview)
    # ============================================================
    col_b1, col_b2, col_b3 = st.columns([1, 1, 1])

    with col_b1:
        with st.container():
            st.markdown('<div class="chart-card">', unsafe_allow_html=True)
            st.markdown("""
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                <div style="font-size: 14px; font-weight: 600;">📊 Live Sensor Data</div>
                <div style="color: #0D6EFD; font-size: 11px; cursor: pointer;">View All</div>
            </div>
            <table class="custom-table">
                <tr><th>Parameter</th><th>Value</th><th>Status</th></tr>
                <tr><td>📳 Vibration</td><td>2.4 mm/s</td><td><span class="badge badge-normal">Normal</span></td></tr>
                <tr><td>🌡️ Temperature</td><td>72 °C</td><td><span class="badge badge-normal">Normal</span></td></tr>
                <tr><td>🛢️ Oil Quality</td><td>Good</td><td><span class="badge badge-normal">Normal</span></td></tr>
                <tr><td>☁️ Pressure</td><td>4.2 bar</td><td><span class="badge badge-normal">Normal</span></td></tr>
                <tr><td>⚡ Current</td><td>12.5 A</td><td><span class="badge badge-normal">Normal</span></td></tr>
                <tr><td>🔄 RPM</td><td>1800</td><td><span class="badge badge-normal">Normal</span></td></tr>
            </table>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    with col_b2:
        with st.container():
            st.markdown('<div class="chart-card">', unsafe_allow_html=True)
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                <div style="font-size: 14px; font-weight: 600;">⚙️ Equipment List</div>
                <div style="color: #0D6EFD; font-size: 11px; cursor: pointer;">View All</div>
            </div>
            <table class="custom-table">
                <tr><th>Equipment</th><th>Location</th><th>Status</th><th></th></tr>
                <tr><td><div style="display:flex; align-items:center; gap:8px;"><img src="data:image/jpeg;base64,{img_eq1}" class="eq-img"> Engine-1</div></td><td>Hangar A</td><td><span class="badge badge-normal">Normal</span></td><td style="color:#6C757D;">›</td></tr>
                <tr><td><div style="display:flex; align-items:center; gap:8px;"><img src="data:image/jpeg;base64,{img_eq2}" class="eq-img"> Engine-2</div></td><td>Hangar B</td><td><span class="badge badge-warning">Warning</span></td><td style="color:#6C757D;">›</td></tr>
                <tr><td><div style="display:flex; align-items:center; gap:8px;"><img src="data:image/jpeg;base64,{img_gen1}" class="eq-img"> Generator-1</div></td><td>Base Yard</td><td><span class="badge badge-critical">Critical</span></td><td style="color:#6C757D;">›</td></tr>
                <tr><td><div style="display:flex; align-items:center; gap:8px;"><img src="data:image/jpeg;base64,{img_gen2}" class="eq-img"> Generator-2</div></td><td>Hangar A</td><td><span class="badge badge-normal">Normal</span></td><td style="color:#6C757D;">›</td></tr>
                <tr><td><div style="display:flex; align-items:center; gap:8px;"><img src="data:image/jpeg;base64,{img_veh1}" class="eq-img"> Vehicle-1</div></td><td>Workshop</td><td><span class="badge badge-normal">Normal</span></td><td style="color:#6C757D;">›</td></tr>
                <tr><td><div style="display:flex; align-items:center; gap:8px;"><img src="data:image/jpeg;base64,{img_veh2}" class="eq-img"> Vehicle-2</div></td><td>Workshop</td><td><span class="badge badge-normal">Normal</span></td><td style="color:#6C757D;">›</td></tr>
            </table>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    with col_b3:
        with st.container():
            st.markdown('<div class="chart-card">', unsafe_allow_html=True)
            st.markdown(f"""
            <div style="font-size: 16px; font-weight: 600; margin-bottom: 15px;">📊 Equipment Health Overview</div>
            
            <div style="width: 100%; height: 160px; border-radius: 8px; overflow: hidden; margin-bottom: 15px; border: 1px solid #DEE2E6;">
                <img src="data:image/jpeg;base64,{img_tank}" style="width: 100%; height: 100%; object-fit: cover;" alt="Tank Equipment">
            </div>
            
            <div style="font-weight: 700; font-size: 15px; color: #1A1D21;">Keep your equipment running</div>
            <div style="font-size: 13px; color: #6C757D; margin: 5px 0 15px 0;">Monitor. Detect. Maintain.</div>
            
            <div style="background: #E7F1FF; border-radius: 8px; padding: 12px; display: flex; gap: 10px; align-items: start; border: 1px solid #B6D4FE;">
                <span style="font-size: 20px;">💡</span>
                <div style="font-size: 12px; color: #084298; line-height: 1.5; font-weight: 500;">
                    Real-time sensor data helps identify potential issues before they become major problems.
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)