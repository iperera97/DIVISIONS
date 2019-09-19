import React from "react"
import PropTypes from "prop-types"
import { FaMapMarkerAlt } from "react-icons/fa";
import { NavLink } from "react-router-dom"
import URLS from "../../routes/urls"
import slugify from "../../helpers/slugify"

export default function PlaceBox(props) {

    let imgUrl = (props.imgUrl) ? `${SERVER_URL}/media/${props.imgUrl}` : `${SERVER_URL}/media/images/defaults/slplace.jpg`;
    let divClasName = `col ${props.divClasName} place-box`;

    let PAGE_URL = slugify(`${URLS.PROVINCES}/${props.englishName}`)

    return (
        <div className={divClasName}>
            <div className="card">
                <div className="card-image waves-effect waves-block waves-light">
                    <img className="activator" src={imgUrl} style={{ width: "100%", height: "200px" }} />
                </div>
                <div className="card-content">
                    <span className="card-title center">{props.englishName}</span>
                </div>
                <div className="card-action">
                    <div>
                        <NavLink to={PAGE_URL} className="btn light-blue darken-4">View More</NavLink>
                    </div>
                    <div className="right">
                        <a href={props.mapUrl} target="_blank">
                            <FaMapMarkerAlt size="2em" color="#008080" />
                        </a>
                    </div>
                </div>
            </div>
        </div>
    )
}

PlaceBox.propTypes = {
    imgUrl: PropTypes.string,
    id: PropTypes.number.isRequired,
    sinhalaName: PropTypes.string,
    englishName: PropTypes.string.isRequired,
    tamilName: PropTypes.string,
    divClasName: PropTypes.string.isRequired
}