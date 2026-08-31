from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class MilyonerApp(App):
    def build(self):
        root = ScrollView()
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        layout.add_widget(Label(text="[b]MİLYONER PANELİ[/b]", markup=True, font_size=24, size_hint_y=None, height=50))
        
        # Finansal Bilgiler
        layout.add_widget(Label(text="--- FİNANSAL AYARLAR ---", font_size=16, size_hint_y=None, height=30))
        layout.add_widget(Label(text="Banka: Ziraat Bankasi", size_hint_y=None, height=30))
        layout.add_widget(Label(text="IBAN Sahibi: Mustafa Sonmez", size_hint_y=None, height=30))
        layout.add_widget(Label(text="IBAN: TR00 0000 0000 0000 0000 0000", size_hint_y=None, height=30))

        # Sorular
        layout.add_widget(Label(text="--- VERİTABANI SORULARI ---", font_size=16, size_hint_y=None, height=40))
        sorular = [
            ("Cumhuriyet hangi yil ilan edildi?", "Tarih"),
            ("Suyun kimyasal formulu nedir?", "Bilim"),
            ("12 x 5 kac eder?", "Matematik"),
            ("Dunyanin en buyuk okyanusu hangisidir?", "Genel Kultur"),
            ("Turkiye'nin baskenti neresidir?", "Genel Kultur")
        ]
        
        for soru, kategori in sorular:
            layout.add_widget(Label(text=f"• {soru} ({kategori})", size_hint_y=None, height=40))

        root.add_widget(layout)
        return root

if __name__ == '__main__':
    MilyonerApp().run()
        
