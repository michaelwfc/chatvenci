const express = require('express');
const { createProxyMiddleware } = require('http-proxy-middleware');
const request = require('request');
const dotenv = require('dotenv');
const bodyParser = require('body-parser');

// Proxy configuration
const proxyUrl = 'http://127.0.0.1:7890';
// Define proxy options
const proxyOptions = {
  target: proxyUrl, // Replace with your target URL
  changeOrigin: true, // Needed for virtual hosted sites
  // Other proxy options as needed
};

// Create the proxy middleware
// const proxy = createProxyMiddleware(proxyOptions);


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
const API_TOKEN_URL = 'https://accounts.spotify.com/api/token';

var spotify_redirect_uri = 'http://localhost:3000/auth/callback'


global.access_token = ''

dotenv.config()

var spotify_client_id = "f49b7a0661594518ad9cf26710e53038" //process.env.SPOTIFY_CLIENT_ID
var spotify_client_secret = "04fae29af5594855bc4eec7a271d5240" // process.env.SPOTIFY_CLIENT_SECRET

var app = express();

console.log("spotify_client_id")
console.log(spotify_client_id)
console.log(spotify_client_secret)
// Use the proxy middleware in your Express app
// app.use('https://accounts.spotify.com/**', proxy); // Specify the endpoint you want to proxy


app.get('/auth/login', (req, res) => {
  /*  to request user authorization by getting an Authorization Code.
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
  /*  to request the Access Token using the Authorization Code
  Now that we have the authorization code, we must exchange it for tokens. 
  Using the code from the previous step, we need to make a POST request to the /api/token endpoint.
  */

  var code = req.query.code || null;
  var state = req.query.state || null;

  // if (state === null)

  var authOptions = {
    url: API_TOKEN_URL,
    proxy: proxyUrl, // add explict proxy 
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

  /* 
  [HPM] Error occurred while proxying request localhost:3000/auth/callback?code=AQC-vFmJEZNi9pyI0yzPpl4_REC4939K8sQGXaFVN1nB5Ko6Bq1fogRy_7yiPz0k_v7dr4vAk9ZeaCc3jsD5NCK4Pog7m5wVOWBXH5_SMMsCmjxHIYKFRkNpLMA_QVcDje3N5KrgZS6NIKBmC1wvcuC7PnUgNqfRoitXS0X7sCpt60K46dbEP6RitbfnxXy11xG731VdZ3xk14Su-BQrXMT1AN5A8z6UC030kqjw71GfKMKi-dY&state=snbQMQGzdzTMBzJf 
  to http://localhost:5000/ [ECONNRESET] (https://nodejs.org/api/errors.html#errors_common_system_errors)
ERROR: "server" exited with 1.
  */

  request.post(authOptions, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      access_token = body.access_token;
      console.log("Success to get Access token");
      res.redirect('/')
    } else {
      console.log(error);
      console.log(response);
    }
  });

  // request.post(authOptions, (error, response, body) => {
  //   if (error) {
  //     console.error(error);
  //     return;
  //   }
  //   console.log(response);
  // });

})


app.get('/auth/token', (req, res) => {
  res.json({ access_token: access_token })
})

app.listen(port, () => {
  console.log(`Listening at http://localhost:${port}`)
})
