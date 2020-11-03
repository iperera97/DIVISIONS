import React, { Fragment } from "react"


export default function Footer(props) {

    return (
        <footer className="page-footer">
            <div className="container">
                <div className="row">
                    <div className="col l6 s12">
                        <h5 className="white-text">SL DIVISIONS</h5>
                    </div>
                    <div className="col l4 offset-l2 s12">
                        <h5 className="white-text">Hi i'M ISURU</h5>
                        <ul>
                            <li>
                                <a className="grey-text text-lighten-3" target="_blank" href="https://github.com/waex97">Github - https://github.com/waex97</a>
                            </li>
                            <li>
                                <a className="grey-text text-lighten-3" href="mailto:isurumahesh97@gmail.com">isurumahesh97@gmail.com</a>
                            </li>
                            <li>
                                <a target="_blank" href="/adminpanel" target="_blank" className="white-text">Admin panel</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
            <div className="footer-copyright">
                <div className="container">
                    ©{new Date().getFullYear()} Srilankan Division App
                </div>
            </div>
        </footer>
    )
}