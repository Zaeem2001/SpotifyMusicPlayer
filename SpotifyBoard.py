import serial
import time
from SpotifyPlayerBETA import SpotifyPlayer

#SERIAL COMMUNICATION WITH BOARD
arduino = serial.Serial(port='COM3', baudrate=9600, timeout = 2)  # establish serial communication with arduino board
player = SpotifyPlayer()

def send_info(sending):
    arduino.flush()
    arduino.write(sending.encode())
    time.sleep(0.25)    # 250ms delay

time.sleep(1)
player.call_refresh() # refresh token at beginning of each run
playlist_num = 0      # start at the first playlist during setup
player.set_playlist(playlist_num)
send_info(player.playlist_name)     # send initial info

# continuously read data coming in from board and complete action based on specific (button) request
while 1:
    recieving = arduino.readline()
    recieving = recieving.decode()

    #COMMANDS
    # SET UP STATE
    if (player.state == 0):

        if (recieving == 'LEFT\n' and playlist_num >= 3):       # (1): PREV PLAYLIST
            playlist_num -= 3
            player.set_playlist(playlist_num)
            send_info(player.playlist_name)

        elif (recieving == 'RIGHT\n' and playlist_num < 38):    # (2): NEXT PLAYLIST
            playlist_num += 3
            player.set_playlist(playlist_num)
            send_info(player.playlist_name)

        elif (recieving == 'SELECT\n'):     # (3): START MUSIC
            player.adjust_volume()
            player.play_music()
            send_info(player.artists)
            time.sleep(1)
            send_info(player.track_name)
            player.state = 2

    # PLAYING MUSIC STATE
    elif (player.state == 1):
        if (recieving == 'SELECT\n'):     # (1): RESUME MUSIC
            player.play_music()
            Send_info(player.artists)
            time.sleep(1)
            send_info(player.track_name)
            player.state = 2

    # CONTROLLING PLAYBACK STATE
    elif (player.state == 2):
         if (recieving == 'SELECT\n'):    # (1): PAUSE
            player.pause_music()
            player.state = 1

         elif (recieving == 'RIGHT\n'):   # (2): SKIP
            player.next_track()

         elif (recieving == 'LEFT\n' and player.track_num != 0):    # (3): BACK
            player.prev_track()

         elif (recieving == 'UP\n' and player.volume <= 95):      # (4): RAISE VOLUME
            player.volume += 5
            player.adjust_volume()

         elif (recieving == 'DOWN\n' and player.volume >= 5):    # (5): LOWER VOLUME
            player.volume -= 5
            player.adjust_volume()

         else:
            time.sleep(0.5)               # POLLING EVERY 500 MILLISECONDS TO UPDATE TRACK INFO
            player.get_time()
            send_info(player.artists)
            time.sleep(1)
            send_info(player.track_name)