const WEB_PLAYBACK_SKD = "Michael Web Playback SDK" // process.env.WEB_PLAYBAK_SDK

const AUTHORIZATION_URL = 'https://accounts.spotify.com/authorize/?'
const API_TOKEN_URL = 'https://accounts.spotify.com/api/token';

var SPOTIFY_REDIRECT_URI = 'http://localhost:3000/auth/callback'


const ACCESS_TOKEN = "access_token";
const EXPIRES_IN = "expires_in";
const REFRESH_TOKEN = "refresh_token";

const PORT = 5000

// Proxy configuration
DEFAULT_PROXY = 'http://127.0.0.1:7890';

module.exports = {
    WEB_PLAYBACK_SKD, AUTHORIZATION_URL, API_TOKEN_URL, SPOTIFY_REDIRECT_URI,
    ACCESS_TOKEN, EXPIRES_IN, REFRESH_TOKEN, PORT, DEFAULT_PROXY
}