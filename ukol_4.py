"""Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

    Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
    Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.

Tvůj program bude obsahovat dvě funkce:

    První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). 
    Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
    Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.

Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, 
v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

Tipy:

    Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
    Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420"."""

def over_telefonni_cislo(cislo):
    if cislo[0:4] == '+420' and len(cislo) == 13:
        return True
    elif len(cislo) == 9 and cislo.isnumeric():
        return True
    else:
        return False
def cena_zpravy(text):
    pocet_znaku = len(text)
    pocet_bloku = (pocet_znaku // 180)
    
    if pocet_znaku % 180 == 0:
        return pocet_bloku * 3
    else: 
        return (pocet_bloku + 1  ) * 3   
        

cislo = input("Zadej telefonní číslo: ")
if not over_telefonni_cislo(cislo):
    print("Zadané číslo není platné.")
else:
    text = input("Napiš zprávu: ")
    cena = cena_zpravy(text)
    print(f"Zpráva stojí {cena} Kč.")