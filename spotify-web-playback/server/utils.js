const { getProxyForUrl, proxyFromEnv } = require('proxy-from-env');
const http = require('http');
const https = require('https');



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


// export default getProxySetting;
module.exports = {
    getProxySetting,
    setGlobalProxy,
    generateRandomString,

};