name_handle = open("kids", "w")
for i in range(2):
    name = input("Enter name: ")
    name_handle.write(name + "\n")
name_handle.close()
