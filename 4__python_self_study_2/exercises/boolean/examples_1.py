is_raining = True
has_umbrella = False
if is_raining and not has_umbrella:
    print("Stay inside!")

else:
    print("Go outside!")

a = 5
b = 3

print(a & b)  # 1


not (a and b) == (not a or not b)  # True

numbers = list(range(1, 21))
# filtered_elements = [x for x in numbers if not (x % 3 == 0 or x % 5 == 0)]
# filtered_elements = [x for x in numbers if x % 3 != 0 and x % 5 != 0]
filtered_elements = [x for x in numbers if not x % 3 == 0 and not x % 5 == 0]
print(filtered_elements)
