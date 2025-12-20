import streamlit as st

st.set_page_config(layout="wide", page_title="AI Solutions Showcase")

# Gradient theme CSS
st.markdown("""
<style>
body { background: linear-gradient(135deg, #FF9933, #001F54); color: white; }
[data-testid="stSidebar"] { background: linear-gradient(180deg, #FF9933, #001F54); color: white; padding-top: 2rem;}
h1, h2, h3 { color: #FFD700; }
.stButton>button { background-color: #FFD700; color: #001F54; width: 100%; margin-bottom: 0.5rem; }
.stButton>button:hover { background-color: #FFA500; color: white; }
</style>
""", unsafe_allow_html=True)

st.title("My AI Solution Showcase")

# Top 3 video tiles (3x1)
col1, col2, col3 = st.columns(3)
col1.video("https://raw.githubusercontent.com/username/repo/main/videos/top1.mp4")
col2.video("https://raw.githubusercontent.com/username/repo/main/videos/top2.mp4")
col3.video("https://raw.githubusercontent.com/username/repo/main/videos/top3.mp4")

st.write("---")

# Sidebar vertical buttons for 8 projects
st.sidebar.title("Select a Project")

projects = {
    "Project 1": "https://raw.githubusercontent.com/username/repo/main/videos/project1.mp4",
    "Project 2": "https://raw.githubusercontent.com/username/repo/main/videos/project2.mp4",
    "Project 3": "https://raw.githubusercontent.com/username/repo/main/videos/project3.mp4",
    "Project 4": "https://raw.githubusercontent.com/username/repo/main/videos/project4.mp4",
    "Project 5": "https://raw.githubusercontent.com/username/repo/main/videos/project5.mp4",
    "Project 6": "https://raw.githubusercontent.com/username/repo/main/videos/project6.mp4",
    "Project 7": "https://raw.githubusercontent.com/username/repo/main/videos/project7.mp4",
    "Project 8": "https://raw.githubusercontent.com/username/repo/main/videos/project8.mp4",
}

# Initialize selected project
if 'selected_project' not in st.session_state:
    st.session_state.selected_project = list(projects.keys())[0]

# Display buttons vertically
for project in projects.keys():
    if st.sidebar.button(project):
        st.session_state.selected_project = project

# Main area for selected project
selected = st.session_state.selected_project
st.subheader(selected)
st.video(projects[selected])
st.write(f"Description for {selected}")
