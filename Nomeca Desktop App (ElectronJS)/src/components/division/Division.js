import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import OperationsNav from '../operationsnav/OperationsNav';
import './Division.css';

export default class Division extends Component {
    render() {
        return (
            <div className='division' >
                <OperationsNav />
                <ul className="divisionLinkGroup" >
                    <li><Link to="/operations/division/learning" className="divisionLinkItem" >Bölme Öğren</Link></li>
                    <li><Link to="/operations/division/examples" className="divisionLinkItem" >Bölme Alıştırmaları</Link></li>
                </ul>
            </div>
        )
    }
}
