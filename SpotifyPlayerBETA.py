import json
import requests
from SpotipyRefresh import Refresh

class SpotifyPlayer:

        # initialize our class variables
        def __init__(self):
            self.user_id = "zaeemghauri"    # my Spotify user ID
            self.spotify_token = ""         # the access token, new one will be generated by call_refresh()
            self.state = 0                  # state of player (0 = setup, 1 = playing music, 2 = controlling music)

            self.playlists_data = []        # stores name, uri, and id of each playlist
            self.playlist_name = ""         # name of playlist being listened to
            self.playlist_uri = ""          # uri of  playlist being listened to
            self.playlist_id = ""           # id of playlist being listened to

            self.track_data = []            # stores name and artists of each track
            self.track_name = ""            # name of track being listened to
            self.artists = ""               # artists of current track
            self.track_num = 0              # track number in playlist

            self.current_time = 0           # how far into the track you are
            self.duration_time = 0          # duration of track being listened to

            self.volume = 50                 # volume of playback

        # retrieves user's playlist names and uris
        def get_playlists(self):
            #print("Getting user's playlists...")

            query = "https://api.spotify.com/v1/users/{}/playlists".format(self.user_id)
            response = requests.get(query, headers={"Content-Type": "application/json",
                                                    "Authorization": "Bearer {}".format(self.spotify_token)})
            response_json = response.json()

            # add all playlist names and context uris to a list
            for item in response_json["items"]:
                self.playlists_data.append(item["name"])
                self.playlists_data.append(item["external_urls"]["spotify"])
                self.playlists_data.append(item["id"])

        # choose what playlist will be selected
        def set_playlist(self, item_num):
            # update class variables
            self.playlist_name = self.playlists_data[item_num]
            self.playlist_uri = self.playlists_data[item_num + 1]
            self.playlist_id = self.playlists_data[item_num + 2]

            self.get_tracks()

        # retrieves track data
        def get_tracks(self):
            #print("Getting track data...")
            self.track_data = [] # empty out previous track data

            query = "https://api.spotify.com/v1/playlists/{}/tracks".format(self.playlist_id)
            response = requests.get(query, headers={"Content-Type": "application/json",
                                                    "Authorization": "Bearer {}".format(self.spotify_token)})
            response_json = response.json()

            #  add all track names and artists from playlist into a list
            for item in response_json["items"]:
                self.track_data.append(item["track"]["name"])
                self.track_data.append(item["track"]["artists"][0]["name"])

        # retrieve track and artist names
        def set_tracks(self, track_num):
            # update class variables
            temp_name = self.track_data[track_num*2]
            self.artists = self.track_data[track_num*2 + 1]

            self.track_name = temp_name.split('(')[0].split('-')        # get rid of brackets and dashes in song names
            self.track_name = self.track_name[0]                        # this is to save space on LCD, make it look nicer

        # gets current time of song being listened to
        def get_time(self):
            #print("Getting current time of track...")

            query = "https://api.spotify.com/v1/me/player/currently-playing"
            response = requests.get(query, headers={"Content-Type": "application/json",
                                                    "Authorization": "Bearer {}".format(self.spotify_token)})
            response_json = response.json()
            self.current_time = response_json["progress_ms"]
            self.duration_time = response_json["item"]["duration_ms"]

            if (self.duration_time - self.current_time < 3000): # if song is within 3 seconds of finishing...
                self.track_num += 1                             # update to next track
                self.set_tracks(self.track_num)

        # start/resume music playback
        def play_music(self):
            #print("Playing music...")

            query = "https://api.spotify.com/v1/me/player/play"
            data = json.dumps({"context_uri": self.playlist_uri,
                               "offset": {"position": self.track_num},
                               "position_ms": self.current_time})
            response = requests.put(query, data, headers={"Content-Type": "application/json",
                                                          "Authorization": "Bearer {}".format(self.spotify_token)})
            self.set_tracks(self.track_num)
            #print(response)

        # pause music playback
        def pause_music(self):
            #print("Pausing music...")

            query = "https://api.spotify.com/v1/me/player/pause"
            response = requests.put(query, headers={"Content-Type": "application/json",
                                                    "Authorization": "Bearer {}".format(self.spotify_token)})

            self.get_time() # update current progress of track

        # go to next track
        def next_track(self):
            #print("Skipping to next track...")

            query = "https://api.spotify.com/v1/me/player/next"
            response = requests.post(query, headers={"Content-Type": "application/json",
                                                    "Authorization": "Bearer {}".format(self.spotify_token)})
            self.track_num += 1
            self.set_tracks(self.track_num)
            #print(response)

        # go to previous track
        def prev_track(self):
            #print("Skipping to prev track...")

            query = "https://api.spotify.com/v1/me/player/previous"
            response = requests.post(query, headers={"Content-Type": "application/json",
                                                    "Authorization": "Bearer {}".format(self.spotify_token)})
            self.track_num -= 1
            self.set_tracks(self.track_num)
            #print(response)

        # sets volume
        def adjust_volume(self):
            #print("Changing volume level...")

            query = "https://api.spotify.com/v1/me/player/volume?volume_percent={}".format(self.volume)
            response = requests.put(query, headers={"Content-Type": "application/json",
                                                    "Authorization": "Bearer {}".format(self.spotify_token)})

            #print(response)

        # REFRESH ACCESS TOKEN
        def call_refresh(self):
            #print ("Refreshing token...")
            
            refreshCaller = Refresh()
            self.spotify_token = refreshCaller.refresh() # new access token created

            self.get_playlists()