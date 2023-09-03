import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import OperationsNav from '../operationsnav/OperationsNav';
import './Multiplication.css';

export default class Multiplication extends Component {
    render() {
        return (
            <div className='multiplication' >
                <OperationsNav />
                <ul className="multiplicationLinkGroup" >
                    <li><Link to="/operations/multiplication/learning" className="multiplicationLinkItem" >Çarpma Öğren</Link></li>
                    <li><Link to="/operations/multiplication/examples" className="multiplicationLinkItem" >Çarpma Alıştırmaları</Link></li>
                </ul>
            </div>
        )
    }
}
