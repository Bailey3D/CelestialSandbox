@echo off
REM Activate the Python virtual environment
call %~dp0venv\Scripts\activate.bat

REM Install requirements if requirements.txt exists
if exist %~dp0requirements.txt pip install -r %~dp0requirements.txt
