import React from 'react'
import { Link } from 'react-router-dom'
import one from '../images/1.png'
import two from '../images/2.png'
import three from '../images/3.png'
import walktroughVideo from '../video/walkthrough_edited.mp4'

import './Home.css'

const Home = () => {
    return (
        <>
            <div class="background-animation-container">
                <div class="background-animation color-1"></div>
                <div class="background-animation color-2"></div>
                <div class="background-animation color-3"></div>
            </div>

            <main role="main" class="main">
                <div class="hero-section bg-blur-light">
                    <div class="hero-left">
                        <div class="hero-title">TailScout</div>
                        <div class="hero-description">
                            TailScout is made with a purpose to create novel Engineered tail
                            proteins. It is first of its kind web application developed to
                            combat the menace created by the Multi-Drug Resistant pathogens. It
                            will allow you to detect different phage tails and thus create
                            engineered R-type pyocins with varying spectra of killing.
                        </div>
                        <div class="hero-buttons">
                            <Link to="/form">
                                <button type="button" class="btn btn-primary btn-lg">
                                    <i class="fas fa-bacterium"></i> Start Modelling
                                </button>
                            </Link>
                            <a href="https://github.com/igemsoftware2020/IIT_Roorkee_India">
                                <button type="button" class="btn btn-success btn-lg">
                                    <i class="fab fa-github"></i> Contribute
                                </button>
                            </a>
                        </div>
                    </div>
                    <div class="hero-right">
                        <video width="445" height="250" controls class="hero-video">
                            <source
                                src={walktroughVideo}
                                type="video/mp4"
                            />
                            Your browser does not support the video tag.
                        </video>
                        <div class="hero-video-description">Walkthrough</div>
                    </div>
                </div>

                <div class="chevron-container">
                    <div class="chevron"></div>
                    <div class="chevron"></div>
                    <div class="chevron"></div>
                </div>

                <div class="hero-spacer"></div>

                <div class="container marketing">
                    <div class="section-title">Get Started</div>
                    <div class="row feature-row">
                        <div class="col-lg-4 feature-box">
                            <div class="feature-step">1</div>
                            <img
                                src={one}
                                alt="Generic placeholder"
                                width="140"
                                height="140"
                            />
                            <h2>Tail Fibre Detection</h2>
                        </div>
                        <div class="col-lg-4 feature-box">
                            <div class="feature-step">2</div>
                            <img
                                src={two}
                                alt="Generic placeholder"
                                width="140"
                                height="140"
                            />
                            <h2>Multiple Sequence Alignment</h2>
                        </div>
                        <div class="col-lg-4 feature-box">
                            <div class="feature-step">3</div>
                            <img
                                src={three}
                                alt="Generic placeholder"
                                width="140"
                                height="140"
                            />
                            <h2>Protein Secondary Structure Prediction</h2>
                        </div>
                    </div>

                    <hr class="featurette-divider" />

                    <div class="row featurette">
                        <div class="col-md-7">
                            <h2 class="featurette-heading" id="step-1">Tail Fibre Detection</h2>
                            <p class="lead">
                                Tail Fibre Detection is a unique algorithm which helps the program
                                in searching for the most lytic phage tail from a pool of tail
                                fibers compiled using genome databases of Bacteriophages.
                            </p>
                        </div>
                        <div class="col-md-5 featurette-image-container">
                            <img
                                class="featurette-image img-fluid mx-auto"
                                src={one}
                                alt="Generic placeholder"
                            />
                        </div>
                    </div>

                    <hr class="featurette-divider" />

                    <div class="row featurette">
                        <div class="col-md-7 order-md-2">
                            <h2 class="featurette-heading" id="step-2">
                                Multiple Sequence Alignment
                            </h2>
                            <p class="lead">
                                This feature will help you in performing sequence alignment of all
                                the bacteriophages of the particular host bacteria so as to find
                                the region responsible for lytic activity of the particular phage.
                                This will in the end give you the sequence of the engineered
                                protein.
                            </p>
                        </div>
                        <div class="col-md-5 order-md-1 featurette-image-container">
                            <img
                                class="featurette-image img-fluid mx-auto"
                                src={two}
                                alt="Generic placeholder"
                            />
                        </div>
                    </div>

                    <hr class="featurette-divider" />

                    <div class="row featurette">
                        <div class="col-md-7">
                            <h2 class="featurette-heading" id="step-3">
                                Protein Secondary Structure Prediction
                            </h2>
                            <p class="lead">
                                Secondary structure protein prediction is one of most inportant
                                process in the program by which the engineered protein structure
                                is predicted using the predifeined Jnet algorithm of Jpred.
                            </p>
                        </div>
                        <div class="col-md-5 featurette-image-container">
                            <img
                                class="featurette-image img-fluid mx-auto"
                                src={three}
                                alt="Generic placeholder"
                            />
                        </div>
                    </div>

                    <hr class="featurette-divider" />

                </div>

            </main>
        </>
    )

}

export default Home