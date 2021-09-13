# Spotify Music Player
## Made by Zaeem Ghauri

### What is this?

The purpose of this project was to create a physical board/player that controls music playback on Spotify. No more interruptions during your current PC activity in order to pull up
the Spotify desktop app just to skip a song. Or waiting forever for the sound overlay to disappear after adjusting your volume. With control's literally within your hand's reach,
Spotify playback has never been easier!

### How does it work?

The board itself consists of 5 push buttons (wired as pull-down resistors) and an LCD screen connected to an Arduino UNO microcontroller. The Arduino is then connected via USB to
the PC that's running the Spotify desktop application and Python script. The LCD screen is used to display playback information such as playlist name, track name, and artists. 
Each button press on the board is detected by the Arduino which sends the corresponding instruction to the Python script via USB (UART communciation). The Python script follows
the instruction by issuing requests to the Spotify server with the help of Spotify web API. If needed, the script will send data back to the Arduino to update the LCD display.

### How to get an authorization token?

There are two ways to obtain authorization for Spotify; a temporary token that expires in roughly 1 hour, or a permanent (refreshing) token that won't expire for a *long* time.
The temporary token is a lot easier to accquire, but it can also be tedious having to create and enter a new one after every hour. The permanent token takes more time, but for an application like this, that may be used several times a day, its well worth it.

TEMPORARY TOKEN
1. Go to https://developer.spotify.com/console/get-several-albums/ and scroll to "OAuth Token" near the bottom of the page.

2. Select "get token" and choose the following scopes: user-modify-playback-state, user-read-currently-playing, user-read-playback-state, playlist-read-private, and playlist-read-collaborative. The generated token should show up in the input parameter right next to the "get token" button.

3. In the "SpotifyPlayerBETA.py" file, copy and paste your token into the variable "self.spotify_token".

4. Comment out or delete all instances of "SpotipyRefresh" or anything pertaining to it:
   - "from SpotipyRefresh import Refresh" beginning of file.
   - The entirety of the "call_refresh" function at the end of the file.

5. Finally, in the "SpotifyBoard.py" file, change "player.call_refresh()" at line 19 to "player.get_playlists". Now you can run the code without the "SpotipyRefresh.py" and "SpotipySecrets.py" files.
   
PERMANENT TOKEN
1. Create a new app through the SpotifyforDevelopers page (https://developer.spotify.com/dashboard/), the name and description doesn't matter.
   
   *NOTE: You will need to have a Spotify account and login*

2. Go to your app's page, then to "edit settings", then to "redirect URIs" and enter a URL. This will be a link to a page that you will be redirected to during the authorization process. This URL doesn't have to be to a real website so choose anything!

3. Fill in the client ID and redirect URI parameters for the following authorization request: 
https://accounts.spotify.com/authorize?client_id=CLIENTID&response_type=code&redirect_uri=REDIRECTURI&scope=user-modify-playback-state%20user-read-currently-playing%20user-read-playback-state%20playlist-read-private%20playlist-read-collaborative

   - The client ID can be found in your app page (left side, under "App Status").
   - The redirect URI is the URI you chose in the app settings (step 2), however it must be URL encoded! Simply copy and paste the plain URL into https://www.urlencoder.org/ and encode.

4. Copy and paste the request from step 3 into your browser. This will take you to your redirect URI which will now contain the parameter "code" to be extracted; 
   ex. URI?code=uRf6VG9V8c3lTJMoL...    => extract the "uRf6VG9V8c3lTJMoL..."

5. Fill in the base 64 paramter, the code (extracted from step 4), and the redirect URI (encoded same as step 3) in the following CURL request:
curl -H "Authorization: Basic BASE64" -d grant_type=authorization_code -d code=CODE -d redirect_uri=URI https://accounts.spotify.com/api/token --ssl-no-revoke

   - The "BASE64" parameter is the "client id:client secret" encoded in base 64. Your client secret can be found in your app page under client ID. Simply copy and paste the client id followed by a semi-colon and then the client secret (no spaces before, after, or between) into https://www.base64encode.org/ and encode. Copy and paste this into "SpotipySecrets.py" as the variable "base_64".

6. Finally, Copy and paste the completed CURL request into Windows command line. It should return a bunch of text that includes your access token, scope, and refresh token. What we're interested in however is the refresh token, so copy and paste that into "SpotipySecrets.py" as the variable "refresh_token". Your "SpotipySecrets.py" file should contain only those two variables (just like the one provided in this repository). All you have to do now is run the code!
 
### How do I use it?

1. Connect the Arduino and board to your PC running the desktop application for Spotify, and then run the Python script.
   
   *NOTE: You still need the desktop application installed and running in order to use this board. This is NOT a replacement for the software itself.*
   
2. Cycle through your playlists with the left and right buttons and then choose the playlist you would like to listen to with the select button. The playlist name will 
   appear on the board's LCD screen.
   
3. Control music playback with the buttons:
   - left to go to the previous track
   - right to go to the next track
   - select to pause or resume playback
   - up to turn up the volume
   - down to turn down the volume 

### Future changes:

This project is a prototype. There are so so many ideas that come to mind when thinking about where I can go with this project:

- **Make it wireless!** The USB connection isn't a constraint as the board does have to be within hand's reach. However, having the connection between PC and board be wireless
  would allow for better wire management and more portability. This could be done with wifi or bluetooth modules that communicate with the Arduino.
  
- **Make it touch!** Instead of pressing buttons, what if the user could swipe or tap a screen to control their music. Using a TFT touch-screen, controls and playback information could
  be laid out almost like a Spotify app. This would eliminate the need for buttons and the LCD screen, and of course, all the wires and resistors connecting them.
  
- **Make it simple!** Originally I had planned for the board to only *control* track playback; go to the next track, previous track, or pause/resume playback. Eventually I let my
  imagination get the best of me and now I have a board that can also let you choose the playlist, control the volume, and display all this information. A lite version of this 
  project could be a simple remote that allows for a simpler control.
  
### Visit [my website](https://zaeem2001.github.io/projects/spotifyplayer.html) to see my project in action!
