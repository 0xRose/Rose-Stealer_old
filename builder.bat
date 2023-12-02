@echo off
color 4
setlocal EnableDelayedExpansion
title Looking for Python...

where python >nul 2>nul
if errorlevel 1 (
    echo Python is not installed. Installing...
    set "URL=https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe"
    set "INSTALL_PATH=C:\Python311"
    Invoke-WebRequest -Uri %URL% -OutFile "$env:TEMP\python-3.11.6-amd64.exe"
    Start-Process -Wait -FilePath "$env:TEMP\python-3.11.6-amd64.exe" -ArgumentList "/quiet", "InstallAllUsers=1", "PrependPath=1", "Include_test=0", "SimpleInstall=1", "TargetDir=%INSTALL_PATH%"
    set "PATH=%INSTALL_PATH%;%PATH%"
    del "$env:TEMP\python-3.11.6-amd64.exe"
    pause
    exit
) else (
    echo Python is installed.
)

title Creating venv...
echo Creating venv...
python -m venv myvenv

title Entering venv...
echo Entering venv...
call myvenv\Scripts\activate

title Installing packages...
echo Installing packages...
pip install --upgrade --force-reinstall --ignore-installed --requirement resources\data\requirements.txt

title Starting builder...
echo Starting builder...
start /min cmd.exe /k "python resources\ui\builder.py"

endlocal
pause
