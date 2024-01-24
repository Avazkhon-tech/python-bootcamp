from bs4 import BeautifulSoup
import requests
# year = input("Which year do you want to travel to? Type the date in this format YYY-MM-DD")
# year = "2020-10-10"
# url = f"https://www.billboard.com/charts/hot-100/{year}/"
# response = requests.get(url)
# webpage = response.text
# soup = BeautifulSoup(webpage, "html.parser")
# texts = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in texts]
# print(song_names)

CLIENT_ID = "bd37f38b08dd4b50885eaf6a849f3447"
CLIENT_SECRET = "7411b810bf2a4028b5c8ba87cc399e84"
import spotipy
from spotipy.oauth2 import SpotifyOAut

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:4304/auth/spotify/callback",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="31pfkgb6s74ml353g5srdmeqtqju",
    )
)
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
