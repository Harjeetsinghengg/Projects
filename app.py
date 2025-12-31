import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Solutions Showcase",
    layout="wide"
)

# ---------------- CSS (THEME + STARS + BUTTON SIZE) ----------------
st.markdown("""
<style>

/* ===== Base gradient ===== */
body {
    background: linear-gradient(135deg, #FF9933, #001F54);
    color: white;
}

/* ===== Sidebar ===== */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #FF9933, #001F54);
    padding-top: 2rem;
}

/* ===== Headings ===== */
h1, h2, h3 {
    color: #FFD700;
}

/* ===== Sidebar Buttons (FIXED SIZE) ===== */
.stButton>button {
    background-color: #FFD700;
    color: #001F54;
    width: 100%;
    height: 55px;
    margin-bottom: 10px;
    border-radius: 8px;
    font-weight: 600;
    font-size: 15px;
}

.stButton>button:hover {
    background-color: #FFA500;
    color: white;
}

/* ===== Floating stars container (RIGHT SIDE ONLY) ===== */
.star-layer {
    position: fixed;
    top: 0;
    right: 0;
    width: 70%;
    height: 100%;
    pointer-events: none;
    z-index: 0;
}

/* ===== Star shape ===== */
.star {
    position: absolute;
    width: 28px;
    height: 28px;
    background: rgba(255, 204, 102, 0.35);
    clip-path: polygon(
        50% 0%, 61% 35%, 98% 35%,
        68% 57%, 79% 91%, 50% 70%,
        21% 91%, 32% 57%, 2% 35%, 39% 35%
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

# ---------------- STAR LAYER ----------------
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

# ---------------- TITLE ----------------
st.title(" PLC + AI Solutions Showcase 🚀")

# ---------------- VIDEO URLS ----------------
BASE = "https://raw.githubusercontent.com/Harjeetsinghengg/Projects/main"

VIDEO_1 = f"{BASE}/protocol.mp4"
VIDEO_2 = f"{BASE}/OPC.mp4"
VIDEO_3 = f"{BASE}/Template Matching.mp4"
VIDEO_4 = f"{BASE}/video4.mp4"

# ---------------- VIDEO PLAYER ----------------
def play_video(url):
    st.markdown(f"""
    <video width="100%" autoplay loop muted controls>
        <source src="{url}" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    """, unsafe_allow_html=True)

# ---------------- TOP VIDEOS GRID ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Comm Protocols")
    play_video(VIDEO_1)

with col2:
    st.subheader("OPC Integration")
    play_video(VIDEO_2)

with col3:
    st.subheader("Vision System")
    play_video(VIDEO_3)

st.markdown("---")

# ---------------- SIDEBAR BUTTONS ----------------
st.sidebar.title("AI Projects")

projects = {
    "AI Vision Inspection": VIDEO_1,
    "PLC + AI Integration": VIDEO_2,
    "Industrial Vision ROI": VIDEO_3,
    "Smart Factory AI": VIDEO_4,
    "Coming Soon 🚧": VIDEO_1,
    "Future Innovation 🚀": VIDEO_2
}

# Default selection
if "selected_project" not in st.session_state:
    st.session_state.selected_project = list(projects.keys())[0]

# Fixed-size buttons
for project in projects:
    if st.sidebar.button(project):
        st.session_state.selected_project = project

# ---------------- MAIN DISPLAY ----------------
st.subheader(st.session_state.selected_project)
play_video(projects[st.session_state.selected_project])

st.write("""
**Project Overview:**  
This AI solution demonstrates real-world industrial automation using  
computer vision, PLC integration, and intelligent analytics.
""")
