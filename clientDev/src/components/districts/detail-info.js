import React from "react"

export default (props) => {

    let imageUrl = props.imageUrl.trim()
    let image = "";

    // set default image
    if (imageUrl === "" || imageUrl === null) image = `${SERVER_URL}/media/images/defaults/slplace.jpg`
    else image = `${SERVER_URL}/media/${imageUrl}`

    return (
        <div className="card">
            <div className="card-content white-text">
                <img src={image} id="banner" alt="province-img" />
                <div id="introduction">
                    <p className="black-text">{props.content}</p>
                </div>
            </div>
        </div>
    )
}