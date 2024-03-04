import argparse
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


def main(city=None):
    # Pobranie danych z API
    url = 'https://api.openbrewerydb.org/v1/breweries?per_page=20'
    if city:
        url += f"&by_city={city}"
    response = requests.get(url)
    breweries_data = response.json()

    # Utworzenie listy instancji klasy Brewery
    breweries_list = [Brewery(brewery) for brewery in breweries_data]

    # Wyświetlenie liczby zwróconych wyników
    print(f"Liczba zwróconych wyników: {len(breweries_list)}\n")

    # Wyświetlenie informacji o każdej browarze
    for brewery in breweries_list:
        print(brewery)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", help="City to filter breweries")
    args = parser.parse_args()

    main(args.city)


# python zad8.py --city=Berlin
