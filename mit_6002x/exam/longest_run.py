def longest_run(roll):
    current_num = roll[0]
    counter = 1
    longest = 1
    for num in roll[1:]:
        if current_num == num:
            counter += 1
            if longest < counter:
                longest = counter
        else:
            current_num = num
            counter = 1
    return longest


print(longest_run([3, 3, 2, 4, 4, 4, 1, 1, 1, 1]))
print(longest_run([1, 4, 3]))
print(longest_run([1, 3, 3, 2]))
