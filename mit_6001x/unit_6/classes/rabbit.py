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


class Rabbit(Animal):
    tag = 1

    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag += 1

    def get_rid(self):
        return str(self.rid).zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
        return Rabbit(0, self, other)

    def __eq__(self, other):
        parents_same = (
            self.parent1.rid == other.parent1.rid
            and self.parent2.rid == other.parent2.rid
        )
        parents_opposite = (
            self.parent2.rid == other.parent1.rid
            and self.parent1.rid == other.parent2.rid
        )

        return parents_same or parents_opposite


peter = Rabbit(2)
peter.set_name("Peter")
hopsy = Rabbit(3)
hopsy.set_name("Hopsy")
cotton = Rabbit(1, peter, hopsy)
cotton.set_name("Cottontail")
print(cotton)
print(cotton.get_parent1())
print(cotton.get_parent2())
mopsy = peter + hopsy
print(mopsy)
print(mopsy.get_parent1(), mopsy.get_parent2())
print(mopsy == cotton)
