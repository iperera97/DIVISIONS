import React from "react"
import { FaMapMarkerAlt } from "react-icons/fa";
import { NavLink } from "react-router-dom"


export const BtnTags = (props) => {

    return (
        <div className="btn-tags">
            {props.btnData.map(btn => {

                //console.log('has href n href', btn.hasOwnProperty('href') && btn.hasOwnProperty('value'))
                console.log(btn.hasOwnProperty('value') && btn.hasOwnProperty('href'), btn)

                let className = `btn ${btn.color} waves-effect waves-light animated zoomIn`
                let value = `${btn.name.toUpperCase()} -  ${btn.value}`

                // only has icon and href just display it (map icon)
                if (btn.hasOwnProperty("hasIcon") && btn.hasOwnProperty("href")) {
                    return <button className={className} key={btn.key}>
                        <a className="white-text" target="_blank" href={btn.href}><FaMapMarkerAlt /></a>
                    </button>

                    // only has value and href display it
                } else if (btn.hasOwnProperty("value") && btn.hasOwnProperty("href")) {

                    console.log('has')

                    return <button className={className} key={btn.key}>
                        <NavLink className="white-text" to={btn.href}>{btn.value}</NavLink>
                    </button>

                    // default
                } else {
                    return <button
                        className={className}
                        key={btn.key}>
                        {value}
                    </button>
                }

            })}
        </div >
    )
}