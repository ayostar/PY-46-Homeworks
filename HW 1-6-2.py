class PersonWGrades:
    def __init__(self):
        self.grades = {}

    def average_grade(self):
        sum_of_grades = 0
        number_of_grades = 0

        for course_grades in self.grades.values():
            sum_of_grades += sum(course_grades)
            number_of_grades = number_of_grades + len(course_grades)

        return round(sum_of_grades / number_of_grades, 2)

    def average_grade_for_course(self, course):
        sum_of_grades = 0
        if course in self.grades.keys():
            course_grades = self.grades[course]
            sum_of_grades += sum(course_grades)
            return round(sum_of_grades / len(course_grades), 2)
        else:
            return 0

    def __lt__(self, other):
        if (isinstance(self, Lecturer) and isinstance(other, Student)) or (isinstance(self, Student) and isinstance(other, Lecturer)):
            return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if (isinstance(self, Lecturer) and isinstance(other, Student)) or (isinstance(self, Student) and isinstance(other, Lecturer)):
            return self.average_grade() > other.average_grade()

class Student(PersonWGrades):
    def __init__(self, name, surname, gender):
        super().__init__()
        # PersonWGrades.__init__()
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, mentor, course, grades_from_students):
        if isinstance(mentor, Lecturer) and course in self.courses_in_progress and course in mentor.courses_attached:
            if course in mentor.grades:
                mentor.grades[course] += [grades_from_students]
            else:
                mentor.grades[course] = [grades_from_students]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Student:\nИмя: {self.name}\n' \
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


class Lecturer(Mentor, PersonWGrades):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        PersonWGrades.__init__(self)

    def __str__(self):
        res = f'Lecturer:\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}\n'
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
        res = f'Reviewer:\nИмя: {self.name}\nФамилия: {self.surname}\n'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Pascal', 'Java']

cool_lecturer = Lecturer('Justin', 'Credible')
cool_lecturer.courses_attached += ['Python', 'Pascal', 'Java', 'Введение в программирование', 'Dart']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Pascal', 'Java', 'Введение в программирование', 'Dart']

cool_reviewer.rate_student_hw(best_student, 'Python', 5)
cool_reviewer.rate_student_hw(best_student, 'Python', 5)
cool_reviewer.rate_student_hw(best_student, 'Java', 10)
cool_reviewer.rate_student_hw(best_student, 'Pascal', 5)
cool_reviewer.rate_student_hw(best_student, 'Введение в программирование', 10)


best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Pascal', 10)

comparison_result = cool_lecturer < best_student
print(f'Хуже ли средняя оценка Лектора {cool_lecturer.name} {cool_lecturer.surname}, чем Студента {best_student.name}'
      f' {best_student.surname}?\n'
      f'Результат = {comparison_result}\n')



print(cool_reviewer)
print(cool_lecturer)
print(best_student)

cool_student = Student('Artem', 'Starodubtsev', 'your_gender')
cool_student.courses_in_progress += ['Python', 'Введение в программирование']

bad_student = Student('Bad', 'Santa', 'your_gender')
bad_student.courses_in_progress += ['Dart', 'Python']

best_lecturer = Lecturer('Stan', 'Allmighty')
best_lecturer.courses_attached += ['Python', 'Pascal', 'HTML', 'Java', 'Basic', 'C++', 'Введение в программирование', 'Dart']

bad_lecturer = Lecturer('Sto', 'Shagovnazad')
bad_lecturer.courses_attached += ['Python', 'Dart', 'HTML']

cool_student.rate_lecturer(cool_lecturer, 'Python', 10)
cool_student.rate_lecturer(best_lecturer, 'Введение в программирование', 10)

bad_student.rate_lecturer(cool_lecturer, 'Введение в программирование', 10)
bad_student.rate_lecturer(cool_lecturer, 'Dart', 10)

cool_reviewer.rate_student_hw(bad_student, 'Dart', 5)
cool_reviewer.rate_student_hw(bad_student, 'Введение в программирование', 5)
cool_reviewer.rate_student_hw(bad_student, 'Python', 5)

cool_reviewer.rate_student_hw(cool_student, 'Python', 5)
cool_reviewer.rate_student_hw(cool_student, 'Java', 5)
cool_reviewer.rate_student_hw(cool_student, 'Введение в программирование', 5)

student_list = [best_student, cool_student, bad_student]
lecturer_list = [best_lecturer, cool_lecturer, bad_lecturer]


def average_grade_for_course_extended(list_in, course):
    grade_sum = 0
    person_count = 0

    for person in list_in:
        average_per_course = person.average_grade_for_course(course)
        if average_per_course > 0:
            grade_sum += average_per_course
            person_count += 1

    if person_count > 0:
        return round(grade_sum / person_count, 2)
    else:
        return 'Курс сейчас не активен'


avg_grade_of_student = average_grade_for_course_extended(student_list, 'Python')
print(f'Среднияя оценка студентов по курсу Python: {avg_grade_of_student}')

avg_grade_of_student = average_grade_for_course_extended(student_list, 'Java')
print(f'Среднияя оценка студентов по курсу Java: {avg_grade_of_student}')

avg_grade_of_student = average_grade_for_course_extended(student_list, 'Pascal')
print(f'Среднияя оценка студентов по курсу Pascal: {avg_grade_of_student}')

avg_grade_of_student = average_grade_for_course_extended(student_list, 'Введение в программирование')
print(f'Среднияя оценка студентов по курсу Введение в программирование: {avg_grade_of_student}')

avg_grade_of_lecturer = average_grade_for_course_extended(lecturer_list, 'Python')
print(f'Среднияя оценка лекторов по курсу Python: {avg_grade_of_lecturer}')

avg_grade_of_lecturer = average_grade_for_course_extended(lecturer_list, 'Java')
print(f'Среднияя оценка лекторов по курсу Java: {avg_grade_of_lecturer}')

avg_grade_of_lecturer = average_grade_for_course_extended(lecturer_list, 'Pascal')
print(f'Среднияя оценка лекторов по курсу Pascal: {avg_grade_of_lecturer}')

avg_grade_of_lecturer = average_grade_for_course_extended(lecturer_list, 'Введение в программирование')
print(f'Среднияя оценка лекторов по курсу Введение в программирование: {avg_grade_of_lecturer}')
