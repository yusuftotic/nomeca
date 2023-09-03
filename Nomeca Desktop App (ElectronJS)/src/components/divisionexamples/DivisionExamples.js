import React, { Component } from 'react';
import Swal from 'sweetalert2';
import OperationsNav from '../operationsnav/OperationsNav';
import OperationsTab from '../operationstab/OperationsTab';
import './DivisionExamples.css';

export default class DivisionExamples extends Component {
    constructor(props){
        super(props);
        this.state = {
            firstNumber_divisionExamples: Number(),
            secondNumber_divisionExamples: Number(),
            result_divisionExamples: Number(),
            input_divisionExamples: Number(),
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
        else if (!Number.isInteger(firstNumber / secondNumber)){
            this.createNumbers();
        }
        else{
            this.setState({
                firstNumber_divisionExamples: firstNumber,
                secondNumber_divisionExamples: secondNumber
            }, this.createResult);
        }
    }

    createResult(){
        this.setState({
            result_divisionExamples: this.state.firstNumber_divisionExamples / this.state.secondNumber_divisionExamples
        })
    }

    handleInput(e){
        this.setState({
            input_divisionExamples: Number(e.target.value)
        });
    }

    resultCheck(e){
        if (this.state.result_divisionExamples === this.state.input_divisionExamples){
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
            <div className='divisionexamples'>
                <OperationsNav />
                <OperationsTab operationType="division" />
                <form className="divisionexamplesForm" >
                    <div className="divisionexamplesNumbers" >
                        <div className="divisionexamplesFirstNumber" >{this.state.firstNumber_divisionExamples}</div>
                        <span>÷</span>
                        <div className="divisionexamplesSecondNumber" >{this.state.secondNumber_divisionExamples}</div>
                        <span>=</span>
                        <input type="text" className="divisionexamplesResult" onChange={this.handleInput} />
                    </div>
                    <button type="submit" className="divisionexamplesButton buttonPrimary buttonPrimaryLarger" onClick={this.resultCheck} >Kontrol Et</button>
                </form>
            </div>
        )
    }
}
