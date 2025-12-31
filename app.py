import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Solutions Showcase", layout="wide")

# ---------------- CSS (THEME + STARS + BUTTON SIZE) ----------------
st.markdown("""
<style>
body { background: linear-gradient(135deg, #FF9933, #001F54); color: white; }
[data-testid="stSidebar"] { background: linear-gradient(180deg, #FF9933, #001F54); padding-top: 2rem; }
h1, h2, h3 { color: #FFD700; }
.stButton > button { background-color: #FFD700; color: #001F54; width: 100%; height: 55px; margin-bottom: 10px; border-radius: 8px; font-weight: 600; font-size: 15px; }
.stButton > button:hover { background-color: #FFA500; color: white; }
.star-layer { position: fixed; top: 0; right: 0; width: 70%; height: 100%; pointer-events: none; z-index: 0; }
.star { position: absolute; width: 28px; height: 28px; background: rgba(255, 204, 102, 0.35); clip-path: polygon(50% 0%,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%); animation: floatStar 20s linear infinite; }
@keyframes floatStar { 0% { transform: translateY(110vh) rotate(0deg); opacity:0;} 20% { opacity:0.6;} 100% { transform: translateY(-10vh) rotate(360deg); opacity:0; } }
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
st.title("PLC + AI Solutions Showcase 🚀")

# ---------------- VIDEO & PDF URLS ----------------
BASE = "https://raw.githubusercontent.com/Harjeetsinghengg/Projects/main"

VIDEO_1 = f"{BASE}/protocol.mp4"
VIDEO_2 = f"{BASE}/OPC.mp4"
VIDEO_3 = f"{BASE}/Template%20Matching.mp4"
VIDEO_4 = f"{BASE}/video4.mp4"      # optional extra video
PDF_1   = f"{BASE}/documentation.pdf"  # ensure this exists

# ---------------- HELPERS ----------------
def play_video(url: str, height: int = 200):
    st.markdown(f"""
        <video width="100%" height="{height}" autoplay loop muted controls>
            <source src="{url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    """, unsafe_allow_html=True)

def show_pdf(url: str, height: int = 800):
    st.markdown(f"""
        <iframe src="{url}" width="100%" height="{height}" style="border:none;"></iframe>
    """, unsafe_allow_html=True)

# ---------------- TOP ROW: 3 VIDEOS ----------------
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

# ---------------- SIDEBAR BUTTONS ----------------
st.sidebar.title("AI Projects")

projects = {
    "AI Vision Inspection": ("video", VIDEO_1),
    "PLC + AI Integration": ("video", VIDEO_2),
    "Industrial Vision ROI": ("video", VIDEO_3),
    "Smart Factory AI": ("video", VIDEO_4),
}

# default selection
if "selected_project" not in st.session_state:
    st.session_state.selected_project = list(projects.keys())[0]

# Sidebar buttons
for project_name in projects.keys():
    if st.sidebar.button(project_name):
        st.session_state.selected_project = project_name

# ---------------- MAIN DISPLAY (Below Top Videos) ----------------
proj_name = st.session_state.selected_project
proj_type, proj_source = projects[proj_name]

st.subheader(proj_name)

if proj_type == "video":
    play_video(proj_source, height=400)  # bigger display
else:
    show_pdf(proj_source, height=800)

st.write("""
**Project Overview:**  
This section dynamically updates based on the selected project while keeping the top 3 showcase videos unchanged.
""")
