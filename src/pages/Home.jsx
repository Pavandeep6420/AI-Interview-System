import { useNavigate } from "react-router-dom";

function Home() {
    const navigate = useNavigate();

    return (
        <div className="app-shell">

            {/* NAVBAR */}
            <nav className="navbar">
                <div
                    className="logo"
                    onClick={() => navigate("/")}
                >
                    <span className="logo-icon">AI</span>
                    <span>InterviewPro</span>
                </div>

                <div className="nav-links">
                    <button onClick={() => navigate("/dashboard")}>
                        Dashboard
                    </button>

                    <button onClick={() => navigate("/history")}>
                        History
                    </button>

                    <button
                        className="nav-start-btn"
                        onClick={() => navigate("/setup")}
                    >
                        Start Interview
                    </button>
                </div>
            </nav>

            {/* HERO */}
            <section className="hero-section">

                <div className="hero-glow glow-one"></div>
                <div className="hero-glow glow-two"></div>

                <div className="hero-content">

                    <div className="hero-badge">
                        <span>✦</span>
                        AI-POWERED INTERVIEW PLATFORM
                    </div>

                    <h1>
                        Your Next Interview
                        <br />
                        <span>Starts Here.</span>
                    </h1>

                    <p>
                        Practice technical interviews with an intelligent
                        AI-powered platform. Answer real interview questions,
                        receive instant feedback, and become placement ready.
                    </p>

                    <div className="hero-buttons">

                        <button
                            className="primary-btn hero-btn"
                            onClick={() => navigate("/setup")}
                        >
                            Start Mock Interview
                            <span>→</span>
                        </button>

                        <button
                            className="outline-btn"
                            onClick={() => navigate("/dashboard")}
                        >
                            View Dashboard
                        </button>

                    </div>

                    <div className="hero-trust">

                        <div>
                            <strong>3+</strong>
                            <span>Job Roles</span>
                        </div>

                        <div className="trust-divider"></div>

                        <div>
                            <strong>3</strong>
                            <span>Difficulty Levels</span>
                        </div>

                        <div className="trust-divider"></div>

                        <div>
                            <strong>10</strong>
                            <span>Point Scoring</span>
                        </div>

                    </div>

                </div>

                {/* INTERVIEW PREVIEW */}
                <div className="hero-preview">

                    <div className="preview-window">

                        <div className="preview-top">

                            <div className="window-dots">
                                <span></span>
                                <span></span>
                                <span></span>
                            </div>

                            <span className="preview-title">
                                AI Interview Session
                            </span>

                        </div>

                        <div className="preview-body">

                            <div className="preview-label">
                                QUESTION 02 / 03
                            </div>

                            <h3>
                                What is the difference between
                                ArrayList and LinkedList?
                            </h3>

                            <div className="preview-answer">
                                <span className="mic-icon">✦</span>
                                <span>
                                    Type your answer here...
                                </span>
                            </div>

                            <div className="preview-bottom">

                                <div className="mini-progress">
                                    <span></span>
                                </div>

                                <span className="preview-time">
                                    ⏱ 08:42
                                </span>

                            </div>

                        </div>

                    </div>

                    <div className="floating-card score-float">

                        <div className="float-icon">
                            ✓
                        </div>

                        <div>
                            <strong>Excellent</strong>
                            <span>Answer evaluated</span>
                        </div>

                    </div>

                    <div className="floating-card ai-float">

                        <div className="ai-symbol">
                            AI
                        </div>

                        <div>
                            <strong>AI Feedback</strong>
                            <span>Instant analysis</span>
                        </div>

                    </div>

                </div>

            </section>

            {/* FEATURES */}
            <section className="features-section">

                <div className="section-heading">

                    <span className="section-label">
                        WHY INTERVIEWPRO
                    </span>

                    <h2>
                        Everything you need to
                        <span> ace your interview.</span>
                    </h2>

                    <p>
                        A complete interview preparation environment
                        designed to help you practice smarter.
                    </p>

                </div>

                <div className="feature-grid">

                    <div className="feature-card">

                        <div className="feature-icon purple">
                            ✦
                        </div>

                        <h3>
                            AI-Powered Evaluation
                        </h3>

                        <p>
                            Get instant feedback on your answers
                            and understand where you can improve.
                        </p>

                    </div>

                    <div className="feature-card">

                        <div className="feature-icon blue">
                            ◉
                        </div>

                        <h3>
                            Real Interview Practice
                        </h3>

                        <p>
                            Practice technical questions based on
                            your selected job role and difficulty.
                        </p>

                    </div>

                    <div className="feature-card">

                        <div className="feature-icon green">
                            ↗
                        </div>

                        <h3>
                            Track Your Progress
                        </h3>

                        <p>
                            Monitor your scores, interview history,
                            strengths and areas for improvement.
                        </p>

                    </div>

                </div>

            </section>

            {/* CTA */}
            <section className="cta-section">

                <div className="cta-content">

                    <span className="section-label">
                        READY TO IMPROVE?
                    </span>

                    <h2>
                        Turn practice into
                        <span> confidence.</span>
                    </h2>

                    <p>
                        Start your first mock interview today
                        and take one step closer to your dream job.
                    </p>

                    <button
                        className="primary-btn"
                        onClick={() => navigate("/setup")}
                    >
                        Start Your Interview →
                    </button>

                </div>

            </section>

            {/* FOOTER */}
            <footer className="footer">

                <div className="footer-logo">
                    <span className="logo-icon">AI</span>
                    InterviewPro
                </div>

                <p>
                    AI Interview Preparation & Mock Interview System
                </p>

                <span>
                    © 2026 InterviewPro
                </span>

            </footer>

        </div>
    );
}

export default Home;