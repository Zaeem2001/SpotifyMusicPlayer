import serial
import time
from SpotifyPlayerBETA import SpotifyPlayer

#SERIAL COMMUNICATION WITH BOARD
arduino = serial.Serial(port='COM3', baudrate=9600, timeout = 2)  # establish serial communication with arduino board
player = SpotifyPlayer()

player.call_refresh() # refresh token at beginning of each run
playlist_num = 0      # start at the first playlist during setup
send_info(player.playlist_name)     # send initial info


def send_info(sending):
    arduino.flush()
    arduino.write(sending.encode())
    time.sleep(0.25)    # 250ms delay

# continuously read data coming in from board and complete action based on specific (button) request
while 1:
    recieving = arduino.readline()
    recieving = recieving.decode()

    #COMMANDS
    # SET UP STATE
    if (player.state == 0):

        if (recieving == 'LEFT\n' and playlist_num >= 2):       # (1): PREV PLAYLIST
            playlist_num -= 2
            player.get_playlists(playlist_num)
            send_info(player.playlist_name)

        elif (recieving == 'RIGHT\n' and playlist_num < 38):    # (2): NEXT PLAYLIST
            playlist_num += 2
            player.get_playlists(playlist_num)
            send_info(player.playlist_name)

        elif (recieving == 'SELECT\n'):     # (3): START MUSIC
            player.play_music()
            player.state = 2

     # PLAYING MUSIC STATE
     elif (player.state == 1):
         if (recieving == 'SELECT\n'):     # (1): RESUME MUSIC
             player.play_music()
             player.state = 2

     # CONTROLLING PLAYBACK STATE
     else:
         if (recieving == 'SELECT\n'):   # (2): PAUSE
            player.pause_music()
            player.state = 1
