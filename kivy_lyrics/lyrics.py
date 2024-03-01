from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
import lyricsgenius
from textblob import TextBlob

from kivy_lyrics import secrets


class LyricsApp(App):
    def build(self):
        bara_sus = BoxLayout(orientation='vertical', padding=10, spacing=5)
        box_jos = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.enter = TextInput(hint_text='Numele melodiei', multiline=False, size_hint=(0.8, 1))
        self.enter.bind(on_text_validate=self.click_enter)
        box_jos.add_widget(self.enter)

        button = Button(text='Caută', size_hint=(0.2, 1), on_press=self.cauta_versurile, background_color=(0, 0, 0, 1))
        box_jos.add_widget(button)
        bara_sus.add_widget(box_jos)

        boxele_jos = BoxLayout(orientation='horizontal', size_hint=(1, 0.9))

        versurile = BoxLayout(orientation='vertical', size_hint=(0.5, 1))
        self.versuri = TextInput(multiline=True, readonly=True, font_size=15)
        versurile.add_widget(self.versuri)

        sentimentul = BoxLayout(orientation='vertical', size_hint=(0.5, 0.999))
        self.sentiment = AsyncImage(source='', size=(100, 100))
        sentimentul.add_widget(self.sentiment)

        boxele_jos.add_widget(versurile)
        boxele_jos.add_widget(sentimentul)
        bara_sus.add_widget(boxele_jos)

        return bara_sus

    def click_enter(self, instance):
        nume_melodie = self.enter.text
        self.versurile(nume_melodie)

    def cauta_versurile(self, instance):
        try:
            nume_melodie = self.enter.text
            self.versurile(nume_melodie)
        except Exception as e:
            print(f"Eroare în timpul căutării versurilor: {e}")

    def versurile(self, nume_melodie):
        api_key = secrets.api_key

        genius = lyricsgenius.Genius(api_key)
        melodie = genius.search_song(nume_melodie)

        if melodie:
            self.versuri.text = f"Informații: {melodie.title} de {melodie.artist}\n{melodie.lyrics}"
            self.afiseaza_sentiment_emoji(melodie.lyrics)
        else:
            self.versuri.text = f"Nu s-au găsit versuri pentru melodia {nume_melodie}"
            self.sentiment.source = ''

    def afiseaza_sentiment_emoji(self, versuri):
        total_sentiment = 0
        for vers in versuri.split('\n'):
            analiza_sentiment = TextBlob(vers)
            sentiment_vers = analiza_sentiment.sentiment.polarity
            total_sentiment += sentiment_vers

        calcul_sentimentului = total_sentiment / len(versuri.split('\n'))
        categoria_sentiment = obtine_categoria(calcul_sentimentului)
        emoji_source = gaseste_emoji(categoria_sentiment)
        self.sentiment.source = emoji_source


def obtine_categoria(sentiment):
    if sentiment > 0:
        return "pozitiv"
    elif sentiment < 0:
        return "negativ"
    else:
        return "neutru"


def gaseste_emoji(sentiment):
    if sentiment == "pozitiv":
        return "https://emojiisland.com/cdn/shop/products/16_large.png?v=1571606116"
    elif sentiment == "negativ":
        return ("https://images.rawpixel.com/image_800/"
                "cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTExL3JtNTg2YmF0Y2gyLWVtb2ppLTAwM18xLmpwZw.jpg")
    else:
        return "https://emojiisland.com/cdn/shop/products/Neutral_Face_Emoji_large.png?v=1571606037"


if __name__ == '__main__':
    LyricsApp().run()
