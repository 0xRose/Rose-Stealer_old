@echo off
set "URL=https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe"
set "INSTALL_PATH=C:\Python311"

echo Scraping Python installer...
curl -o "%TEMP%\python-3.11.6-amd64.exe" %URL%

echo Starting installation...
echo This may take a while...
"%TEMP%\python-3.11.6-amd64.exe" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 SimpleInstall=1 TargetDir=%INSTALL_PATH%
setx PATH "%PATH%;C:\Python311"
del "%TEMP%\python-3.11.6-amd64.exe"
