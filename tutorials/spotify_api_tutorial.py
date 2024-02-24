
import os
import requests

from constants import SPOTIFY_CLIENT_ID,SPOTIFY_CLIENT_SECRET


class SpotifyWebAPIBot():
    def __init__(self) -> None:
        # Your Spotify Developer credentials
        self.client_id =os.getenv(SPOTIFY_CLIENT_ID)
        self.client_secrect = os.getenv(SPOTIFY_CLIENT_SECRET)
        
        self.access_token_url ="https://accounts.spotify.com/api/token"
        self.artist_url ="https://api.spotify.com/v1/artists/"

        # Authenticate and obtain access token
    def _get_access_token(self):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        auth_response = requests.post('https://accounts.spotify.com/api/token', 
                                      data =  {
            'grant_type': 'client_credentials',
            'client_id': self.client_id,
            'client_secret': self.client_secrect,
        
        },
        headers=headers
        
        )

        auth_response_data = auth_response.json()
        access_token = auth_response_data['access_token']
        return access_token
    

    def _build_header(self, access_token):
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
        }
        return headers

    
    def get_artist_data(self,artist="4Z8W4fKeB5YxbusRsdQVPb"):
        access_token =  self._get_access_token()
        print(f"access_token={access_token}")
        
        headers =  self._build_header(access_token=access_token)

        artist_data =  requests.post(self.artist_url,params=artist,headers=headers).json()
        print(f"artist_data={artist_data}")
        return artist_data




    # Play a track
    def play_track(self, headers, track_uri):

        payload = {
            'uris': [track_uri]
        }

        play_response = requests.put('https://api.spotify.com/v1/me/player/play', json=payload, headers=headers)

        if play_response.status_code == 204:
            print('Track is now playing.')
        else:
            print('Error playing track:', play_response.json())


# Example usage
def main():
    from utils.environments import set_gpt_env
    set_gpt_env()

    # access_token = get_access_token()
    # track_uri = 'spotify:track:your_track_uri'
    # play_track(track_uri, access_token)

    spotify_api_bot = SpotifyWebAPIBot()
    spotify_api_bot.get_artist_data()



if __name__ == '__main__':
    main()
