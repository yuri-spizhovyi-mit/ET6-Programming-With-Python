class Animal(object):
    """Class for animals"""

    def __init__(self, age):
        self.years = age
        self.name = None

    def get_age(self):
        return self.years

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.years = new_age

    def set_name(self, new_name=""):
        self.name = new_name

    def __str__(self):
        return "animal:" + str(self.name) + ":" + str(self.years)


my_animal = Animal(3)
my_animal.set_name('John')
print(my_animal)
print(my_animal.get_age())
print(my_animal.years)
