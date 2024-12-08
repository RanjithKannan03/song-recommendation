import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = "ADD_SPOTIFY_CLIENT_ID"
secret = "ADD_SPOTIFY_SECRET_KEY"
redirect_uri = "ADD_REDIRECT_URL"

auth_manager = SpotifyOAuth(client_id=client_id, client_secret=secret, redirect_uri=redirect_uri,
                            cache_path="token.txt",
                            show_dialog=True, scope="playlist-modify-public")
sp = spotipy.Spotify(client_credentials_manager=auth_manager)


def get_song_features(song_name):
    results = sp.search(q=song_name, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_id = track['id']
        features = sp.audio_features([track_id])[0]
        print(features)
        return [
            features['danceability'], features['energy'], features['key'], features['loudness'],
            features['acousticness'],  features['instrumentalness'],
            features['liveness'],features['valence'], features['tempo']
        ]
    return None

def create_playlist(songs,song_name):
    song_uris=[]
    current_user=sp.current_user()
    for song in songs:
        result=sp.track(song['id'])
        song_uris.append(result['uri'])
    playlist=sp.user_playlist_create(current_user['id'],f"{song_name}",public=True,collaborative=False,description=f"50 songs similar to {song_name}")
    playlist_id=playlist['id']


    sp.playlist_add_items(playlist_id=playlist_id,items=song_uris)

    return playlist['external_urls']['spotify']