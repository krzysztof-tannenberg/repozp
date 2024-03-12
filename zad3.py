def czy_parzysta(liczba):
    return liczba % 2 == 0

moja_liczba = 10

wynik = czy_parzysta(moja_liczba)

if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
