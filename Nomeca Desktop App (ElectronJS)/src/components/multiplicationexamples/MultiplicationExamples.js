import React, { Component } from 'react';
import Swal from 'sweetalert2';
import OperationsNav from '../operationsnav/OperationsNav';
import OperationsTab from '../operationstab/OperationsTab';
import './MultiplicationExamples.css';

export default class MultiplicationExamples extends Component {
    constructor(props){
        super(props);
        this.state = {
            firstNumber_multiplicationExamples: Math.floor(Math.random() * 11),
            secondNumber_multiplicationExamples: Math.floor(Math.random() * 11),
            result_multiplicationExamples: Number(),
            input_multiplicationExamples: Number(),
            answerControl: Boolean()
        };
        this.handleInput = this.handleInput.bind(this);
        this.resultCheck = this.resultCheck.bind(this);
    }

    componentWillMount(){
        this.createResult();
    }

    createResult(){
        this.setState({
            result_multiplicationExamples: this.state.firstNumber_multiplicationExamples * this.state.secondNumber_multiplicationExamples
        })
    }

    handleInput(e){
        this.setState({
            input_multiplicationExamples: Number(e.target.value)
        });
    }

    resultCheck(e){
        if (this.state.result_multiplicationExamples === this.state.input_multiplicationExamples){
            this.setState({
                answerControl: true
            })
            Swal.fire({
                title: 'Aferin!',
                text: 'Çok iyi gidiyorsun.',
                icon: 'success',
                confirmButtonText: 'Devam et',
            }).then(result => {
                if (result.isConfirmed){
                    window.location.reload()
                }
            })
        }
        else{
            this.setState({
                answerControl: false
            })
            Swal.fire({
                title: 'Bilemedin!',
                text: 'Tekrar denemelisin.',
                icon: 'error',
                confirmButtonText: 'Tekrar Dene!'
            })
        }

        e.preventDefault();
    }

    render() {
        return (
            <div className='multiplicationexamples'>
                <OperationsNav />
                <OperationsTab operationType="multiplication" />
                <form className="multiplicationexamplesForm" >
                    <div className="multiplicationexamplesNumbers" >
                        <div className="multiplicationexamplesFirstNumber" >{this.state.firstNumber_multiplicationExamples}</div>
                        <span>×</span>
                        <div className="multiplicationexamplesSecondNumber" >{this.state.secondNumber_multiplicationExamples}</div>
                        <span>=</span>
                        <input type="text" className="multiplicationexamplesResult" onChange={this.handleInput} />
                    </div>
                    <button type="submit" className="multiplicationexamplesButton buttonPrimary buttonPrimaryLarger" onClick={this.resultCheck} >Kontrol Et</button>
                </form>
            </div>
        )
    }
}
