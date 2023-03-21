import requests 
import time

def uploadToAnonfiles(path):
    for x in range(10): #Makes 10 tries to upload because gofile ratelimit is RAHHHHH
        try:
            rr = requests.post(
                f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile',
                files={
                    "file": open(path, "rb")
                },
            ).json()["data"]["downloadPage"]
            return rr
        except Exception as e:
            print(f'Advanced Eror: {e}')
            time.sleep(2)
    return False #If nothing worked we'll just return false 