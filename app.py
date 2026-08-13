import streamlit as st
from datetime import datetime

st.set_page_config(page_title="AI Attendance System", page_icon="📸")

st.title("📸 AI-Based Attendance System")
st.subheader("Face Recognition Attendance Demo")
st.info("Educational prototype: face recognition is simulated for demonstration.")

students = {"23CSE101": "Student A", "23CSE102": "Student B", "23CSE103": "Student C"}

if "attendance" not in st.session_state:
    st.session_state.attendance = []

reg_no = st.selectbox(
    "Select Demo Student",
    list(students),
    format_func=lambda x: f"{x} - {students[x]}"
)

if st.button("🔍 Simulate Face Recognition"):
    now = datetime.now()
    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M:%S %p")
    exists = any(
        r["Register No"] == reg_no and r["Date"] == date
        for r in st.session_state.attendance
    )
    if exists:
        st.warning(f"{students[reg_no]} ({reg_no}) — Attendance Already Recorded!")
    else:
        st.session_state.attendance.append({
            "Register No": reg_no,
            "Name": students[reg_no],
            "Date": date,
            "Time": time,
            "Status": "Present"
        })
        st.success(f"✅ Face Recognized: {students[reg_no]} — Attendance Recorded!")

st.header("📋 Attendance Report")
if st.session_state.attendance:
    st.dataframe(st.session_state.attendance, use_container_width=True)
else:
    st.write("No attendance recorded yet.")

st.header("🔄 System Workflow")
st.write("Camera → Face Detection → Feature Extraction → Face Recognition → Student Identification → Attendance → Report")
st.caption("AI-Based Attendance System | Sir Issac Newton College of Engineering and Technology")
