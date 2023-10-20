@echo off && color b
setlocal EnableDelayedExpansion

REM Step 1: Check if Python is installed
title Looking for Python...
python --version >nul 2>nul
if errorlevel 1 (
    echo Python is not installed. Installing...
    
    REM Step 2: Install Python silently
    
    REM Define variables
    set "URL=https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe"
    set "INSTALL_PATH=C:\Python311"

    REM Download Python installer
    curl -o "%TEMP%\python-3.11.5-amd64.exe" %URL%

    REM Install Python silently
    "%TEMP%\python-3.11.5-amd64.exe" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 SimpleInstall=1 TargetDir=%INSTALL_PATH%

    REM Add Python to system PATH
    setx PATH "%INSTALL_PATH%;%PATH%"

    REM Clean up downloaded installer
    del "%TEMP%\python-3.11.5-amd64.exe"
    
    REM Close and reopen the console to apply PATH changes
    exit
) else (
    echo Python is installed.
)

REM Step 3: Change console title
title Creating venv...
echo Creating venv...

REM Step 4: Create venv
python -m venv myvenv

REM Step 5: Change console title
title Entering venv...
echo Entering venv...

REM Step 6: Activate venv
call myvenv\Scripts\activate

REM Step 7: Change console title
title Installing packages...
echo Installing packages...

REM Step 8: Install modules from requirements.txt
pip install --upgrade --force-reinstall --ignore-installed --requirement resources\data\requirements.txt

REM Step 9: Change console title
title Starting builder...
echo Starting builder...

REM Step 10: Run builder.py
title Rose UI Builder

python resources\ui\builder.py

REM Step 11: End local environment
endlocal
