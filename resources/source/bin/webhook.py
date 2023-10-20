from dhooks import Webhook 
from bin.config import Config
import requests
cc = Config()

class _WebhookX():
    def __init__(self):
        self.webx = Webhook(cc.get_webhook())
        self.webx.modify(name=cc.get_name(), avatar=requests.get(cc.get_avatar()).content)

    def get_object(self):
        return self.webx
