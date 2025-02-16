grades = {"Ana": "A", "Ben": "B", "Daniel": "D", "Evan": "E", "Frank": "F"}
grades["Bob"] = "B"
del grades["Ben"]
print(grades)
print(type(grades.keys()))
print(grades.values())
print(len(grades["Ana"]))
print("A" in grades.values())
print(grades.values())
