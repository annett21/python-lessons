from tabnanny import check


def check_char(text, chars):
    for char in chars:
        if text.startswith(char):
            return True


wrong_char = "@№$%^&\*()"
type_file = (".txt", ".doxc")

name = input("Your file name: ")

if not check_char(name, wrong_char) and name.endswith(type_file):
    print("File name is correct")
elif not check_char(name, wrong_char) and not name.endswith(type_file):
    print(f"Error: wrong file type. Expected {type_file[0]} or {type_file[1]}.")
elif check_char(name, wrong_char) and name.endswith(type_file):
    print("Error: file name starts with one of special char")
else:
    print("Error: file name starts with one of special char")
    print(f"Error: wrong file type. Expected {type_file[0]} or {type_file[1]}.")
