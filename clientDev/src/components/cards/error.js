import React from "react"

export default Error = (props) => {

    return (
        <div className="card-panel red darken-1 err" >
            <p className="center white-text">{props.errName}</p>
        </div>
    )
}