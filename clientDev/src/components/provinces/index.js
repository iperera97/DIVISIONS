import React, { Fragment } from "react"
import Title from "../title/index"
import SearchBox from "../search/index"
import ProvinceList from "./list"
import { connect } from "react-redux"

function Provinces(props) {

    return (
        <Fragment>
            {/* title goes here */}
            <Title titleName="Provinces" />

            {/* search box goes here */}
            {props.data_load_status && <SearchBox
                findTitle="Search Province"
                data_source={props.data_source}
                data_load_status={props.data_load_status}
                parentUrl="provinces" />}

            {/* province list goes here */}
            <ProvinceList />
        </Fragment>
    )

}

const mapStateToProps = state => {
    return {
        'data_source': state.provinceR.provinces_data,
        'data_load_status': state.provinceR.status
    }
}

export default connect(mapStateToProps, null)(Provinces)