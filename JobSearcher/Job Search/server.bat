REM vchealy 2021 - Use this as you wish
REM https://www.linkedin.com/in/vincenthealy/

REM This is Node.JS Back Server that pull info from the api

REM Minimise the cosole
if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit

echo off
mode con: cols=32 lines=10
cls
title Job Searcher
echo Job Server Activated
echo - - - - - - - - - - - 
echo *** Have Fun ***
echo - - - - - - - - - - - 

cd C:\VC_Healy\Node.JS\JobSearch\api
node server.js
timeout /t 10
