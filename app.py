import streamlit as st

st.set_page_config(layout="wide", page_title="AI Solutions Showcase")

# Gradient theme CSS
st.markdown("""
<style>
body { background: linear-gradient(135deg, #FF9933, #001F54); color: white; }
[data-testid="stSidebar"] { background: linear-gradient(180deg, #FF9933, #001F54); color: white; }
h1, h2, h3 { color: #FFD700; }
</style>
""", unsafe_allow_html=True)

st.title("My AI Solution Showcase")

# Top 3 video tiles (3x1)
col1, col2, col3 = st.columns(3)
col1.video("https://raw.githubusercontent.com/username/repo/main/videos/top1.mp4")
col2.video("https://raw.githubusercontent.com/username/repo/main/videos/top2.mp4")
col3.video("https://raw.githubusercontent.com/username/repo/main/videos/top3.mp4")

st.write("---")

# Sidebar project selection
projects = {
    "Project A": "https://raw.githubusercontent.com/username/repo/main/videos/projectA.mp4",
    "Project B": "https://raw.githubusercontent.com/username/repo/main/videos/projectB.mp4",
    "Project C": "https://raw.githubusercontent.com/username/repo/main/videos/projectC.mp4",
}
selected = st.sidebar.selectbox("Select a Project", list(projects.keys()))

# Main area
st.subheader(selected)
st.video(projects[selected])
st.write("Description for", selected)
st.download_button("Download Project Code", data=b"Sample code here", file_name=f"{selected}_code.zip")
