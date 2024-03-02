'use strict';

var Request = require('./base-request');

var DEFAULT_HOST = 'accounts.spotify.com',
  DEFAULT_PORT = 443,
  DEFAULT_SCHEME = 'https';

const { DEFAULT_PROXY } = require('./proxy_config');

module.exports.builder = function () {
  return Request.builder()
    .withHost(DEFAULT_HOST)
    .withPort(DEFAULT_PORT)
    .withScheme(DEFAULT_SCHEME)
    .withProxy(DEFAULT_PROXY)

};
