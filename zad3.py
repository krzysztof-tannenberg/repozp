class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"Area: {self.area} sqm\nRooms: {self.rooms}\nPrice: ${self.price}\nAddress: {self.address}"


class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"House\n{super().__str__()}\nPlot size: {self.plot} sqm"


class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"Flat\n{super().__str__()}\nFloor: {self.floor}"


# Tworzenie obiektów
dom = House(200, 6, 350000, "ul. Wiejska 5", 500)

mieszkanie = Flat(80, 3, 150000, "ul. Podwale 10", 2)


print(dom)
print()
print(mieszkanie)
