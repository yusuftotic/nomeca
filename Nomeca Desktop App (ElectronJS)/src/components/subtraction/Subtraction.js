import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import OperationsNav from '../operationsnav/OperationsNav';
import './Subtraction.css';

export default class Subtraction extends Component {
    render() {
        return (
            <div className='subtraction' >
                <OperationsNav />
                <ul className="subtractionLinkGroup" >
                    <li><Link to="/operations/subtraction/learning" className="subtractionLinkItem" >Çıkarma Öğren</Link></li>
                    <li><Link to="/operations/subtraction/examples" className="subtractionLinkItem" >Çıkarma Alıştırmaları</Link></li>
                </ul>
            </div>
        )
    }
}
