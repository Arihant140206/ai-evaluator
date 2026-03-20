from flask import Flask, request, jsonify, render_template
import json
from utils.evaluator import evaluate_answer

app = Flask(__name__)

# Load questions from JSON
with open("questions.json") as f:
    questions = json.load(f)


# Home route (loads webpage)
@app.route("/")
def home():
    return render_template("index.html")


# API route to evaluate answer
@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.json
    answer = data["answer"]
    question_id = data["question_id"]

    ideal_points = questions[question_id]["ideal_points"]

    score, missing = evaluate_answer(answer, ideal_points)

    return jsonify({
        "score": round(score * 10, 2),
        "missing": missing
    })


if __name__ == "__main__":
    import os

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))