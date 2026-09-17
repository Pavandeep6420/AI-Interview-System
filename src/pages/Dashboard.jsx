import {
    useEffect,
    useState
} from "react";


import {
    useNavigate
} from "react-router-dom";


import {
    getHistory
} from "../api";


function Dashboard() {

    const navigate = useNavigate();


    const [history, setHistory] =
        useState([]);


    useEffect(() => {

        getHistory()

            .then((response) => {

                setHistory(
                    response.data
                );

            })

            .catch((error) => {

                console.error(error);

            });

    }, []);


    const totalInterviews =
        history.length;


    const scores = history

        .map(
            (item) =>
                Number(item.score || 0)
        )

        .filter(
            (score) =>
                score > 0
        );


    const averageScore =
        scores.length > 0

            ? (
                scores.reduce(
                    (a, b) => a + b,
                    0
                ) / scores.length
            ).toFixed(1)

            : 0;


    const bestScore =
        scores.length > 0

            ? Math.max(...scores).toFixed(1)

            : 0;


    return (

        <div className="page">

            <div className="dashboard-container">

                <div className="dashboard-header">

                    <div>

                        <div className="badge">
                            AI Interview Dashboard
                        </div>


                        <h1>
                            Your Interview Progress
                        </h1>


                        <p>
                            Track your interview
                            practice and improve
                            your performance.
                        </p>

                    </div>


                    <button
                        className="primary-btn"
                        onClick={() =>
                            navigate("/setup")
                        }
                    >
                        + New Interview
                    </button>

                </div>


                <div className="dashboard-stats">


                    <div className="dashboard-stat">

                        <div className="stat-icon">
                            🎤
                        </div>


                        <div>

                            <h2>
                                {totalInterviews}
                            </h2>

                            <p>
                                Total Interviews
                            </p>

                        </div>

                    </div>


                    <div className="dashboard-stat">

                        <div className="stat-icon">
                            📊
                        </div>


                        <div>

                            <h2>
                                {averageScore}
                            </h2>

                            <p>
                                Average Score
                            </p>

                        </div>

                    </div>


                    <div className="dashboard-stat">

                        <div className="stat-icon">
                            🏆
                        </div>


                        <div>

                            <h2>
                                {bestScore}
                            </h2>

                            <p>
                                Best Score
                            </p>

                        </div>

                    </div>


                </div>


                <div className="dashboard-section">


                    <div className="section-heading">

                        <h2>
                            Recent Interviews
                        </h2>


                        <button
                            onClick={() =>
                                navigate("/history")
                            }
                        >
                            View All →
                        </button>

                    </div>


                    {history.length === 0 ? (

                        <div className="dashboard-empty">

                            <h3>
                                No interviews yet
                            </h3>


                            <p>
                                Start your first
                                mock interview to
                                see your progress here.
                            </p>


                            <button
                                className="primary-btn"
                                onClick={() =>
                                    navigate("/setup")
                                }
                            >
                                Start Interview
                            </button>

                        </div>

                    ) : (

                        history
                            .slice(0, 5)
                            .map(
                                (item) => (

                                    <div
                                        className="dashboard-interview"
                                        key={item.id}
                                    >

                                        <div className="interview-icon">
                                            💼
                                        </div>


                                        <div className="interview-info">

                                            <h3>
                                                {item.role}
                                            </h3>


                                            <p>
                                                {item.name}
                                                {" • "}
                                                {item.difficulty}
                                            </p>

                                        </div>


                                        <div className="dashboard-score">

                                            {Number(
                                                item.score || 0
                                            ).toFixed(1)}
                                            /100

                                        </div>


                                        <div className="interview-date">

                                            {item.created_at}

                                        </div>

                                    </div>

                                )
                            )

                    )}

                </div>

            </div>

        </div>
    );
}


export default Dashboard;