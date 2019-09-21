import React from "react"
import "./css/404.css"
import { NavLink } from "react-router-dom"

function Page404(props) {
    return (
        <div id="notfound">
            <div className="notfound">
                <div className="notfound-404">
                    <h1>Oops!</h1>
                    <h2>404 - The Page can't be found</h2>
                </div>
                <NavLink to="/">GO TO Homepage</NavLink>
            </div>
        </div>
    )
}

export default Page404