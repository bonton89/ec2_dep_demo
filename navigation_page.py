import streamlit as st

import streamlit as st

# Example credentials (for demonstration only)
USERNAME = "demo_user"
PASSWORD = "June2025"

def login_form():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login = st.button("Login")
    if login:
        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success(f"Welcome, demo_user!")
            st.rerun()# Reload to show main page
        else:
            st.error("Invalid username or password")
    return

# Initialize login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_form()
    st.stop()  # Prevents rest of the navigation page from loading if not logged in

# ---- Main Navigation Content (after login) ----
# Set page configuration

st.set_page_config(
    page_title="AWS Bedrock Demo",
    page_icon="📊",
    layout="wide",
)

# --- PAGE SETUP ---
info_page = st.Page(
    "home.py",
    title="🏠 Home Page",
    icon=":material/account_circle:",
    default=True,

)


project_2_page = st.Page(
    "fixed_income_page.py",
    title="Fixed Income - Quarter Back",
    icon=":material/search:",
    )

project_1_page = st.Page(
    "plan_audit_page.py",
    title="Plan Audit Demo",
    icon=":material/smart_toy:",
)


# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info":[info_page],
        "Use Case": [project_1_page, project_2_page],
       
    }
)

# --- SHARED ON ALL PAGES ---
st.sidebar.markdown("  © infosys bpm  ")
# --- Logout Button in the Sidebar ---
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()  # Use st.experimental_rerun() if Streamlit < 1.32

# --- RUN NAVIGATION ---
pg.run()

# Add your navigation links or page logic below






