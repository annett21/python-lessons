people_quantity = int(input("Количество человек: "))
step = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {step} человек.")

circle = list(range(1, people_quantity + 1))
count = 0

while len(circle) > 1:
    print("Текущий круг людей", circle)
    print(f"Начало счета с номера {circle[count]}")
    count = (count + step - 1) % len(circle)
    if circle[count] == circle[-1]:
        print(f"Выбывает человек под номером {circle.pop(count)}")
        count = 0
    else:
        print(f"Выбывает человек под номером {circle.pop(count)}")
print("Остался человек под номером", circle[0])
