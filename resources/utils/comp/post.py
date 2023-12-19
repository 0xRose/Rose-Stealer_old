import os
from sigthief import signfile

def RemoveMetaData(path: str):
    print("Removing MetaData")
    with open(path, "rb") as file:
        data = file.read()
    
    data = data.replace(b"PyInstaller:", b"PyInstallem:")
    data = data.replace(b"pyi-runtime-tmpdir", b"bye-runtime-tmpdir")
    data = data.replace(b"pyi-windows-manifest-filename", b"bye-windows-manifest-filename")
    
    with open(path, "wb") as file:
        file.write(data)

def AddCertificate(path: str):
    print("Adding Certificate")
    certFile = "resources/utils/comp/cert"
    if os.path.isfile(certFile):
        signfile(path, certFile, path)

def RenameEntryPoint(path: str, entryPoint: str):
    print("Renaming Entry Point")
    with open(path, "rb") as file:
        data = file.read()

    entryPoint = entryPoint.encode()
    new_entryPoint = b'\x00' + os.urandom(len(entryPoint) - 1)
    data = data.replace(entryPoint, new_entryPoint)

    with open(path, "wb") as file:
        file.write(data)

if __name__ == "__main__":
    builtFile = os.path.join("dist", "Built.exe")
    if os.path.isfile(builtFile):
        RemoveMetaData(builtFile)
        AddCertificate(builtFile)
        RenameEntryPoint(builtFile, "rose")
    else:
        print("Not Found")