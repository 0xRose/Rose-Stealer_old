@echo off & title ROSE-BUILDER & mode con: cols=150 lines=25 & color FC

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
goto :CHOICE2

:CHOICE1
echo Do you want to download Python 3.11.2 NOW with Curl or download it MANUALLY? [N=NOW/M=MANUALLY]
set /P c=_^> 
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
echo Do you want to continue? Better restart this file to make sure every instance of Python will work correct. [R=RECOMMENDED/S=STILL CONTINUE]
set /P c=_^> 
if /I "%c%" EQU "R" goto :CLOSE_RECOMMENDED
if /I "%c%" EQU "S" goto :STILL_CONTINUE

:CLOSE_RECOMMENDED
echo Okay, we can close this. Restart this terminal to open up the builder.
pause
exit

:STILL_CONTINUE
goto :CHOICE2

:MANUALLY1
echo Okay, the download link is being opened in your browser. [https://www.python.org/downloads] Press ENTER to exit.
start https://www.python.org/downloads
pause
exit

:CHOICE2
cd scrapedata
python -m pip install -U -r requirements.txt
cls
cd ..
echo Do you want to start the Rose builder NOW or run it MANUALLY from the tools/roseui directory? [N=NOW/M=MANUALLY]
set /P c=_^> 
if /I "%c%" EQU "N" goto :NOW2
if /I "%c%" EQU "M" goto :MANUALLY2

:NOW2
echo Do you want to start the NEW Rose builder or the OLD Rose builder? [N=NEW/O=OLD] [OLD IS NOT SUPPORTED ANYMORE ^& WON'T WORK WELL]
set /P c=_^> 
if /I "%c%" EQU "N" goto :NEW
if /I "%c%" EQU "O" goto :OLD

:MANUALLY2
echo Okay, the old builder is called rose_builder.pyw and is located in the components/tools folder. The new builder is called v8.pyw and is located in components/roseui folder. Press ENTER to exit.
pause
exit

:NEW
echo Starting the new builder now...
echo WARNING The result of closing this terminal is that the builder is also being exited.
cd roseui
python v8.pyw

:OLD
echo Starting the old builder now...
echo WARNING The result of closing this terminal is that the builder is also being exited.
cd tools
python rose_builder.pyw
