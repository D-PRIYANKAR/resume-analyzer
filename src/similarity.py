from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(text1, text2):
    if not text1.strip() or not text2.strip():
        return 0.0

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return similarity * 100