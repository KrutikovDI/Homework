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
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'   
    def __average_grade(self):
        sum_grade = 0
        number_grade = 0
        for i in self.grades.values():
            number_grade += len(i)
            for k in i:
                sum_grade += k
        return sum_grade / number_grade    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__average_grade()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\n'
        return res
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такого студента нет')
            return 
        return self.__average_grade() < other.__average_grade()
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __average_grade(self):
        sum_grade = 0
        number_grade = 0
        for i in self.grades.values():
            number_grade += len(i)
            for k in i:
                sum_grade += k
        return sum_grade / number_grade    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_grade()}\n'
        return res
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого лектора нет')
            return 
        return self.__average_grade() < other.__average_grade()
                
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}/nФамилия: {self.surname}'
        return res


student1 = Student('Иван', 'Иванов', 'мужчина')
student1.courses_in_progress += ['Python']
student1.add_courses('Java')
student1.add_courses('JavaScript')
student2 = Student('Петр', 'Петров', 'мужчина')
student2.courses_in_progress += ['Python']
student2.add_courses('JavaScript')

lector1 = Lecturer('Ольга', 'Хотова')
lector1.courses_attached += ['Python']
lector2 = Lecturer('Денис', 'Ветров')
lector2.courses_attached += ['Python']

reviewer1 = Reviewer('Наталья', 'Дорова')
reviewer2 = Reviewer('Сергей', 'Сидоров')

student1.rate_hw(lector1, 'Python', 9)
student1.rate_hw(lector2, 'Python', 7)
student2.rate_hw(lector1, 'Python', 10)
student1.rate_hw(lector1, 'Python', 2)
student2.rate_hw(lector2, 'Python', 8)

reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 10)

print(student1)
print(student2)
print(lector1)
print(lector2)
print(student1 < student2)
print(lector1 < lector2)

students_list = [student1, student2]
def average_grade_all_students(list_student, course_name):
    sum_grade = 0
    number_grade = 0
    for i in list_student:
        for k in i.grades[course_name]:
            sum_grade += k
            number_grade += 1
    return f'Средняя оценка за лекции всех студентов в рамках курса {course_name}: {sum_grade / number_grade}'

lecturer_list = [lector1, lector2]
def average_grade_all_lecturer(list_lecturer, course_name):
    sum_grade = 0
    number_grade = 0
    for i in list_lecturer:
        for k in i.grades[course_name]:
            sum_grade += k
            number_grade += 1
    return f'Средняя оценка за лекции всех лекторов в рамках курса {course_name}: {sum_grade / number_grade}'
    
print(average_grade_all_students(students_list, 'Python'))
print(average_grade_all_lecturer(lecturer_list, 'Python'))     
