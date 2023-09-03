import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import './OperationsTab.css';

export default class OperationsTab extends Component {
    render() {
        return (
            <div className="operationstab" >
                <ul className="operationstabLinkGroup" >
                    <li><Link to={`/operations/${this.props.operationType}/learning`} className="operationstabLinkItem" >Öğren</Link></li>
                    <li><Link to={`/operations/${this.props.operationType}/examples`} className="operationstabLinkItem" >Alıştırma Yap</Link></li>
                </ul>
            </div>
        );
    }
}
