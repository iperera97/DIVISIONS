import React, { Component, Fragment } from "react"
import Title from "../title/index"
import { Redirect } from "react-router-dom"
import { BtnTags } from "../cards/tags"
import DetailInfo from "./detail-info"
import Loader from "react-loader-spinner"
import URLS from "../../routes/urls"
import slugify from "../../helpers/slugify"
import "./css/detail.css"



export default class DistrictDetails extends Component {

    state = {
        'data_obj_status': false,
        'data_obj_isLoading': true,
        'data_district': null,
    }

    getDistrictDetails() {

        const DISTRICT_ID = this.props.match.params.district_en.split("-").pop()
        const API_URL = `/api/district/${DISTRICT_ID}/`

        fetch(API_URL).then(response => {

            if (response.ok) return response.json()
            else return Promise.reject(response.status)

        }).then(data => {

            // success
            this.setState({
                data_obj_status: true,
                data_obj_isLoading: false,
                data_district: data
            })

        }).catch(error => {

            // has errr
            this.setState({
                data_obj_isLoading: false,
            })

        });
    }

    componentDidMount() {

        // request district data
        this.getDistrictDetails()

    }


    render() {


        let btnTagData = []
        let image = ""

        let titleArr = this.props.match.params.district_en.split('-')
        titleArr.pop()
        let titleName = titleArr.join(' ')

        // if success
        if (this.state.data_obj_status) {

            let provinceName = this.state.data_district.province.englishName;
            let provinceID = this.state.data_district.province.pk;

            btnTagData = [
                { 'key': '1', 'name': 'sinhala name', 'value': this.state.data_district.sinhalaName, 'color': ' teal lighten-1' },
                { 'key': '2', 'name': 'english name', 'value': this.state.data_district.englishName, 'color': 'teal lighten-1' },
                { 'key': '3', 'name': 'tamil Name', 'value': this.state.data_district.tamilName, 'color': 'teal lighten-1' },
                { 'key': '4', 'name': 'area', 'value': this.state.data_district.area, 'color': 'teal lighten-1' },
                {
                    'key': '5',
                    'name': 'Province',
                    'href': slugify(`${URLS.PROVINCES}/${provinceName}-${provinceID}`),
                    'color': 'teal lighten-1',
                    'value': `${this.state.data_district.province.englishName} Province`
                },
                { 'key': '6', 'name': 'Google Map', 'href': this.state.data_district.mapUrl, 'color': 'teal lighten-1', hasIcon: true },
            ]

            image = this.state.data_district.featureImage

        }

        return (
            <Fragment>
                {(!this.state.data_obj_status && !this.state.data_obj_isLoading) ? <Redirect to="/404" /> : null}

                {/* title tag goes here */}
                <Title titleName={`${titleName} District`} />

                {/* spinner loading */}
                {this.state.data_obj_isLoading && <div className="col s12 center">
                    <Loader type="ThreeDots" color="#01579b" height={150} width={150} />
                </div>}

                <div className="container" id="district-detail">

                    {/* btn tags goes here */}
                    <div className="row">
                        <div className="col s12">
                            {this.state.data_obj_status && <BtnTags btnData={btnTagData} />}
                        </div>
                    </div>

                    {/* district detail goes here */}
                    <div className="row">
                        <div className="col s12">
                            {this.state.data_obj_status && <DetailInfo
                                imageUrl={image}
                                content={this.state.data_district.introduction} />}
                        </div>
                    </div>

                </div>
            </Fragment>
        )
    }
}