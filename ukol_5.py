"""Mějme zadaný následující seznam naměřených teplot. 
Seznam obsahuje teploty naměřené pro každý den v týdnu ve čtyřech časech - ráno, v poledne, večer a v noci.

 1.Vytvoř seznam průměrných teplot pro každý den.
 2.Vytvoř seznam ranních teplot.
 3.Vytvoř seznam nočních teplot.
 4.Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu."""

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

# Seznam průměrných teplot pro každý den
prumerne_teploty = []
for den in teploty:
    prumerne_teploty.append(sum(den) / len(den))

print(prumerne_teploty)

# Seznam ranních teplot
ranni_teploty = []
for den in teploty:
    ranni_teploty.append(den[0])

print(ranni_teploty)

# Seznam nočních teplot
nocni_teploty = []
for den in teploty:
    nocni_teploty.append(den[3])

print(nocni_teploty)

# Seznamů obsahující pouze polední a noční teplotu
poledni_nocni_teploty = []
for den in teploty:
    poledni_nocni_teploty.append([den[0], den[3]])

print(poledni_nocni_teploty)


