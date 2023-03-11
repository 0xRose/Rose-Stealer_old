@echo off & title %~nx0 & color 0C

goto :DOES_PYTHON_EXIST

:DOES_PYTHON_EXIST
python -V | find /v "Python" >NUL 2>NUL && (goto :PYTHON_DOES_NOT_EXIST)
python -V | find "Python"    >NUL 2>NUL && (goto :PYTHON_DOES_EXIST)
goto :EOF

:PYTHON_DOES_NOT_EXIST
echo Python is not installed on your system.
echo Running the installer now. Please install and then restart this terminal.
echo DONT FORGET TO ADD IT TO PATH. OPENED IMAGE IN YOUR BROWSER.
start https://imgur.com/a/KSG2G88
pause
cd tools
python-3.11.2-amd64.exe
goto :EOF

:PYTHON_DOES_EXIST
for /f "delims=" %%V in ('python -V') do @set ver=%%V
echo Looks good, %ver% is installed...
echo Ready to install requirements.
pause
cd tools
python -m pip install -r requirements.txt
python new_builder.py
goto :EOF
