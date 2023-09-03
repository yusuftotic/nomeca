import React, { Component } from 'react';
import Swal from 'sweetalert2';
import './Numbers.css'

export default class Numbers extends Component {
    constructor(props){
        super(props);
        this.state = {
            numbers: [
                ["1", 'Ocak'],
                ["2", 'Şubat'],
                ["3", 'Mart'],
                ["4", 'Nisan'],
                ["5", 'Mayıs'],
                ["6", 'Haziran'],
                ["7", 'Temmuz'],
                ["8", 'Ağustos'],
                ["9", 'Eylül'],
                ["10", 'Ekim'],
                ["11", 'Kasım'],
                ["12", 'Aralık'],
            ],
            randomIndex: Math.floor(Math.random() * 12),
            randomNumber: '',
            inputNumber: '',
            answerControl: Boolean()
        };
        this.randomNumberChoose = this.randomNumberChoose.bind(this);
        this.handleInput = this.handleInput.bind(this);
        this.resultCheck = this.resultCheck.bind(this);
    }

    componentWillMount(){
        this.randomNumberChoose();
    }
    
    randomNumberChoose(){
        this.setState({
            randomNumber: this.state.numbers[this.state.randomIndex]
        });
    }

    handleInput(e){
        this.setState({
            inputNumber: e.target.value
        });
    }

    resultCheck(e){
        if (this.state.randomNumber[0] === this.state.inputNumber){
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
            <div className="numbers" >
                <form className="numbersForm" >
                    <div className="numbersQuestionContainer" >
                        <div className="numbersQuestion" >{`${this.state.randomNumber[1]}, yazı ile yazınız.`}</div>
                    </div>
                    <input type="text" placeholder="_" className="numbersInput" onChange={this.handleInput} />
                    <button type="submit" className='numbersButton buttonPrimary buttonPrimaryLarger' onClick={this.resultCheck} >Kontrol Et</button>
                </form>
            </div>
        )
    }
}
