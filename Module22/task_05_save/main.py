import os


# def make_abs_dir_path(path):
#     return os.path.join("/", *path.split())


# def make_abs_file_path(dir_path, file_name):
#     return os.path.join(dir_path, file_name + ".txt")


# def check_path(path):
#     return os.path.exists(path)


def save_file(path, text):
    with open(path, "w") as opened_file:
        opened_file.write(text)


# text = input("Введите строку: ")

# file_name = input("Введите имя файла: ")

# while True:
#     save_place = input(
#         "Куда хотите сохранить документ? Введите последовательность папок"
#         " (через пробел): "
#     )
#     dir_path = make_abs_dir_path(save_place)
#     if check_path(dir_path):
#         break
#     print("Данный путь не существует!")

# file_path = make_abs_file_path(dir_path, file_name)
# file_exists = check_path(file_path)

# if file_exists:
#     answer = input("Вы действительно хотите перезаписать файл? ")
#     if answer != "да":
#         exit()

# save_file(file_path, text)
# if file_exists:
#     print("Файл успешно перезаписан!")
# else:
#     print("Файл успешно сохранён!")


def input_abs_dir_path() -> str:
    # This function asks user input absolute path separated by whitespases
    # and check if it exists (if not, asks again)

    # Test expects calling input("Where would you like to save the document?
    # Enter the sequence of folders (separated by a space): ")
    # and print("This path is not exists!")
    pass


def input_file_name(abs_dir_path: str) -> tuple[str, bool]:
    # This function asks user to input file name.
    # If file exists already, function will ask user confirm overwriting file.
    # If user don't confirm, function will ask file name again and again.
    # It returns absolute file path and boolean value does the file exist.

    # Test expects calling input("Enter a file name: ")
    # and input("Do you want to overwrite this file? (yes/no) ")
    pass


if __name__ == "__main__":
    text = input("Enter a text: ")
    abs_dir_path = input_abs_dir_path()
    abs_file_path, file_is_exists = input_file_name(abs_dir_path)
    save_file(abs_file_path, text)

    if file_is_exists:
        print("File was overwritten successfully!")
    else:
        print("File was saved successfully!")
