from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import sqlite3
import os

class MilyonerApp(App):
    def build(self):
        db_path = 'milyoner.db'
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        cursor.execute("CREATE TABLE IF NOT EXISTS sistem_ayar (anahtar TEXT PRIMARY KEY, deger TEXT NOT NULL)")
        cursor.execute("CREATE TABLE IF NOT EXISTS sorular (id INTEGER PRIMARY KEY AUTOINCREMENT, kategori TEXT, soru TEXT NOT NULL, siklar TEXT NOT NULL, cevap INTEGER NOT NULL, aktif INTEGER NOT NULL DEFAULT 1)")
        
        cursor.execute("INSERT OR IGNORE INTO sistem_ayar (anahtar, deger) VALUES ('banka_adi', 'Ziraat Bankasi')")
        cursor.execute("INSERT OR IGNORE INTO sistem_ayar (anahtar, deger) VALUES ('iban_sahibi', 'Mustafa Sonmez')")
        cursor.execute("INSERT OR IGNORE INTO sistem_ayar (anahtar, deger) VALUES ('aktif_iban', 'TR00 0000 0000 0000 0000 0000')")
        
        cursor.execute("SELECT COUNT(*) FROM sorular")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO sorular (kategori, soru, siklar, cevap) VALUES ('Tarih', 'Cumhuriyet hangi yil ilan edildi?', '1919|1920|1922|1923', 3)")
            cursor.execute("INSERT INTO sorular (kategori, soru, siklar, cevap) VALUES ('Bilim', 'Suyun kimyasal formulu nedir?', 'CO2|H2O|O2|NaCl', 1)")
            conn.commit()

        root = ScrollView()
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        layout.add_widget(Label(text="[b]MİLYONER PANELİ[/b]", markup=True, font_size=24, size_hint_y=None, height=50))

        cursor.execute("SELECT anahtar, deger FROM sistem_ayar")
        ayarlar = {row[0]: row[1] for row in cursor.fetchall()}
        
        layout.add_widget(Label(text="--- FİNANSAL AYARLAR ---", font_size=16, size_hint_y=None, height=30))
        layout.add_widget(Label(text=f"Banka: {ayarlar.get('banka_adi')}", size_hint_y=None, height=30))
        layout.add_widget(Label(text=f"IBAN Sahibi: {ayarlar.get('iban_sahibi')}", size_hint_y=None, height=30))
        layout.add_widget(Label(text=f"IBAN: {ayarlar.get('aktif_iban')}", size_hint_y=None, height=30))

        cursor.execute("SELECT soru, kategori FROM sorular WHERE aktif = 1")
        sorular = cursor.fetchall()
        
        layout.add_widget(Label(text="--- VERİTABANI SORULARI ---", font_size=16, size_hint_y=None, height=40))
        for q in sorular:
            layout.add_widget(Label(text=f"• {q[0]} ({q[1]})", size_hint_y=None, height=40))

        conn.close()
        root.add_widget(layout)
        return root

if __name__ == '__main__':
    MilyonerApp().run()
      
