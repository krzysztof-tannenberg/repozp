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


