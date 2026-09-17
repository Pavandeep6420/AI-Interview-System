import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { getRoles, startInterview } from "../api";

function Setup() {

    const navigate = useNavigate();

    const [name, setName] = useState("");

    const [role, setRole] = useState("");

    const [difficulty, setDifficulty] =
        useState("Medium");

    const [roles, setRoles] = useState([]);

    const [loading, setLoading] =
        useState(false);

    const [error, setError] =
        useState("");


    useEffect(() => {

        loadRoles();

    }, []);


    const loadRoles = async () => {

        try {

            const response = await getRoles();

            setRoles(
                response.data.roles
            );

        } catch (error) {

            setError(
                "Unable to load technical roles."
            );
        }
    };


    const handleSubmit = async (e) => {

        e.preventDefault();

        setError("");

        if (!name.trim()) {

            setError(
                "Please enter your name."
            );

            return;
        }

        if (!role) {

            setError(
                "Please select a technical role."
            );

            return;
        }

        try {

            setLoading(true);

            const response =
                await startInterview({

                    name: name.trim(),

                    role: role,

                    difficulty: difficulty
                });


            sessionStorage.setItem(
                "interview",
                JSON.stringify(
                    response.data
                )
            );


            navigate("/interview");

        } catch (error) {

            setError(
                error.response?.data?.error ||
                "Unable to start interview."
            );

        } finally {

            setLoading(false);
        }
    };


    return (

        <div className="setup-page">

            <div className="setup-card">

                <div className="setup-header">

                    <span className="setup-badge">
                        MOCK INTERVIEW
                    </span>

                    <h1>
                        Configure Your Interview
                    </h1>

                    <p>
                        Select your technical role
                        and difficulty level.
                    </p>

                </div>


                <form
                    onSubmit={handleSubmit}
                    className="setup-form"
                >

                    <div className="form-group">

                        <label>
                            Candidate Name
                        </label>

                        <input
                            type="text"
                            placeholder="Enter your name"
                            value={name}
                            onChange={(e) =>
                                setName(
                                    e.target.value
                                )
                            }
                        />

                    </div>


                    <div className="form-group">

                        <label>
                            Technical Role
                        </label>

                        <select
                            value={role}
                            onChange={(e) =>
                                setRole(
                                    e.target.value
                                )
                            }
                        >

                            <option value="">
                                Select Technical Role
                            </option>

                            {roles.map(
                                (item) => (

                                    <option
                                        key={item}
                                        value={item}
                                    >
                                        {item}
                                    </option>

                                )
                            )}

                        </select>

                    </div>


                    <div className="form-group">

                        <label>
                            Difficulty Level
                        </label>

                        <div className="difficulty-options">

                            {[
                                "Easy",
                                "Medium",
                                "Hard"
                            ].map(
                                (level) => (

                                    <button
                                        type="button"
                                        key={level}
                                        className={
                                            difficulty === level
                                                ? "difficulty active"
                                                : "difficulty"
                                        }
                                        onClick={() =>
                                            setDifficulty(
                                                level
                                            )
                                        }
                                    >
                                        {level}
                                    </button>

                                )
                            )}

                        </div>

                    </div>


                    <div className="question-info">

                        <strong>
                            Smart Question Bank
                        </strong>

                        <p>
                            You will receive 10
                            relevant technical
                            questions based on
                            your selected role
                            and difficulty.
                        </p>

                    </div>


                    {error && (

                        <div className="error-message">
                            {error}
                        </div>

                    )}


                    <button
                        type="submit"
                        className="primary-btn"
                        disabled={loading}
                    >

                        {loading
                            ? "Generating 10 Questions..."
                            : "Start Interview"
                        }

                    </button>

                </form>

            </div>

        </div>
    );
}

export default Setup;