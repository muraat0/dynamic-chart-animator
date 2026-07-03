@echo off
title Cinar Software - Grafik Animator Motoru
color 0B
echo ===================================================
echo     CINAR SOFTWARE GRAFIK ANIMATOR BASLATILIYOR
echo ===================================================
echo.
echo 1. Arka plan motoru (Python) calistiriliyor...
echo    Lutfen kullaniminiz bitene kadar BU SIYAH EKRANI KAPATMAYIN!
echo.

:: Arka planda app.py'yi çalıştır
start "Cinar Software Sunucu" cmd /k "python app.py"

:: Sunucunun hazır olması için 3 saniye bekle
timeout /t 3 /nobreak >nul

:: Müşterinin varsayılan tarayıcısında sistemi otomatik aç
echo 2. Arayuz tarayicida aciliyor...
start http://127.0.0.1:5001