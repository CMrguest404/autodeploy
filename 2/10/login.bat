@REM @Author: Eka Syahwan
@REM @Date:   2017-09-14 06:18:06
@REM @Last Modified by:   Byr1nC0deAjar
@REM Modified time: 2024-11-27 11:08:07
@echo off
C:\Python27\Scripts\pip.exe install pyperclip==1.6.0
set PATH=%PATH%;C:\Python27
title Auto Login GMAIL
:runsendinbox
python 31.py

pause
cls
goto runsendinbox