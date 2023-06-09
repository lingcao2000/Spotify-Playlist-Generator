import spotipy
import spotipy.util
from spotipy import SpotifyException

# Modify
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
username = 'YOUR_USERNAME'
playlist_name = 'Algorithm Generated Playlist' # Name of the playlist
public = True # True = public playlist, False = private playlist
artists = ['ARTIST_NAME_1', 'ARTIST_NAME_2'] # List of artist names, you may add more
number_of_songs = 10 # Number of songs per artist to add to playlist per artist
# playlist_description = 'Top {} songs for each artist: {}'.format(number_of_songs, artists)

# Do not modify
redirect_uri = 'http://localhost/'
search_type_artist = 'artist'
scope = 'playlist-modify-public'

# Authenticate with Spotify APIs
sp = spotipy.Spotify(auth = spotipy.util.prompt_for_user_token(username,
                                                               scope,client_id,
                                                               client_secret,
                                                               redirect_uri))

# Create new playlist
user_id = sp.me()['id']
playlist = sp.user_playlist_create(user = user_id,
                                   name = playlist_name,
                                   public = public)

for artist_name in artists:
    try:
        # Search for artist by name
        results = sp.search(q = artist_name,
                            type = search_type_artist,
                            limit = 1)

        if results['artists']['items']:
            artist = results['artists']['items'][0]

            # Retrieve top [number of] tracks of the artist
            top_tracks = sp.artist_top_tracks(artist['id']) # Omitting country pararmeter to retrieve global popularity

            track_ids = [track['id'] for track in top_tracks['tracks'][:number_of_songs]]

            # Add tracks to the playlist
            sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=track_ids)

    except SpotifyException as e:
        # Artist not found errors
        print("Artist not found", artist_name)
        print("Error:", e)

print('Playlist created.')
