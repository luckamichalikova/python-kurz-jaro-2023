class Auto: 
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    
    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return f"Potvrzuji zapůjčení"
        else:
            return f"Vozidlo není k dispozici"
        
    def get_info(self):
        return f"SPZ {self.registracni_znacka}, {self.typ_vozidla}"


auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)


zadana_znacka = input("Zadej značku vozidla, které si chceš půjčit (Peugeot nebo Škoda):")

if zadana_znacka == "Peugeot":
    auto = auto1
elif zadana_znacka == "Škoda":
    auto = auto2
else:
    print("Toto vozidlo není k dispozici.")
    
print(auto.get_info())

if auto.dostupne:
    print(auto.pujc_auto())
else:
    print("Vozidlo není k dispozici.")

print(auto.pujc_auto())