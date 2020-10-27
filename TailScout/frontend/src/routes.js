
import React from "react"
import { Route, Switch } from "react-router-dom"

import Home from "./Home/Home"
import Form from "./Form/Form"
import Results from "./Results/Results"

const Router = (props) => {
    return (
        <Switch>
            <Route exact path="/form" component={Form} />
            <Route exact path="/results" component={Results} />
            <Route path="/" component={Home} />
        </Switch>
    )
}

export default Router