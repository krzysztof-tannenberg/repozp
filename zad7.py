import requests


class Brewery:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.brewery_type = data['brewery_type']
        self.address_1 = data['address_1']
        self.address_2 = data['address_2']
        self.address_3 = data['address_3']
        self.city = data['city']
        self.state_province = data['state_province']
        self.postal_code = data['postal_code']
        self.country = data['country']
        self.longitude = data['longitude']
        self.latitude = data['latitude']
        self.phone = data['phone']
        self.website_url = data['website_url']
        self.state = data['state']
        self.street = data['street']

    def __str__(self):
        return f"ID: {self.id}\nName: {self.name}\nType: {self.brewery_type}\nAddress: {self.address_1}, {self.city}, {self.state_province}, {self.postal_code}\nWebsite: {self.website_url}\n"


# Pobranie danych z API
response = requests.get('https://api.openbrewerydb.org/v1/breweries?per_page=20')
breweries_data = response.json()

# Utworzenie listy instancji klasy Brewery
breweries_list = [Brewery(brewery) for brewery in breweries_data]

print(f"Liczba zwróconych wyników: {len(breweries_list)}\n")

for brewery in breweries_list:
    print(brewery)
