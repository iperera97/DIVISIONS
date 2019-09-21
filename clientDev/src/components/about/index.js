import React from "react"

export default (props) => {

    return (
        <div className="container" id="about">
            <div className="row">
                <div className="col s12" style={{ margin: "20px 10px 10px 10px" }}>
                    <p className="title center" style={{ fontSize: "20px" }}>
                        <span className="bold">Hi I'm ISURU MAHESH,</span> I created this project for View Srilankan Provinces and Districts</p>
                </div>
                <div className="col s12 m2"></div>
                <div className="col s12 m8">
                    <h4 className="title center">Technologies i have used</h4>
                    <ul className="collection tech">
                        <li className="collection-item">
                            <span>Client Side</span>
                            <span className="btn light-blue">React &amp; Redux</span>
                        </li>
                        <li className="collection-item">
                            <span>Backend Side</span>
                            <span className="btn teal">Django &amp; RestFramework</span>
                        </li>
                        <li className="collection-item">
                            <span>Deployment Platform</span>
                            <span className="btn deep-purple">Heroku</span>
                        </li>
                    </ul>
                </div>
                <div className="col s12 m2"></div>
            </div>
            <div className="row">
                <div className="col s12 m2"></div>
                <div className="col s12 m8" style={{ marginBottom: '150px' }}>
                    <ul className="collection social">
                        <li className="collection-item">
                            <span>Github URL</span>
                            <span className="btn light-blue">
                                <a
                                    target="_blank"
                                    href="https://github.com/waex97/PUBLIC-PLACES"
                                    className="white-text">https://github.com/waex97/PUBLIC-PLACES</a>
                            </span>
                        </li>
                        <li className="collection-item">
                            <span>Email</span>
                            <span className="btn light-blue">
                                <a
                                    target="_blank"
                                    href="mailto:isurumahesh97@gmail.com"
                                    className="white-text">isurumahesh97@gmail.com</a>
                            </span>
                        </li>
                        <li className="collection-item">
                            <span>Admin Panel</span>
                            <span className="btn blue-grey">
                                <a
                                    target="_blank"
                                    href="/admin"
                                    className="white-text">Admin panel</a>
                            </span>
                        </li>
                    </ul>
                </div>
                <div className="col s12 m2"></div>
            </div>
        </div>
    )
}