class requirementsinstallation():
    try:
        import requests
    except Exception:
        import subprocess
        subprocess.run("python -m pip install requests", shell=True)

    import requests
    import subprocess
    import os

    requirementsurl = requests.get("https://raw.githubusercontent.com/DamagingRose/Rose-Injector/main/scrapedata/requirements.txt").text
    spliee = requirementsurl.split()
    done00:int = 0

    for split in spliee:
        os.system("color 7c")
        print(f"\n[INFO]: [Installing the missing libraries.... Wait till you see the finish message. ({done00}/{len(spliee)})]\n")
        subprocess.run(f"python -m pip install {split}", shell=True)
        subprocess.run("cls", shell=True)
        done00+=1
