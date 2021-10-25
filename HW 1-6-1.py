class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_cool_lecturer(self, cool_lecturer, course, grades_from_students):
        if isinstance(cool_lecturer, Lecturer) and course in self.courses_in_progress and course in cool_lecturer.courses_attached:
            if course in cool_lecturer.grades_from_students:
                cool_lecturer.grades_from_students[course] += [grades_from_students]
            else:
                cool_lecturer.grades_from_students[course] = [grades_from_students]
        else:
            return 'Ошибка'

    def average_grade(self):
        sum_of_grades = 0
        number_of_grades = 0

        for course_grades in self.grades.values():
            sum_of_grades += sum(course_grades)
            number_of_grades = number_of_grades + len(course_grades)

        return round(sum_of_grades / number_of_grades, 2)

    def __str__(self):
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашние задания: {self.average_grade()}\n' \
              f'Курсы в процессе обучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}\n'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades_from_students = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grades_from_students}\n'
        return res


class Reviewer(Mentor):
    def rate_student_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            student.add_courses(course)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Pascal', 'Введение в программирование']

cool_lecturer = Lecturer('Justin', 'Credible')
cool_lecturer.courses_attached += ['Python', 'Pascal', 'HTML', 'Java']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Pascal']

cool_reviewer.rate_student_hw(best_student, 'Python', 10)
cool_reviewer.rate_student_hw(best_student, 'Python', 8)
cool_reviewer.rate_student_hw(best_student, 'Pascal', 8)
cool_reviewer.rate_student_hw(best_student, 'HTML', 8)

best_student.rate_cool_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_cool_lecturer(cool_lecturer, 'Pascal', 10)
best_student.rate_cool_lecturer(cool_lecturer, 'HTML', 7)



print(cool_reviewer)
print(cool_lecturer)
print(best_student)
