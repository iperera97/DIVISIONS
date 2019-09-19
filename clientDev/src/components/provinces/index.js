import React, { Fragment } from "react"
import Title from "../title/index"
import ProvinceList from "./list"

export default function Provinces(props) {
    return (
        <Fragment>
            <Title titleName="Provinces" />
            <ProvinceList />
        </Fragment>
    )

}