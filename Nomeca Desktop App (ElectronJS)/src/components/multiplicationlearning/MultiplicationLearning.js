import React, { Component } from 'react';
import Swal from 'sweetalert2';
import OperationsNav from '../operationsnav/OperationsNav';
import OperationsTab from '../operationstab/OperationsTab';
import './MultiplicationLearning.css';

export default class MultiplicationLearning extends Component {
    constructor(props){
        super(props);
        this.state = {
            firstNumber_multiplicationLearning: Number(),
            secondNumber_multiplicationLearning: Number(),
            result_multiplicationLearning: ''
        };
        this.handleFirstNumber = this.handleFirstNumber.bind(this);
        this.handleSecondNumber = this.handleSecondNumber.bind(this);
        this.createResult = this.createResult.bind(this);
    }

    handleFirstNumber(e){
        this.setState({
            firstNumber_multiplicationLearning: Number(e.target.value)
        });
    }

    handleSecondNumber(e){
        this.setState({
            secondNumber_multiplicationLearning: Number(e.target.value)
        })
    }

    createResult(e){
        this.setState({
            result_multiplicationLearning: this.state.firstNumber_multiplicationLearning * this.state.secondNumber_multiplicationLearning
        });
        Swal.fire({
            title: 'Aferin!',
            text: `${this.state.firstNumber_multiplicationLearning} × ${this.state.secondNumber_multiplicationLearning} = ${this.state.firstNumber_multiplicationLearning * this.state.secondNumber_multiplicationLearning}`,
            icon: 'success',
            confirmButtonText: 'Devam et',
        }).then(result => {
            if (result.isConfirmed){
                window.location.reload()
            }
        })
        e.preventDefault();
    }

    render() {
        return (
            <div className="multiplicationlearning" >
                <OperationsNav />
                <OperationsTab operationType="multiplication" />
                <form className="multiplicationlearningForm" >
                    <div className="multiplicationlearningInputGroup" >
                        <input type="text" className='multiplicationlearningInput' onChange={this.handleFirstNumber} />
                        <span>×</span>
                        <input type="text" className='multiplicationlearningInput' onChange={this.handleSecondNumber} />
                        <span>=</span>
                        <div className="multiplicationlearningResult" >{this.state.result_multiplicationLearning}</div>
                    </div>
                    <button type="submit" className="multiplicationlearningButton buttonPrimary buttonPrimaryLarger" onClick={this.createResult} >Sonucu Gör</button>
                </form>
            </div>
        )
    }
}
