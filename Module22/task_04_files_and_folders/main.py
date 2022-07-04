import os

# path = os.path.abspath("Module22")
# dirs = 0
# files = 0
# size = os.path.getsize(path)

# for i_elem in os.listdir(path):
#     new_path = os.path.join(path, i_elem)
#     size += os.path.getsize(new_path)
#     if os.path.isdir(new_path):
#         files += len(os.listdir(new_path))
#         dirs += 1
#     elif os.path.isfile(new_path):
#         files += 1


# print(path)
# print("Размер каталога (в Кб):", size / 1024)
# print("Количество подкаталогов:", dirs)
# print("Количество файлов:", files)


def count_size_kb(path: str) -> float:
    # use os.scandir(path) to iterate by dir's content
    # and recursion :)
    pass


def count_subdirs(path: str) -> int:
    pass


def count_files(path: str) -> int:
    pass


if __name__ == "__main__":
    dir_abs_path = os.path.abspath("module14")

    size_kb = count_size_kb(dir_abs_path)
    subdirs_quantity = count_subdirs(dir_abs_path)
    files_quantity = count_files(dir_abs_path)

    print(dir_abs_path)
    print("Размер каталога (в Kb):", size_kb)
    print("Количество подкаталогов:", subdirs_quantity)
    print("Количество файлов:", files_quantity)
