import streamlit as st
import pandas as pd
import os

from src.extract import extract_text_from_pdf
from src.preprocess import preprocess
from src.skills import extract_skills
from src.similarity import calculate_similarity

# -----------------------------
# 📌 Page Config
# -----------------------------
st.set_page_config(page_title="Resume Analyzer", layout="wide")

st.title("📄 AI Resume Analyzer")
st.markdown("### 🚀 Match resumes with job description using NLP")
st.divider()

# -----------------------------
# 📌 Skills List
# -----------------------------
skills_list = [
    "python", "sql", "machine learning", "deep learning",
    "nlp", "data analysis", "pandas", "numpy", "sklearn"
]

# -----------------------------
# 📌 Upload Section
# -----------------------------
st.subheader("📌 Upload Job Description")
jd_file = st.file_uploader("Upload JD (.txt)", type=["txt"])

st.subheader("📂 Upload Resumes")
resume_files = st.file_uploader(
    "Upload PDF resumes",
    type=["pdf"],
    accept_multiple_files=True
)

# -----------------------------
# 🚀 Analyze Button
# -----------------------------
if st.button("🚀 Analyze"):

    if jd_file and resume_files:

        with st.spinner("Analyzing resumes... ⏳"):

            jd_text = jd_file.read().decode("utf-8")
            clean_jd = preprocess(jd_text)

            results = []

            for resume in resume_files:
                with open("temp.pdf", "wb") as f:
                    f.write(resume.read())

                text = extract_text_from_pdf("temp.pdf")
                clean_text = preprocess(text)

                score = calculate_similarity(clean_text, clean_jd)

                resume_skills = extract_skills(text.lower(), skills_list)
                jd_skills = extract_skills(jd_text.lower(), skills_list)

                missing_skills = list(set(jd_skills) - set(resume_skills))

                results.append({
                    "Resume": resume.name,
                    "Score": round(score, 2),
                    "Skills": ", ".join(resume_skills),
                    "Missing Skills": ", ".join(missing_skills)
                })

            # -----------------------------
            # 📊 Results
            # -----------------------------
            df = pd.DataFrame(results)
            df = df.sort_values(by="Score", ascending=False)

            st.subheader("📊 Results")
            st.dataframe(df, use_container_width=True)

            # 🏆 Best Resume
            best = df.iloc[0]
            st.success(f"🏆 Best Match: {best['Resume']} (Score: {best['Score']})")

            # 📥 Download
            st.download_button(
                "⬇ Download CSV",
                df.to_csv(index=False),
                "results.csv"
            )

    else:
        st.warning("⚠️ Please upload both JD and resumes")