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
  
