try:
    from tabulate import tabulate
except Exception:
    import subprocess
    subprocess.run('python -m pip install tabulate', check=True)

class FileX:
    def table_wifi(self, data):
        listx = [["SSID", "Password"]]

        for value in data:
            listx.append([value["ssid"], value["password"]])

        tablex = tabulate(listx, headers="firstrow", tablefmt="grid")
        return tablex
