class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50

# Tworzenie dwóch przykładowych obiektów klasy Student
student1 = Student("John", [70, 65, 80, 90])
student2 = Student("Alice", [40, 35, 45, 50])

# Sprawdzenie, czy studenci zaliczyli
print(f"Czy {student1.name} zaliczył: {student1.is_passed()}")  # Powinno zwrócić True
print(f"Czy {student2.name} zaliczył: {student2.is_passed()}")  # Powinno zwrócić False
