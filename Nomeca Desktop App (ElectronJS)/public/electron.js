const { app, BrowserWindow } = require('electron');

const path = require('path');
const isDev = require('electron-is-dev');

require('@electron/remote/main').initialize();

function createWindow() {
    const win = new BrowserWindow({
        width: 1024,
        height: 768,
        webPreferences: {
            enableRemoteModule: true,
            nodeIntegration: true
        },
        autoHideMenuBar: true,
        icon: "src/assets/images/fsmal-logo.ico",
    });

    win.loadURL('http://localhost:3000');
    // win.loadURL(
    //     isDev
    //     ? 'http://localhost:3000'
    //     : `file://${path.join(__dirname, 'build/index.html')}`
    // );
}

app.on('ready', createWindow);

app.on('window-all-closed', function(){
    if (process.platform !== 'darwin'){
        app.quit()
    }
});

app.on('activate', function () {
    if (BrowserWindow.getAllWindows().length === 0) createWindow()
});