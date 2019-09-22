// import React from "react"
// import { FaMapMarkerAlt } from "react-icons/fa";


// export const BtnTags = (props) => {

//     console.log(props)

//     return (
//         <div className="btn-tags">
//             {props.btnData.map(btn => {

//                 let className = `btn ${btn.color} waves-effect waves-light`
//                 let value = `${btn.name.toUpperCase()} -  ${btn.value}`

//                 return <button
//                     className={className}
//                     key={btn.key}>
//                     {value}
//                 </button>
//             })}
//             <button className="btn">
//                 <a className="white-text" target="_blank" href={props.googleMap}><FaMapMarkerAlt /></a>
//             </button>
//         </div>
//     )
// }