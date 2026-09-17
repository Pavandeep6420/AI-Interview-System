import {
    useEffect,
    useState
} from "react";


import {
    getHistory
} from "../api";


function History() {

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


    return (

        <div className="page">

            <div className="history-container">

                <div className="badge">
                    Your Progress
                </div>


                <h1>
                    Interview History
                </h1>


                <p className="subtitle">
                    Review your previous
                    interview sessions.
                </p>


                {history.length === 0 ? (

                    <div className="empty">

                        No interviews
                        completed yet.

                    </div>

                ) : (

                    history.map(
                        (item) => (

                            <div
                                className="history-card"
                                key={item.id}
                            >

                                <div>

                                    <h3>
                                        {item.role}
                                    </h3>

                                    <p>
                                        {item.name}
                                    </p>

                                </div>


                                <div>

                                    <span>
                                        {item.difficulty}
                                    </span>


                                    <p>
                                        Score:{" "}
                                        {Number(
                                            item.score
                                        ).toFixed(1)}
                                        / 100
                                    </p>


                                    <p>
                                        {item.created_at}
                                    </p>

                                </div>

                            </div>

                        )
                    )

                )}

            </div>

        </div>
    );
}


export default History;