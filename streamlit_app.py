import streamlit as st
from planner import generate_plan, generate_notes

# Page config
st.set_page_config(page_title="AI Study Planner", page_icon="📚", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #38bdf8;
        margin-bottom: 20px;
    }
    .card {
        background-color: #1e293b;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 10px;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title"> AI Study Planner Agent</div>', unsafe_allow_html=True)

# ---------------- INPUT SECTION ---------------- #
col1, col2 = st.columns(2)

with col1:
    goal = st.text_area(" Enter your syllabus/topics")

with col2:
    days = st.number_input(" Days left for exam", min_value=1, max_value=100)

level = st.selectbox(" Your Level", ["Beginner", "Intermediate", "Revision"])
hours = st.slider(" Study hours per day", 1, 10, 4)

# ---------------- GENERATE PLAN ---------------- #
if st.button(" Generate Smart Plan"):
    if goal and days:
        with st.spinner(" AI is planning your schedule..."):
            plan = generate_plan(goal, int(days), level, hours)

        st.success(" Plan Generated! :)")

        st.subheader(" Your Study Plan")
        st.markdown("---")
        st.markdown(plan)

        # Save plan in session
        st.session_state["plan"] = plan

    else:
        st.warning("⚠️ Please fill all fields")

# ---------------- NOTES SECTION ---------------- #
st.markdown("---")
st.subheader(" Generate Notes")

topic_input = st.text_input("Enter topic (e.g., Trigonometry identities)")

if st.button(" Generate Notes"):
    if topic_input:
        with st.spinner("Generating notes..."):
            notes = generate_notes(topic_input, level)

        st.success(" Notes Ready! :)")
        st.markdown(notes)
    else:
        st.warning("⚠️ Enter a topic first")