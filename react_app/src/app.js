import React, { Component, Fragment } from "react"
import Header from "./components/header/index"
import Footer from "./components/footer/index"
import 'materialize-css/dist/css/materialize.min.css';
import "./assets/common.css"
import "animate.css"
import MainRoutes from "./routes/main"

export default class App extends Component {

    render() {
        return (
            <Fragment>
                <Header />

                {/* main routes goes here */}
                <MainRoutes />

                <Footer />
            </Fragment>
        )
    }
}