import React, { Component, Fragment } from "react"
import Title from "../title/index"
import { Redirect } from "react-router-dom"
import { BtnTags } from "../cards/tags"
import DetailInfo from "./detail-info"
import Loader from "react-loader-spinner"
import DistrictLinks from "../cards/placelinks"
import URLS from "../../routes/urls"
import "./css/detail.css"



export default class ProvinceDetail extends Component {

    state = {
        'data_obj_status': false,
        'data_obj_isLoading': true,
        'data_province': null,

        'data_relevent_districts': [],
        'data_relevet_districts_status': false
    }

    getProvinceDetails() {

        const PROVINCE_ID = this.props.match.params.province_en.split("-").pop()
        const API_URL = `/api/province/${PROVINCE_ID}/`

        fetch(API_URL).then(response => {

            if (response.ok) return response.json()
            else return Promise.reject(response.status)

        }).then(data => {

            // success
            this.setState({
                data_obj_status: true,
                data_obj_isLoading: false,
                data_province: data
            })

        }).catch(error => {

            // has errr
            this.setState({
                data_obj_isLoading: false,
            })

        });
    }

    releventDistricts() {

        const PROVINCE_ID = this.props.match.params.province_en.split("-").pop()
        const API_URL = `/api/province/relevet-districts/${PROVINCE_ID}/`

        fetch(API_URL).then(res => {

            if (res.ok) return res.json()
            else return Promise.reject(res.statusText)

        }).then(data => {

            this.setState({
                data_relevent_districts: data,
                data_relevet_districts_status: true,
            })

        }).catch(err => {
            this.setState({
                data_relevet_districts_status: false,
            })
        })
    }

    componentDidMount() {

        // request province data
        this.getProvinceDetails()

        // request relevent district
        this.releventDistricts()
    }


    render() {

        let btnTagData = []
        let image = ""

        let titleArr = this.props.match.params.province_en.split('-')
        titleArr.pop()
        let titleName = titleArr.join(' ')

        // if success
        if (this.state.data_obj_status) {

            btnTagData = [
                { 'key': '1', 'name': 'sinhala name', 'value': this.state.data_province.sinhalaName, 'color': 'cyan' },
                { 'key': '2', 'name': 'english name', 'value': this.state.data_province.englishName, 'color': 'light-blue' },
                { 'key': '3', 'name': 'tamil Name', 'value': this.state.data_province.tamilName, 'color': 'green' },
                { 'key': '4', 'name': 'area', 'value': this.state.data_province.area, 'color': 'indigo' },
                { 'key': '6', 'name': 'Google Map', 'href': this.state.data_province.mapUrl, 'color': 'indigo', hasIcon: true },
            ]

            image = this.state.data_province.featureImage

        }

        return (
            <Fragment>
                {(!this.state.data_obj_status && !this.state.data_obj_isLoading) ? <Redirect to="/404" /> : null}

                {/* title tag goes here */}
                <Title titleName={`${titleName} Province`} />

                {/* spinner loading */}
                {this.state.data_obj_isLoading && <div className="col s12 center">
                    <Loader type="ThreeDots" color="#01579b" height={150} width={150} />
                </div>}

                <div className="container" id="province-detail">

                    {/* btn tags goes here */}
                    <div className="row">
                        <div className="col s12">
                            {this.state.data_obj_status && <BtnTags btnData={btnTagData} googleMap={this.state.data_province.mapUrl} />}
                        </div>
                    </div>

                    {/* province detail goes here */}
                    <div className="row">
                        <div className="col s12 m9">
                            <div className="row">
                                <div className="col s12">
                                    {this.state.data_obj_status && <DetailInfo
                                        imageUrl={image}
                                        content={this.state.data_province.introduction} />}
                                </div>
                            </div>
                        </div>
                        <div className="col s12 m3">
                            {(this.state.data_obj_status && this.state.data_relevet_districts_status) ?
                                <DistrictLinks
                                    name="Districts"
                                    parentUrl={URLS.DISTRICTS}
                                    id="related_distrcits"
                                    links={this.state.data_relevent_districts} /> : null}
                        </div>
                    </div>

                </div>
            </Fragment>
        )
    }
}