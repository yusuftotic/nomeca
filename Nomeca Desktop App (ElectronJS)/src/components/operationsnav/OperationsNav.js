import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import './OperationsNav.css';

export default class OperationsNav extends Component {
    render() {
        return (
            <div className="operationsnav" >
                <ul className="operationsnavLinkGroup" >
                    <li><Link to="/operations/addition" className="operationsnavLinkItem" >Toplama</Link></li>
                    <li><Link to="/operations/subtraction" className="operationsnavLinkItem" >Çıkarma</Link></li>
                    <li><Link to="/operations/multiplication" className="operationsnavLinkItem" >Çarpma</Link></li>
                    <li><Link to="/operations/division" className="operationsnavLinkItem" >Bölme</Link></li>
                </ul>
            </div>
        );
    }
}
