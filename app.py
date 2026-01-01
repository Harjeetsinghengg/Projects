import streamlit as st

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

/* ================= GENERAL ================= */
body {
    background: linear-gradient(135deg, #FF9933, #001F54);
    color: white;
}

/* ================= SIDEBAR ================= */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #FF9933, #001F54);
    padding-top: 2rem;
    width: 280px !important;
}

/* ================= HEADINGS ================= */
h1, h2, h3 {
    color: #FFD700;
}

/* ================= SIDEBAR BUTTONS ================= */
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

    text-align: center;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;

    margin-bottom: 14px;
    box-sizing: border-box;
}

.stButton > button:hover {
    background-color: #FFA500;
    color: white;
}

/* ================= FLOATING STARS ================= */
.star-layer {
    position: fixed;
    top: 0;
    right: 0;
    width: 70%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
}

.star {
    position: absolute;
    width: 28px;
    height: 28px;
    background: rgba(255, 204, 102, 0.35);
    clip-path: polygon(
        50% 0%, 61% 35%, 98% 35%, 68% 57%,
        79% 91%, 50% 70%, 21% 91%, 32% 57%,
        2% 35%, 39% 35%
    );
    animation: floatStar 20s linear infinite;
}

@keyframes floatStar {
    0% { transform: translateY(110vh) rotate(0deg); opacity: 0; }
    20% { opacity: 0.6; }
    100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# BACKGROUND STARS
# -------------------------------------------------
st.markdown("""
<div class="star-layer">
    <div class="star" style="left:10%; animation-delay:0s;"></div>
    <div class="star" style="left:25%; animation-delay:4s;"></div>
    <div class="star" style="left:40%; animation-delay:8s;"></div>
    <div class="star" style="left:55%; animation-delay:12s;"></div>
    <div class="star" style="left:70%; animation-delay:16s;"></div>
    <div class="star" style="left:85%; animation-delay:20s;"></div>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.title("🚀 PLC + AI Solutions Showcase")

# -------------------------------------------------
# FILE PATHS
# -------------------------------------------------
BASE = "https://raw.githubusercontent.com/Harjeetsinghengg/Projects/main"

VIDEO_1 = f"{BASE}/protocol.mp4"
VIDEO_2 = f"{BASE}/OPC.mp4"
VIDEO_3 = f"{BASE}/Template%20Matching.mp4"
VIDEO_4 = f"{BASE}/video4.mp4"
VIDEO_5 = f"{BASE}/video5.mp4"
VIDEO_6 = f"{BASE}/video6.mp4"

PDF_1 = f"{BASE}/Documents/Dashboard.pdf"

# -------------------------------------------------
# HELPERS
# -------------------------------------------------
def play_video(url, height=260):
    st.markdown(f"""
    <video width="100%" height="{height}" autoplay loop muted controls>
        <source src="{url}" type="video/mp4">
    </video>
    """, unsafe_allow_html=True)


def show_pdf(url):
    st.pdf(url)


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
    st.subheader("Predictive Maintenance")
    play_video(VIDEO_5)

with col6:
    st.subheader("Quality Control")
    play_video(VIDEO_6)

st.markdown("---")

# -------------------------------------------------
# SIDEBAR NAVIGATION
# -------------------------------------------------
st.sidebar.title("AI Projects")

projects = {
    "Industrial Protocol": ("video", VIDEO_1),
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
# MAIN DISPLAY
# -------------------------------------------------
proj_name = st.session_state.selected_project
proj_type, proj_src = projects[proj_name]

st.subheader(proj_name)

if proj_type == "video":
    play_video(proj_src, height=420)
else:
    show_pdf(proj_src)

# -------------------------------------------------
# DESCRIPTION
# -------------------------------------------------
st.markdown("""
### Project Overview

This section showcases the different projects I have been working on in my spare time.

### My Technical Values
- **Continuous Learning**
- **Innovation & Creativity**
- **Quality & Reliability**
- **Problem Solving**
- **Automation & Efficiency**
- **Collaboration & Growth**
""")
