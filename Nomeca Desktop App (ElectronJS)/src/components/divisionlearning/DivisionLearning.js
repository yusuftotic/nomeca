import React, { Component } from 'react';
import Swal from 'sweetalert2';
import OperationsNav from '../operationsnav/OperationsNav';
import OperationsTab from '../operationstab/OperationsTab';
import './DivisionLearning.css';

export default class DivisionLearning extends Component {
    constructor(props){
        super(props);
        this.state = {
            firstNumber_divisionLearning: Number(),
            secondNumber_divisionLearning: Number(),
            result_divisionLearning: ''
        };
        this.handleFirstNumber = this.handleFirstNumber.bind(this);
        this.handleSecondNumber = this.handleSecondNumber.bind(this);
        this.createResult = this.createResult.bind(this);
    }

    handleFirstNumber(e){
        this.setState({
            firstNumber_divisionLearning: Number(e.target.value)
        });
    }

    handleSecondNumber(e){
        this.setState({
            secondNumber_divisionLearning: Number(e.target.value)
        })
    }

    createResult(e){
        this.setState({
            result_divisionLearning: this.state.firstNumber_divisionLearning / this.state.secondNumber_divisionLearning
        });
        Swal.fire({
            title: 'Aferin!',
            text: `${this.state.firstNumber_divisionLearning} ÷ ${this.state.secondNumber_divisionLearning} = ${this.state.firstNumber_divisionLearning / this.state.secondNumber_divisionLearning}`,
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
            <div className="divisionlearning" >
                <OperationsNav />
                <OperationsTab operationType="division" />
                <form className="divisionlearningForm" >
                    <div className="divisionlearningInputGroup" >
                        <input type="text" className='divisionlearningInput' onChange={this.handleFirstNumber} />
                        <span>÷</span>
                        <input type="text" className='divisionlearningInput' onChange={this.handleSecondNumber} />
                        <span>=</span>
                        <div type="text" className="divisionlearningResult" >{this.state.result_divisionLearning}</div>
                    </div>
                    <button type="submit" className="divisionlearningButton buttonPrimary buttonPrimaryLarger" onClick={this.createResult} >Sonucu Gör</button>
                </form>
            </div>
        )
    }
}
