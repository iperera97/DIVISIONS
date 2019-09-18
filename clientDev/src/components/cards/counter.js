import React from "react"
import PropTypes from 'prop-types';
import "./css/counter.css"
import { NavLink } from "react-router-dom"

class Card extends React.Component {

    state = {
        start: 0
    }

    componentDidMount() {
        this.counter = setInterval(
            () => this.tick(),
            this.props.timeSec
        );
    }

    componentWillUnmount() {
        clearInterval(this.counter);
    }

    tick() {

        if (this.state.start == this.props.number) {
            clearInterval(this.counter);
        } else {
            this.setState((prevState) => {
                return {
                    'start': ++prevState.start
                }
            })
        }
    }

    render() {

        // check has more
        let startCounter = `${this.state.start} ${(this.props.more_numbers && this.state.start == this.props.number) ? "+" : ""}`
        let className = `card counter-block`
        let textColor = `${this.props.textColor}-text center counter-title`
        let btnColor = `${this.props.textColor} center btn`

        return (
            <div className={className}>
                <div className="card-content">
                    <h2 className={textColor}>{startCounter.replace(/\s/g, "")}</h2>
                </div>
                <div className="card-action">
                    <h4 className="center">{this.props.title}</h4>
                    <NavLink to={this.props.url} className={btnColor}>{this.props.btnValue}</NavLink>
                </div>
            </div >
        )
    }
}



Card.propTypes = {
    // required
    title: PropTypes.string.isRequired,
    number: PropTypes.number.isRequired,
    textColor: PropTypes.string.isRequired,
    url: PropTypes.string.isRequired,

    // optional
    more_numbers: PropTypes.bool,
    classNames: PropTypes.string,
}

export default Card