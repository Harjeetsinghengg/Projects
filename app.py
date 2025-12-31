import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="AI Solutions Showcase",
    layout="wide"
)

# ================= CSS STYLING =================
st.markdown("""
<style>
/* ===== REMOVE TOP SPACE ===== */
header[data-testid="stHeader"] { display: none; }
.stApp { padding-top: 0rem !important; }
.block-container { padding-top: 1rem !important; }

/* ===== Base background ===== */
body { background: linear-gradient(135deg, #FF9933, #001F54); color: white; }

/* ===== Sidebar ===== */
[data-testid="stSidebar"] { background: linear-gradient(180deg, #FF9933, #001F54); padding-top: 2rem; }

/* ===== Headings ===== */
h1, h2, h3 { color: #FFD700; }

/* ===== FIXED SIZE SIDEBAR BUTTONS ===== */
.stButton > button {
    width: 100%;
    height: 55px;
    background-color: #FFD700;
    color: #001F54;
    font-size: 14px;
    font-weight: 600;
    border-radius: 8px;
    margin-bottom: 10px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    display: flex;
    align-items: center;
    justify-content: center;
}
.stButton > button:hover { background-color: #FFA500; color: white; }

/* ===== Floating Stars ===== */
.star-layer { position: fixed; top: 0; right: 0; width: 70%; height: 100%; pointer-events: none; z-index: 0; }
.star {
    position: absolute; width: 28px; height: 28px;
    background: rgba(255, 204, 102, 0.35);
    clip-path: polygon(50% 0%, 61% 35%, 98% 35%,68% 57%, 79% 91%, 50% 70%, 21% 91%, 32% 57%, 2% 35%, 39% 35%);
    animation: floatStar 20s linear infinite;
}
@keyframes floatStar {
    0% { transform: translateY(110vh) rotate(0deg); opacity: 0; }
    20% { opacity: 0.6; }
    100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# ================= STAR EFFECT =================
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

# ================= TITLE =================
st.title("🚀 PLC + AI Solutions Showcase")

# ================= FILE SOURCES =================
BASE = "https://raw.githubusercontent.com/Harjeetsinghengg/Projects/main"

VIDEO_1 = f"{BASE}/protocol.mp4"
VIDEO_2 = f"{BASE}/OPC.mp4"
VIDEO_3 = f"{BASE}/Template_Matching.mp4"
VIDEO_4 = f"{BASE}/video4.mp4"

PDF_1 = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
PDF_2 = "https://www.orimi.com/pdf-test.pdf"

# ================= VIDEO PLAYER WITH AUTOPLAY =================
def play_video_autoplay(url, height=240):
    st.markdown(f"""
        <video width="100%" height="{height}" controls autoplay muted loop>
            <source src="{url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    """, unsafe_allow_html=True)

# ================= TOP 3 AUTOPLAY VIDEOS =================
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Comm Protocols")
    play_video_autoplay(VIDEO_1, height=200)

with col2:
    st.subheader("OPC Integration")
    play_video_autoplay(VIDEO_2, height=200)

with col3:
    st.subheader("Vision System")
    play_video_autoplay(VIDEO_3, height=200)

st.markdown("---")

# ================= SIDEBAR =================
st.sidebar.title("AI Projects")

projects = {
    "AI Vision Inspection": {"type": "video", "src": VIDEO_1},
    "PLC + AI Integration": {"type": "video", "src": VIDEO_2},
    "Industrial Vision ROI": {"type": "video", "src": VIDEO_3},
    "Smart Factory AI": {"type": "video", "src": VIDEO_4},
    "AI Documentation": {"type": "pdf", "src": PDF_1},
    "System Architecture": {"type": "pdf", "src": PDF_2},
}

# Session state
if "selected_project" not in st.session_state:
    st.session_state.selected_project = list(projects.keys())[0]

# Sidebar buttons
for project in projects:
    if st.sidebar.button(project, key=project, use_container_width=True):
        st.session_state.selected_project = project

# ================= MAIN DISPLAY =================
st.markdown("## 🔍 Project Viewer")

selected = projects[st.session_state.selected_project]

if selected["type"] == "video":
    play_video_autoplay(selected["src"], height=400)
elif selected["type"] == "pdf":
    st.markdown(f"""
        <iframe src="{selected['src']}"
                width="100%"
                height="650px"
                style="border:none;">
        </iframe>
    """, unsafe_allow_html=True)

st.markdown(f"""
### {st.session_state.selected_project}

**Description:**  
This content updates dynamically when you select a project from the left panel.
""")
