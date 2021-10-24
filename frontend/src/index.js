import React from "react"
import ReactDom from "react-dom"

import App from "./components/App.js";

let myComponent = document.getElementById("app")
if (myComponent !== null){
    ReactDom.render(<App />, myComponent)
}
