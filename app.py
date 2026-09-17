from flask import Flask, request, jsonify
from flask_cors import CORS

from database import init_db, get_connection
from evaluator import evaluate_answer
from questions import QUESTIONS, get_questions


app = Flask(__name__)

CORS(app)

init_db()


@app.route("/")
def home():
    return jsonify({
        "message": "AI Interview System Backend Running"
    })


# GET ALL TECHNICAL ROLES
@app.route("/api/roles")
def get_roles():

    roles = list(QUESTIONS.keys())

    return jsonify({
        "roles": roles
    })


# START INTERVIEW
@app.route("/api/start", methods=["POST"])
def start_interview():

    data = request.json

    name = data.get("name", "").strip()
    role = data.get("role", "")
    difficulty = data.get(
        "difficulty",
        "Medium"
    )

    if not name:

        return jsonify({
            "error": "Candidate name is required"
        }), 400

    if role not in QUESTIONS:

        return jsonify({
            "error": "Invalid technical role"
        }), 400

    if difficulty not in [
        "Easy",
        "Medium",
        "Hard"
    ]:

        return jsonify({
            "error": "Invalid difficulty"
        }), 400

    # GET 10 QUESTIONS
    questions = get_questions(
        role,
        difficulty,
        10
    )

    if len(questions) < 10:

        return jsonify({
            "error": "Not enough questions available."
        }), 500

    conn = get_connection()

    cursor = conn.execute(
        """
        INSERT INTO interviews
        (name, role, difficulty)
        VALUES (?, ?, ?)
        """,
        (
            name,
            role,
            difficulty
        )
    )

    interview_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return jsonify({

        "interview_id": interview_id,

        "name": name,

        "role": role,

        "difficulty": difficulty,

        "questions": questions,

        "question_source": "Smart Question Bank",

        "message":
            "10 technical questions generated successfully."
    })


# EVALUATE ANSWER
@app.route("/api/evaluate", methods=["POST"])
def evaluate():

    data = request.json

    interview_id = data.get(
        "interview_id"
    )

    question = data.get(
        "question",
        ""
    )

    answer = data.get(
        "answer",
        ""
    )

    keywords = data.get(
        "keywords",
        []
    )

    result = evaluate_answer(
        answer,
        keywords
    )

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO answers
        (
            interview_id,
            question,
            answer,
            score,
            feedback,
            analysis
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            interview_id,
            question,
            answer,
            result["score"],
            result["feedback"],
            str(result)
        )
    )

    conn.commit()
    conn.close()

    return jsonify(result)


# RESULT
@app.route("/api/result/<int:interview_id>")
def get_result(interview_id):

    conn = get_connection()

    interview = conn.execute(
        """
        SELECT *
        FROM interviews
        WHERE id = ?
        """,
        (interview_id,)
    ).fetchone()

    answers = conn.execute(
        """
        SELECT *
        FROM answers
        WHERE interview_id = ?
        ORDER BY id
        """,
        (interview_id,)
    ).fetchall()

    conn.close()

    if not interview:

        return jsonify({
            "error": "Interview not found"
        }), 404

    answer_list = []

    total_score = 0
    technical_total = 0
    relevance_total = 0
    completeness_total = 0
    quality_total = 0

    strong_answers = 0
    improvement_answers = 0

    strengths = []
    improvements = []
    recommended_topics = []

    import ast

    for answer in answers:

        analysis = {}

        try:

            analysis = ast.literal_eval(
                answer["analysis"]
            )

        except Exception:

            analysis = {}

        score = answer["score"] or 0

        total_score += score

        technical_total += analysis.get(
            "technical_score",
            0
        )

        relevance_total += analysis.get(
            "relevance_score",
            0
        )

        completeness_total += analysis.get(
            "completeness_score",
            0
        )

        quality_total += analysis.get(
            "quality_score",
            0
        )

        if score >= 8:

            strong_answers += 1

        elif score < 6:

            improvement_answers += 1

        strengths.extend(
            analysis.get(
                "strengths",
                []
            )
        )

        improvements.extend(
            analysis.get(
                "improvements",
                []
            )
        )

        recommended_topics.extend(
            analysis.get(
                "recommended_topics",
                []
            )
        )

        answer_list.append({

            "question":
                answer["question"],

            "answer":
                answer["answer"],

            "score":
                score,

            "feedback":
                answer["feedback"],

            "technical_score":
                analysis.get(
                    "technical_score",
                    0
                ),

            "relevance_score":
                analysis.get(
                    "relevance_score",
                    0
                ),

            "completeness_score":
                analysis.get(
                    "completeness_score",
                    0
                ),

            "quality_score":
                analysis.get(
                    "quality_score",
                    0
                ),

            "strengths":
                analysis.get(
                    "strengths",
                    []
                ),

            "improvements":
                analysis.get(
                    "improvements",
                    []
                )
        })

    count = len(answers)

    if count > 0:

        average_score = round(
            total_score / count
        )

        technical_score = round(
            technical_total / count
        )

        relevance_score = round(
            relevance_total / count
        )

        completeness_score = round(
            completeness_total / count
        )

        quality_score = round(
            quality_total / count
        )

    else:

        average_score = 0
        technical_score = 0
        relevance_score = 0
        completeness_score = 0
        quality_score = 0

    conn = get_connection()

    conn.execute(
        """
        UPDATE interviews
        SET score = ?
        WHERE id = ?
        """,
        (
            average_score,
            interview_id
        )
    )

    conn.commit()
    conn.close()

    return jsonify({

        "interview": {

            "id":
                interview["id"],

            "name":
                interview["name"],

            "role":
                interview["role"],

            "difficulty":
                interview["difficulty"],

            "created_at":
                interview["created_at"]
        },

        "score":
            average_score,

        "technical_score":
            technical_score,

        "relevance_score":
            relevance_score,

        "completeness_score":
            completeness_score,

        "quality_score":
            quality_score,

        "questions_answered":
            count,

        "strong_answers":
            strong_answers,

        "improvement_answers":
            improvement_answers,

        "strengths":
            list(
                dict.fromkeys(
                    strengths
                )
            )[:5],

        "improvements":
            list(
                dict.fromkeys(
                    improvements
                )
            )[:5],

        "recommended_topics":
            list(
                dict.fromkeys(
                    recommended_topics
                )
            )[:5],

        "answers":
            answer_list
    })


# HISTORY
@app.route("/api/history")
def history():

    conn = get_connection()

    interviews = conn.execute(
        """
        SELECT *
        FROM interviews
        ORDER BY id DESC
        """
    ).fetchall()

    conn.close()

    result = []

    for interview in interviews:

        result.append({

            "id":
                interview["id"],

            "name":
                interview["name"],

            "role":
                interview["role"],

            "difficulty":
                interview["difficulty"],

            "score":
                interview["score"],

            "created_at":
                interview["created_at"]
        })

    return jsonify(result)


if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )