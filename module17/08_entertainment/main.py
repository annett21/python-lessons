from random import randint

number_sticks = int(input("Количество палок: "))
raw = ["I" for _ in range(number_sticks)]

number_throws = int(input("Количество бросков: "))

for throws in range(1, number_throws + 1):
    Left_i = randint(1, number_sticks)
    Right_i = randint(Left_i, number_sticks)
    print(f"Бросок {throws}. Сбиты палки с номера {Left_i} по номер {Right_i}.")
    for stick in range(Left_i, Right_i + 1):
        raw[stick - 1] = "."

print("\nРезультат:", "".join(raw))
