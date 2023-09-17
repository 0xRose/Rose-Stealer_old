@echo off
title ROSE-INSTALLER

REM Check if Python is installed
python --version >nul 2>nul
if errorlevel 1 (
    echo Python is not installed. Installing Python...

    REM Download Python 3.10.13 installer
    curl -o python-installer.exe https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe

    REM Install Python quietly with add to path, quiet, force, and all features
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    REM Remove the installer
    del python-installer.exe
) else (
    echo Python is installed.
)

REM Install dependencies
pip install colorama logging
cls

REM Run Python script
python components\install.py
