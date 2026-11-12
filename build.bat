@echo off
rem Builds KS_QR.exe into this folder. Needs Python installed.
cd /d "%~dp0"
if not exist .venv py -m venv .venv
.venv\Scripts\python -m pip install -q "qrcode[pil]" pyinstaller
rem -m instead of pyinstaller.exe: that launcher hardcodes the venv path and breaks if this folder moves
.venv\Scripts\python -m PyInstaller --onefile --name KS_QR --distpath . ks_qr.py
