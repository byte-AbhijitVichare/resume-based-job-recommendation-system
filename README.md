💼 AI Job Recommender & Resume Analyzer

This is a Machine Learning web application that analyzes a user's resume and recommends suitable job roles based on their skills.

🚀 Features
📄 Upload resume (PDF or TXT)
🧠 Automatic skill extraction using NLP
💼 Job recommendations based on skills
📊 Match score (%) for each job
🌐 Simple and interactive UI using Streamlit

🛠️ Tech Stack
Python
pandas
scikit-learn
Streamlit
PyPDF2

📂 Project Structure
project/
│
├── app.py
├── jobs.csv
├── requirements.txt
└── README.md

⚙️ How to Run
Install dependencies:
pip install -r requirements.txt
Run the app:
streamlit run app.py

🧠 How It Works
Resume is uploaded
Text is extracted from PDF/TXT
Skills are detected using keyword matching
TF-IDF + cosine similarity is used to match jobs

📌 Use Case
Helps users find suitable jobs based on their skills
Useful for students and job seekers

🚀 Future Improvements
Better skill extraction using advanced NLP
Add real job listings
Improve UI design
