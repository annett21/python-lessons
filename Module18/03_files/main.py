wrong_char = tuple("@№$%^&\*()")
type_file = (".txt", ".doxc")

name = input("Your file name: ")

if name.startswith(wrong_char):
    print("Error: file name starts with one of special char")
if not name.endswith(type_file):
    print(f"Error: wrong file type. Expected {type_file[0]} or {type_file[1]}.")
if not name.startswith(wrong_char) and name.endswith(type_file):
    print("File name is correct")
