# if you dont have requests do "pip install requests"

import webbrowser
from requests import get
error = "Error! Error Code = "
id = input("Enter LevelID: ")
gd = get('https://gdbrowser.com/api/level/' + id)
songlink = gd.json()['songLink']
download = input("Do you want the song to open in browser?(Y/N): ")
if download == "Y":
 webbrowser.open(songlink)
 print(songlink)
elif download == "y":
 webbrowser.open(songlink)
 print(songlink)
elif download == "N":
 print(songlink)
elif download == "n":
 print(songlink)
else:
 print(error + "1") # no download
