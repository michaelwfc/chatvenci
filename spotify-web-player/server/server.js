/* 
npm i spotify-web-api-node --save-dev
*/

const express = require('express');
const dotenv = require('dotenv');
const SpotifyWebAPI = require('spotify-web-api-node');
const cors = require('cors');
const bodyParser = require('body-parser');

dotenv.config()

var spotify_client_id = process.env.SPOTIFY_CLIENT_ID
var spotify_client_secret = process.env.SPOTIFY_CLIENT_SECRET

const REDIRECT_URI = 'http://localhost:3000'
const app = express();
app.use(cors());
app.use(bodyParser.json());

const port = 3001



app.post('/login', (req, res) => {

    const code = req.body.code

    const spotifyApi = new SpotifyWebAPI({
        redirectUri: REDIRECT_URI,
        clientId: spotify_client_id,
        clientSecret: spotify_client_secret
    })

    spotifyApi.authorizationCodeGrant(code)
        .then(data => {
            res.json({
                accessToken: data.body.access_token,
                refreshToken: data.body.refresh_token,
                expiresIn: data.body.expires_in
            }
            )
        })
        .catch(err => {
            console.log('somethin is wrong in /login');
            console.log(err);
            res.sendStatus(400)
        })

})

app.listen(port, () => {
    console.log(`Listening at http://localhost:${port}`)
})