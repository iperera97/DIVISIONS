import React from "react"
import CardCounter from "../cards/counter"
import { NavLink } from "react-router-dom"
import URLS from "../../routes/urls"
import Title from "../title/index"

export default function Home(props) {

    return (
        <div className="container main">
            <div className="row" style={{ marginBottom: 0 }}>
                <div className="col s12">
                    <Title titleName="Sri Lanka Divisions" />
                </div>
                <div className="col s12">
                    <p className="sub-title">Sri Lanka is divided into <NavLink to={URLS.PROVINCES} className="bold">9 provinces</NavLink>,
                    which are further subdivided into <NavLink to={URLS.DISTRICTS} className="bold">25 Districts</NavLink>s.
                                                                Districts are further subdivided into Municipalities, of which are sorted into three categories. Each municipality is divided into Wards and wards
                    into Grama Niladhari divisions.</p>
                </div>
            </div>
            <div className="row counter-parent">
                <div className="col s12 m2"></div>
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
                        timeSec={100}
                        title="Districts"
                        textColor="green"
                        btnValue="view Districts"
                        url="/districts" />
                </div>
                <div className="col s12 m2"></div>
                {/* <div className="col s12 m4">
                    <CardCounter
                        number={1800}
                        more_numbers={true}
                        timeSec={5}
                        title="Cities"
                        textColor="deep-purple"
                        btnValue="view Cities"
                        url="/city" />
                </div> */}
            </div>
            <div className="row">
                <div className="col s12">
                    <h4>History,</h4>
                    <p style={{ fontSize: "18px" }}>
                        The country was first divided into several administrative units during the Anuradhapura
                        Kingdom. The kingdom was divided into three provinces; Rajarata, Ruhuna and Malaya Rata.
                        These were further subdivided into smaller units called <span className="bold">rata.</span> Over time, the number of
                        provinces increased, but the second-level administrative division continued to be the rata.
                        However, with the country eventually being divided into more than one kingdom and with foreign
                        colonial missions landing and taking parts of the country under their control, this structure began to change.
                        The territory of the Kotte Kingdom was organized into four disavas, which were further subdivided into forty korales.
                        The korales had their own civil and military officials with a small militia. The Jaffna kingdom appears to have
                        had a similar administrative structure to this with <span className="bold">four provinces.</span> When the Portuguese took over parts of the
                        country after their arrival in <span className="bold">1505</span>, they maintained more or less the same administrative structure followed by Sri
                        Lankan rulers.[4] During the Dutch rule in the country, the terrain under their control was divided into three
                        administrative divisions. These were subdivided into disavas as in earlier systems. The British initially continued
                        this system, but following reforms in 1796 to 1802, the country was divided according to ethnic composition.
                        This was abolished by the Colebrook–Cameron reforms in 1833 and a legislative council was created, making the island
                        a politically and administratively single unit. Five provinces were created, later expanded into nine, and these were
                        subdivided into twenty-one districts. These districts were administered by officials known as Government Agents or
                        Assistant Government Agents. In 1955, the district replaced the province as the country's main
                        administrative unit. Ampara District was created in April 1961, followed by the creation of
                        Mullaitivu and Gampaha districts in September <span className="bold">1978</span> through a new constitution, which also reintroduced the
                        province as the main administrative unit. The last district to be created was Kilinochchi in February 1984,
                         and the current constitution (that of 1978) states that the territory of Sri Lanka consists of 25 administrative
                        districts. These districts may be subdivided or amalgamated by a resolution of the Parliament of Sri Lanka.
                    </p>
                </div>
            </div>
        </div>
    )

}