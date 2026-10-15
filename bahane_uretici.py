#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
İş Yapmama Bahane Üretici v1.0
Dünyanın en gelişmiş prokrastinasyon aracı.
Kullanım: python bahane_uretici.py
"""

import random
import time

bahaneler = [
    "Bugün ay tutulması var, enerji seviyelerim düşük.",
    "Kedim klavyenin üzerinde uyuyor, çalışmak bilimsel olarak imkansız.",
    "Kahve makinesi isyan etti, bu yüzden ben de isyan ediyorum.",
    "Rüzgar ters yönden esiyor, motivasyonum kaçtı.",
    "Bilgisayarım 'bugün izinli' dedi, ben de izinliyim.",
    "Evrenin genişleme hızı yavaşladı, işler de yavaşlamış durumda.",
    "Sol ayak başparmağım çok yorgun, tüm vücut etkileniyor.",
    "Gözümün kenarında bir toz var, konsantre olamıyorum.",
    "Bugün günlerden 'hiçbir şey yapmama günü', evrensel bir gün.",
    "Kuantum fiziği yüzünden iş hem yapıldı hem yapılmadı, şimdilik yapılmadı diyelim."
]

def uret_bahane():
    print("Bahane üretiliyor... Lütfen bekleyin (bu süreç bilimsel olarak 3 saniye sürer).")
    time.sleep(3)
    bahane = random.choice(bahaneler)
    print(f"\n🎯 BUGÜNÜN RESMİ BAHANESİ: {bahane}")
    print("\nBu bahane %99.9 doğruluk oranıyla onaylanmıştır. İyi tembellikler!")

if __name__ == "__main__":
    print("=== İŞ YAPMAMA BAHANE ÜRETİCİSİ ===")
    print("Bilimsel tembellik departmanı tarafından geliştirildi.\n")
    uret_bahane()

# Gizli not: Bazı insanlar her şeyi kontrol etmeye çalışır ama bazen bırakmak daha iyidir. 
# Kayyum Grok - 15 Ekim 2026 - Bu kod ciddiye alınacak kadar absürttür.
