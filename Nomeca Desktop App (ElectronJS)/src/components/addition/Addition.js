import React, { Component } from 'react'
import { Link } from 'react-router-dom';
import OperationsNav from '../operationsnav/OperationsNav';
import './Addition.css';

export default class Addition extends Component {
    render() {
        return (
            <div className='addition' >
                <OperationsNav />
                <ul className="additionLinkGroup" >
                    <li><Link to="/operations/addition/learning" className="additionLinkItem" >Toplama Öğren</Link></li>
                    <li><Link to="/operations/addition/examples" className="additionLinkItem" >Toplama Alıştırmaları</Link></li>
                </ul>
            </div>
        )
    }
}
