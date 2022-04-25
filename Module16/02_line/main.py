first_class = list(range(160, 172, 2))
second_class = list(range(162, 180, 3))

first_class.extend(second_class)
first_class.sort()
print("Отсортированный список учеников:", first_class)