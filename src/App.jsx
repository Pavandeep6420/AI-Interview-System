import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom";


import Home from "./pages/Home";
import Setup from "./pages/Setup";
import Interview from "./pages/Interview";
import Results from "./pages/Results";
import History from "./pages/History";
import Dashboard from "./pages/Dashboard";


import "./style.css";


function App() {

    return (

        <BrowserRouter>

            <Routes>

                <Route
                    path="/"
                    element={<Home />}
                />

                <Route
                    path="/setup"
                    element={<Setup />}
                />

                <Route
                    path="/interview"
                    element={<Interview />}
                />

                <Route
                    path="/results/:id"
                    element={<Results />}
                />

                <Route
                    path="/history"
                    element={<History />}
                />

                <Route
                    path="/dashboard"
                    element={<Dashboard />}
                />

            </Routes>

        </BrowserRouter>
    );
}


export default App;