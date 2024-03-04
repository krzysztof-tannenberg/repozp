def operacje_na_listach(lista1, lista2):
    # Połączenie list
    polaczona_lista = lista1 + lista2

    # Usunięcie duplikatów
    unikalna_lista = list(set(polaczona_lista))

    # Podniesienie każdego elementu do potęgi 3
    potegi_3 = [x ** 3 for x in unikalna_lista]

    return potegi_3


# Przykładowe listy
lista1 = [1, 2, 3]
lista2 = [3, 4, 5]

# Wywołanie funkcji i zwrócenie wyniku
wynik = operacje_na_listach(lista1, lista2)

# Wyświetlenie wyniku
print(wynik)
