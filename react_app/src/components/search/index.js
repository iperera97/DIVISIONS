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
            minLength: 2,
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
        // has type value
        let typedValue = event.target.value

        // check has data on redux
        let hasValues = Object.keys(this.search_source.textOnly).filter(eachValue => {

            let lowerEachVal = eachValue.toLocaleLowerCase();
            let lowerTypedVale = typedValue.toLocaleLowerCase()

            if (lowerEachVal.includes(lowerTypedVale)) return true
            else return false
        })

        // if redux doesnt hav values => request data
        if (hasValues.length == 0) {

            fetch(`${this.props.endpoint}?englishName=${typedValue}`).then(res => {
                if (res.ok) return res.json()
                else return Promise.reject(res.statusText)

                // success
            }).then(data => {

                let textOnly = {}
                let textWithHref = {}

                data.map(eachData => {

                    textOnly[eachData.englishName] = null
                    textWithHref[eachData.englishName] = slugify(`${this.props.parentUrl}/${eachData.englishName}-${eachData.pk}`)
                })

                // set property
                this.search_source = {
                    textOnly,
                    textWithHref
                }

                // update data clips
                this.searchInstance.updateData(textOnly)

            }).catch(err => console.log(err))
        }
    }

    render() {

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
                                placeholder={this.props.findTitle}
                                autoComplete="off" />
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

SearchBox.propTypes = {
    findTitle: PropTypes.string.isRequired,
    data_load_status: PropTypes.bool.isRequired,
    parentUrl: PropTypes.string.isRequired
}

export default withRouter(SearchBox)