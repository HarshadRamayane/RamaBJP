import streamlit as st

def render_top_header():
    # Yahan hum login session se user ka naam aur role utha rahe hain
    # Agar login system abhi nahi hai, toh default "Tech Engineer" dikhega
    user_name = st.session_state.get("username", "Tech Engineer")
    user_role = st.session_state.get("role", "Maintenance Team")
    
    # Initials nikalne ke liye (e.g., Tech Engineer -> TE)
    initials = "".join([word[0] for word in user_name.split()[:2]]).upper()
    if not initials:
        initials = "TE"

    st.markdown(f"""
    <div style="
        display: flex; justify-content: space-between; align-items: center;
        background-color: #FFFFFF; padding: 10px 20px; border-radius: 8px;
        border: 1px solid #DEE2E6; margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.02);
    ">
        <!-- Left Side: Logo & Title -->
        <div style="display: flex; align-items: center; gap: 15px;">
            <span style="font-size: 20px;">🛡️</span>
            <div style="color: #1A1D21; font-weight: 700; font-size: 16px;">
                RAMEDOX 
                <span style="font-weight: normal; font-size: 13px; margin-left: 10px; color: #6C757D;">
                    Predictive Maintenance for Defence Equipment
                </span>
            </div>
        </div>

        <!-- Right Side: System Online, Notification, User Profile -->
        <div style="display: flex; align-items: center; gap: 20px; font-size: 13px;">
            <span style="color: #198754; display: flex; align-items: center; gap: 6px; font-weight: 600;">
                <span style="height: 8px; width: 8px; background-color: #198754; border-radius: 50%; display: inline-block;"></span>
                System Online
            </span>
            
            <span style="position: relative; cursor: pointer; font-size: 16px;">
                🔔 
                <span style="position: absolute; top: -5px; right: -8px; background: #DC3545; color: white; border-radius: 50%; padding: 2px 6px; font-size: 9px; font-weight: bold;">
                    3
                </span>
            </span>
            
            <div style="display: flex; align-items: center; gap: 10px; background: #F8F9FA; padding: 4px 12px 4px 4px; border-radius: 20px; border: 1px solid #DEE2E6;">
                <div style="background: #E7F1FF; color: #0D6EFD; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 12px;">
                    {initials}
                </div>
                <div style="line-height: 1.2;">
                    <div style="font-weight: 600; color: #1A1D21;">{user_name}</div>
                    <div style="font-size: 10px; color: #6C757D;">{user_role} ▼</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)