import {
    useEffect,
    useState
} from "react";

import {
    useNavigate
} from "react-router-dom";

import {
    evaluateAnswer
} from "../api";


function Interview() {

    const navigate = useNavigate();

    const [interview, setInterview] =
        useState(null);

    const [currentQuestion, setCurrentQuestion] =
        useState(0);

    const [answer, setAnswer] =
        useState("");

    const [loading, setLoading] =
        useState(false);

    const [timeLeft, setTimeLeft] =
        useState(600);


    // =====================================
    // LOAD INTERVIEW
    // =====================================

    useEffect(() => {

        const savedInterview =
            sessionStorage.getItem(
                "interview"
            );

        if (!savedInterview) {

            navigate("/setup");

            return;
        }

        setInterview(
            JSON.parse(savedInterview)
        );

    }, [navigate]);


    // =====================================
    // TIMER
    // =====================================

    useEffect(() => {

        if (!interview) return;

        if (timeLeft <= 0) {

            navigate(
                `/results/${interview.interview_id}`
            );

            return;
        }

        const timer =
            setInterval(() => {

                setTimeLeft(
                    time =>
                        time - 1
                );

            }, 1000);

        return () =>
            clearInterval(timer);

    }, [
        timeLeft,
        interview,
        navigate
    ]);


    if (!interview) {

        return (
            <div className="page loading-page">

                <div className="loading-box">
                    Loading interview...
                </div>

            </div>
        );
    }


    const question =
        interview.questions[
            currentQuestion
        ];

    const total =
        interview.questions.length;


    const progress =
        (
            (currentQuestion + 1) /
            total
        ) * 100;


    const minutes =
        Math.floor(
            timeLeft / 60
        );

    const seconds =
        timeLeft % 60;


    const wordCount =
        answer.trim()
            ? answer.trim().split(/\s+/).length
            : 0;


    const characterCount =
        answer.length;


    const submitAnswer =
        async () => {

            if (!answer.trim()) {

                alert(
                    "Please enter your answer."
                );

                return;
            }


            setLoading(true);


            try {

                await evaluateAnswer({

                    interview_id:
                        interview.interview_id,

                    question:
                        question.question,

                    answer,

                    keywords:
                        question.keywords

                });


                setAnswer("");


                if (
                    currentQuestion <
                    total - 1
                ) {

                    setCurrentQuestion(
                        currentQuestion + 1
                    );

                } else {

                    navigate(
                        `/results/${interview.interview_id}`
                    );

                }

            } catch (error) {

                console.error(error);

                alert(
                    "Could not evaluate your answer."
                );

            } finally {

                setLoading(false);

            }
        };


    return (

        <div className="page interview-page">

            <div className="interview-container">

                {/* HEADER */}

                <div className="interview-header">

                    <div>

                        <span className="small-label">
                            AI MOCK INTERVIEW
                        </span>

                        <h2>
                            {interview.role}
                        </h2>

                        <div className="interview-meta">

                            <span>
                                {interview.difficulty}
                            </span>

                            <span>
                                •
                            </span>

                            <span>
                                Technical Interview
                            </span>

                        </div>

                    </div>


                    <div
                        className={
                            timeLeft <= 120
                                ? "timer danger"
                                : "timer"
                        }
                    >
                        ⏱️{" "}
                        {String(minutes)
                            .padStart(2, "0")}
                        :
                        {String(seconds)
                            .padStart(2, "0")}
                    </div>

                </div>


                {/* PROGRESS */}

                <div className="interview-progress-area">

                    <div className="progress-info">

                        <span>
                            Question{" "}
                            {currentQuestion + 1}
                            {" "}
                            of{" "}
                            {total}
                        </span>

                        <strong>
                            {Math.round(progress)}%
                        </strong>

                    </div>


                    <div className="progress">

                        <div
                            style={{
                                width:
                                    `${progress}%`
                            }}
                        />

                    </div>

                </div>


                {/* QUESTION */}

                <div className="question-box">

                    <span className="question-label">
                        QUESTION{" "}
                        {String(
                            currentQuestion + 1
                        ).padStart(2, "0")}
                    </span>


                    <h1>
                        {question.question}
                    </h1>


                    <div className="answer-tip">

                        <span>
                            💡
                        </span>

                        <div>

                            <strong>
                                Interview Tip
                            </strong>

                            <p>
                                Start with the definition,
                                explain how it works, and
                                give a practical example.
                            </p>

                        </div>

                    </div>

                </div>


                {/* ANSWER */}

                <div className="answer-area">

                    <div className="answer-header">

                        <div>

                            <h3>
                                Your Answer
                            </h3>

                            <span>
                                Explain your answer clearly
                                and confidently.
                            </span>

                        </div>


                        <div className="answer-count">

                            <span>
                                {wordCount} words
                            </span>

                            <span>
                                {characterCount} characters
                            </span>

                        </div>

                    </div>


                    <textarea
                        value={answer}
                        onChange={(e) =>
                            setAnswer(
                                e.target.value
                            )
                        }
                        placeholder="Type your interview answer here..."
                    />


                    <div className="answer-footer">

                        <span>
                            Recommended: 25+ words
                        </span>

                        <span>
                            {wordCount >= 25
                                ? "✓ Good answer length"
                                : "Keep explaining your answer"}
                        </span>

                    </div>

                </div>


                {/* SUBMIT */}

                <button
                    className="primary-btn full"
                    onClick={submitAnswer}
                    disabled={loading}
                >

                    {loading

                        ? "Analyzing Your Answer..."

                        : currentQuestion ===
                          total - 1

                        ? "Finish Interview →"

                        : "Submit Answer →"

                    }

                </button>


                {/* FOOTER INFO */}

                <div className="interview-bottom">

                    <span>
                        🔒 Your interview data is
                        securely stored.
                    </span>

                    <span>
                        AI evaluation happens after
                        each answer.
                    </span>

                </div>

            </div>

        </div>
    );
}


export default Interview;