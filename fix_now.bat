@echo off
echo ========================================
echo FIXING VISHWAKARMA AI - QUICK FIX
echo ========================================
echo.

echo [1/3] Upgrading OpenAI from 0.27.2 to 1.x.x...
pip install --upgrade openai
echo.

echo [2/3] Installing python-dotenv...
pip install python-dotenv
echo.

echo [3/3] Fixing playsound (downgrading to 1.2.2)...
pip uninstall playsound -y
pip install playsound==1.2.2
echo.

echo ========================================
echo FIXES APPLIED!
echo ========================================
echo.
echo Verifying installations...
echo.
pip show openai | findstr "Version"
pip show python-dotenv | findstr "Version"
pip show playsound | findstr "Version"
echo.

echo ========================================
echo READY TO RUN!
echo ========================================
echo.
echo Now run: python run.py
echo.
pause
