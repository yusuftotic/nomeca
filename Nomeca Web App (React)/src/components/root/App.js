import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';

import LeftMenu from '../leftmenu/LeftMenu';
import Home from '../home/Home';
import Operations from '../operations/Operations';
import Addition from '../addition/Addition';
import AdditionLearning from '../additionlearning/AdditionLearning';
import AdditionExamples from '../additionexamples/AdditionExamples';
import Subtraction from '../subtraction/Subtraction';
import SubtractionLearning from '../subtractionlearning/SubtractionLearning';
import SubtractionExamples from '../subtractionexamples/SubtractionExamples';
import Multiplication from '../multiplication/Multiplication';
import MultiplicationLearning from '../multiplicationlearning/MultiplicationLearning';
import MultiplicationExamples from '../multiplicationexamples/MultiplicationExamples';
import Division from '../division/Division';
import DivisionLearning from '../divisionlearning/DivisionLearning';
import DivisionExamples from '../divisionexamples/DivisionExamples';
import Numbers from '../numbers/Numbers';
import Days from '../days/Days';
import Months from '../months/Months';

import './App.css';

export default class App extends Component {
    constructor(props){
        super(props);
        this.state = {};
    }

    render() {
        return(
            <div className="app" >
                <LeftMenu />
                <Switch>
                    <Route 
                    exact 
                    path="/" 
                    render={props =>(
                        <Home {...props} />
                    )} 
                    />
                    <Route exact path="/operations" component={Operations} />
                    <Route exact path="/operations/addition" component={Addition} />
                    <Route exact path="/operations/addition/learning" component={AdditionLearning} />
                    <Route exact path="/operations/addition/examples" component={AdditionExamples} />
                    <Route exact path="/operations/subtraction" component={Subtraction} />
                    <Route exact path="/operations/subtraction/learning" component={SubtractionLearning} />
                    <Route exact path="/operations/subtraction/examples" component={SubtractionExamples} />
                    <Route exact path="/operations/multiplication" component={Multiplication} />
                    <Route exact path="/operations/multiplication/learning" component={MultiplicationLearning} />
                    <Route exact path="/operations/multiplication/examples" component={MultiplicationExamples} />
                    <Route exact path="/operations/division" component={Division} />
                    <Route exact path="/operations/division/learning" component={DivisionLearning} />
                    <Route exact path="/operations/division/examples" component={DivisionExamples} />

                    <Route exact path="/numbers" component={Numbers} />
                    
                    <Route exact path="/days" component={Days} />

                    <Route exact path="/months" component={Months} />
                </Switch>
            </div>
        );
    }
}
