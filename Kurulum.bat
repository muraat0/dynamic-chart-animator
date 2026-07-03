@echo off
title Cinar Software - Sistem Kurulumu
color 0A
echo ===================================================
echo     CINAR SOFTWARE GEREKSINIMLERI YUKLENIYOR
echo ===================================================
echo.
echo Lutfen bekleyin, gerekli kutuphaneler internetten indiriliyor...
echo Bu islem bilgisayarinizin hizina gore 1-2 dakika surebilir.
echo.

pip install -r requirements.txt

echo.
echo ===================================================
echo KURULUM TAMAMLANDI! Bu pencereyi kapatabilirsiniz.
echo Artik sistemi 'Baslat.bat' uzerinden calistirabilirsiniz.
echo ===================================================
pause