def forem(lista):
    wynik = []
    for liczba in lista:
        wynik.append(liczba * 2)
    return wynik

# Przykładowa lista liczb
lista_liczb = [1, 2, 3, 4, 5]

# Wywołanie funkcji
wynik_for = forem(lista_liczb)
print(wynik_for)


def lista(lista):
    return [liczba * 2 for liczba in lista]

# Przykładowa lista liczb
lista_liczb = [1, 2, 3, 4, 5]

# Wywołanie funkcji
wynik_list_comprehension = lista(lista_liczb)
print(wynik_list_comprehension)
