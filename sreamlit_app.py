import streamlit as st
import pandas as pd
from fpdf import FPDF
import base64

st.set_page_config(page_title="AI Leave Request Bot", page_icon="🤖")

st.title("🤖 AI H.R. Bot")
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

def create_pdf(name, total, used, days, balance, approved, reason):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="AI Leave Request Summary", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Total Leaves: {total}", ln=True)
    pdf.cell(200, 10, txt=f"Used Leaves: {used}", ln=True)
    pdf.cell(200, 10, txt=f"Requested: {days}", ln=True)
    pdf.cell(200, 10, txt=f"Remaining: {balance - days if approved else balance}", ln=True)
    pdf.cell(200, 10, txt=f"Status: {'Approved' if approved else 'Rejected'}", ln=True)
    pdf.multi_cell(200, 10, txt=f"Reason: {reason}")
    return pdf

def download_pdf_button(pdf):
    pdf.output("leave_summary.pdf")
    with open("leave_summary.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    href = f'<a href="data:application/octet-stream;base64,{base64_pdf}" download="Leave_Summary.pdf"> Download PDF Summary</a>'
    st.markdown(href, unsafe_allow_html=True)

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
        approved = days <= balance

        if approved:
            st.success(f"✅ Leave Approved. You have {balance - days} day(s) remaining.")
        else:
            st.error(f"❌ Rejected. You only have {balance} day(s) left.")

        st.write("📋 *Your Leave Summary:*")
        st.write(f"- *Name:* {st.session_state.name}")
        st.write(f"- *Total Leaves:* {total}")
        st.write(f"- *Used Leaves:* {used}")
        st.write(f"- *Requested:* {days}")
        st.write(f"- *Remaining:* {balance - days if approved else balance}")
        st.write(f"- *Reason:* {st.session_state.reason}")
        st.write(f"- *Status:* {'Approved ✅' if approved else 'Rejected ❌'}")

        # ✅ Generate and offer PDF download
        pdf = create_pdf(
            st.session_state.name,
            total,
            used,
            days,
            balance,
            approved,
            st.session_state.reason
        )
        download_pdf_button(pdf)

        st.session_state.step = 4

if st.session_state.step == 4:
    if st.button("Start Over"):
        for key in ["step", "name", "reason", "leave_days"]:
            del st.session_state[key]
        st.rerun()
