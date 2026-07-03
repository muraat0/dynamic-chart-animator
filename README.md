# 📊 Dinamik Grafik Animatörü (Dynamic Chart Animator)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey?logo=flask)
![OpenCV](https://img.shields.io/badge/OpenCV-Image%20Processing-green?logo=opencv)
![License](https://img.shields.io/badge/License-MIT-blue)

Statik piyasa grafiklerini (örneğin CS2 skin fiyat geçmişleri) soldan sağa akıcı bir şekilde açılan, **kesin zaman ayarlı (6 saniye)** hareketli GIF animasyonlarına dönüştüren yapay zeka destekli web uygulaması. Python, OpenCV ve Flask tabanlı güçlü bir arka plan motoruna ve modern bir "Glassmorphism" arayüze sahiptir.

## ✨ Öne Çıkan Özellikler (V2 Güncellemeleri)

- **VDS/VPS RAM Optimizasyonu:** Animasyon kareleri (frame) bellekte ham olarak biriktirilmez. "Garbage Collector" (`gc`) ve anında sıkıştırma (on-the-fly quantization) mimarisiyle en düşük RAM'e sahip sunucularda bile `MemoryError` vermeden çalışır.
- **Orantısal Render Motoru (Proportional Timing):** Yüklenen grafiğin piksel genişliğinden bağımsız olarak, matematiksel interpolasyon ile animasyonu her zaman kusursuz bir şekilde 180 kareye (tam 6 saniyeye) böler.
- **Akıllı Renk Maskeleme:** OpenCV (`cv2.inRange`) kullanarak arayüzdeki buton ve metinleri korumak için üst %45'lik alanı izole eder, sadece grafik çizgisini algılar.
- **Kayıpsız Sıkıştırma (Color Quantization):** Arayüzün cam gibi keskinliğini bozmadan dosya boyutunu %50'ye kadar küçültmek için Pillow üzerinden Adaptif Renk Paleti Sıkıştırması (128 renk) kullanır.

## 🚀 Kurulum ve Çalıştırma

1. Repoyu bilgisayarınıza klonlayın:
   ```bash
   git clone [https://github.com/KULLANICI_ADIN/dynamic-chart-animator.git](https://github.com/KULLANICI_ADIN/dynamic-chart-animator.git)
   cd dynamic-chart-animator
