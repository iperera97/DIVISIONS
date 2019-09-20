import React, { Fragment } from "react"
import PropTypes from "prop-types"
import { NavLink } from "react-router-dom"
import slugify from "../../helpers/slugify"

export default function PlaceLInks(props) {

    console.log('props', props)


    return (
        <Fragment>
            <h4 className="center blue-grey darken-3 white-text" style={{ 'marginTop': 0, 'padding': '10px 5px' }}>{props.name}</h4>
            <ul className="collection" id={props.id}>
                {props.links.map(link => {

                    let url = slugify(`${props.parentUrl}/${link.englishName}-${link.pk}`);

                    return (
                        <li key={link.pk} className="collection-item center">
                            <button className="btn btn-small blue-grey">
                                <NavLink className="white-text" to={url}>{link.englishName}</NavLink>
                            </button>
                        </li>
                    )
                })}
            </ul>
        </Fragment >
    )
}

PlaceLInks.propTypes = {
    id: PropTypes.string.isRequired,
    name: PropTypes.string.isRequired,
}