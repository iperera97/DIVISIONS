import React from "react"
import CardCounter from "../cards/counter"

export default function Home(props) {

    return (
        <div className="container main">
            <div className="row" style={{ marginBottom: 0 }}>
                <div className="col s12">
                    <h1 className='title center cyan-text'>Sri Lanka Places</h1>
                </div>
            </div>
            <div className="row counter-parent">
                <div className="col s12 m4">
                    <CardCounter
                        number={9}
                        timeSec={100}
                        title="Provinces"
                        textColor="light-blue"
                        btnValue="view Provinces"
                        url="/provinces" />
                </div>
                <div className="col s12 m4">
                    <CardCounter
                        number={25}
                        timeSec={75}
                        title="Districts"
                        textColor="green"
                        btnValue="view Districts"
                        url="/districts" />
                </div>
                <div className="col s12 m4">
                    <CardCounter
                        number={1800}
                        more_numbers={true}
                        timeSec={5}
                        title="Cities"
                        textColor="deep-purple"
                        btnValue="view Cities"
                        url="/city" />
                </div>
            </div>
        </div>
    )

}