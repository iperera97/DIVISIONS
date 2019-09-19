import React from "react"
import { Switch, Route } from 'react-router'
import Home from "../components/home/index"
import ProvinceList from "../components/provinces/index"
import ProvinceDetail from "../components/provinces/detail"
import URLS from "./urls"


const MainRoute = (props) => {
    return (
        <Switch>
            <Route path={URLS.HOME} exact component={Home} />
            <Route path={URLS.PROVINCES} exact component={ProvinceList} />
            <Route path={URLS.DISTRICTS} component={Home} />
            <Route path={URLS.CITIES} component={Home} />
            <Route path={URLS.ABOUT_ME} component={Home} />

            <Route path={`${URLS.PROVINCES}/:province_en`} component={ProvinceDetail} />
        </Switch>
    )
}

export default MainRoute