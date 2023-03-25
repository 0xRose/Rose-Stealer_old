import os 
import shutil

try:
    shutil.rmtree('dist')
    shutil.rmtree('build')
    os.remove('main.spec')
except FileNotFoundError:
    pass