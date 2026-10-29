@echo off
setlocal
set "PATH=%~dp0.hyperframes\bin;%PATH%"
cd /d "%~dp0out\mission-entry\video"
"%~dp0.hyperframes\bin\node.exe" "%ProgramFiles%\nodejs\node_modules\npm\bin\npx-cli.js" --yes hyperframes@0.8.198 preview --background
if errorlevel 1 (pause & exit /b 1)
start "" "http://localhost:3002/#project/video"
