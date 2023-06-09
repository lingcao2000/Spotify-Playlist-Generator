# Spotify-Playlist-Generator

## Overview:

`generate_playlist` takes a list of artist and creates a playlist with top 10 songs per artist. You may choose the number of top most popular songs.

## Documentation References:

- Spotify for Developers: https://developer.spotify.com/documentation/web-api
- Spotipy Library: https://spotipy.readthedocs.io/en/2.22.1/

## How to use:

1. Visit the [Spotify for Developers website](https://developer.spotify.com/) and create or log in to your account.
2. Visit Dashboard and select "Create an App" and fill the info and create app:

- app name: (your choice)
- description: (your choice)
- redirect url: http://localhost/

3. Grab client ID and client secret and replace `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` respectively.
4. Replace `YOUR_USERNAME` with your spotify username. To find your username you can copy link to your profile and your username is located between "..user/`YOUR_USERNAME`?" (i.e. https://open.spotify.com/user/YOUR_USERNAME?si=aaaaaaaaaaaa).
5. Go to the current directory that contains the file and run `python generate_playlist.py` and follow any further directions from terminal and browser.