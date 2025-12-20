import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Solutions Showcase",
    layout="wide"
)

# ---------------- CSS (THEME + STARS) ----------------
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

/* ===== Buttons ===== */
.stButton>button {
    background-color: #FFD700;
    color: #001F54;
    width: 100%;
    margin-bottom: 0.6rem;
    border-radius: 6px;
    font-weight: 600;
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
    width: 14px;
    height: 14px;
    background: rgba(255, 204, 102, 0.35);
    clip-path: polygon(
        50% 0%, 61% 35%, 98% 35%,
        68% 57%, 79% 91%, 50% 70%,
        21% 91%, 32% 57%, 2% 35%, 39% 35%
    );
    animation: floatStar 20s linear infinite;
}

/* ===== Animation ===== */
@keyframes floatStar {
    0% {
        transform: translateY(110vh) rotate(0deg);
        opacity: 0;
    }
    20% { opacity: 0.6; }
    100% {
        transform: translateY(-10vh) rotate(360deg);
        opacity: 0;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------------- STAR LAYER ----------------
st.markdown("""
<div class="star-layer">
    <div class="star" style="left:10%; animation-delay:0s;"></div>
    <div class="star" style="left:20%; animation-delay:4s;"></div>
    <div class="star" style="left:35%; animation-delay:8s;"></div>
    <div class="star" style="left:50%; animation-delay:12s;"></div>
    <div class="star" style="left:65%; animation-delay:16s;"></div>
    <div class="star" style="left:80%; animation-delay:20s;"></div>
</div>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("🚀 My AI Solutions Showcase")

# ---------------- TOP 3 VIDEOS (3x1) ----------------
col1, col2, col3 = st.columns(3)

col1.video("https://raw.githubusercontent.com/USERNAME/REPO/main/videos/top1.mp4")
col2.video("https://raw.githubusercontent.com/USERNAME/REPO/main/videos/top2.mp4")
col3.video("https://raw.githubusercontent.com/USERNAME/REPO/main/videos/top3.mp4")

st.markdown("---")

# ---------------- SIDEBAR PROJECT BUTTONS ----------------
st.sidebar.title("AI Projects")

projects = {
    "AI Vision Inspection": "https://raw.githubusercontent.com/USERNAME/REPO/main/videos/project1.mp4",
    "PLC + AI Defect Detection": "https://raw.githubusercontent.com/USERNAME/REPO/main/videos/project2.mp4",
    "NLP Answer Evaluation": "https://raw.githubusercontent.com/USERNAME/REPO/main/videos/project3.mp4",
    "Student Paper Checker": "https://raw.githubusercontent.com/USERNAME/REPO/main/videos/project4.mp4",
    "Industrial Vision ROI": "https://raw.githubusercontent.com/USERNAME/REPO/main/videos/project5.mp4",
    "Streamlit AI Dashboard": "https://raw.githubusercontent.com/USERNAME/REPO/main/videos/project6.mp4",
    "PDF AI Chatbot": "https://raw.githubusercontent.com/USERNAME/REPO/main/videos/project7.mp4",
    "Quiz Grader AI": "https://raw.githubusercontent.com/USERNAME/REPO/main/videos/project8.mp4",
}

if "selected_project" not in st.session_state:
    st.session_state.selected_project = list(projects.keys())[0]

for project in projects:
    if st.sidebar.button(project):
        st.session_state.selected_project = project

# ---------------- MAIN CONTENT ----------------
selected = st.session_state.selected_project

st.subheader(selected)
st.video(projects[selected])

st.write(
    f"""
    **Project Overview:**  
    This AI solution demonstrates real-world implementation with
    intelligent automation, modern UI, and industry-ready architecture.
    """
)
