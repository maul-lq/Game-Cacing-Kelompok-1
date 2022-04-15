@echo off
@color 0f

@REM coba pakai ini jika terjadi error karena file tidak ditemukan!
cd "Include"

pyinstaller game.py -n "Game" -F -w -i "./res/ikon/ikon.ico" --clean --distpath "./bin/" --workpath "./bin/__temp__build/"
rmdir /S  /Q ".\bin\__temp__build"
rmdir /S  /Q ".\bin\res"
xcopy ".\res" ".\bin\res" /E/H/I