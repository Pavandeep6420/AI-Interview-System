import {
    useEffect,
    useState
} from "react";

import {
    useNavigate,
    useParams
} from "react-router-dom";

import {
    getResult
} from "../api";


function Results() {

    const { id } = useParams();

    const navigate = useNavigate();

    const [result, setResult] =
        useState(null);


    useEffect(() => {

        getResult(id)

            .then((response) => {

                setResult(
                    response.data
                );

            })

            .catch((error) => {

                console.error(error);

            });

    }, [id]);


    if (!result) {

        return (

            <div className="page loading-page">

                <div className="loading-box">
                    Loading your performance report...
                </div>

            </div>
        );
    }


    const score =
        Number(
            result.overall_score || 0
        );


    const performance =
        score >= 80
            ? "Excellent Performance"
            : score >= 60
            ? "Good Performance"
            : score >= 40
            ? "Average Performance"
            : "Keep Practicing";


    const strongAnswers =
        result.answers.filter(
            item =>
                Number(item.score) >= 8
        ).length;


    const improvementAnswers =
        result.answers.filter(
            item =>
                Number(item.score) < 8
        ).length;


    // =====================================
    // CALCULATE METRICS
    // =====================================

    const getAverage = (field) => {

        const values =
            result.answers
                .map(
                    item =>
                        Number(
                            item[field] || 0
                        )
                )
                .filter(
                    value => value > 0
                );

        if (!values.length)
            return 0;

        return (
            values.reduce(
                (a, b) => a + b,
                0
            ) / values.length
        ).toFixed(1);
    };


    const technical =
        getAverage(
            "technical_score"
        );

    const relevance =
        getAverage(
            "relevance_score"
        );

    const completeness =
        getAverage(
            "completeness_score"
        );

    const quality =
        getAverage(
            "quality_score"
        );


    // =====================================
    // COLLECT INSIGHTS
    // =====================================

    const strengths = [];

    const improvements = [];

    const topics = [];


    result.answers.forEach(
        item => {

            if (item.strengths) {

                item.strengths.forEach(
                    value => {

                        if (
                            !strengths.includes(
                                value
                            )
                        ) {

                            strengths.push(
                                value
                            );

                        }

                    }
                );

            }


            if (item.improvements) {

                item.improvements.forEach(
                    value => {

                        if (
                            !improvements.includes(
                                value
                            )
                        ) {

                            improvements.push(
                                value
                            );

                        }

                    }
                );

            }


            if (
                item.recommended_topics
            ) {

                item.recommended_topics.forEach(
                    value => {

                        if (
                            !topics.includes(
                                value
                            )
                        ) {

                            topics.push(
                                value
                            );

                        }

                    }
                );

            }

        }
    );


    return (

        <div className="page">

            <div className="results-container">

                {/* =================================
                    HEADER
                ================================= */}

                <div className="results-header">

                    <div className="badge">
                        INTERVIEW COMPLETED
                    </div>


                    <h1>
                        Great job,{" "}
                        {result.interview.name}! 🎉
                    </h1>


                    <p>
                        Here's your personalized
                        interview performance report.
                    </p>

                </div>


                {/* =================================
                    SCORE CARD
                ================================= */}

                <div className="premium-score-card">

                    <div
                        className="big-score"
                        style={{
                            "--score":
                                `${score * 3.6}deg`
                        }}
                    >

                        <div className="score-inner">

                            <strong>
                                {Math.round(score)}
                            </strong>

                            <span>
                                /100
                            </span>

                        </div>

                    </div>


                    <div className="score-summary">

                        <span className="summary-label">
                            OVERALL PERFORMANCE
                        </span>


                        <h2>
                            {performance}
                        </h2>


                        <p>
                            You completed{" "}
                            <strong>
                                {result.answers.length}
                            </strong>{" "}
                            technical questions for
                            the{" "}
                            <strong>
                                {result.interview.role}
                            </strong>{" "}
                            role.
                        </p>


                        <div className="summary-meta">

                            <span>
                                ◉{" "}
                                {result.interview.difficulty}
                            </span>


                            <span>
                                ✓{" "}
                                {strongAnswers}
                                {" "}
                                strong answers
                            </span>

                        </div>

                    </div>

                </div>


                {/* =================================
                    PERFORMANCE METRICS
                ================================= */}

                <div className="metric-grid">

                    <div className="metric-card">

                        <div className="metric-top">

                            <span>
                                Technical
                            </span>

                            <strong>
                                {technical}/10
                            </strong>

                        </div>


                        <div className="metric-bar">

                            <div
                                style={{
                                    width:
                                        `${Number(technical) * 10}%`
                                }}
                            />

                        </div>

                        <p>
                            Technical concept coverage
                        </p>

                    </div>


                    <div className="metric-card">

                        <div className="metric-top">

                            <span>
                                Relevance
                            </span>

                            <strong>
                                {relevance}/10
                            </strong>

                        </div>


                        <div className="metric-bar">

                            <div
                                style={{
                                    width:
                                        `${Number(relevance) * 10}%`
                                }}
                            />

                        </div>

                        <p>
                            Answer relevance
                        </p>

                    </div>


                    <div className="metric-card">

                        <div className="metric-top">

                            <span>
                                Completeness
                            </span>

                            <strong>
                                {completeness}/10
                            </strong>

                        </div>


                        <div className="metric-bar">

                            <div
                                style={{
                                    width:
                                        `${Number(completeness) * 10}%`
                                }}
                            />

                        </div>

                        <p>
                            Explanation depth
                        </p>

                    </div>


                    <div className="metric-card">

                        <div className="metric-top">

                            <span>
                                Answer Quality
                            </span>

                            <strong>
                                {quality}/10
                            </strong>

                        </div>


                        <div className="metric-bar">

                            <div
                                style={{
                                    width:
                                        `${Number(quality) * 10}%`
                                }}
                            />

                        </div>

                        <p>
                            Technical reasoning
                        </p>

                    </div>

                </div>


                {/* =================================
                    QUICK STATS
                ================================= */}

                <div className="stats-grid">

                    <div className="stat-card premium-stat">

                        <div className="stat-card-icon">
                            📋
                        </div>

                        <h3>
                            {result.answers.length}
                        </h3>

                        <p>
                            Questions Answered
                        </p>

                    </div>


                    <div className="stat-card premium-stat">

                        <div className="stat-card-icon success">
                            ✓
                        </div>

                        <h3>
                            {strongAnswers}
                        </h3>

                        <p>
                            Strong Answers
                        </p>

                    </div>


                    <div className="stat-card premium-stat">

                        <div className="stat-card-icon warning">
                            ↗
                        </div>

                        <h3>
                            {improvementAnswers}
                        </h3>

                        <p>
                            Need Improvement
                        </p>

                    </div>

                </div>


                {/* =================================
                    AI INSIGHTS
                ================================= */}

                <div className="analysis-grid">

                    {/* STRENGTHS */}

                    <div className="analysis-card">

                        <div className="analysis-title">

                            <span className="analysis-icon">
                                💪
                            </span>

                            <div>

                                <h2>
                                    Your Strengths
                                </h2>

                                <p>
                                    What you did well
                                </p>

                            </div>

                        </div>


                        {strengths.length > 0

                            ? strengths
                                .slice(0, 5)
                                .map(
                                    (
                                        item,
                                        index
                                    ) => (

                                        <div
                                            className="insight-item"
                                            key={index}
                                        >

                                            <span>
                                                ✓
                                            </span>

                                            <p>
                                                {item}
                                            </p>

                                        </div>

                                    )
                                )

                            : (

                                <div className="insight-item">

                                    <span>
                                        →
                                    </span>

                                    <p>
                                        Continue practicing
                                        to develop stronger
                                        technical answers.
                                    </p>

                                </div>

                            )
                        }

                    </div>


                    {/* IMPROVEMENTS */}

                    <div className="analysis-card">

                        <div className="analysis-title">

                            <span className="analysis-icon warning">
                                🎯
                            </span>

                            <div>

                                <h2>
                                    Areas to Improve
                                </h2>

                                <p>
                                    Focus areas for your
                                    next interview
                                </p>

                            </div>

                        </div>


                        {improvements.length > 0

                            ? improvements
                                .slice(0, 5)
                                .map(
                                    (
                                        item,
                                        index
                                    ) => (

                                        <div
                                            className="insight-item improvement"
                                            key={index}
                                        >

                                            <span>
                                                !
                                            </span>

                                            <p>
                                                {item}
                                            </p>

                                        </div>

                                    )
                                )

                            : (

                                <div className="insight-item">

                                    <span>
                                        ✓
                                    </span>

                                    <p>
                                        Excellent! Keep
                                        practicing advanced
                                        questions.
                                    </p>

                                </div>

                            )
                        }

                    </div>

                </div>


                {/* =================================
                    RECOMMENDED TOPICS
                ================================= */}

                {topics.length > 0 && (

                    <div className="topics-card">

                        <div>

                            <span className="summary-label">
                                PERSONALIZED LEARNING
                            </span>

                            <h2>
                                Recommended Topics 📚
                            </h2>

                            <p>
                                Review these concepts
                                before your next interview.
                            </p>

                        </div>


                        <div className="topic-list">

                            {topics
                                .slice(0, 8)
                                .map(
                                    (
                                        topic,
                                        index
                                    ) => (

                                        <span
                                            key={index}
                                        >
                                            {topic}
                                        </span>

                                    )
                                )
                            }

                        </div>

                    </div>

                )}


                {/* =================================
                    QUESTION ANALYSIS
                ================================= */}

                <div className="results-section-title">

                    <div>

                        <span>
                            DETAILED BREAKDOWN
                        </span>

                        <h2>
                            Question Analysis
                        </h2>

                    </div>

                </div>


                {result.answers.map(
                    (item, index) => (

                        <div
                            className="premium-answer-card"
                            key={item.id}
                        >

                            <div className="answer-top">

                                <div>

                                    <span className="question-label">
                                        QUESTION{" "}
                                        {index + 1}
                                    </span>

                                    <h3>
                                        {item.question}
                                    </h3>

                                </div>


                                <div
                                    className={
                                        Number(
                                            item.score
                                        ) >= 8
                                            ? "score-pill good"
                                            : "score-pill"
                                    }
                                >
                                    {item.score}/10
                                </div>

                            </div>


                            {/* ANSWER */}

                            <div className="answer-content">

                                <span>
                                    YOUR ANSWER
                                </span>

                                <p>
                                    {item.answer}
                                </p>

                            </div>


                            {/* METRICS */}

                            <div className="question-metrics">

                                <div>

                                    <span>
                                        Technical
                                    </span>

                                    <strong>
                                        {item.technical_score || 0}/10
                                    </strong>

                                </div>


                                <div>

                                    <span>
                                        Relevance
                                    </span>

                                    <strong>
                                        {item.relevance_score || 0}/10
                                    </strong>

                                </div>


                                <div>

                                    <span>
                                        Completeness
                                    </span>

                                    <strong>
                                        {item.completeness_score || 0}/10
                                    </strong>

                                </div>


                                <div>

                                    <span>
                                        Quality
                                    </span>

                                    <strong>
                                        {item.quality_score || 0}/10
                                    </strong>

                                </div>

                            </div>


                            {/* FEEDBACK */}

                            <div className="ai-feedback">

                                <div className="feedback-icon">
                                    AI
                                </div>

                                <div>

                                    <strong>
                                        AI Feedback
                                    </strong>

                                    <p>
                                        {item.feedback}
                                    </p>

                                </div>

                            </div>

                        </div>

                    )
                )}


                {/* =================================
                    ACTIONS
                ================================= */}

                <div className="result-actions">

                    <button
                        className="primary-btn"
                        onClick={() =>
                            navigate("/setup")
                        }
                    >
                        Take Another Interview →
                    </button>


                    <button
                        className="secondary-btn"
                        onClick={() =>
                            navigate("/dashboard")
                        }
                    >
                        View Dashboard
                    </button>

                </div>

            </div>

        </div>
    );
}


export default Results;