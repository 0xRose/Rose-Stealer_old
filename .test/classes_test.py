import time 
import ctypes

MB_YESNO = 0x04
MB_HELP = 0x4000
ICON_STOP = 0x10
ctypes.windll.user32.MessageBoxW(0, "YOU BITCH L", "Error", MB_HELP | MB_YESNO | ICON_STOP)