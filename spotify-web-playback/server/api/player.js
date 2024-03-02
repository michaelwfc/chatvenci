
/* 
0. run the local web skd player: npm run dev
1. get access_token
2. get available devices
3. get device_id of local device by device_name
4. Transfer playback to the local device
5. search the track/playlist/ablum 

6. play the music on the local device


export http_proxy=http://127.0.0.1:7890
export https_proxy=http://127.0.0.1:7890


export access_token="BQBSbrAdtYUEq6jlAm70I7VQtuVBJI7OT1RRCxJedfQvyb9qBndtvfcXteWLTJLsHC1ZLig2Drz54oyzf5j5Z9DF8BC6F0tmR80jKY-04m74iLv0smHK6dplI_-JxTAMwQCIFrGvi5yUbb5HQi0xexai51O5XTljVQtG406l5ouru9xqdmEJBn85hlvAblp7j6snHx6kOVmDlRnEv2YujMaZ3Q_PA6VdEMjD3g"
export header="Authorization: Bearer ${access_token}"
echo $header




// get available devices
// https://developer.spotify.com/documentation/web-api/reference/get-a-users-available-devices

curl --request GET  --url https://api.spotify.com/v1/me/player/devices  --header "$header"

export device_id="7b4be5e3dc51cfc7011ca0047c70b5958bb4099c"



// Transfer playback to the local device
// https://developer.spotify.com/documentation/web-api/reference/transfer-a-users-playback
curl --request PUT \
  --url https://api.spotify.com/v1/me/player \
  --header "$header" \
  --header 'Content-Type: application/json' \
  --data '{ "device_ids": ["'"$device_id"'"]}'








// start/resume the music on the local device
// https://developer.spotify.com/documentation/web-api/reference/start-a-users-playback

curl --request PUT --url "https://api.spotify.com/v1/me/player/play?device_id=${device_id}" \
  --header  "$header" \
  --header 'Content-Type: application/json' \
  --data '{
    "context_uri": "spotify:album:5ht7ItJgpBH7W6vJ5BqpPr",
    "offset": {
        "position": 1
    },
    "position_ms": 0
}'


curl --request PUT --url "https://api.spotify.com/v1/me/player/play?device_id=${device_id}" \
  --header  "$header" \
  --header 'Content-Type: application/json' \
  --data '{
    "uris": ["spotify:track:1301WleyT98MSxVHPZCA6M"],
    "offset": {
        "position": 0
    },
    "position_ms": 0
}'


curl --request PUT --url "https://api.spotify.com/v1/me/player/pause?device_id=${device_id}" --header "$header" --header "Content-Length: 0"


// https://developer.spotify.com/documentation/web-api/reference/search
curl --request GET \
  --url 'https://api.spotify.com/v1/search?q=remaster%2520track%3ADoxy%2520artist%3AMiles%2520Davis&type=album' \
  --header  "$header"



*/
// Assume you have obtained an access token after authenticating the user
const accessToken = 'YOUR_ACCESS_TOKEN';

// Specify the track URI or ID you want to play
const trackUri = 'spotify:track:TRACK_ID';

// Make a POST request to the Spotify Web API to start playback
fetch('https://api.spotify.com/v1/me/player/play', {
    method: 'PUT',
    headers: {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        uris: [trackUri],
    }),
})
    .then(response => {
        if (response.ok) {
            console.log('Song started playing successfully.');
        } else {
            console.error('Failed to start playback:', response.statusText);
        }
    })
    .catch(error => {
        console.error('Error starting playback:', error);
    });
