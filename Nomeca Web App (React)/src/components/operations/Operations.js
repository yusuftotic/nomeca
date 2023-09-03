import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import './Operations.css';

export default class Operations extends Component {
    render() {
        return (
            <div className="operations" >
                <ul className="operationsLinkGroup" >
                    <li><Link to="/operations/addition" className="operationsLinkItem" >Toplama</Link></li>
                    <li><Link to="/operations/subtraction" className="operationsLinkItem" >Çıkarma</Link></li>
                    <li><Link to="/operations/multiplication" className="operationsLinkItem" >Çarpma</Link></li>
                    <li><Link to="/operations/division" className="operationsLinkItem" >Bölme</Link></li>
                </ul>
                {/* <div className="operationsLinkGroup" >
                    <Link to="/operations/addition" className="operationsLinkItem" >Toplama</Link>
                    <Link to="/operations/subtraction" className="operationsLinkItem" >Çıkarma</Link>
                    <Link to="/operations/multiplication" className="operationsLinkItem" >Çarpma</Link>
                    <Link to="/operations/division" className="operationsLinkItem" >Bölme</Link>
                </div> */}
            </div>
        );
    }
}
