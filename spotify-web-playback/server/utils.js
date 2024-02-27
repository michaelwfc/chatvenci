const { getProxyForUrl } = require('proxy-from-env');


function getProxySetting() {
    // URL to check proxy settings for
    const url = 'https://example.com';

    // Get proxy server for the URL
    const proxyServer = getProxyForUrl(url);

    console.log('Proxy Server:', proxyServer);
    return proxyServer
}

getProxySetting()