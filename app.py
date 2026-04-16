import streamlit as st
import pandas as pd
import re
import PyPDF2

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page config
st.set_page_config(page_title="AI Job Recommender", page_icon="💼")

st.title("💼 AI Job Recommender + Resume Analyzer")

# Sidebar
st.sidebar.title("📊 Info")
st.sidebar.write("Upload resume (PDF/TXT) → Extract skills → Get job recommendations")

# Load dataset
df = pd.read_csv("jobs.csv")

# Skill database
SKILLS_DB = [
    "python","java","sql","machine learning","deep learning",
    "tensorflow","pytorch","nlp","aws","docker","kubernetes",
    "excel","power bi","tableau","data analysis","statistics"
]

# Extract text from TXT
def extract_text_txt(file):
    return file.read().decode("utf-8")

# Extract text from PDF
def extract_text_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

# Extract skills
def extract_skills(text):
    text = text.lower()
    found = []
    for skill in SKILLS_DB:
        if re.search(r"\b" + skill + r"\b", text):
            found.append(skill)
    return list(set(found))

# Upload resume
uploaded_file = st.file_uploader("📄 Upload Resume", type=["pdf", "txt"])

skills = []

if uploaded_file:
    if uploaded_file.type == "application/pdf":
        text = extract_text_pdf(uploaded_file)
    else:
        text = extract_text_txt(uploaded_file)

    skills = extract_skills(text)

    st.subheader("🧠 Extracted Skills")
    if skills:
        for s in skills:
            st.write(f"✔ {s}")
    else:
        st.warning("No skills detected. Try manual input.")

# Manual input
manual_input = st.text_input("OR Enter skills manually:")

if manual_input:
    skills = [s.strip() for s in manual_input.split(',')]

# Recommendation
if st.button("🚀 Recommend Jobs"):
    if skills:
        user_input = " ".join(skills)

        vectorizer = TfidfVectorizer()
        skill_matrix = vectorizer.fit_transform(df['skills'])

        user_vec = vectorizer.transform([user_input])
        similarity = cosine_similarity(user_vec, skill_matrix)

        scores = similarity[0]
        top_indices = scores.argsort()[-3:][::-1]

        st.subheader("🎯 Job Recommendations")

        for i in top_indices:
            job = df.iloc[i]['job_title']
            job_skills = df.iloc[i]['skills']
            score = scores[i] * 100

            with st.expander(f"💼 {job} — Match: {score:.2f}%"):
                st.write(f"Skills Required: {job_skills}")

    else:
        st.warning("⚠️ Please upload resume or enter skills")