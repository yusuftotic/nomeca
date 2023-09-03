import React, { Component } from 'react'
import Swal from 'sweetalert2';
import OperationsNav from '../operationsnav/OperationsNav';
import OperationsTab from '../operationstab/OperationsTab';
import './AdditionLearning.css';

export default class AdditionLearning extends Component {
    constructor(props){
        super(props);
        this.state = {
            firstNumber_additionLearning: Number(),
            secondNumber_additionLearning: Number(),
            result_additionLearning: ''
        };
        this.handleFirstNumber = this.handleFirstNumber.bind(this);
        this.handleSecondNumber = this.handleSecondNumber.bind(this);
        this.createResult = this.createResult.bind(this);
    }

    handleFirstNumber(e){
        this.setState({
            firstNumber_additionLearning: Number(e.target.value)
        });
    }

    handleSecondNumber(e){
        this.setState({
            secondNumber_additionLearning: Number(e.target.value)
        })
    }

    createResult(e){
        this.setState({
            result_additionLearning: this.state.firstNumber_additionLearning + this.state.secondNumber_additionLearning
        });
        Swal.fire({
            title: 'Aferin!',
            text: `${this.state.firstNumber_additionLearning} + ${this.state.secondNumber_additionLearning} = ${this.state.firstNumber_additionLearning + this.state.secondNumber_additionLearning}`,
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
            <div className="additionlearning" >
                <OperationsNav />
                <OperationsTab operationType="addition" />
                <form className="additionlearningForm" >
                    <div className="additionlearningInputGroup" >
                        <input type="text" className='additionlearningInput' onChange={this.handleFirstNumber} />
                        <span>+</span>
                        <input type="text" className='additionlearningInput' onChange={this.handleSecondNumber} />
                        <span>=</span>
                        <div type="text" className="additionlearningResult" >{this.state.result_additionLearning}</div>
                    </div>
                    <button type="submit" className="additionlearningButton buttonPrimary buttonPrimaryLarger" onClick={this.createResult} >Sonucu Gör</button>
                </form>
            </div>
        )
    }
}
