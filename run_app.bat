@echo off
title FC Barcelona Match Analytics Hub
cls
echo ==========================================================
echo       FC BARCELONA MATCH ANALYTICS HUB
echo       Temporadas 2024/25, 2025/26 y 2026/27
echo ==========================================================
echo.
echo Liberando puerto 8501 si estuviera ocupado...
for /f "tokens=5" %%a in ('netstat -aon ^| find ":8501" ^| find "LISTENING"') do (
    taskkill /F /PID %%a >nul 2>&1
)

echo.
echo Iniciando servidor Streamlit local (Zero-Tokens)...
echo.
echo Abre tu navegador en: http://localhost:8501
echo (Para detener la app, cierra esta ventana)
echo.

.\venv\Scripts\streamlit.exe run app.py --server.port 8501 --server.headless false

pause
