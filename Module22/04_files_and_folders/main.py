import os

path = os.path.abspath("Module22")
dirs = 0
files = 0

for i_elem in os.listdir(path):
    new_path = os.path.join(path, i_elem)
    if os.path.isdir(new_path):
        files += len(os.listdir(new_path))
        dirs += 1
    elif os.path.isfile(new_path):
        files += 1


size = os.path.getsize(path)

print(path)
print("Размер каталога (в Кб):", size / 1024)
print("Количество подкаталогов:", dirs)
print("Количество файлов:", files)
