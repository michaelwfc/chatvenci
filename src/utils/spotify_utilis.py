import os
import requests
from utils.string_utils import encoding_string_to_base64_string

from constants import SPOTIFY_CLIENT_ID,SPOTIFY_CLIENT_SECRET


SPOTIFY_BASE_URL = "https://accounts.spotify.com"

# URLS
SPOTIFY_AUTH_URL = 'https://accounts.spotify.com/authorize'
SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_BASE_URL = 'https://api.spotify.com/v1/'





# Authenticate and obtain access token
def get_access_token(client_id,client_secret):
    authorization = encoding_string_to_base64_string(f"{client_id}:{client_secret}")

    headers = {"Content-Type": "application/x-www-form-urlencoded",
               "Authorization": "Basic " + authorization}

    auth_response = requests.post(SPOTIFY_TOKEN_URL, 
                                  data={'grant_type': 'client_credentials'},
                                  headers=headers)

    auth_response_data = auth_response.json()
    return auth_response_data['access_token']



# Play a track
def play_track(track_uri, access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }

    payload = {
        'uris': [track_uri]
    }

    play_response = requests.put('https://api.spotify.com/v1/me/player/play', json=payload, headers=headers)

    if play_response.status_code == 204:
        print('Track is now playing.')
    else:
        print('Error playing track:', play_response.json())


if __name__ == '__main__':
    from utils.environments import set_gpt_env
    set_gpt_env(set_proxy=False)
    client_id =os.getenv(SPOTIFY_CLIENT_ID)
    client_secrect = os.getenv(SPOTIFY_CLIENT_SECRET)
    access_token =  get_access_token(client_id=client_id, client_secret=client_secrect)
    print(f"access_token={access_token}")
    
    # encoding_string_to_base64()