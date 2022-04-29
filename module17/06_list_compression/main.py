from random import randint

number = int(input("Количество чисел в списке: "))

base_list = [randint(0, 2) for _ in range(number)]
print("Список до сжатия:", base_list)

updated_list = [x for x in base_list if x != 0]
print("Список после сжатия:", updated_list)
