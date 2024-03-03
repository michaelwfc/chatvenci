import React from 'react';
import { Container, Form } from "react-bootstrap"

import { useState, useEffect } from "react"

// import UseAuth from './useAuth';

function Dashboard({ token }) {
    // const use_auth = UseAuth(code);
    console.log("show Dashboard");
    return (<>
        <div>
            {token}
        </div>

    </>)

}

export default Dashboard;