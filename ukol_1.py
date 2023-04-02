"""Napiš program, který bude obsahovat jednu proměnnou jmeno
Tato proměnná bude obsahovat libovolné křestní jméno (třeba tvoje). Tvůj program vytvoří e-mailovou adresu na základě této proměnné, s doménou czechitas.cz a tuto e-mailovou adresu vypíše"""

jmeno = "Lucka"
print(f"{jmeno}@czechitas.cz") 

# všechna písmena velká (vypíše např. JANA MALÁ)
jmeno_a_prijmeni = input("Zadej své jméno a prijmení:")
print(jmeno_a_prijmeni.upper())

# všechna písmena malá (vypíše např. jana malá)
jmeno_a_prijmeni = input("Zadej své jméno a příjmení:")
print(jmeno_a_prijmeni.lower())

# standardní varianta - první písmeno velké, další malá (vypíše např. Jana Malá)
jmeno_a_prijmeni = input("Zadej své jméno a příjmení:")
print(jmeno_a_prijmeni)


# iniciály (vypíše např. J. M.)
jmeno = input("Zadej jméno:")
prijmeni = input("Zadej prijmeni:")
inicialy = jmeno[0] + prijmeni[0]
print("Iniciály:", (jmeno[0] + "." + " " + prijmeni[0] + ".").upper())


"""křestní jméno zkrácené na první písmeno a příjmení, 
pokud je křestní jméno delší než 5 znaků
Jinak vypíše standardní variantu, tj. první písmeno velké,
další malá (u vstupu Jarmila Malá by došlo ke zkrácení
křestního jména, zatímco u vstupu Jana Malá nikoliv)"""

jmeno = input("Zadej jméno:")
prijmeni = input("Zadej prijmeni:")
delka_jmena = len(jmeno)

if delka_jmena >5:
    zkracene_jmeno = (jmeno[0]).upper()
    print(zkracene_jmeno + "." + " " + prijmeni)
else: 
    print(jmeno + " " + prijmeni)