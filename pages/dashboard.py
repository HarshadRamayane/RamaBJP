import streamlit as st
import plotly.graph_objects as go
import numpy as np

def render_dashboard():
    # Initialize session state for 3D view
    if "show_3d" not in st.session_state:
        st.session_state.show_3d = False

    # ============================================================
    # CSS
    # ============================================================
    st.markdown("""
    <style>
        .stApp {
            background: radial-gradient(circle at top left, rgba(255, 153, 51, 0.08), transparent 40%),
                        radial-gradient(circle at bottom right, rgba(19, 136, 8, 0.08), transparent 40%),
                        #0A1929 !important;
        }
        h1, h2, h3, h4, p, span, div { color: #FFFFFF; }
        .top-nav {
            display: flex; justify-content: space-between; align-items: center;
            background-color: rgba(13, 27, 42, 0.8); padding: 10px 20px;
            border-radius: 8px; border: 1px solid #1E3A5F; margin-bottom: 20px;
        }
        .nav-links span { color: #8892B0; margin-right: 20px; font-size: 13px; }
        .nav-links span.active { color: #64FFDA; background-color: #112240; padding: 4px 10px; border-radius: 4px; }
        .metric-card { background-color: rgba(17, 34, 64, 0.9); padding: 15px; border-radius: 8px; border: 1px solid #1E3A5F; margin-bottom: 15px; }
        .alert-card { background-color: rgba(45, 27, 27, 0.9); border-left: 5px solid #FF1744; padding: 15px; border-radius: 8px; margin-bottom: 15px; }
        .log-item { background-color: rgba(17, 34, 64, 0.9); padding: 10px; border-left: 3px solid; border-radius: 4px; margin-bottom: 8px; font-size: 12px; }
        .3d-view-box {
            background: linear-gradient(135deg, rgba(17,34,64,1) 0%, rgba(10,25,41,1) 100%);
            padding: 15px; border-radius: 8px; border: 1px solid #1E3A5F; 
            height: 200px; position: relative; cursor: pointer;
        }
        .3d-view-box:hover { border: 1px solid #64FFDA; }
    </style>
    """, unsafe_allow_html=True)

    # ============================================================
    # 1. TOP NAV BAR
    # ============================================================
    st.markdown("""
    <div class="top-nav">
        <div style="color: #64FFDA; font-weight: bold; font-size: 16px;">
            ⚙️ PREDICTIVE MAINTENANCE DASHBOARD // DEFENCE MRO
        </div>
        <div class="nav-links">
            <span class="active">DASHBOARD</span>
            <span>ASSET VIEW</span>
            <span>ALERTS</span>
            <span>ANALYTICS</span>
            <span>SETTINGS</span>
            <span style="color: #FFFFFF;">👤 ENGINEER_JONES ▼</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ============================================================
    # 2. MAIN LAYOUT
    # ============================================================
    col_left, col_right = st.columns([2.5, 1])

    with col_left:
        st.markdown('<div style="display: flex; justify-content: space-between; margin-bottom: 10px;"><span style="color: #FFFFFF; font-weight: bold; font-size: 14px;">VIBRATION LEVEL (mm/s) // MACHINE ID: TANK_ENGINE_T90</span><span style="color: #64FFDA; font-size: 12px;">DEFENCE MRO 🟢🟡🔴</span></div>', unsafe_allow_html=True)

        x = list(range(30))
        y = [2.0, 2.1, 2.0, 2.2, 2.1, 2.3, 2.2, 2.5, 2.8, 3.0,
             3.2, 3.5, 3.8, 4.0, 4.2, 4.5, 4.8, 5.0, 5.2, 5.5,
             5.8, 6.0, 6.2, 6.5, 6.8, 7.0, 7.1, 7.2, 7.3, 7.2]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='#FF1744', width=3), fill='tozeroy', fillcolor='rgba(255, 23, 68, 0.1)'))
        fig.add_hline(y=6.0, line_dash="dash", line_color="#FFD600")
        fig.add_hline(y=4.0, line_dash="dash", line_color="#FF1744")
        fig.add_trace(go.Scatter(x=[29], y=[7.2], mode='markers+text', marker=dict(size=12, color='#FF1744', line=dict(color='white', width=2)), text=['CURRENT: 7.2 mm/s ⚠️'], textposition='top left', textfont=dict(color='#FFFFFF', size=11)))

        fig.update_layout(
            template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(10, 25, 41, 0.5)",
            height=350, margin=dict(l=20, r=20, t=10, b=20),
            xaxis=dict(title=dict(text="TIME", font=dict(color="#8892B0")), tickvals=[0, 5, 10, 15, 20, 25, 29], ticktext=["08:00", "10:00", "12:00", "14:00", "16:00", "17:00", "NOW"], gridcolor="#1E3A5F"),
            yaxis=dict(title=dict(text="LEVEL (mm/s)", font=dict(color="#8892B0")), range=[0, 10], gridcolor="#1E3A5F"),
            showlegend=False
        )
        st.plotly_chart(fig, width='stretch')

    with col_right:
        st.markdown('<div style="color: #FFFFFF; font-weight: bold; font-size: 14px; margin-bottom: 10px;">STATUS OVERVIEW</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="alert-card">
            <div style="color: #FF1744; font-weight: bold; font-size: 13px;">⚠️ CRITICAL ALERT:<br>VIBRATION ANOMALY DETECTED</div>
            <div style="color: #FFCDD2; font-size: 11px; margin-top: 8px;">Machine: <b>TANK_ENGINE_T90</b><br>Severity: <b style="color: white;">HIGH</b><br>Time: 16:05:32</div>
        </div>
        <div class="metric-card">
            <div style="color: #FF9800; font-size: 11px;">🌡️ TEMPERATURE</div>
            <div style="color: #FFFFFF; font-size: 20px; font-weight: bold;">85°C</div>
            <div style="background: #1E3A5F; height: 6px; border-radius: 3px; margin-top: 8px;"><div style="background: #FF9800; width: 85%; height: 6px; border-radius: 3px;"></div></div>
        </div>
        <div class="metric-card">
            <div style="color: #FF1744; font-size: 11px;">📳 VIBRATION</div>
            <div style="color: #FFFFFF; font-size: 20px; font-weight: bold;">7.2 mm/s</div>
            <div style="background: #1E3A5F; height: 6px; border-radius: 3px; margin-top: 8px;"><div style="background: #FF1744; width: 92%; height: 6px; border-radius: 3px;"></div></div>
        </div>
        <div class="metric-card">
            <div style="color: #FF9800; font-size: 11px;">⏱️ RUL (REMAINING USEFUL LIFE)</div>
            <div style="color: #FFFFFF; font-size: 20px; font-weight: bold;">48 Hours</div>
            <div style="background: #1E3A5F; height: 6px; border-radius: 3px; margin-top: 8px;"><div style="background: #FF1744; width: 40%; height: 6px; border-radius: 3px;"></div></div>
        </div>
        """, unsafe_allow_html=True)

    # ============================================================
    # 3. BOTTOM LAYOUT
    # ============================================================
    st.markdown("<hr style='border: 1px solid #1E3A5F; margin: 10px 0;'>", unsafe_allow_html=True)
    
    col_bottom_left, col_bottom_right = st.columns([1.2, 2])

    # --- BOTTOM LEFT: 3D CARD ---
    with col_bottom_left:
        st.markdown('<div style="color: #FFFFFF; font-weight: bold; font-size: 14px; margin-bottom: 10px;">DEFENCE COMPONENT (3D)</div>', unsafe_allow_html=True)
        
        if st.button("🖱️ Open 3D Component Viewer", use_container_width=True):
            st.session_state.show_3d = not st.session_state.show_3d

        st.markdown("""
        <div class="3d-view-box">
            <svg width="100%" height="100%" viewBox="0 0 300 150">
                <!-- 3D-ish Tank Engine representation -->
                <rect x="50" y="50" width="100" height="60" fill="#4A5568" rx="10" stroke="#64FFDA" stroke-width="2"/>
                <rect x="160" y="60" width="40" height="40" fill="#2D3748" rx="5"/>
                <circle cx="100" cy="80" r="15" fill="#1A202C" stroke="#FF1744" stroke-width="2"/>
                <text x="100" y="85" text-anchor="middle" fill="#64FFDA" font-size="10">ENGINE</text>
                <text x="70" y="40" fill="#FFFFFF" font-size="10">T-90 Engine Assembly</text>
                <!-- Anomaly marker -->
                <circle cx="130" cy="70" r="4" fill="#FF1744"/>
                <line x1="130" y1="70" x2="160" y2="40" stroke="#FF1744" stroke-width="1" stroke-dasharray="2"/>
                <text x="165" y="45" fill="#FF1744" font-size="9">Anomaly</text>
            </svg>
        </div>
        """, unsafe_allow_html=True)

    # --- BOTTOM RIGHT: ALERTS ---
    with col_bottom_right:
        st.markdown('<div style="color: #FFFFFF; font-weight: bold; font-size: 14px; margin-bottom: 10px;">RECENT ALERTS & MAINTENANCE LOGS</div>', unsafe_allow_html=True)

        logs = [
            ("16:05", "CRITICAL", "Tank_Engine_T90 - Vibration > 7mm/s", "#FF1744"),
            ("15:45", "WARNING", "Tank_Engine_T90 - Temp Rise", "#FFD600"),
            ("14:30", "OK", "Radar_Module - Routine Check", "#00C853"),
            ("12:00", "INFO", "System Check Complete", "#64FFDA")
        ]

        for time, status, msg, color in logs:
            st.markdown(f"""
            <div class="log-item" style="border-left-color: {color};">
                <span style="color: #8892B0;">{time}</span>
                <span style="color: {color}; font-weight: bold; margin: 0 10px;">{status}</span>
                <span style="color: #FFFFFF;">{msg}</span>
            </div>
            """, unsafe_allow_html=True)

    # ============================================================
    # 4. 3D INTERACTIVE MODAL (Defence Component)
    # ============================================================
    if st.session_state.show_3d:
        with st.expander("🔍 3D Defence Component Viewer (Interactive)", expanded=True):
            st.markdown("### 🛠️ Tank Engine Assembly (T-90) - 3D View")
            st.info("Mouse se drag karke 360° rotate karo aur scroll se zoom karo. Red marker anomaly point ko darsha raha hai.")
            
            # Create a 3D representation of a Tank Engine (gearbox shape)
            # Base cylinder (Engine Block)
            theta = np.linspace(0, 2*np.pi, 50)
            z = np.linspace(0, 6, 30)
            theta, z = np.meshgrid(theta, z)
            x = np.cos(theta) * 2.5
            y = np.sin(theta) * 1.5

            fig_3d = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Greys', showscale=False, opacity=0.9)])
            
            # Add a secondary block (Gearbox)
            x2 = np.cos(theta) * 1.5
            y2 = np.sin(theta) * 1.5
            z2 = z + 6
            fig_3d.add_trace(go.Surface(z=z2, x=x2, y=y2, colorscale='Blues', showscale=False, opacity=0.9))

            # Add Anomaly Marker (Red Hotspot)
            fig_3d.add_trace(go.Scatter3d(
                x=[2.5], y=[0], z=[3],
                mode='markers+text',
                marker=dict(size=12, color='red', symbol='x'),
                text=["Anomaly (Vibration)"],
                textposition="top center",
                textfont=dict(color="red", size=12)
            ))

            fig_3d.update_layout(
                template="plotly_dark",
                scene=dict(
                    xaxis_title='X Axis',
                    yaxis_title='Y Axis',
                    zaxis_title='Z Axis',
                    bgcolor="rgba(10, 25, 41, 0.95)",
                    camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
                ),
                margin=dict(l=0, r=0, b=0, t=0),
                height=500
            )
            
            st.plotly_chart(fig_3d, width='stretch')
            
            if st.button("❌ Close 3D Viewer"):
                st.session_state.show_3d = False
                st.rerun()