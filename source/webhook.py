
from configuration import Config 
cc = Config()

class WebhookX():
    def __init__(self):
        self.webhook = cc.get_webhook()