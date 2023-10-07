class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}      

    def __lt__ (self,other):
        return self.average_grades() < other.average_grades()

    #task 2
    def rate_lecturer(self, lecturer, course, score):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.scores:
                lecturer.scores[course] += [score]
            else:
                lecturer.scores[course] = [score]
        else:
            return 'Ошибка'

    def average_grades(self):
        if self.grades:
            common_list = sum(self.grades.values(), start=[])
            return sum(common_list)/len(common_list)
        elif not self.grades:
            return "Нет оценок"    
                  
    def __str__(self):
        return f'Имя студента: {self.name} \n Фамилия: {self.surname}\
              \n Средняя оценка за домашние задания: {self.average_grades()}\
                \n Курсы в процессе изучения: {self.courses_in_progress}\
                  \nЗавершенные курсы: {self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.scores = {}

    def show_grades(self):
        print (f'В словаре у лектора: {self.scores}')    

#task 3
    def average_score(self):
        if self.scores:
            common_list = sum(self.scores.values(), start=[])
            return sum(common_list)/len(common_list)
        elif not self.scores:
            return "Нет оценок"
            
    def __str__(self):
        return f'Имя лектора: {self.name} \n Фамилия: {self.surname} \
              \n средняя оценка за лекции: {self.average_score()}' 
    
    def __lt__(self, other):
        return self.average_score() < other.average_score()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname) 
#task 2
    def rate_home_work(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached  and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"             
        
#task 3
    def __str__(self):
        return f'Имя ревьюера: {self.name} \n Фамилия: {self.surname}'


some_student1 = Student('Frodo', 'Baggins', 'Male')
some_student1.courses_in_progress+= ['Python']
some_student1.courses_in_progress+= ['Git'] 
some_student1.finished_courses += ['Введение в программирование']

some_reviewer1 = Reviewer('Bilbo', 'Baggins')
some_reviewer1.courses_attached += ['Python']
some_reviewer1.courses_attached += ['Git']
some_reviewer1.rate_home_work(some_student1, 'Python', 10)
some_reviewer1.rate_home_work(some_student1, 'Git', 5)

some_lecturer1 = Lecturer('Gandalf', 'Gray')
some_lecturer1.courses_attached += ['Python']
some_lecturer1.courses_attached += ['Git']
 
some_student1.rate_lecturer(some_lecturer1, 'Python', 9)
some_student1.rate_lecturer(some_lecturer1, 'Python', 10)
some_student1.rate_lecturer(some_lecturer1, 'Git', 8)

print(f"{some_reviewer1}\n")
print(f"{some_lecturer1}\n")
print(f"{some_student1}\n")

some_student2 = Student('Harry', 'Potter', 'Male')
some_student2.courses_in_progress+= ['Python']
some_student2.courses_in_progress+= ['Git']
some_student2.finished_courses += ['Введение в программирование']

some_reviewer2 = Reviewer('Severus', 'Snape')
some_reviewer2.courses_attached += ['Python']
some_reviewer2.courses_attached += ['Git']
some_reviewer2.rate_home_work(some_student2, 'Python', 8)
some_reviewer2.rate_home_work(some_student2, 'Git', 10)

some_lecturer2 = Lecturer('Albus', 'Dumbledore')
some_lecturer2.courses_attached += ['Python']
some_lecturer2.courses_attached += ['Git']

some_student2.rate_lecturer(some_lecturer2, 'Python', 9)
some_student2.rate_lecturer(some_lecturer2, 'Python', 5)
some_student2.rate_lecturer(some_lecturer2, 'Git', 10)

print(f"{some_reviewer2}\n")
print(f"{some_lecturer2}\n")
print(f"{some_student2}\n")

students_list= [some_student1,some_student2]
def average_all_students_grade_list(students_list,course):
    overall_grades=[]
    for student in students_list:
        for key, value in student.grades.items():
            if key==course:
                overall_grades +=value
    return sum(overall_grades)/len(overall_grades)

print(f"Средняя оценка студентов по курсам {'Python'}: {average_all_students_grade_list(students_list,'Python')}")

lectors_list= [some_lecturer1,some_lecturer2]
def average_all_lectors_grade_list(lectors_list,course):
    overall_grades=[]
    for lecturer in lectors_list:
        for key, value in lecturer.scores.items():
            if key==course:
                overall_grades +=value
    return sum(overall_grades)/len(overall_grades)

print(f"Средняя оценка лекторов по курсам {'Python'}: {average_all_lectors_grade_list(lectors_list,'Python')}")

print(f'Оценки студента {some_student1.name} больше оценки студента {some_student2.name} \n Ответ: {some_student1 < some_student2}')
print(f'Оценки лектора {some_lecturer1.name} больше оценки лектора {some_lecturer2.name} \n Ответ: {some_lecturer1 < some_lecturer2}')

