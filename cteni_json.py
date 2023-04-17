import json

with open('absolventi.json') as prvni_soubor:
    data = prvni_soubor.read()

with open('absolventi.json', encoding='utf-8') as prvni_soubor:
    seznam_absolventu = json.load(prvni_soubor)

print(seznam_absolventu[0])    