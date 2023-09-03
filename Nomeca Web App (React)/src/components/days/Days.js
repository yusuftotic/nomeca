import React, { Component } from 'react';
import Swal from 'sweetalert2'
import './Days.css';

export default class Days extends Component{
    constructor(props){
        super(props);
        this.state = {
            days: [
                ["1", 'Pazartesi'],
                ["2", 'Salı'],
                ["3", 'Çarşamba'],
                ["4", 'Perşembe'],
                ["5", 'Cuma'],
                ["6", 'Cumartesi'],
                ["7", 'Pazar']
            ],
            randomIndex: Math.floor(Math.random() * 7),
            randomMonth: '',
            inputMonth: '',
            answerControl: Boolean()
        };
        this.randomMonthChoose = this.randomMonthChoose.bind(this);
        this.handleInput = this.handleInput.bind(this);
        this.resultCheck = this.resultCheck.bind(this);
    }

    componentWillMount(){
        this.randomMonthChoose();
    }
    
    randomMonthChoose(){
        this.setState({
            randomMonth: this.state.days[this.state.randomIndex]
        });
    }

    handleInput(e){
        this.setState({
            inputMonth: e.target.value
        });
    }

    resultCheck(e){
        if (this.state.randomMonth[0] === this.state.inputMonth){
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
            <div className="days" >
                <form className="daysForm" >
                    <div className="daysQuestionContainer" >
                        <div className="daysQuestion" >{`${this.state.randomMonth[1]}, haftanın kaçıncı günüdür?`}</div>
                    </div>
                    <input type="text" placeholder="_" className="daysInput" onChange={this.handleInput} />
                    <button type="submit" className='daysButton buttonPrimary buttonPrimaryLarger' onClick={this.resultCheck} >Kontrol Et</button>
                </form>
            </div>
        );
    }
}