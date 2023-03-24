import os 
import shutil

shutil.rmtree('dist')
shutil.rmtree('build')
os.remove('main.spec')