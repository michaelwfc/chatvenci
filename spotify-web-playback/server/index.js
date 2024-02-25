const express = require('express')
const request = require('request');
const dotenv = require('dotenv');

// import generateRandomString from './utils';
var generateRandomString = function (length) {
  var text = '';
  var possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

  for (var i = 0; i < length; i++) {
    text += possible.charAt(Math.floor(Math.random() * possible.length));
  }
  return text;
};

/* 
During the development phase, our React app and backend will run on different hosts and ports:
The client runs on localhost:3000
The backend runs on localhost:5000
Thus, we need to tell our React app where to find the server when doing API calls such as /auth/login or /auth/token.
*/

const port = 5000

const AUTHORIZATION_URL = 'https://accounts.spotify.com/authorize/?'

var spotify_redirect_uri = 'http://localhost:3000/auth/callback'


global.access_token = ''

dotenv.config()

var spotify_client_id = process.env.SPOTIFY_CLIENT_ID
var spotify_client_secret = process.env.SPOTIFY_CLIENT_SECRET

var app = express();

app.get('/auth/login', (req, res) => {
  /* 
npm run dev > frontend: login button > server: localhost:3000/auth/login >middlewar > localhost:5000/auth/login > redirect to  https://accounts.spotify.com/authorize/ >
web  approve > callback (code & state)>  localhost:3000/auth/callback

redirect the user to a web page where they can choose to grant our application access to their premium account.
To do so, we need to send a GET request to the /authorize endpoint of the Spotify account service with the following parameters: 

Once the user approves the application request, the user is redirected back to the application using the redirect_uri passed on 
the authorized request  http://localhost:3000/auth/callback just described above.
The callback contains two query parameters:  code  & state
*/


  var scope = "streaming user-read-email user-read-private"
  var state = generateRandomString(16);

  var auth_query_parameters = new URLSearchParams({
    response_type: "code",
    client_id: spotify_client_id,
    scope: scope,
    redirect_uri: spotify_redirect_uri,
    state: state
  })

  res.redirect(AUTHORIZATION_URL + auth_query_parameters.toString());
})

app.get('/auth/callback', (req, res) => {
  /* 
  Now that we have the authorization code, we must exchange it for tokens. 
  Using the code from the previous step, we need to make a POST request to the /api/token endpoint.
  */

  var code = req.query.code;

  var authOptions = {
    url: 'https://accounts.spotify.com/api/token',
    form: {
      code: code,
      redirect_uri: spotify_redirect_uri,
      grant_type: 'authorization_code'
    },
    headers: {
      'Authorization': 'Basic ' + (Buffer.from(spotify_client_id + ':' + spotify_client_secret).toString('base64')),
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    json: true
  };

  function callback_fn(error, response, body) {
    if (!error && response.statusCode === 200) {
      access_token = body.access_token;
      res.redirect('/')
    }
    else {
      /* 
      Error: read ECONNRESET
       */
      console.log(error);
      console.log(response);
    }

  }
  request.post(authOptions, callback_fn);

})


app.get('/auth/token', (req, res) => {
  res.json({ access_token: access_token })
})

app.listen(port, () => {
  console.log(`Listening at http://localhost:${port}`)
})
