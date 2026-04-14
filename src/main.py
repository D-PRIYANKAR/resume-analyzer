import os
import pandas as pd

from extract import extract_text_from_pdf
from preprocess import preprocess
from skills import extract_skills
from similarity import calculate_similarity

# -----------------------------
# 🔧 Setup Paths
# -----------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RESUME_FOLDER = os.path.join(BASE_DIR, "data", "resumes")
JD_PATH = os.path.join(BASE_DIR, "data", "job_description.txt")
OUTPUT_PATH = os.path.join(BASE_DIR, "results", "output.csv")

# -----------------------------
# 📌 Skills List
# -----------------------------
skills_list = [
    "python", "sql", "machine learning", "deep learning",
    "nlp", "data analysis", "pandas", "numpy", "sklearn"
]

# -----------------------------
# 📄 Load Job Description
# -----------------------------
with open(JD_PATH, "r") as f:
    jd_text = f.read()

clean_jd = preprocess(jd_text)

# -----------------------------
# 🚀 Process Resumes
# -----------------------------
results = []

for file in os.listdir(RESUME_FOLDER):
    if file.endswith(".pdf"):
        file_path = os.path.join(RESUME_FOLDER, file)

        # Extract + Clean
        text = extract_text_from_pdf(file_path)
        clean_text = preprocess(text)

        # Similarity Score
        score = calculate_similarity(clean_text, clean_jd)

        # Skills
        resume_skills = extract_skills(text.lower(), skills_list)
        jd_skills = extract_skills(jd_text.lower(), skills_list)

        missing_skills = list(set(jd_skills) - set(resume_skills))

        results.append({
            "Resume": file,
            "Score": round(score, 2),
            "Skills": ", ".join(resume_skills),
            "Missing Skills": ", ".join(missing_skills)
        })

# -----------------------------
# 📊 Output
# -----------------------------
df = pd.DataFrame(results)

if df.empty:
    print("❌ No resumes found!")
else:
    df = df.sort_values(by="Score", ascending=False)

    print("\n📊 ===== Resume Ranking ===== 📊\n")

    for _, row in df.iterrows():
        print(f"📄 {row['Resume']}")
        print(f"   🔹 Score: {row['Score']}%")
        print(f"   🔹 Skills: {row['Skills']}")
        print(f"   🔹 Missing: {row['Missing Skills']}")
        print("-" * 50)

    df.to_csv(OUTPUT_PATH, index=False)