import React, { Component } from 'react';
import './Home.css';

export default class App extends Component{
    constructor(props){
        super(props);
        this.state = {};
    }

    render(){
        return(
            <div className="home" >
                <h1>Nomeca'ya Hoşgeldiniz!</h1>
            </div>
        );
    }
}