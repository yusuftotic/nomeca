import React, { Component } from 'react';
import Swal from 'sweetalert2';
import OperationsNav from '../operationsnav/OperationsNav';
import OperationsTab from '../operationstab/OperationsTab';
import './SubtractionExamples.css';

export default class SubtractionExamples extends Component {
    constructor(props){
        super(props);
        this.state = {
            firstNumber_subtractionExamples: Number(),
            secondNumber_subtractionExamples: Number(),
            result_subtractionExamples: Number(),
            input_subtractionExamples: Number(),
            answerControl: Boolean()
        };
        this.handleInput = this.handleInput.bind(this);
        this.resultCheck = this.resultCheck.bind(this);
    }

    componentWillMount(){
        this.createNumbers();
    }

    createNumbers(){
        let firstNumber = Math.floor(Math.random() * 100);
        let secondNumber = Math.floor(Math.random() * 100);

        if (firstNumber < secondNumber){
            this.createNumbers();
        }
        else{
            this.setState({
                firstNumber_subtractionExamples: firstNumber,
                secondNumber_subtractionExamples: secondNumber
            }, this.createResult);
        }
    }

    createResult(){
        this.setState({
            result_subtractionExamples: this.state.firstNumber_subtractionExamples - this.state.secondNumber_subtractionExamples
        })
    }

    handleInput(e){
        this.setState({
            input_subtractionExamples: Number(e.target.value)
        });
    }

    resultCheck(e){
        if (this.state.result_subtractionExamples === this.state.input_subtractionExamples){
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
            <div className='subtractionexamples'>
                <OperationsNav />
                <OperationsTab operationType="subtraction" />
                <form className="subtractionexamplesForm" >
                    <div className="subtractionexamplesNumbers" >
                        <div className="subtractionexamplesFirstNumber" >{this.state.firstNumber_subtractionExamples}</div>
                        <span>-</span>
                        <div className="subtractionexamplesSecondNumber" >{this.state.secondNumber_subtractionExamples}</div>
                        <span>=</span>
                        <input type="text" className="subtractionexamplesResult" onChange={this.handleInput} />
                    </div>
                    <button type="submit" className="subtractionexamplesButton buttonPrimary buttonPrimaryLarger" onClick={this.resultCheck} >Kontrol Et</button>
                </form>
            </div>
        )
    }
}
