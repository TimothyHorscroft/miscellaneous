from selenium import webdriver
from time import sleep
import spotipy
import re

inpurl = "https://rateyourmusic.com/charts/top/single/2000s/"

# spotipy init
TIMOTHY = # SECRET
CLIENT_ID = # SECRET
CLIENT_SECRET = # SECRET

scope = "user-library-modify playlist-modify-public"

sp = spotipy.Spotify(auth_manager=spotipy.oauth2.SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri="http://localhost", scope=scope))
playlist = sp.user_playlist_create(TIMOTHY, "webscraping test", description=inpurl)

# selenium init
opts = webdriver.ChromeOptions()
opts.add_argument("--headless")
opts.add_argument("--disable-gpu")
opts.add_argument("--no-proxy-server")
opts.add_argument("--incognito")
driver = webdriver.Chrome(options=opts)
driver.implicitly_wait(5)

# program
driver.get(inpurl)
for i in range(1, 41):
    try:
        artist = driver.find_element_by_xpath(f"//div[@id='pos{i}']/div[@class='topcharts_textbox_top']/div[@class='topcharts_item_artist_newmusicpage topcharts_item_artist']/a").get_attribute("innerHTML")
    except:
        artist = "Prince"
    name = driver.find_element_by_xpath(f"//div[@id='pos{i}']/div[@class='topcharts_textbox_top']/div[@class='topcharts_item_title']/a").get_attribute("innerHTML").split(" / ")[0]
    obj = re.search(r"\(([^()]+)\)$", name)
    if obj:
        name = obj.group(1).rstrip()
    obj = re.search(r">\[(.+)\]<", artist)
    if obj:
        artist = obj.group(1)
    results = sp.search(f"{name} {artist}")
    if results['tracks']['items']:
        print("SUCCESS:", artist, "|", name)
        track = results['tracks']['items'][0]
        trackid = track['id']
        sp.user_playlist_add_tracks(TIMOTHY, playlist['id'], [trackid])
    else:
        print("    FAILURE:", artist, "|", name)

driver.close()
print("All Done!")
