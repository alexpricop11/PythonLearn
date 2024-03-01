from googletrans import LANGUAGES, Translator

# Afisează toate limbile disponibile și codurile lor de limbă
for language_code, language_name in LANGUAGES.items():
    print(f"{language_code}: {language_name}")
