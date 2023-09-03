import React, { Component } from 'react'
import Swal from 'sweetalert2';
import OperationsNav from '../operationsnav/OperationsNav';
import OperationsTab from '../operationstab/OperationsTab';
import './SubtractionLearning.css';

export default class SubtractionLearning extends Component {
    constructor(props){
        super(props);
        this.state = {
            firstNumber_subtractionLearning: Number(),
            secondNumber_subtractionLearning: Number(),
            result_subtractionLearning: ''
        };
        this.handleFirstNumber = this.handleFirstNumber.bind(this);
        this.handleSecondNumber = this.handleSecondNumber.bind(this);
        this.createResult = this.createResult.bind(this);
    }

    handleFirstNumber(e){
        this.setState({
            firstNumber_subtractionLearning: Number(e.target.value)
        });
    }

    handleSecondNumber(e){
        this.setState({
            secondNumber_subtractionLearning: Number(e.target.value)
        })
    }

    createResult(e){
        this.setState({
            result_subtractionLearning: this.state.firstNumber_subtractionLearning - this.state.secondNumber_subtractionLearning
        });
        Swal.fire({
            title: 'Aferin!',
            text: `${this.state.firstNumber_subtractionLearning} - ${this.state.secondNumber_subtractionLearning} = ${this.state.firstNumber_subtractionLearning - this.state.secondNumber_subtractionLearning}`,
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
            <div className="subtractionlearning" >
                <OperationsNav />
                <OperationsTab operationType="subtraction" />
                <form className="subtractionlearningForm" >
                    <div className="subtractionlearningInputGroup" >
                        <input type="text" className='subtractionlearningInput' onChange={this.handleFirstNumber} />
                        <span>-</span>
                        <input type="text" className='subtractionlearningInput' onChange={this.handleSecondNumber} />
                        <span>=</span>
                        <div className="subtractionlearningResult" >{this.state.result_subtractionLearning}</div>
                    </div>
                    <button type="submit" className="subtractionlearningButton buttonPrimary buttonPrimaryLarger" onClick={this.createResult} >Sonucu Gör</button>
                </form>
            </div>
        )
    }
}
