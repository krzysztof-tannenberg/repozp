def czy_parzysta(liczba):
    return liczba % 2 == 0

# Przykładowa liczba
moja_liczba = 10

# Wywołanie funkcji i zapisanie wyniku
wynik = czy_parzysta(moja_liczba)

# Wykorzystanie warunku logicznego do wyświetlenia odpowiedniego tekstu
if wynik:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
