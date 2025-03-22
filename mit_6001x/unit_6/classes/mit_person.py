import datetime


class Person(object):
    def __init__(self, name):
        """create a person called name"""
        super().__init__()
        self.name = name
        self.birthday = None
        self.last_name = name.split(" ")[-1]

    def get_last_name(self):
        """return self's last name"""
        return self.last_name

    def __str__(self):
        """returns self's name"""
        return self.name

    def set_birthday(self, month, day, year):
        """sets self's birthday to birth date"""
        self.birthday = datetime.date(year, month, day)

    def get_birthday(self):
        return self.birthday

    def get_age(self):
        """returns self's current age in days"""
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """return True if self's name is lexicographically less
        than other's name, and False otherwise"""
        if self.last_name == other.last_name:
            return self.name < other.name
        return self.last_name < other.last_name


p1 = Person("Mark Zuckerberg")
p1.set_birthday(5, 14, 84)
p2 = Person("Drew Houston")
p2.set_birthday(3, 4, 83)
p3 = Person("Bill Gates")
p3.set_birthday(10, 28, 55)
p4 = Person("Andrew Gates")
p5 = Person("Steve Wozniak")
person_list = [p1, p2, p3, p4, p5]

for e in person_list:
    print(e)
print()
person_list.sort()
for e in person_list:
    print(e)


class MITPerson(Person):
    next_id_num = 0  # next ID number to assign

    def __init__(self, name):
        super().__init__(name)  # initialize Person attributes
        self.id_num = MITPerson.next_id_num
        MITPerson.next_id_num += 1

    def get_id_num(self):
        return str(self.id_num).zfill(3)

    # Sorting MIT people uses their ID numbers, not names!
    def __lt__(self, other):
        return self.id_num < other.id_num

    def speak(self, utterance):
        return self.name + " says: " + utterance


print()
print("***********")
print("MIT People")
m1 = MITPerson("Drew Houston")
print(m1.get_id_num())
Person.set_birthday(m1, 3, 4, 1983)
print(m1.get_birthday())
m2 = MITPerson("Mark Zuckerberg")
print(m2.get_id_num())
Person.set_birthday(m2, 5, 14, 84)
m3 = MITPerson("Bill Gates")
Person.set_birthday(m3, 10, 28, 55)

MITPerson_list = [m1, m2, m3]
print()
print(m1.speak("hi there"))
MITPerson_list.sort()
for e in MITPerson_list:
    print(e)
print("*****************")
print()
print("UG Class\n")


class Student(MITPerson):
    pass


class UG(Student):
    """Class UG"""

    def __init__(self, name, class_year):
        MITPerson.__init__(self, name)
        self.year = class_year

    def get_class(self):
        return self.year

    def speak(self, utterance):
        return MITPerson.speak(self, " Yo Bro, " + utterance)


class Grad(Student):
    pass


class TransferStudent(Student):
    pass


def is_student(obj):
    return isinstance(obj, UG) or isinstance(obj, Grad)


s1 = UG("Matt Damon", 2017)
s2 = UG("Ben Affleck", 2017)
s3 = UG("Lin Manuel Miranda", 2018)
s4 = Grad("Leonardo di Caprio")
s5 = TransferStudent("Robert deNiro")

ug1 = UG("Mat Damon", 2019)
ug2 = UG("Drew Houston", 2017)
ug3 = UG("Ben Affleck", 2019)
ug4 = UG("Mark Zuckerberg", 2017)

g1 = Grad("Bill Gates")
g2 = Grad("Steve Wozniak")

student_list = [s1, s2, s3, s4, s5]

print(s1)
print(s1.get_class())
print(s1.speak("where is the quiz?"))
print(s2.speak("I have no clue!"))


class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department

    def speak(self, utterance):
        new = "In course " + self.department + " we say "
        return MITPerson.speak(self, new + utterance)

    def lecture(self, topic):
        return self.speak("it is obvious that " + topic)


faculty = Professor("Doctor Arrogant", "six")
print(m1.speak("hi there"))
print(s1.speak("hi there"))
print(faculty.speak("hi there"))
print(faculty.lecture("hi there"))


class Grades(object):
    """A mapping from students to a list of grades"""

    def __init__(self):
        """Create empty grade book"""
        self.students = []  # list of Student objects
        self.grades = {}  # maps id_num -> list of grades
        self.is_sorted = True  # true if self.students is sorted

    def add_student(self, student):
        """Assumes: student is of type Student
        Add student to the grade book"""
        if student in self.students:
            raise ValueError("Duplicate student")
        self.students.append(student)
        self.grades[student.get_id_num()] = []
        self.is_sorted = False

    def add_grades(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student"""
        try:
            self.grades[student.get_id_num()].append(grade)
        except KeyError:
            raise ValueError("Student not in grade book")

    def get_grades(self, student):
        """Return a list of grades for student"""
        try:
            return self.grades[student.get_id_num()][:]
        except KeyError:
            raise ValueError("Student not in grade book")

    def all_students(self):
        """Return a list of the students in the grade book"""
        if not self.is_sorted:
            self.students.sort()
            self.is_sorted = True
        # return self.students[:] # return a copy of list of students
        for s in self.students:
            yield s


def grade_report(course):
    """Assumes: course if of type grades"""
    report = []
    for s in course.all_students():
        tot = 0.0
        num_grades = 0
        for g in course.get_grades(s):
            tot += g
            num_grades += 1
        try:
            average = tot / num_grades
            report.append(str(s) + "' s mean grade is " + str(average))
        except ZeroDivisionError:
            report.append(str(s) + " has no grades")
    return "\n".join(report)


six00 = Grades()
six00.add_student(g1)
six00.add_student(ug2)
six00.add_student(ug1)
six00.add_student(g2)
six00.add_student(ug4)
six00.add_student(ug3)

six00.add_grades(g1, 100)
six00.add_grades(g2, 25)
six00.add_grades(ug1, 95)
six00.add_grades(ug2, 85)
six00.add_grades(ug3, 75)
print("All students", six00.all_students())
print("All students", six00.all_students().__next__())
print("All students", six00.all_students().__next__())
print(grade_report(six00))
print(ug1.get_id_num())
for s in six00.all_students():
    print(s)
