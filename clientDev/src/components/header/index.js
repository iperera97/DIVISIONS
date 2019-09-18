import React, { Fragment, useEffect, useState } from "react"
import { NavLink } from "react-router-dom"
import URLS from "../../routes/urls"
import M from 'materialize-css';



export default function Header(props) {

    useEffect(() => {
        var elems = document.querySelectorAll('.sidenav');
        M.Sidenav.init(elems);
    }, [])

    return (
        <header>
            <nav>
                <div className="nav-wrapper">
                    <a href="#!" className="brand-logo">Logo</a>
                    <a href="#" data-target="mobile-demo" className="sidenav-trigger"><i className="material-icons">menu</i></a>
                    <ul className="right hide-on-med-and-down">
                        <li><NavLink to={URLS.HOME}>HOME</NavLink></li>
                        <li><NavLink to={URLS.PROVINCES}>PROVINCES</NavLink></li>
                        <li><NavLink to={URLS.DISTRICTS}>DISTRICTS</NavLink></li>
                        <li><NavLink to={URLS.CITIES}>CITIES</NavLink></li>
                        <li><NavLink to={URLS.ABOUT_ME}>ABOUT US</NavLink></li>
                    </ul>
                </div>
            </nav>

            <ul className="sidenav" id="mobile-demo">
                <li><a href="sass.html">Home</a></li>
                <li><a href="badges.html">Provinces</a></li>
                <li><a href="collapsible.html">Districts</a></li>
                <li><a href="mobile.html">City</a></li>
            </ul>
        </header>
    )
}