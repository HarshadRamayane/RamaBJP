"""
RamaBJP Theme Configuration
Defines the white/light theme colors and CSS.
"""

# ============================================================
# COLOR PALETTE (White/Light Theme)
# ============================================================

COLORS = {
    "background": "#FFFFFF",
    "surface": "#F8F9FA",
    "surface_alt": "#F1F3F5",
    "border": "#DEE2E6",
    "text_primary": "#1A1D21",
    "text_secondary": "#495057",
    "text_muted": "#6C757D",
    "primary": "#0D6EFD",
    "primary_hover": "#0B5ED7",
    "success": "#198754",
    "warning": "#FFC107",
    "danger": "#DC3545",
    "info": "#0DCAF0",
    "normal": "#198754",
    "warning_status": "#FFC107",
    "critical": "#DC3545",
    "unknown": "#6C757D",
}


# ============================================================
# CUSTOM CSS
# ============================================================

def get_custom_css():
    """Return custom CSS for the white theme."""
    return """
    <style>
        /* Main app background */
        .stApp {
            background-color: #FFFFFF;
        }
        
        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #F8F9FA;
            border-right: 1px solid #DEE2E6;
        }
        
        /* Headings */
        h1, h2, h3, h4, h5, h6 {
            color: #1A1D21 !important;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        /* Body text */
        p, li, span, div {
            color: #495057;
        }
        
        /* Metric cards */
        div[data-testid="stMetric"] {
            background-color: #F8F9FA;
            border: 1px solid #DEE2E6;
            border-radius: 8px;
            padding: 15px;
        }
        
        div[data-testid="stMetric"] > label {
            color: #6C757D !important;
            font-size: 12px !important;
        }
        
        div[data-testid="stMetric"] > div {
            color: #1A1D21 !important;
        }
        
        /* Buttons */
        .stButton > button {
            background-color: #0D6EFD;
            color: #FFFFFF;
            border: none;
            border-radius: 6px;
            padding: 8px 16px;
            font-weight: 500;
        }
        
        .stButton > button:hover {
            background-color: #0B5ED7;
        }
        
        /* DataFrames */
        div[data-testid="stDataFrame"] {
            border: 1px solid #DEE2E6;
            border-radius: 8px;
        }
        
        /* Alerts */
        div[data-testid="stAlert"] {
            border-radius: 8px;
        }
        
        /* Expander */
        div[data-testid="stExpander"] {
            border: 1px solid #DEE2E6;
            border-radius: 8px;
        }
        
        /* Selectbox / Input */
        .stSelectbox > div > div {
            border-radius: 6px;
        }
        
        .stTextInput > div > div > input {
            border-radius: 6px;
        }
        
        /* Hide default Streamlit navigation */
        [data-testid="stSidebarNav"] {
            display: none !important;
        }
    </style>
    """


# ============================================================
# STATUS BADGE HELPER
# ============================================================

def get_status_color(status):
    """Get color for a status."""
    mapping = {
        "Normal": COLORS["normal"],
        "Warning": COLORS["warning_status"],
        "Critical": COLORS["critical"],
        "Unknown": COLORS["unknown"],
        "Open": COLORS["info"],
        "In Progress": COLORS["warning"],
        "Completed": COLORS["success"],
        "ACKNOWLEDGED": COLORS["info"],
        "RESOLVED": COLORS["success"],
        "OPEN": COLORS["danger"],
    }
    return mapping.get(status, COLORS["unknown"])


def get_status_badge(status):
    """Get HTML for a status badge."""
    color = get_status_color(status)
    return f"""
    <span style="
        background-color: {color}20;
        color: {color};
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
        border: 1px solid {color}40;
    ">{status}</span>
    """