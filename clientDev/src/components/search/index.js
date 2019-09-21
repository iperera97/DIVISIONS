import React from "react"
import { FaSearchengin } from "react-icons/fa"
import PropTypes from "prop-types"
import M from 'materialize-css';
import { withRouter } from "react-router";
import slugify from "../../helpers/slugify"

class SearchBox extends React.Component {

    state = {
        searchValue: null
    }

    generateData() {

        let textOnly = {}
        let textWithHref = {}

        this.props.data_source.map(eachData => {

            textOnly[eachData.englishName] = null
            textWithHref[eachData.englishName] = slugify(`${this.props.parentUrl}/${eachData.englishName}-${eachData.pk}`)
        })

        this.search_source = {
            textOnly,
            textWithHref
        }
    }

    componentDidMount() {
        var elem = document.getElementById('searchbox');

        // generate store
        this.generateData()

        this.searchInstance = M.Autocomplete.init(elem, {
            data: this.search_source.textOnly,
            onAutocomplete: (val) => {

                let textWithHref = this.search_source.textWithHref

                // value found
                if (textWithHref.hasOwnProperty(val)) {
                    let url = textWithHref[val]
                    this.props.history.push(url)
                }
            },
        });
    }

    getSearchInput = (event) => {
        //console.log(this.searchInstance)
    }

    render() {

        console.log('render', this.props.data_load_status)

        return (
            <div className="container" id="search-box">
                <div className="row">
                    <div className="col s12">
                        <div className="input-field col s12">
                            <FaSearchengin className="prefix" />
                            <input
                                type="text"
                                id="searchbox"
                                className="autocomplete"
                                onKeyUp={this.getSearchInput}
                                placeholder={this.props.findTitle} />
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

SearchBox.propTypes = {
    findTitle: PropTypes.string.isRequired,
    data_source: PropTypes.shape.isRequired,
    data_load_status: PropTypes.bool.isRequired,
    parentUrl: PropTypes.string.isRequired
}

export default withRouter(SearchBox)