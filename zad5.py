def czy_zawiera_wartosc(lista, wartosc):
    return wartosc in lista

moja_lista = [1, 2, 3, 4, 5]
moja_wartosc = 2

wynik_sprawdzenia = czy_zawiera_wartosc(moja_lista, moja_wartosc)

print(wynik_sprawdzenia)
