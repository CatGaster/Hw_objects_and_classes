class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
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
                  

#task 3    
    def __str__(self):
        return f'Имя студента: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за домашние задания: {self.average_grades()} \n Курсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}'


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
        return f'Имя лектора: {self.name} \n Фамилия: {self.surname} \n средняя оценка за лекции: {self.average_score()}' 


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
    

some_student = Student('Frodo', 'Baggins', 'Male')
some_student.courses_in_progress+= ['Python']
some_student.courses_in_progress+= ['Git'] 
some_student.finished_courses += ['Введение в программирование']

some_reviewer = Reviewer('Bilbo', 'Baggins')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
some_reviewer.rate_home_work(some_student, 'Python', 10)
some_reviewer.rate_home_work(some_student, 'Git', 9)

some_lecturer1 = Lecturer('Gandalf', 'Gray')
some_lecturer1.courses_attached += ['Python']
some_lecturer1.courses_attached += ['Git']
 
some_student.rate_lecturer(some_lecturer1, 'Python', 9)
some_student.rate_lecturer(some_lecturer1, 'Python', 10)
some_student.rate_lecturer(some_lecturer1, 'Git', 8)

some_student1 = Student('Ruoy', 'Eman', 'Male')
print(some_reviewer)
print()

print(some_lecturer1)
some_lecturer1.show_grades()

print()
print(some_student)

some_student2 = Student('Harry', 'Potter', 'Male')
some_student2.courses_in_progress+= ['Python']
some_student2.courses_in_progress+= ['Git']
some_student2.finished_courses += ['Введение в программирование']

# some_lecturer2 = Lecturer('Albus', 'Dumbledore')
# some_lecturer2.courses_attached += ['Python']
# some_lecturer2.courses_attached += ['Git']

print(some_student2)

