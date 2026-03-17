import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath('..'))

sound = 'lizard-button.mp3'
path = Path(sound).resolve()

print(path)

from Helpers import installLibs
installLibs.install_package("playsound")

from playsound import playsound
import keyboard
import requests

if installLibs.worked == True:
    def playSound():
        playsound(os.path.abspath(sound))
        
    keyboard.add_hotkey('space',playSound)

    keyboard.wait('esc')
    
else:
    print("did not work")


 