import React from "react"
import { Switch, Route } from 'react-router'
import Home from "../components/home/index"
import ProvinceList from "../components/provinces/index"
import ProvinceDetail from "../components/provinces/detail"
import DistrictList from "../components/districts/index"
import DistrictDetail from "../components/districts/detail"
import About from "../components/about/index"
import Page404 from "../components/errPages/404"
import URLS from "./urls"


const MainRoute = (props) => {
    return (
        <Switch>
            <Route path={URLS.HOME} exact component={Home} />
            <Route path={URLS.PROVINCES} exact component={ProvinceList} />
            <Route path={URLS.DISTRICTS} exact component={DistrictList} />
            <Route path={URLS.ABOUT_ME} component={About} />

            <Route path={`${URLS.PROVINCES}/:province_en`} component={ProvinceDetail} />
            <Route path={`${URLS.DISTRICTS}/:district_en`} component={DistrictDetail} />

            <Route component={Page404} />
        </Switch>
    )
}

export default MainRoute