#file reading
with open("data.txt") as file:
    contents = file.read()
    print(contents)

    file.close()

#file record
with open("new_file.txt", mode="w") as file:
    file.write("New text. ")

