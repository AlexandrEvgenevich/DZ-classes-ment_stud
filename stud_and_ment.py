courses = ['Python', 'C#', 'C++', 'Java']
students = []
lecturers = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students.append(self)

    def lect_grade(self, lect, course, grade):
        if isinstance(lect, Lecturer) and course in lect.courses_attached and course in self.courses_in_progress:
            if course in lect.grades:
                lect.grades[course] += [grade]
            else:
                lect.grades[course] = [grade]
        else:
            return 'Ошибка'

    def grad_mid(self):
        z = []
        for sgv in self.grades.values():
            for y in sgv:
                z.append(y)
        gm1 = (sum(z) / len(z))
        gm2 = ("{:1.1f}".format(gm1))
        return gm2

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.grad_mid()}\n\
Курсы в процессе изучения: {self.courses_in_progress}\n\
Завершенные курсы: {self.finished_courses}\n-----".replace("'", '').replace('[', '').replace(']', '')
        return text

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.grad_mid() < other.grad_mid()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturers.append(self)

    def grad_mid(self):
        z = []
        for lgv in self.grades.values():
            for y in lgv:
                z.append(y)
        gm1 = (sum(z) / len(z))
        gm2 = ("{:1.1f}".format(gm1))
        return gm2

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grad_mid()}\n-----"
        return text

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.grad_mid() < other.grad_mid()


class Reviewer(Mentor):
    def stud_grade(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}\n-----"
        return text


def stud_mid_grade(crs, std):
    cor_count = {}
    for curs in crs:
        a = curs
        for stud in std:
            for dk, dv in stud.grades.items():
                if a == dk:
                    if dk in cor_count:
                        cor_count[dk] += dv
                    else:
                        cor_count[dk] = dv
    for x, y in cor_count.items():
        count = []
        for z in y:
            count.append(z)
        print(f"средние оценки за домашние задания {x}: {sum(count) / len(count)}")
    print('+++++')


def lect_mid_grade(crs, lct):
    cor_count = {}
    for curs in crs:
        a = curs
        for stud in lct:
            for dk, dv in stud.grades.items():
                if a == dk:
                    if dk in cor_count:
                        cor_count[dk] += dv
                    else:
                        cor_count[dk] = dv
    for x, y in cor_count.items():
        count = []
        for z in y:
            count.append(z)
        print(f"средние оценки за лекции {x}: {sum(count) / len(count)}")
    print('+++++')


stud1 = Student('Cat', 'Catman', 'm')
stud1.courses_in_progress += ['Python', 'C#']
stud1.finished_courses += ['C++']

stud2 = Student('Dog', 'Dogman', 'm')
stud2.courses_in_progress += ['Java']

stud3 = Student('Loh', 'Lohman', 'm')
stud3.courses_in_progress += ['Python', 'C#']
stud3.finished_courses += ['C++']

stud4 = Student('Rak', 'Rakman', 'm')
stud4.courses_in_progress += ['C#', 'C++']

rev1 = Reviewer('Bat', 'Batman')
rev1.courses_attached += ['Python']

rev2 = Reviewer('Bot', 'Botman')
rev2.courses_attached += ['Java']

rev3 = Reviewer('Tor', 'Torman')
rev3.courses_attached += ['C#']

rev4 = Reviewer('Tor', 'Torman')
rev4.courses_attached += ['C++']

lect1 = Lecturer('Rat', 'Ratman')
lect1.courses_attached += ['Python']

lect2 = Lecturer('Dom', 'Domman')
lect2.courses_attached += ['Java']

rev1.stud_grade(stud1, 'Python', 10)
rev1.stud_grade(stud1, 'Python', 7)
rev1.stud_grade(stud3, 'Python', 3)
rev1.stud_grade(stud3, 'Python', 2)

rev2.stud_grade(stud2, 'Java', 8)

rev3.stud_grade(stud1, 'C#', 8)
rev3.stud_grade(stud4, 'C#', 2)

rev4.stud_grade(stud4, 'C++', 1)

stud1.lect_grade(lect1, 'Python', 10)
stud2.lect_grade(lect2, 'Java', 5)


print(stud1)
print(stud2)
print(stud3)
print(stud4)
print(rev1)
print(rev2)
print(rev3)
print(lect1)
print(lect2)

print(lect1 < lect2)
print(lect1 > lect2)

print(stud1 < stud2)
print(stud1 > stud2)

stud_mid_grade(courses, students)
lect_mid_grade(courses, lecturers)
