"""Vyvíjíš software pro obchod s elektronickými součástkami. 
Firma eviduje informace o počtu součástek na skladě ve slovníku. 
Klíč slovníku je kód součástky a hodnota klíče je počet součástek na skladě.

1.  Napiš software, který bude využívat prodavač v případě,
    že do obchodu přijde zákazník. Software se nejprve zeptá na kód součástky
    a poté na množství, které si zákazník chce koupit. Obě informace si ulož. 
    Následně naprogramuj následující varianty:

2.  Pokud zadaný kód není ve slovníku, není součástka skladem.
    Vypiš tedy zprávu, že součástka není skladem.
3.  Pokud zadaná součástka na skladě je, ale je jí méně,
    než požaduje zákazník, vypiš text o tom, 
    že lze prodat pouze omezené množství kusů. 
4.  Následně součástku odeber ze slovníku, protože je vyprodaná.
    Pokud zadaná součástka na skladě je a je jí dostatek, 
    vypiš informaci, že poptávku lze uspokojit v plné výši, 
    a sniž počet součástek na skladě o množství požadované zákazníkem."""


sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

#Nevím, jestli jsem dobře pochopila, takže 2 varianty, liší se jen úvodem

#1.varianta
soucastka_kod = input("Zadej kod součástky")

if soucastka_kod in sklad:
    soucastka_mnozstvi = int(input("Zadej množství"))
    
    if sklad[soucastka_kod]>=soucastka_mnozstvi:
        print("Poptávku lze uspokojit v plné výši")
        sklad[soucastka_kod]=sklad[soucastka_kod]-soucastka_mnozstvi
        print(sklad)
       
    else:
        print("K dispozici je omezené množství kusů")
        soucastka_mnozstvi=sklad.pop(soucastka_kod)
        print(sklad)
    
else:  print("Součástka není skladem")
     
#2.varianta
soucastka_mnozstvi = int(input("Zadej množství"))
if soucastka_kod in sklad:
      
    if sklad[soucastka_kod]>=soucastka_mnozstvi:
        print("Poptávku lze uspokojit v plné výši")
        sklad[soucastka_kod]=sklad[soucastka_kod]-soucastka_mnozstvi
        print(sklad)
       
    else:
        print("K dispozici je omezené množství kusů")
        soucastka_mnozstvi=sklad.pop(soucastka_kod)
        print(sklad)
    
else:  print("Součástka není skladem")
     


