#vysvedceni = {
 #   "cesky_jazyk": 1,
 #   "matematika" : 2,
 #   "dejepis" : 1,
#}

#predmety = ["cesky_jazyk", "matematika", "dejepis"]
#print(vysvedceni)


#sales = {
 #   "Zkus mě chytit": 4165,
 #   "Vrah zavolá v deset": 5681,
 #   "Zločinný steh": 2565,
#}

#sales["Noc, která mě zabila"] = 0
#print(sales)


#sales["Vrah zavolá v deset"] +=100
#print(sales)


#tombola = {
 #   7: "Láhev kvalitního vína Château Headache",
 #   15: "Pytel brambor z místního družstva",
 #   23: "Čokoládový dort",
 #   47: "Kniha o historii města",
  #  55: "Šiška salámu",
 #   67: "Vyhlídkový let balónem",
 #   79: "Moderní televizor",
 #   91: "Roční předplatné městského zpravodaje",
 #   93: "Společenská hra Sázky a dostihy",
#}


#cislo_listku = int(input("Jaké máš číslo lístku?"))
#if cislo_listku in tombola()

"""1. Vytvoř slovník, který reprezentuje vysvědčení.
#Klíč slovníku bude název předmětu a hodnota známka z daného předmětu.
#Pro zjednodušení vlož do slovníku pouze tři předměty (například český jazyk, matematiku a dějepis).
#Vypiš obsah slovníku pomocí funkce print()."""

#vysvedceni = {
#    "Český jazyk": 1,
#    "Matematika": 1,
#    "Dějepis": 1,
  
#}

#print(school_report)

"""2. Vydavatel detektivek si eviduje prodané kusy u jednotlivých knih.
V následujícím slovníku najdeš tři knihy a u každé z nich je počet prodaných kusů.
Přidej do slovníku nově vydanou detektivku "Noc, která mě zabila", která zatím nebyla uvedena na trh, je tedy prodáno 0 kusů.
U knihy "Vrah zavolá v deset" zvyš počet prodaných kusů o 100"""
#prodano = {
#    'Zkus mě chytit'     : 4165,
#    'Vrah zavolá v deset': 5681,
#    'Zločinný steh'      : 2565,
#}

#prodano["Noc, která mě zabila"] = 0
#prodano["Vrah zavolá v deset"] +=100



"""V následujícím slovníku jsou uložena čísla lístků tomboly a příslušné výhry."""

tombola = {
    7 : 'Láhev kvalitního vína Château Headache',
    15: 'Pytel brambor z místního družstva',
    23: 'Čokoládový dort',
    47: 'Kniha o historii města',
    55: 'Šiška salámu',
    67: 'Vyhlídkový let balónem',
    79: 'Moderní televizor',
    91: 'Roční předplatné městského zpravodaje',
    93: 'Společenská hra Sázky a dostihy',
}

"""cislo_listku = int (input("Zadej číslo lístku"))
if cislo_listku in tombola:
    print (f"Číslo {cislo_listku} vyhrává: {tombola[cislo_listku]}")
else: 
    print(f"Bohužel nevyhráváš nic")"""


cislo_uzivatele = int(input('Zadej sve cislo listku: '))

if cislo_uzivatele in tombola:
    vyhra = tombola[cislo_uzivatele]
else:
    vyhra = 'Bohužel nevyhráváš nic.'
print(f'Vyhrál jsi: {vyhra}')

