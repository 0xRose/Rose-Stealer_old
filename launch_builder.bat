@echo off & title %~nx0 & color 0C

goto :DOES_PYTHON_EXIST

:DOES_PYTHON_EXIST
python -V | find /v "Python" >NUL 2>NUL && (goto :PYTHON_DOES_NOT_EXIST)
python -V | find "Python"    >NUL 2>NUL && (goto :PYTHON_DOES_EXIST)

:PYTHON_DOES_NOT_EXIST
echo Python is not installed on your system.
goto :CHOICE1

:PYTHON_DOES_EXIST
for /f "delims=" %%V in ('python -V') do @set ver=%%V
echo Looks good, %ver% is installed...
goto :INSTALL_REQUIREMENTS

:INSTALL_REQUIREMENTS
echo Installing requirements...
cd scrapedata
python -m pip install -r requirements.txt
goto :CHOICE2

:CHOICE1
set /P c=Do you want to download Python 3.11.2 NOW with Curl or download it MANUALLY? [N/M] 
if /I "%c%" EQU "N" goto :NOW1
if /I "%c%" EQU "M" goto :MANUALLY1

:NOW1
cd tools
curl -o python-installer.exe https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe
echo Running the installer now. PLEASE INSTALL AND THEN RESTART THIS TERMINAL.
echo DONT FORGET TO ADD IT TO PATH. OPENED TUTORIAL IMAGE IN YOUR BROWSER.
start https://imgur.com/a/KSG2G88
pause
python-installer.exe
echo Deleting the installer now.
echo WARNING | ONLY CONTINUE IF THE INSTALLATION IS COMPLETED.
pause
taskkill /f /im python-installer.exe
del /P python-installer.exe

:MANUALLY1
echo Okay, the download link is being opened in your browser. [https://www.python.org/downloads] Press ENTER to exit.
start https://www.python.org/downloads
pause
exit

:CHOICE2
set /P c=Do you want to start the Rose builder NOW or run it MANUALLY from the tools directory? [N/M] 
if /I "%c%" EQU "N" goto :NOW2
if /I "%c%" EQU "M" goto :MANUALLY2

:NOW2
echo Starting the builder now...
cd tools
python rose_builder.pyw
echo WARNING | Closing this results that the builder is also being exited.

:MANUALLY2
echo Okay, the builder is called rose_builder.pyw and is located in the tools folder. Press ENTER to exit.
pause
exit