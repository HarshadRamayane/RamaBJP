"""
RamaBJP Session Management
Handles user sessions in Streamlit.
"""

import streamlit as st
from datetime import datetime, timedelta
from security.auth import authenticate, get_user, has_permission


# Session timeout in minutes
SESSION_TIMEOUT_MINUTES = 30


def init_session():
    """Initialize session state."""
    if "user" not in st.session_state:
        st.session_state.user = None
    if "login_time" not in st.session_state:
        st.session_state.login_time = None
    if "failed_attempts" not in st.session_state:
        st.session_state.failed_attempts = 0


def login_user(username, password):
    """Attempt to log in a user."""
    user, message = authenticate(username, password)
    
    if user:
        st.session_state.user = user
        st.session_state.login_time = datetime.now()
        st.session_state.failed_attempts = 0
        return True, "Login successful"
    else:
        st.session_state.failed_attempts += 1
        return False, message


def logout_user():
    """Log out the current user."""
    st.session_state.user = None
    st.session_state.login_time = None


def is_logged_in():
    """Check if a user is logged in."""
    if st.session_state.get("user") is None:
        return False
    
    # Check session timeout
    login_time = st.session_state.get("login_time")
    if login_time:
        elapsed = (datetime.now() - login_time).total_seconds() / 60
        if elapsed > SESSION_TIMEOUT_MINUTES:
            logout_user()
            return False
    
    return True


def current_user():
    """Get current logged-in user."""
    return st.session_state.get("user")


def require_login():
    """Require login to access the app. Returns True if logged in."""
    if not is_logged_in():
        render_login_page()
        return False
    return True


def require_role(required_role):
    """Require a specific role to perform an action."""
    user = current_user()
    if not user:
        st.error("❌ You must be logged in.")
        return False
    
    if not has_permission(user, required_role):
        st.error(f"❌ You need **{required_role}** permission to do this.")
        return False
    
    return True


def render_login_page():
    """Render the login page."""
    st.markdown("""
    <div style="
        max-width: 400px;
        margin: 80px auto;
        padding: 30px;
        background-color: #F8F9FA;
        border: 1px solid #DEE2E6;
        border-radius: 12px;
    ">
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="font-size: 48px;">🛡️</div>
            <h2 style="color: #0D6EFD; margin: 10px 0 5px 0;">RamaBJP</h2>
            <p style="color: #6C757D; font-size: 13px;">Predictive Maintenance for Defence Equipment</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### 🔐 Login")
        
        with st.form("login_form"):
            username = st.text_input("Username", placeholder="admin")
            password = st.text_input("Password", type="password", placeholder="••••••••")
            
            submitted = st.form_submit_button("🔓 Login", use_container_width=True)
            
            if submitted:
                if not username or not password:
                    st.error("❌ Please enter username and password.")
                else:
                    success, message = login_user(username, password)
                    if success:
                        st.success("✅ Login successful!")
                        st.rerun()
                    else:
                        st.error(f"❌ {message}")
        
        st.markdown("---")
        
        st.markdown("""
        <div style="
            background-color: #FFF3CD;
            border: 1px solid #FFECB5;
            border-radius: 8px;
            padding: 12px;
            font-size: 11px;
            color: #664D03;
        ">
            <b>🔑 Demo Credentials</b><br>
            <b>Admin:</b> admin / admin123<br>
            <b>Engineer:</b> engineer / engineer123<br>
            <b>Viewer:</b> viewer / viewer123
        </div>
        """, unsafe_allow_html=True)