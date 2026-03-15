class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = []

    def add_grades(self):
        n = int(input(f"Сколько оценок добавить для {self.name} {self.surname}? "))
        for i in range(n):
            i=i+1
            grade = int(input(f"Введите оценку: "))
            self.grades.append(grade)

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def show_info(self):
        print(self.name, self.surname, self.age, self.get_average_grade())


class Course:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Имя студента: ")
        surname = input("Фамилия студента: ")
        age = int(input("Возраст студента: "))
        student = Student(name, surname, age)
        self.students.append(student)
        print(f"Студент {name} {surname} добавлен!")

    def choose_student(self):
        if not self.students:
            print("Нет студентов!")
            return None
        print("Выберите студента по номеру:")
        for i, s in enumerate(self.students):
            print(i + 1, s.name, s.surname)
        idx = int(input()) - 1
        if 0 <= idx < len(self.students):
            return self.students[idx]
        print("Неверный выбор!")
        return None

    def show_all_students(self):
        if not self.students:
            print("Студентов нет")
        for s in self.students:
            s.show_info()

    def show_best_student(self):
        if not self.students:
            print("Нет студентов")
            return
        best = max(self.students, key=lambda s: s.get_average_grade())
        print("Лучший студент:")
        best.show_info()


course = Course()

while True:
    print("\nМеню:")
    print("1. Добавить студента")
    print("2. Добавить оценки студенту")
    print("3. Показать всех студентов")
    print("4. Показать лучшего студента")
    print("5. Показать средний балл студента")
    print("6. Выйти")

    choice = input("Выберите действие: ")

    if choice == "1":
        course.add_student()
    elif choice == "2":
        student = course.choose_student()
        if student:
            student.add_grades()
    elif choice == "3":
        course.show_all_students()
    elif choice == "4":
        course.show_best_student()
    elif choice == "5":
        student = course.choose_student()
        if student:
            print(f"Средний балл {student.name} {student.surname}: {student.get_average_grade()}")
    elif choice == "6":
        break
    else:
        print("Неверный выбор!")