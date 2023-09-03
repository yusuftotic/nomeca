import React, { Component } from 'react';
import Swal from 'sweetalert2';
import './Months.css';

export default class Months extends Component{
    constructor(props){
        super(props);
        this.state = {
            months: [
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
            randomIndex: Math.floor(Math.random() * 13),
            randomDay: '',
            inputDay: '',
            answerControl: Boolean()
        };
        this.randomDayChoose = this.randomDayChoose.bind(this);
        this.handleInput = this.handleInput.bind(this);
        this.resultCheck = this.resultCheck.bind(this);
    }

    componentDidMount(){
        this.randomDayChoose();
    }
    
    randomDayChoose(){
        this.setState({
            randomDay: this.state.months[this.state.randomIndex]
        });
    }

    handleInput(e){
        this.setState({
            inputDay: e.target.value
        });
    }

    resultCheck(e){
        if (this.state.randomDay[0] === this.state.inputDay){
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

    render(){
        return(
            <div className="months" >
                <form className="monthsForm" >
                    <div className="monthsQuestionContainer" >
                        <div className="monthsQuestion" >{`${this.state.randomDay && this.state.randomDay[1]}, yılın kaçıncı ayıdır?`}</div>
                    </div>
                    <input type="text" placeholder="_" className="monthsInput" onChange={this.handleInput} />
                    <button type="submit" className='monthsButton buttonPrimary buttonPrimaryLarger' onClick={this.resultCheck} >Kontrol Et</button>
                </form>
            </div>
        );
    }
}