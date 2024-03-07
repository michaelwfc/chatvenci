const { getProxyForUrl, proxyFromEnv } = require('proxy-from-env');
const http = require('http');
const https = require('https');
const cron = require('node-cron');
const axios = require('axios');
const { ACCESS_TOKEN, REFRESH_TOKEN } = require('./constants');

function getProxySetting() {
    // URL to check proxy settings for
    const url = 'https://example.com';

    // Get proxy server for the URL
    const proxyServer = getProxyForUrl(url);

    console.log('Proxy Server:', proxyServer);
    return proxyServer
}

function setGlobalProxy(proxyServer = 'http://127.0.0.1:7890') {
    // Get current proxy settings
    // const currentProxy = process.env.http_proxy || process.env.HTTP_PROXY;
    // console.log('Current proxy:', currentProxy);

    // Set proxy settings
    http.globalAgent = new http.Agent({ "proxy": proxyServer });
    https.globalAgent = new https.Agent({ "proxy": proxyServer });

    // Now all HTTP and HTTPS requests will use the specified proxy

}

// setGlobalProxy();
// getProxySetting();


// import generateRandomString from './utils';
var generateRandomString = function (length) {
    var text = '';
    var possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

    for (var i = 0; i < length; i++) {
        text += possible.charAt(Math.floor(Math.random() * possible.length));
    }
    console.log('text:', text);
    return text;
};


// Schedule a task to run every minute
var schedule_refresh_token = function (schedule_interval = '*/50 * * * *') {
    cron.schedule(schedule_interval, () => {
        console.log("start by scheduler at " + Date());
        const refresh_token = global.refresh_token

        axios.post('http://localhost:5000/auth/refresh_token', { "refreshToken": refresh_token },
            {
                headers: { 'Content-Type': 'application/json' }
            })
            .then(response => {
                access_token = response.data[ACCESS_TOKEN];
                refresh_token = response.data[REFRESH_TOKEN];
                console.log("refreshed by scheduler" + refresh_token);
                console.log("access_token: " + access_token);
                console.log("refresh token: " + refresh_token);
                return response.data
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });
}




// export default getProxySetting;
module.exports = {
    getProxySetting,
    setGlobalProxy,
    generateRandomString,
    schedule_refresh_token
};