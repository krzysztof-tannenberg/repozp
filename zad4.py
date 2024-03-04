def wyswietl_co_drugi(lista):
    for i in range(0, len(lista), 2):
        print(lista[i])

# Utworzenie listy 10 liczb za pomocą funkcji range
lista_liczb = list(range(1, 21))  # Zakres od 1 do 20

# Wywołanie funkcji
wyswietl_co_drugi(lista_liczb)
