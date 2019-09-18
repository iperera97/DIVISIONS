import React from "react"
import { render } from "react-dom"
import App from "./app"
import 'materialize-css/dist/css/materialize.min.css';
import { BrowserRouter, HashRouter } from 'react-router-dom'


// get dom root
const DOM_ROOT = document.getElementById('root')

// react dom render
render(
    <HashRouter>
        <App />
    </HashRouter>, DOM_ROOT)
