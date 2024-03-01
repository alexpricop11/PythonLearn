def analiza_text():
    sir = input("Introdu un text: ")
    cate_cuvinte = sir.split()
    numar_de_cuvinte = len(cate_cuvinte)
    print(f'in acest text sunt {numar_de_cuvinte} cuvinte')
    lung = max(cate_cuvinte, key=len)
    scurt = min(cate_cuvinte, key=len)
    print(f"Cel mai lung cuvant este {lung} si cel mai scurt este {scurt}")
    lungimea_medie = sum(len(cuvant) for cuvant in cate_cuvinte)/ numar_de_cuvinte
    print(f'Lungimea medie a sirului este {round(lungimea_medie)}')
    litere_mari = sir.upper()
    litere_mici = sir.lower()
    print(f'Textul convertit in litere mare este {litere_mari} '
          f'\nSi textul convertit in litere mici este {litere_mici}')
    inlocuire = sir.replace(' ', '_')
    print(f'Textul cu spatiile inlocuite este {inlocuire}')


analiza_text()