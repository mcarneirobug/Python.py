import webbrowser
import time
import os

url     = ('https://www.youtube.com/watch?v=6qpCMck9njQ&t=3s')
refresh = ('20')
brow    = ('firefox')

def OpenUrl():
        print('Sucesso viwed.')
        os.system('killall -9 ' + brow)
        webbrowser.open(url)
        time.sleep(int(refresh))


while True:
        OpenUrl()
