import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Leave Request Bot", page_icon="🤖")

st.title("🤖 AI Leave Request Bot")
st.write("I'm here to help you apply for a leave. Let's get started!")

@st.cache_data
def load_data():
    return pd.read_csv("employee_data.csv")

df = load_data()

if "step" not in st.session_state:
    st.session_state.step = 1

if "name" not in st.session_state:
    st.session_state.name = ""

if "reason" not in st.session_state:
    st.session_state.reason = ""

if "leave_days" not in st.session_state:
    st.session_state.leave_days = 0

if st.session_state.step == 1:
    name_input = st.text_input("What's your name?")
    if name_input:
        emp = df[df["Name"].str.lower().str.strip() == name_input.lower().strip()]
        if emp.empty:
            st.error("❌ Name not found. Please try again.")
        else:
            st.success(f"Welcome, {name_input} 👋")
            st.session_state.name = name_input
            st.session_state.step = 2

if st.session_state.step == 2:
    reason_input = st.text_area("Why do you want to take leave?")
    if reason_input:
        st.session_state.reason = reason_input
        st.session_state.step = 3

if st.session_state.step == 3:
    days = st.number_input("How many days of leave do you need?", min_value=1, max_value=30)
    if st.button("Submit Request"):
        st.session_state.leave_days = days
        emp = df[df["Name"].str.lower().str.strip() == st.session_state.name.lower().strip()]
        used = emp["Used Leaves"].values[0]
        total = emp["Total Leaves"].values[0]
        balance = total - used

        if days <= balance:
            st.success(f"✅ Leave Approved. You have {balance - days} day(s) remaining.")
        else:
            st.error(f"❌ Rejected. You only have {balance} day(s) left.")
        st.session_state.step = 4

if st.session_state.step == 4:
    if st.button("Start Over"):
        for key in ["step", "name", "reason", "leave_days"]:
            del st.session_state[key]
        st.experimental_rerun()
