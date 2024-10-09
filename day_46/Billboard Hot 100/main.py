import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = "YOUR ID"
SPOTIPY_CLIENT_SECRET = "PUT YOUR SECRET CODE"
SPOTIPY_REDIRECT_URI = "http://example.com"

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="playlist-modify-private"))

# Function to get the Billboard Hot 100 songs for a given date
def get_billboard_songs(date):
    url = f'https://www.billboard.com/charts/hot-100/{date}/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract song titles and artists
    songs = []
    for entry in soup.select('li.o-chart-results-list__item h3'):
        song_title = entry.get_text(strip=True)
        artist = entry.find_next('span').get_text(strip=True)
        songs.append((song_title, artist))
    return songs

# Function to search for a song on Spotify and return its URI
def search_spotify_song(song_title, artist):
    query = f'track:{song_title} artist:{artist}'
    result = sp.search(q=query, type='track', limit=1)
    tracks = result['tracks']['items']
    if tracks:
        return tracks[0]['uri']
    return None

# Function to create a playlist on Spotify
def create_spotify_playlist(user_id, playlist_name, track_uris):
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
    sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)

# Main function
def generate_spotify_playlist(date):
    # Get the Billboard songs for the given date
    songs = get_billboard_songs(date)

    # Prepare playlist name (e.g., "Billboard 2000")
    year = date.split('-')[0]
    playlist_name = f'Billboard {year}'

    # Search for songs on Spotify and collect URIs
    track_uris = []
    for song_title, artist in songs:
        track_uri = search_spotify_song(song_title, artist)
        if track_uri:
            track_uris.append(track_uri)

    # Get the current user's ID
    user_id = sp.current_user()['id']

    # Create the playlist and add songs to it
    create_spotify_playlist(user_id, playlist_name, track_uris)
    print(f'Playlist "{playlist_name}" created with {len(track_uris)} songs.')

# Ask user for a date in the format yyyy-mm-dd
date_input = input("Enter a date (yyyy-mm-dd): ")
generate_spotify_playlist(date_input)