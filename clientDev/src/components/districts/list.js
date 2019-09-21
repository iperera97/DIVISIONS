import React from "react"
import { connect } from "react-redux"
import { get_districtList } from "../../store/actions/districts"
import PlaceBox from "../cards/placebox"
import Loader from 'react-loader-spinner'
import slugify from "../../helpers/slugify"
import URLS from "../../routes/urls"
import Error from "../cards/error"
import Pagination from "react-js-pagination";



class DistrictList extends React.Component {

    state = {
        activePage: 1,
        obj_per_page: 6
    }

    componentDidMount() {
        this.props.get_district_list(this.state.obj_per_page)
    }

    handlePageChange = (pageNumber) => {

        let limit = this.props.district_list_pagination.limit;
        let offset = this.getLimitNoffSet(pageNumber)

        // set pageNumber
        this.setState({ activePage: pageNumber });

        // request page data
        this.props.get_district_list(limit, offset)

    }

    // calculate page offset (pagenum - 1) * objPerpage
    // 1 - 1 * 10 - first page offset
    // 2 - 1 * 10 - second
    // 3 - 1 * 10 - third
    getLimitNoffSet = (pageNumber) => (pageNumber - 1) * this.state.obj_per_page

    render() {

        let listBlock = null

        if (this.props.district_list_isLoading) {
            listBlock = <div className="col s12 center">
                <Loader type="ThreeDots" color="#01579b" height={100} width={100} />
            </div>
        } else {
            listBlock = this.props.district_list.map(district => {

                let PAGE_URL = slugify(`${URLS.DISTRICTS}/${district.englishName}-${district.pk}`)

                return <PlaceBox
                    pageUrl={PAGE_URL}
                    imgUrl={district.featureImage}
                    key={district.pk}
                    id={district.pk}
                    englishName={district.englishName}
                    mapUrl={district.mapUrl}
                    divClasName="s12 m4" />
            })
        }

        return (
            <div className="container">
                {!this.props.district_iist_status && (<div className="row">
                    <Error errName="Districts Not Found" />
                </div>)}
                <div className="row">
                    {listBlock}
                </div>
                <div className="row">
                    <Pagination
                        innerClass="pagination right"
                        activeClass="teal"
                        activeLinkClass="white-text"
                        activePage={this.state.activePage}
                        itemsCountPerPage={this.props.district_list_pagination.limit}
                        totalItemsCount={this.props.district_list_pagination.count}
                        onChange={this.handlePageChange}
                    />
                </div>
            </div>
        )
    }

}


const mapStateToProps = state => {
    return {
        district_list: state.districtR.district_list,
        district_iist_status: state.districtR.district_iist_status,
        district_list_isLoading: state.districtR.district_list_isLoading,
        district_list_pagination: state.districtR.district_list_pagination
    }
}

const mapActionsToProps = dispatch => {
    return {
        get_district_list: (limit = 0, offset = 0) => dispatch(get_districtList(limit, offset))
    }
}

export default connect(mapStateToProps, mapActionsToProps)(DistrictList)