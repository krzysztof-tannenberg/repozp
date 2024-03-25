from zad1 import Student
from zad2 import Library, Employee, Book, Order

# ______ zad1

# Dwa obiekty klasy Student
student1 = Student("John", [70, 65, 80, 90])
student2 = Student("Alice", [40, 35, 45, 50])

# Sprawdzenie, czy studenci zaliczyli
print(f"Czy {student1.name} zaliczył: {student1.is_passed()}")  # True
print(f"Czy {student2.name} zaliczył: {student2.is_passed()}")  # False


# ______ zad2
print(f"\n::::: Zadanie 2 :::::\n")

# Tworzenie obiektów
library1 = Library("New York", "Broadway 123", "10001", "9:00 - 18:00", "+1234567890")
library2 = Library("Los Angeles", "Hollywood Blvd 456", "90028", "10:00 - 20:00", "+1987654321")

book1 = Book(library1, "2022-01-01", "John", "Smith", 300)
book2 = Book(library1, "2021-12-15", "Emily", "Brown", 250)
book3 = Book(library2, "2021-11-20", "Michael", "Johnson", 400)
book4 = Book(library2, "2022-02-28", "Emma", "Williams", 350)
book5 = Book(library2, "2022-03-10", "Daniel", "Taylor", 280)

employee1 = Employee("Alice", "Jones", "2021-05-10", "1990-03-15", "New York", "Broadway 123", "10001")
employee2 = Employee("Bob", "Davis", "2020-12-01", "1985-08-20", "Los Angeles", "Hollywood Blvd 456", "90028")
employee3 = Employee("Eva", "Martinez", "2022-02-20", "1995-11-05", "Los Angeles", "Hollywood Blvd 456", "90028")

order1 = Order(employee1, "Student A", [book1, book3, book5], "2022-03-20")
order2 = Order(employee2, "Student B", [book2, book4], "2022-03-25")

print(order1)
print("\n")
print(order2)
