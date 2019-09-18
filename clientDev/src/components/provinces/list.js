import React, { Component } from "react"
import PropTypes from "prop-types"
import { connect } from "react-redux"
import { getProvinceList } from "../../store/actions/province"


class ProvincesList extends Component {

    state = {
        'counter': 0
    }

    componentDidMount() {
        this.props.getProvinceList()
    }

    handler = () => {
        this.setState((prevState, props) => {
            return {
                'counter': prevState.counter + 1
            }
        })
    }

    render() {

        console.log('state', this.props)

        return (
            <div className="container">
                <div className="row">
                    <p onClick={this.handler}>list goes here</p>
                </div>
            </div>
        )
    }
}

const mapStateToProps = state => {
    return {
        "provinceList": state.provinceR.provinces_data
    }
}

const mapDispatchToProps = dispatch => {
    return {
        "getProvinceList": () => dispatch(getProvinceList())
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(ProvincesList)