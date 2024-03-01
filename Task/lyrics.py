import lyricsgenius
from textblob import TextBlob


def obtine_categoria(sentiment):
    if sentiment > 0:
        return "pozitiv"
    elif sentiment < 0:
        return "negativ"
    else:
        return "neutru"


def afiseaza_versuri(cantec):
    if not cantec.lyrics:
        print(f'Cantecul {cantec.title} de {cantec.artist} nu are versuri sau nu le gasesc')
        return
    print(f"Informatii: {cantec.title} de {cantec.artist}")
    print(f"Versurile pentru {cantec.title}")
    print(cantec.lyrics)


def analizeaza_sentiment_versuri(versuri):
    total_sentiment = 0
    for vers in versuri.split('\n'):
        analiza_sentiment = TextBlob(vers)
        sentiment_vers = analiza_sentiment.sentiment.polarity
        total_sentiment += sentiment_vers

    calcul_sentimentului = total_sentiment / len(versuri.split('\n'))
    categoria_sentiment = obtine_categoria(calcul_sentimentului)
    print(f'Sentimentul cantecului: {categoria_sentiment}')


def analizeaza_sentiment(api_key, nume_cantec):
    genius = lyricsgenius.Genius(api_key)
    cantec = genius.search_song(nume_cantec)

    if cantec:
        afiseaza_versuri(cantec)
        analizeaza_sentiment_versuri(cantec.lyrics)
    else:
        print(f"Nu s-au gasit versuri pentru cantecul {nume_cantec}")


if __name__ == '__main__':
    api_key = "tYOw4vcdXqtTl44eDUJPAC-Ou10CgfB_KmHO5gP_ssOXfqTt9TRMhYObRQwcz7ScgCY9JEm-YHtfDWm5DxYihA"
    nume_cantec = input("Introduceti numele cantecului: ")
    analizeaza_sentiment(api_key, nume_cantec)
