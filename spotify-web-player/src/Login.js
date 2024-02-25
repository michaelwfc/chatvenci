// npm i bootstrap react-bootstrap

import React from "react";
import { Container } from "react-bootstrap";


const AUTH_URL = "https://accounts.spotify.com/authorize?\
client_id=f49b7a0661594518ad9cf26710e53038&\
response_type=code&\
redirect_uri=http://localhost:3000&\
scope=streaming%20user-read-private%20user-read-email"


export default function Login() {
    return < Container>
        < a className="btn btn-success btn-login" href={AUTH_URL}>
            Login Spotify

        </a>
    </Container>
}