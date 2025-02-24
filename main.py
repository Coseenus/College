class ChatGPT:
    def __init__(self, first_name=None, last_name=None, birth_year=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year

    def calculate_course(self):
        if self.birth_year is None:
            return None
        current_year = 2025
        age = current_year - self.birth_year
        course = age - 16  # Припустимо, студент вступає у 17 років
        return course if 1 <= course <= 4 else None

    def name_list(self):
        """Повертає список з імені та прізвища."""
        return [name for name in [self.first_name, self.last_name] if name]


class Student(ChatGPT):
    def __init__(self, first_name=None, last_name=None, birth_year=None, student_id=None, faculty=None, average_grade=None):
        super().__init__(first_name, last_name, birth_year)  # Викликає конструктор батьківського класу
        self.student_id = student_id
        self.faculty = faculty
        self.average_grade = average_grade

    def _protected_method(self):
        """Захищений метод: виводить інформацію про студента."""
        info = f"Student ID: {self.student_id}, Name: {self.first_name} {self.last_name}, Faculty: {self.faculty}, Average Grade: {self.average_grade}"
        print(info)

    def __private_method(self):
        """Приватний метод: перевіряє, чи студент отримує стипендію (бал ≥ 90)."""
        return self.average_grade is not None and self.average_grade >= 90

    def check_scholarship(self):
        """Публічний метод, який використовує приватний метод."""
        if self.__private_method():
            print("✅ Студент отримує стипендію.")
        else:
            print("❌ Студент не отримує стипендію.")


student = Student("Andrii", "Shevchenko", 2006, "TVC1234", "Computer Engineering", 92)

print("Курс:", student.calculate_course())
print("Ім'я та прізвище:", student.name_list())

student._protected_method()
student.check_scholarship()
