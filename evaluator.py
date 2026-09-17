def evaluate_answer(answer, keywords):

    if not answer or not answer.strip():
        return {
            "score": 0,
            "technical_score": 0,
            "relevance_score": 0,
            "completeness_score": 0,
            "quality_score": 0,
            "feedback": "No answer was provided.",
            "strengths": [],
            "improvements": [
                "Provide an answer to the question."
            ],
            "recommended_topics": keywords[:3]
        }

    answer_lower = answer.lower()

    words = answer.split()
    word_count = len(words)

    # ---------------------------------
    # KEYWORD / TECHNICAL ANALYSIS
    # ---------------------------------

    matched = []

    for keyword in keywords:

        if keyword.lower() in answer_lower:
            matched.append(keyword)

    keyword_percentage = (
        len(matched) / len(keywords) * 100
        if keywords
        else 0
    )

    # ---------------------------------
    # TECHNICAL SCORE
    # ---------------------------------

    if keyword_percentage >= 80:
        technical_score = 10

    elif keyword_percentage >= 60:
        technical_score = 8

    elif keyword_percentage >= 40:
        technical_score = 6

    elif keyword_percentage >= 20:
        technical_score = 4

    else:
        technical_score = 2

    # ---------------------------------
    # COMPLETENESS
    # ---------------------------------

    if word_count >= 60:
        completeness_score = 10

    elif word_count >= 40:
        completeness_score = 8

    elif word_count >= 25:
        completeness_score = 7

    elif word_count >= 15:
        completeness_score = 5

    elif word_count >= 8:
        completeness_score = 3

    else:
        completeness_score = 2

    # ---------------------------------
    # RELEVANCE
    # ---------------------------------

    if keyword_percentage >= 70:
        relevance_score = 10

    elif keyword_percentage >= 50:
        relevance_score = 8

    elif keyword_percentage >= 30:
        relevance_score = 6

    elif keyword_percentage >= 15:
        relevance_score = 4

    else:
        relevance_score = 2

    # ---------------------------------
    # ANSWER QUALITY
    # ---------------------------------

    technical_terms = [
        "because",
        "example",
        "used",
        "works",
        "process",
        "advantage",
        "difference",
        "implementation",
        "performance",
        "memory"
    ]

    quality_matches = 0

    for term in technical_terms:

        if term in answer_lower:
            quality_matches += 1

    if quality_matches >= 4 and word_count >= 30:
        quality_score = 10

    elif quality_matches >= 3 and word_count >= 20:
        quality_score = 8

    elif quality_matches >= 2:
        quality_score = 6

    elif quality_matches >= 1:
        quality_score = 4

    else:
        quality_score = 2

    # ---------------------------------
    # OVERALL SCORE
    # ---------------------------------

    overall_score = (
        technical_score * 0.40
        + relevance_score * 0.25
        + completeness_score * 0.20
        + quality_score * 0.15
    )

    overall_score = round(overall_score)

    # ---------------------------------
    # STRENGTHS
    # ---------------------------------

    strengths = []

    if technical_score >= 8:
        strengths.append(
            "Strong understanding of technical concepts."
        )

    if relevance_score >= 8:
        strengths.append(
            "Answer is relevant to the question."
        )

    if completeness_score >= 8:
        strengths.append(
            "Good level of explanation and detail."
        )

    if quality_score >= 8:
        strengths.append(
            "Answer demonstrates good technical reasoning."
        )

    if not strengths:
        strengths.append(
            "You have started addressing the question."
        )

    # ---------------------------------
    # IMPROVEMENTS
    # ---------------------------------

    improvements = []

    if technical_score < 8:
        improvements.append(
            "Include more important technical concepts."
        )

    if relevance_score < 8:
        improvements.append(
            "Keep the answer more directly focused on the question."
        )

    if completeness_score < 8:
        improvements.append(
            "Provide more explanation and examples."
        )

    if quality_score < 8:
        improvements.append(
            "Explain why and how the concept works."
        )

    if not improvements:
        improvements.append(
            "Continue practicing advanced interview questions."
        )

    # ---------------------------------
    # FEEDBACK
    # ---------------------------------

    if overall_score >= 9:

        feedback = (
            "Excellent answer. You demonstrated strong "
            "technical understanding and good explanation."
        )

    elif overall_score >= 8:

        feedback = (
            "Very good answer. Your main concepts are correct. "
            "Add a practical example to make it even stronger."
        )

    elif overall_score >= 6:

        feedback = (
            "Good attempt. You covered some important concepts, "
            "but your explanation needs more technical depth."
        )

    elif overall_score >= 4:

        feedback = (
            "Average answer. Focus on the core concepts and "
            "explain them with a simple example."
        )

    else:

        feedback = (
            "The answer needs improvement. Review the topic "
            "and try to explain the main concepts clearly."
        )

    # ---------------------------------
    # RECOMMENDED TOPICS
    # ---------------------------------

    recommended_topics = []

    for keyword in keywords:

        if keyword not in matched:

            recommended_topics.append(keyword)

    if not recommended_topics:
        recommended_topics = keywords[:3]

    return {

        "score": overall_score,

        "technical_score": technical_score,

        "relevance_score": relevance_score,

        "completeness_score": completeness_score,

        "quality_score": quality_score,

        "feedback": feedback,

        "strengths": strengths,

        "improvements": improvements,

        "recommended_topics": recommended_topics[:5]
    }