import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Analysis from "./pages/Analysis";

function App() {

    return (

        <Routes>

            <Route

                path="/"

                element={<Home />}

            />

            <Route

                path="/analysis/:ticker"

                element={<Analysis />}

            />

        </Routes>

    );

}

export default App;