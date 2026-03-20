from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def evaluate_answer(user_answer, ideal_points):
    # Combine user answer + ideal points
    texts = [user_answer] + ideal_points

    # Convert text to vectors
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(texts)

    # Compute similarity
    similarities = cosine_similarity(vectors[0:1], vectors[1:])

    # Average score
    score = similarities.mean()

    # Find missing keywords
    missing_points = []
    for point in ideal_points:
        if point.lower() not in user_answer.lower():
            missing_points.append(point)

    return score, missing_points


# 🔥 TEST BLOCK (this is what prints output)
if __name__ == "__main__":
    user_answer = "I will use hashing and database for scalability"

    ideal_points = [
        "hashing",
        "database",
        "scalability",
        "load balancing",
        "caching",
        "fault tolerance"
    ]

    score, missing = evaluate_answer(user_answer, ideal_points)

    print("Score:", round(score * 10, 2), "/10")
    print("Missing Points:", missing)