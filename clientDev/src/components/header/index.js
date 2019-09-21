import React, { Fragment, useEffect, useState } from "react"
import { NavLink } from "react-router-dom"
import URLS from "../../routes/urls"
import M from 'materialize-css';
import { FaAlignJustify } from "react-icons/fa"


export default function Header(props) {

    useEffect(() => {
        var elems = document.querySelectorAll('.sidenav');
        let sideNav = M.Sidenav.init(elems);

        document.querySelector('#header .sidenav li').addEventListener('click', function () {
            sideNav[0].close()
        })

    }, [])

    return (
        <header id="header">
            <nav>
                <div className="nav-wrapper">
                    <NavLink to="/" className="brand-logo">SL DIVISIONS</NavLink>
                    <a href="#" data-target="mobile-demo" className="sidenav-trigger">
                        <FaAlignJustify />
                    </a>
                    <ul className="right hide-on-med-and-down">
                        <li><NavLink to={URLS.HOME}>HOME</NavLink></li>
                        <li><NavLink to={URLS.PROVINCES}>PROVINCES</NavLink></li>
                        <li><NavLink to={URLS.DISTRICTS}>DISTRICTS</NavLink></li>
                        <li><NavLink to={URLS.ABOUT_ME}>ABOUT PROJECT</NavLink></li>
                        <li><a className="btn light-blue accent-3" href={URLS.ADMIN}>ADMIN PANEL</a></li>
                    </ul>
                </div>
            </nav>

            <ul className="sidenav" id="mobile-demo">
                <li><NavLink to={URLS.HOME}>HOME</NavLink></li>
                <li><NavLink to={URLS.PROVINCES}>PROVINCES</NavLink></li>
                <li><NavLink to={URLS.DISTRICTS}>DISTRICTS</NavLink></li>
                <li><NavLink to={URLS.ABOUT_ME}>ABOUT ME</NavLink></li>
            </ul>
        </header>
    )
}