/* 
https://github.com/thelinmichael/spotify-web-api-node/
*/
const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const request = require('request');
const dotenv = require('dotenv');
const bodyParser = require('body-parser');
const { getProxySetting, setGlobalProxy, generateRandomString } = require('./utils');


// var SpotifyWebApi = require('spotify-web-api-node');
var SpotifyWebApi = require("./spotify_web_api/server")


const port = 5000

const AUTHORIZATION_URL = 'https://accounts.spotify.com/authorize/?'
const API_TOKEN_URL = 'https://accounts.spotify.com/api/token';
var spotify_redirect_uri = 'http://localhost:3000/auth/callback'

// Proxy configuration
DEFAULT_PROXY = 'http://127.0.0.1:7890';

global.access_token = ''

dotenv.config();

// setGlobalProxy();

var app = express();


var spotify_client_id = process.env.SPOTIFY_CLIENT_ID
var spotify_client_secret = process.env.SPOTIFY_CLIENT_SECRET
var scopes = "streaming app-remote-control user-read-playback-state user-modify-playback-state user-read-currently-playing user-read-email user-read-private".split(" ")
var state = generateRandomString(16);

// credentials are optional
var spotifyApi = new SpotifyWebApi({
    clientId: spotify_client_id,
    clientSecret: spotify_client_secret,
    redirectUri: spotify_redirect_uri
});

// // Set proxy settings for the superagent instance
// const agent = superagent.agent().proxy(proxyUrl);


console.log("initialized spotifyApi");
// console.log(spotifyApi.)



app.get('/auth/login', (req, res) => {
    // Create the authorization URL
    var authorizeURL = spotifyApi.createAuthorizeURL(scopes, state);
    // https://accounts.spotify.com:443/authorize?client_id=5fe01282e44241328a84e7c5cc169165&response_type=code&redirect_uri=https://example.com/callback&scope=user-read-private%20user-read-email&state=some-state-of-my-choice
    // console.log(authorizeURL);
    res.redirect(authorizeURL)

})


app.get('/auth/callback', (req, res) => {
    var code = req.query.code || null;
    var state = req.query.state || null;

    // Retrieve an access token and a refresh token
    spotifyApi.authorizationCodeGrant(code).then(
        function (data) {
            console.log('The token expires in ' + data.body['expires_in']);
            console.log('The access token is ' + data.body['access_token']);
            console.log('The refresh token is ' + data.body['refresh_token']);

            // Set the access token on the API object to use it in later calls
            spotifyApi.setAccessToken(data.body['access_token']);
            spotifyApi.setRefreshToken(data.body['refresh_token']);

            access_token = data.body['access_token']
            refresh_token = data.body['refresh_token']
            res.redirect('/')
        },
        function (err) {
            console.log('Something went wrong!', err);

        })
})

app.get('/auth/token', (req, res) => {
    res.json({ access_token: access_token })
})

app.get('/api/get_device_id', (req, res) => {
    // Get a User's Available Devices
    spotifyApi.getMyDevices()
        .then(function (data) {
            let availableDevices = data.body.devices;
            // for (let i = 0; i < availableDevices.length; i++) {
            //     console.log(availableDevices[i]);
            // }
            // Return the array as a JSON response
            res.json(availableDevices)

        }, function (err) {
            console.log('Something went wrong!', err);
        });
})

app.listen(port, () => {
    console.log(`Spotify API server listening at http://localhost:${port}`)
})
