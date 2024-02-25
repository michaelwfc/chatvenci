import React from 'react';
import UseAuth from './useAuth';

export default function Dashboard({ code }) {
    const use_auth = UseAuth(code);
    return <div>
        {code}
    </div>

}