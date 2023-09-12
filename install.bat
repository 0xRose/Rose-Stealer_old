@echo off & title ROSE-INSTALLER & color F

setlocal EnableDelayedExpansion

REM Check if Python is installed
python --version 2>nul
if errorlevel 1 (
    echo Python is not installed.
    
    REM Download Python 3.10.13 installer
    curl -o python-installer.exe https://www.python.org/ftp/python/3.10.13/python-3.10.13-amd64.exe

    REM Install Python quietly with add to path, quiet, force, and all features
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    REM Remove the installer
    del python-installer.exe
) else (
    echo Python is installed.
)

REM Check if required modules are installed
for /f %%i in (components\scrapedata\requirements.txt) do (
    python -c "import %%i" 2>nul
    if errorlevel 1 (
        echo Installing %%i...
        pip install %%i
    )
)

REM Run start.vbs
call start.vbs

endlocal
