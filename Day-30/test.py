# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key" : "value"}
#     print(a_dictionary["sdfsdf"])

# except FileNotFoundError:
#     # print("There was an error")
#     file = open("a_file.txt", "w")
#     file.write("Something")

# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")

# else:
#     content = file.read()
#     print(content)

# finally:
#     # file.close()
#     # print("File was closed.")
#     raise TypeError("This is an error that I made up")

height = float(input("Height : "))
weight = float(input("Weight : "))

if height >3:
    raise ValueError("Huamn Height should not be over 3 meters.")

bmi = weight/height **2
print(bmi)