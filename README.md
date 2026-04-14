# Resume Matcher (NLP Project)

## Features
- Extract text from PDF resumes
- Clean text using NLP (spaCy)
- Match resume with job description
- Calculate similarity score
- Detect missing skills

## Tech Stack
- Python
- spaCy
- Scikit-learn
- TF-IDF + Cosine Similarity


## Sample Output

```
Resume Ranking:

📄 data_science_resume.pdf
Score: 28.7%
Skills: python, sql, machine learning, pandas
Missing: deep learning, nlp

📄 Updated resume.pdf
Score: 0.9%
Skills: -
Missing: python, sql, machine learning, etc.
```


Web App (Streamlit UI)

This project includes an interactive web application built using Streamlit.

✨ Features of the Web App
Upload job description (.txt)
Upload multiple resumes (.pdf)
Automatically analyze resumes using NLP
Calculate similarity scores
Extract skills from resumes
Identify missing skills
Display ranked results in a table
Download results as CSV
