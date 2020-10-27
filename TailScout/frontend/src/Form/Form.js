import { React, useState } from 'react'
import axios from 'axios'

import { API_JOBS } from "../api-links"
import './Form.css'
import loadingImg from '../images/loading.gif'

const Form = () => {

    const [formData, setFormData] = useState({
        bacteria: "acinetobacter baumannii",
        email_id: ""
    })
    const [err, setErr] = useState({
        err: false,
        errMsg: ""
    })
    const [resultsRecieved, setResultsRecieved] = useState({
        recieved: false,
        resultUrl: ""
    })
    const [loading, setLoading] = useState(false)

    const updateFormData = (event) => {
        setFormData((prevFormData) => ({
            ...prevFormData,
            [event.target.name]: event.target.value
        }))
    }

    const submitForm = (event) => {
        setLoading(true)
        event.preventDefault()
        axios.post(API_JOBS, formData)
            .then((res) => {
                setLoading(false)
                setResultsRecieved({
                    recieved: true,
                    resultUrl: res.data.url
                })
                updateErr(false, "")
                console.log(res)
            })
            .catch((err => {
                setLoading(false)
                updateErr(true, err.message)
                console.log(err)
            }))
    }

    const updateErr = (isErr, errMsg) => {
        setErr({
            err: isErr,
            errMsg: errMsg
        })
    }


    return (
        !resultsRecieved.recieved
            ? <div className="main-block" >
                <h1><b>Enter input parameters:</b></h1>
                <form action="/" onSubmit={submitForm}>
                    <label id="icon" for="name"><i className="fas fa-bacterium"></i></label>
                    {/* <input
                        type="text"
                        name="bacteria"
                        value={formData.bacteria}
                        onChange={updateFormData}
                        id="bacteria"
                        placeholder="Bacteria Name"
                        required
                    /> */}
                    <select
                        type="text"
                        id="bacteria"
                        name="bacteria"
                        value={formData.bacteria}
                        onChange={updateFormData}
                        placeholder="Bacteria Name"
                        required
                    >
                        <option value="acinetobacter baumannii" selected>Acinetobacter baumannii</option>
                        <option value="klebsiella pnuemoniae">Klebsiella pnuemoniae</option>
                        <option value="escherichia coli">Escherichia coli</option>
                        <option value="campylobacter jejuni">Campylobacter jejuni</option>
                    </select>
                    <br />
                    <label id="icon" for="name"><i className="fas fa-envelope"></i></label>
                    <input
                        type="text"
                        name="email_id"
                        value={formData.email_id}
                        onChange={updateFormData}
                        id="email_id"
                        placeholder="Email ID"
                        required
                    />
                    <br />
                    <div className="btn-block">
                        <button type="submit" href="/" disabled={loading}>
                            {
                                loading
                                    ? "Loading..."
                                    : "Submit"
                            }
                        </button>
                    </div>
                    {
                        loading && <img
                            src={loadingImg}
                            style={{ width: "50px" }}
                            alt="Loading GIF"
                        />
                    }
                    {
                        err.err && <h3 color="tomato">Error: {err.message} <br />Please try again later.</h3>
                    }
                </form>
            </div >
            : <h1>Result URL: <a href={resultsRecieved.resultUrl}>{resultsRecieved.resultUrl}</a></h1>
    )
}

export default Form
