@echo off
setlocal EnableDelayedExpansion

:: Step 1: Check if Python is installed
title Looking for Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo "Python is not installed. Installing..."
    
    :: Step 2: Install Python silently
    
    :: Define variables
    set "URL=https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe"
    set "INSTALL_PATH=C:\Python311"

    :: Download Python installer
    curl -o "%TEMP%\python-3.11.5-amd64.exe" %URL%

    :: Install Python silently
    "%TEMP%\python-3.11.5-amd64.exe" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 SimpleInstall=1 TargetDir=%INSTALL_PATH%

    :: Add Python to system PATH
    setx PATH "%INSTALL_PATH%;%PATH%"

    :: Clean up downloaded installer
    del "%TEMP%\python-3.11.5-amd64.exe"
    
    :: Close and reopen the console to apply PATH changes
    exit
)

:: Step 3: Change console title
title Creating venv...

:: Step 4: Create venv
python -m venv myvenv

:: Step 5: Change console title
title Entering venv...

:: Step 6: Activate venv
call myvenv\Scripts\activate

:: Step 7: Change console title
title Installing packages...

:: Step 8: Install modules from requirements.txt
pip install --upgrade --force-reinstall --ignore-installed --requirement resources\data\requirements.txt

:: Step 9: Change console title
title Starting builder...

:: Step 10: Run builder.py
title Rose UI Builder

python resources\ui\builder.py

:: Step 11: End local environment
endlocal
