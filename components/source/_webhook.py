from config import Config 
from dhooks import Embed
from __webhook import _WebhookX
cc = Config()

class WebhookX():
    def __init__(self):
        self.webx = _WebhookX().get_object()

    def locations_webhook(self, dictx):
        embed = Embed(
            description='Location Infos:',
            color=cc.get_color(),
            timestamp='now'  # sets the timestamp to current time
        )


        embed.set_author(name=cc.get_name(), icon_url=cc.get_avatar())
        embed.set_footer(text=cc.get_footer(), icon_url=cc.get_avatar())

        for j in dictx:
            print(j)
            zvalue = dictx[j]
            embed.add_field(name=j, value=f'`{zvalue}`')

        self.webx.send(embed=embed)
