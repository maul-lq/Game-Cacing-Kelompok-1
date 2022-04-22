@echo off
@color 0f

cd "Include"

pyinstaller game.py -n "Game Cacing" -F --key b'MM7ZQJpk8anrBIORj3YgyAdu5cnfaZZkI_E4_528bLw=' -w -i "./res/ikon/ikon.ico" --clean --distpath "./bin/" --workpath "./bin/__temp__build/"
rmdir /S  /Q ".\bin\__temp__build"
rmdir /S  /Q ".\bin\res"
xcopy ".\res" ".\bin\res" /E/H/I