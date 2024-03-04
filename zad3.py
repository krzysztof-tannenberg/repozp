def wyswietl_parzyste(lista):
    for liczba in lista:
        if liczba % 2 == 0:
            print(liczba)

# Utworzenie listy 10 liczb za pomocą funkcji range
lista_liczb = list(range(1, 21))  # Zakres od 1 do 20

# Wywołanie funkcji
wyswietl_parzyste(lista_liczb)
