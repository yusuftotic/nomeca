import React, { Component } from 'react';
import Swal from 'sweetalert2';
import OperationsNav from '../operationsnav/OperationsNav';
import OperationsTab from '../operationstab/OperationsTab';
import './AdditionExamples.css';

export default class AdditionExamples extends Component {
    constructor(props){
        super(props);
        this.state = {
            firstNumber_additionExamples: Math.floor(Math.random() * 100),
            secondNumber_additionExamples: Math.floor(Math.random() * 100),
            result_additionExamples: Number(),
            input_additionalExamples: Number(),
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
            result_additionExamples: this.state.firstNumber_additionExamples + this.state.secondNumber_additionExamples
        })
    }

    handleInput(e){
        this.setState({
            input_additionalExamples: Number(e.target.value)
        });
    }

    resultCheck(e){
        if (this.state.result_additionExamples === this.state.input_additionalExamples){
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
            <div className='additionexamples'>
                <OperationsNav />
                <OperationsTab operationType="addition" />
                <form className="additionexamplesForm" >
                    <div className="additionexamplesNumbers" >
                        <div className="additionexamplesFirstNumber" >{this.state.firstNumber_additionExamples}</div>
                        <span>+</span>
                        <div className="additionexamplesSecondNumber" >{this.state.secondNumber_additionExamples}</div>
                        <span>=</span>
                        <input type="text" className="additionexamplesResult" onChange={this.handleInput} />
                    </div>
                    <button type="submit" className="additionexamplesButton buttonPrimary buttonPrimaryLarger" onClick={this.resultCheck} >Kontrol Et</button>
                </form>
            </div>
        )
    }
}
