import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import './LeftMenu.css';

import logo from '../../assets/images/fsmal-logo.jpg';

export default class LeftMenu extends Component {
    render() {
        return (
            <div className="leftmenu">
                <div className="leftmenuLogo" >
                    <span><img src={logo} alt="" /></span>
                </div>
                <ul className="leftmenuLinkGroup" >
                    <Link to="/" className="leftmenuLinkItem" ><li>Ana Sayfa</li></Link>
                    <Link to="/operations" className="leftmenuLinkItem" ><li>İşlemler</li></Link>
                    {/* <Link to="/numbers" className="leftmenuLinkItem" ><li>Sayılar</li></Link> */}
                    <Link to="/days" className="leftmenuLinkItem" ><li>Günler</li></Link>
                    <Link to="/months" className="leftmenuLinkItem" ><li>Aylar</li></Link>
                </ul>
            </div>
        )
    }
}
