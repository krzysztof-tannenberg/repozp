class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Library: {self.street}, {self.city}, {self.zip_code}\n" \
               f"Open hours: {self.open_hours}\nPhone: {self.phone}\n"


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code

    def __str__(self):
        return f"Employee: {self.first_name} {self.last_name}\n" \
               f"Hire date: {self.hire_date}\nBirth date: {self.birth_date}\n" \
               f"Address: {self.street}, {self.city}, {self.zip_code}\n"


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Book: {self.author_name} {self.author_surname}\n" \
               f"Publication date: {self.publication_date}\n" \
               f"Number of pages: {self.number_of_pages}\n" \
               f"Available at: {self.library}\n"


class Order:
    def __init__(self, employee, student, books, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        order_info = f"Order by: {self.employee.first_name} {self.employee.last_name}\n" \
                     f"Order date: {self.order_date}\n" \
                     f"Student: {self.student}\n" \
                     f"Books:\n"
        for book in self.books:
            order_info += f"{book}\n"
        return order_info


# Tworzenie obiektów bibliotek
library1 = Library("New York", "Broadway 123", "10001", "9:00 - 18:00", "+1234567890")
library2 = Library("Los Angeles", "Hollywood Blvd 456", "90028", "10:00 - 20:00", "+1987654321")

# Tworzenie obiektów książek
book1 = Book(library1, "2022-01-01", "John", "Smith", 300)
book2 = Book(library1, "2021-12-15", "Emily", "Brown", 250)
book3 = Book(library2, "2021-11-20", "Michael", "Johnson", 400)
book4 = Book(library2, "2022-02-28", "Emma", "Williams", 350)
book5 = Book(library2, "2022-03-10", "Daniel", "Taylor", 280)

# Tworzenie obiektów pracowników
employee1 = Employee("Alice", "Jones", "2021-05-10", "1990-03-15", "New York", "Broadway 123", "10001")
employee2 = Employee("Bob", "Davis", "2020-12-01", "1985-08-20", "Los Angeles", "Hollywood Blvd 456", "90028")
employee3 = Employee("Eva", "Martinez", "2022-02-20", "1995-11-05", "Los Angeles", "Hollywood Blvd 456", "90028")

# Tworzenie obiektów zamówień
order1 = Order(employee1, "Student A", [book1, book3, book5], "2022-03-20")
order2 = Order(employee2, "Student B", [book2, book4], "2022-03-25")

# Wyświetlenie obu zamówień
print(order1)
print("\n")
print(order2)
