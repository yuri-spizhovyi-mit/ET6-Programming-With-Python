def process_number(num):
    if not isinstance(num, (int, float)):
        raise TypeError("num must be an int or a float")
    return num**2


print(process_number(4))  # Should print 16
print(process_number(3.5))  # Should print 12.25
# print(process_number("abc"))  # Should raise TypeError

items = [42, "hello", 3.14, None, [1, 2, 3], 33]

# Filter integers
ints = [item for item in items if isinstance(item, int)]
print(ints)  # Should print [42]


class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))  # Should print True
print(isinstance(dog, Animal))  # Should print True
