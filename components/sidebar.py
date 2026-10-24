import streamlit as st
from security.session import current_user

def render_sidebar():
    # ============================================================
    # SIDEBAR CSS (Hide default nav, Add Background, Big Text)
    # ============================================================
    st.markdown("""
    <style>
        /* 1. Hide Default Streamlit Navigation */
        [data-testid="stSidebarNav"] {
            display: none !important;
        }
        
        /* 2. Sidebar Background & Tank Image */
        section[data-testid="stSidebar"] {
            background-color: #0B132B !important;
            background-image: 
                linear-gradient(rgba(11, 19, 43, 0.9), rgba(11, 19, 43, 0.95)), 
                url('https://images.unsplash.com/photo-1579912268200-5e4b4d9c5c1e?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80');
            background-size: cover;
            background-position: center bottom;
            border-right: 1px solid #1C2A4A;
        }

        /* 3. Hide the default radio circles */
        section[data-testid="stSidebar"] div[role="radiogroup"] > label > div:first-child {
            display: none !important;
        }
        
        /* 4. Style the menu items */
        section[data-testid="stSidebar"] div[role="radiogroup"] > label {
            padding: 12px 15px;
            margin-bottom: 4px;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.2s;
        }
        
        /* 5. Text size badi aur white color */
        section[data-testid="stSidebar"] div[role="radiogroup"] > label p {
            color: #E2E8F0 !important;  /* Light white */
            font-size: 15px !important; /* Bada text */
            font-weight: 500 !important;
            font-family: 'Inter', sans-serif;
        }

        /* 6. Hover effect */
        section[data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
            background-color: rgba(255, 255, 255, 0.08);
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] > label:hover p {
            color: #FFFFFF !important;
        }
        
        /* 7. Selected item (Blue background + White bold text) */
        section[data-testid="stSidebar"] div[role="radiogroup"] > label[data-checked="true"] {
            background-color: #1D4ED8 !important; /* Royal Blue */
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] > label[data-checked="true"] p {
            color: #FFFFFF !important;
            font-weight: 600 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        # --- Logo ---
        st.markdown("""
        <div style="padding: 20px 10px; display: flex; align-items: center; gap: 10px;">
            <div style="background: white; padding: 6px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
                <span style="font-size: 24px;">🛡️</span>
            </div>
            <div>
                <div style="color: #FFFFFF; font-weight: 800; font-size: 22px; letter-spacing: 0.5px;">RAMEDOX</div>
                <div style="color: #A0ABC0; font-size: 12px;">Defence</div>
            </div>
        </div>
        <hr style="border-color: #1C2A4A; margin: 0 10px 15px 10px;">
        """, unsafe_allow_html=True)
        
        # --- Navigation (Clean List) ---
        page = st.radio(
            "Navigation",
            [
                "🏠 Dashboard",
                "🚜 Equipment Management",
                "📡 Sensor Monitoring",
                "📥 Data Import & Ingestion",
                "⚙️ Rules & Analysis",
                "🔔 Alerts & Notifications",
                "🛠️ Maintenance Management",
                "📈 Analytics & Trends",
                "📄 Reports",
                "⚙️ Settings"
            ],
            label_visibility="collapsed"
        )
        
        # --- Bottom User Card ---
        st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
        
        user = current_user()
        if user:
            st.markdown(f"""
            <div style="background: rgba(255, 255, 255, 0.05); border: 1px solid #1C2A4A; border-radius: 10px; padding: 15px; margin: 10px;">
                <div style="display: flex; align-items: center; gap: 10px;">
                    <span style="font-size: 20px;">🛡️</span>
                    <div>
                        <div style="color: #FFFFFF; font-size: 13px; font-weight: bold;">RAMEDOX Defence</div>
                        <div style="color: #A0ABC0; font-size: 10px;">Software Proof of Concept</div>
                    </div>
                </div>
                <div style="color: #6B7A99; font-size: 10px; margin-top: 10px;">v1.0.0</div>
            </div>
            """, unsafe_allow_html=True)
    
    return page