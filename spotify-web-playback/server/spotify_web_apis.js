/**
 * This is an example of a basic node.js script that performs
 * the Client Credentials oAuth2 flow to authenticate against
 * the Spotify Accounts.
 * https://github.com/spotify/web-api-examples/blob/master/authorization/client_credentials/app.js
 * 
 * For more information, read
 *  * https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow
 * 
 * 
 * In JavaScript running on a web browser, you can't directly access system-level proxy settings like you can with Python and the Windows Registry. 
 * 
 */

const dotenv = require('dotenv');
dotenv.config();

// import axios from 'axios';
const request = require('request');


var spotify_client_id = "52eca94ab8c44a3ba96a8d4e30e858ad" //process.env.SPOTIFY_CLIENT_ID
var spotify_client_secret = "6c3bb6bbc4c64fd0b640f4941fb070c9"//process.env.SPOTIFY_CLIENT_SECRET

// Proxy configuration
const proxyUrl = 'http://127.0.0.1:7890';

const apiTokenUrl = 'https://accounts.spotify.com/api/token';

var authOptions = {
    url: 'https://accounts.spotify.com/api/token',
    // add proxyUrl
    proxy: proxyUrl,
    headers: {
        'Authorization': 'Basic ' + (new Buffer.from(spotify_client_id + ':' + spotify_client_secret).toString('base64'))
    },
    form: {
        grant_type: 'client_credentials'
    },
    json: true // Automatically parse JSON response
};


request.post(authOptions, function (error, response, body) {
    if (!error && response.statusCode === 200) {
        var token = body.access_token;
        console.log("Success to get Access token");
        console.log(token);
    }
    else {
        console.log("There was an error in request!");
        console.log(error);
    }
});



async function getToken() {
    const response = await fetch(apiTokenUrl, {
        method: 'POST',
        body: new URLSearchParams({
            'grant_type': 'client_credentials',
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' + (Buffer.from(spotify_client_id + ':' + spotify_client_secret).toString('base64')),
        },
    });

    return await response.json();
}




async function getTrackInfo(access_token) {
    const response = await fetch("https://api.spotify.com/v1/tracks/4cOdK2wGLETKBW3PvgPWqT", {
        method: 'GET',
        headers: { 'Authorization': 'Bearer ' + access_token },
    });

    return await response.json();
}

console.log(spotify_client_id);
console.log(spotify_client_secret);


// getToken().then(response => {
//     // Handle response
//     console.log(response.access_token);
// }).
//     catch(err => {
//         console.log("There was an error!")
//         console.log(err);
//     })
//     ;



// getToken().then(response => {
//     getTrackInfo(response.access_token).then(profile => {
//         console.log(profile)
//     })
// });