import random

class Animal(object):
    """Class for animals"""

    def __init__(self, age):
        self.age = age
        self.name = None

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self, new_name=""):
        self.name = new_name

    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.age)


class Cat(Animal):
    def speak(self):
        print("meow")

    def __str__(self):
        return "cat:" + str(self.name) + ":" + str(self.years)


# jelly = Cat(5)
# jelly.set_name("Jelly")
# jelly.speak()
# print(jelly)
# print(Animal.__str__(jelly))
# blob = Animal(1)

# blob.set_name("Blob")
# print(blob)


class Rabbit(Animal):
    def speak(self):
        print("meep")

    def __str__(self):
        return "rabbit:" + str(self.name) + ":" + str(self.years)


# peter = Rabbit(5)
# jelly.speak()
# peter.speak()
# peter.set_name('Peter')
# print(peter)

class Person(Animal):
    def __init__(self, name,  age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []

    def get_friend(self):
        return self.friends
    def add_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("Hello")  

    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, 'is', diff, ' years older than ', other.name)
        else:
            print(self.name,  'is', -diff, ' years younger than ' , other.name)
    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)

eric = Person('eric', 45)
john = Person('john', 55)
eric.speak()
eric.age_diff(john)

class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()  
        if r < 0.25:
            print("I have homework")
        elif 0.25 <= r < 0.5:
            print('I need sleep')
        elif 0.5 <= r < 0.75:
            print('I should eat')
        else:
            print("I am watching TV")
    def __str__(self):
        return "student:" + str(self.name) + ":" + str(self.age) + ':' + str(self.major)      

fred = Student('Fred', 18, 'Course VI')
print(fred)
fred.speak()
        