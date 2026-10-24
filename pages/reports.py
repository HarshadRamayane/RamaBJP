import streamlit as st
from pages import reports # Naya import

# ... aapka baaki code ...

# Sidebar menu mein option add karein
menu = st.sidebar.selectbox("Menu", ["Dashboard Overview", "Analytics", "Reports", "Equipment"])

if menu == "Reports":
    reports.render_reports() # Naya page call karein
elif menu == "Analytics":
    from pages import analytics
    analytics.render_analytics()
# ... baaki pages ...