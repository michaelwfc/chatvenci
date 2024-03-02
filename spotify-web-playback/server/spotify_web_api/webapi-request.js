'use strict';
const { DEFAULT_PROXY } = require('./proxy_config');

var Request = require('./base-request');

var DEFAULT_HOST = 'api.spotify.com',
  DEFAULT_PORT = 443,
  DEFAULT_SCHEME = 'https';



module.exports.builder = function (accessToken) {
  return Request.builder()
    .withHost(DEFAULT_HOST)
    .withPort(DEFAULT_PORT)
    .withScheme(DEFAULT_SCHEME)
    .withAuth(accessToken)
    .withProxy(DEFAULT_PROXY);  // ADD PROXY HERE
};
