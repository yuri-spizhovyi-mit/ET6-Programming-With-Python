class Animal:
    def speak(self):
        return "Some sound"


def make_animal_speak(animal):
    print(animal.speak())


class Dog(Animal):
    def speak(self):
        return "Woof!"


dog = Dog()
make_animal_speak(dog)  # Output: Woof!


class Cat(Animal):
    def speak(self):
        return "Meow!"


cat = Cat()
make_animal_speak(cat)  # Output: Meow!


class SilentFish(Animal):
    def speak(self):
        raise NotImplementedError("Fish don't speak")


fish = SilentFish()
make_animal_speak(fish)  # ❌ BOOM! Runtime error
