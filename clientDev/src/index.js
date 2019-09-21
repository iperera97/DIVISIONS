import React from "react"
import { render } from "react-dom"
import App from "./app"
import { BrowserRouter, HashRouter } from 'react-router-dom'
import { createStore, applyMiddleware, compose } from "redux"
import Reducers from "./store/reducers/index"
import { Provider } from "react-redux"
import thunk from 'redux-thunk'

// get dom root
const DOM_ROOT = document.getElementById('root')

// init store
const store = createStore(
    Reducers,
    compose(
        applyMiddleware(thunk),
        window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
    )
)

// react dom render
render(
    <Provider store={store}>
        <HashRouter>
            <App />
        </HashRouter>
    </Provider>, DOM_ROOT)
