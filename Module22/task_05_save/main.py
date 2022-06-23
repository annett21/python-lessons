import os


def make_abs_dir_path(path):
    return os.path.join("/", *path.split())


def make_abs_file_path(dir_path, file_name):
    return os.path.join(dir_path, file_name + ".txt")


def check_path(path):
    return os.path.exists(path)


def save_file(path, text):
    with open(path, "w") as opened_file:
        opened_file.write(text)


text = input("Введите строку: ")

file_name = input("Введите имя файла: ")

while True:
    save_place = input(
        "Куда хотите сохранить документ? Введите последовательность папок"
        " (через пробел): "
    )
    dir_path = make_abs_dir_path(save_place)
    if check_path(dir_path):
        break
    print("Данный путь не существует!")

file_path = make_abs_file_path(dir_path, file_name)
file_exists = check_path(file_path)

if file_exists:
    answer = input("Вы действительно хотите перезаписать файл? ")
    if answer != "да":
        exit()

save_file(file_path, text)
if file_exists:
    print("Файл успешно перезаписан!")
else:
    print("Файл успешно сохранён!")
