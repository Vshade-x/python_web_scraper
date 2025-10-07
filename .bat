@echo off
cls
echo.
echo ======================================================
echo           INICIANDO RASTREO WEB DE DATOS
echo ======================================================

REM Llama al interprete de Python para ejecutar el script
"C:\Program Files\Python311\python.exe" web_scraper.py

echo.
echo ======================================================
echo   PROCESO TERMINADO. Revisa el archivo reporte_libros.csv
echo ======================================================

pause