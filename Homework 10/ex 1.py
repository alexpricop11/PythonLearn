import re
import requests
from collections import Counter
url = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"
response = requests.get(url)
text = response.text
text = re.sub(r'\W', ' ', text.lower())
cuvinte = text.split()
numar_total_cuvinte = len(cuvinte)
frecventa_cuvinte = Counter(cuvinte)
top_50_utilizate = frecventa_cuvinte.most_common(50)
top_50_putin_utilizate = frecventa_cuvinte.most_common()[:-51:-1]
print(f"Numărul total de cuvinte: {numar_total_cuvinte}")
print("\nTop 50 cele mai utilizate cuvinte:")
for cuvant, frecventa in top_50_utilizate:
    print(f"{cuvant}: {frecventa}")
print("\nTop 50 cele mai puțin utilizate cuvinte:")
for cuvant, frecventa in top_50_putin_utilizate:
    print(f"{cuvant}: {frecventa}")