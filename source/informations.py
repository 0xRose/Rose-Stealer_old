from json import loads
import getpass

from urllib.request import Request, urlopen

class Info():
    def __init__(self):
        self.ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()

    def get_ip(self):
        return self.ip

    def global_info(self):
        ipdatanojson = (urlopen(Request(
            f"https://geolocation-db.com/jsonp/{self.ip}")).read().decode().replace(
                "callback(", "").replace("})", "}"))
        ipdata = loads(ipdatanojson)
        obj = {
            "Country": ipdata["country_name"],
            "City": ipdata["city"],
            "Postal": ipdata["postal"],
            "Latitude": ipdata["latitude"],
            "Longitude": ipdata["longitude"],
            "State": ipdata["state"]
        }
        return obj

    @staticmethod
    def get_username():
        return getpass.getuser()
