import streamlit as st
import urllib.parse

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="AI Solutions Showcase",
    layout="wide"
)

# -------------------------------------------------
# CSS STYLING
# -------------------------------------------------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #FF9933, #001F54);
    color: white;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #FF9933, #001F54);
    padding-top: 2rem;
    width: 280px !important;
}

h1, h2, h3 {
    color: #FFD700;
}

.stButton > button {
    width: 100% !important;
    min-width: 240px !important;
    max-width: 240px !important;
    height: 42px !important;
    background-color: #FFD700;
    color: #001F54;
    border-radius: 10px;
    font-weight: 600;
    font-size: 15px;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    margin-bottom: 14px;
}

.stButton > button:hover {
    background-color: #FFA500;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.title("🚀 PLC + SCADA + IoT + Industry 4.0 + AI")

# -------------------------------------------------
# FILE PATHS
# -------------------------------------------------
BASE = "https://raw.githubusercontent.com/Harjeetsinghengg/Projects/main"

VIDEO_1 = f"{BASE}/protocol.mp4"
VIDEO_2 = f"{BASE}/OPC.mp4"
VIDEO_3 = f"{BASE}/Template%20Matching.mp4"
VIDEO_4 = f"{BASE}/AI Development Cycle.mp4"
VIDEO_5 = f"{BASE}/AI H2 Project.mp4"
VIDEO_6 = f"{BASE}/video6.mp4"
PDF_1   = f"{BASE}/Documents/Dashboard.pdf"
PDF_2   = f"{BASE}/Documents/Flask App.pdf"

# -------------------------------------------------
# HELPERS
# -------------------------------------------------
def play_video(url, height=260):
    st.markdown(f"""
    <video width="100%" height="{height}" autoplay loop muted controls>
        <source src="{url}" type="video/mp4">
    </video>
    """, unsafe_allow_html=True)


def show_pdf(url, height=900):
    encoded_url = urllib.parse.quote(url, safe="")
    viewer = f"https://docs.google.com/gview?url={encoded_url}&embedded=true"

    st.markdown(
        f"""
        <iframe 
            src="{viewer}" 
            width="100%" 
            height="{height}" 
            style="border:none;">
        </iframe>
        """,
        unsafe_allow_html=True
    )

# -------------------------------------------------
# VIDEO GRID
# -------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Protocols")
    play_video(VIDEO_1)

with col2:
    st.subheader("OPC Integration")
    play_video(VIDEO_2)

with col3:
    st.subheader("Vision System")
    play_video(VIDEO_3)

st.markdown("---")

col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("Smart Factory AI")
    play_video(VIDEO_4)

with col5:
    st.subheader("Digital Twins")
    play_video(VIDEO_5)

with col6:
    st.subheader("Quality Control")
    play_video(VIDEO_6)

st.markdown("---")

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.title("AI Projects")

projects = {
    "Flask Application": ("pdf", PDF_2),
    "PLC + OPC Integration": ("video", VIDEO_2),
    "Industrial Vision": ("video", VIDEO_3),
    "Dashboard Grafana": ("pdf", PDF_1),
    "Smart Factory AI / ML": ("video", VIDEO_4),
    "Predictive Maintenance": ("video", VIDEO_5),
    "Quality Control": ("video", VIDEO_6),
}

if "selected_project" not in st.session_state:
    st.session_state.selected_project = list(projects.keys())[0]

for name in projects:
    if st.sidebar.button(name):
        st.session_state.selected_project = name

# -------------------------------------------------
# MAIN CONTENT
# -------------------------------------------------
proj_name = st.session_state.selected_project
proj_type, proj_src = projects[proj_name]

st.subheader(proj_name)

if proj_type == "video":
    play_video(proj_src, height=420)
else:
    show_pdf(proj_src)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown("""
### Project Overview
This section showcases the different projects I have been working on.

### My Technical Values
- **Continuous Learning**
- **Innovation & Creativity**
- **Quality & Reliability**
- **Problem Solving**
- **Automation & Efficiency**
- **Collaboration & Growth**

harjeetsinghengg@gmail.com
""")
