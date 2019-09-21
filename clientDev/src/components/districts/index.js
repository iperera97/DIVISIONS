import React, { Fragment } from "react"
import Title from "../title/index"
import List from "./list"
import SearchBox from "../search/index"
import { connect } from "react-redux"


function District(props) {

    return (
        <Fragment>
            {/* title goes here */}
            <Title titleName="Districts" />

            {/* search box goes here */}
            {props.data_load_status && <SearchBox
                findTitle="Search District"
                data_source={props.data_source}
                data_load_status={props.data_load_status}
                parentUrl="districts"
                endpoint="/api/district/find/" />}

            {/* list goes here */}
            <List />
        </Fragment>
    )

}

const mapStateToProps = state => {

    return {
        'data_source': state.districtR.district_list,
        'data_load_status': state.districtR.district_iist_status
    }
}

export default connect(mapStateToProps, null)(District)