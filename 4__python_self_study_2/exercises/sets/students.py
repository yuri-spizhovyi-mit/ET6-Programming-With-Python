course_a_students = {"Bob", "John", "Camilla", "Evan"}
course_b_students = {"Camilla", "Anna", "Evan"}

both_courses_students = course_a_students.intersection(course_b_students)
one_course_students = course_a_students.union(course_b_students) - both_courses_students

print(both_courses_students)
print(one_course_students)
