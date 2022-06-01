# string = input("Строка: ")
# tuple_numbers = tuple(map(int, input("Кортеж чисел: ").split()))

string = "abcd"
numbers = (10, 20, 30, 40)

print(zip(string, numbers))
print(list(zip(string, numbers)))


def new_zip(a, b):
    return ((a[index], b[index]) for index in range(len(a)))


zip_generator = (
    (string[index], numbers[index]) for index in range(len(string))
)

print("Результат:")
print(zip_generator)
for item in zip_generator:
    print(item)
