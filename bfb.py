from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
import tkinter as tk
from tkinter import filedialog
import psutil

#brightness
import screen_brightness_control as pct

#audio
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw  import AudioUtilities , IAudioEndpointVolume

#weather
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from  datetime import datetime
import requests
import pytz

#clock
from time import strftime

#cleander
from tkcalendar import *

#open google
import pyautogui

import subprocess
import webbrowser as wb
import random
 

root=Tk()
root.title('mac-soft Tool')
root.geometry("850x500+300+170")
root.resizable(False,False)
root.configure(bg='#292e2e')



#icon
image_icon=PhotoImage(file=)


root.mainloop()