import React from "react"
import PropTypes from "prop-types"

function Title(props) {
    return (
        <div className="container">
            <div className="row" style={{ margin: "5px 0" }}>
                <div className="col s12">
                    <h1 className="center title">{props.titleName}</h1>
                </div>
            </div>
        </div>
    )
}

Title.propTypes = {
    titleName: PropTypes.string.isRequired
}

export default Title