import React from "react"
import { Switch, Route } from 'react-router'
import Home from "../components/home/index"
import Provinces from "../components/provinces/index"
import URLS from "./urls"


const MainRoute = (props) => {
    return (
        <Switch>
            <Route path={URLS.HOME} exact component={Home} />
            <Route path={URLS.PROVINCES} component={Provinces} />
            <Route path={URLS.DISTRICTS} component={Home} />
            <Route path={URLS.CITIES} component={Home} />
            <Route path={URLS.ABOUT_ME} component={Home} />
        </Switch>
    )
}

export default MainRoute