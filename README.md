🤖 AI Leave Request Bot

An interactive AI-powered HR chatbot built with Streamlit that helps employees apply for leave and download a PDF summary of their leave request.

🔍 Overview

This bot streamlines the leave application process by:

Interacting with users in a conversational style.

Validating employee names from a CSV database.

Collecting the reason and number of leave days requested.

Calculating available leave balance.

Approving or rejecting leave requests.

Generating a downloadable PDF summary of the leave request.



---

🚀 Demo




---

📁 Features

👤 Employee name validation from a dataset (employee_data.csv)

📝 Text-based reason input for leave

📅 Number of leave days with validation

✅ Smart leave approval logic based on available balance

📄 Auto-generated PDF leave summary

🔁 Option to restart the conversation from scratch



---

📂 File Structure

├── app.py                 # Streamlit application code
├── employee_data.csv      # Employee dataset with leave details
├── leave_summary.pdf      # (Generated) Leave summary PDF
├── README.md              # Project documentation


---

📊 Sample employee_data.csv

Ensure your employee_data.csv is formatted like:

Name,Total Leaves,Used Leaves
Alice,30,10
Bob,25,20
Charlie,20,5


---

🛠️ How to Run

1. Install Requirements



pip install streamlit pandas fpdf

2. Place your CSV



Ensure employee_data.csv is in the same directory as app.py.

3. Run the App



streamlit run app.py


---

📥 PDF Summary

Once the leave request is submitted, the app will:

Generate a summary using fpdf.

Provide a download link for the generated Leave_Summary.pdf.



---

🔁 Reset Conversation

After submission, you can click "Start Over" to restart the chatbot from step 1.


---

✅ To-Do / Enhancements

🔐 Add authentication for employee login.

💾 Save leave history to a database.

📧 Email the leave summary automatically.

💬 Add NLP to improve reason understanding.

🌐 Deploy on Streamlit Cloud or HuggingFace Spaces.



---

🧠 Powered By

Streamlit

pandas

fpdf



---

📬 Contact

For feedback or contributions, feel free to open an issue or pull request
