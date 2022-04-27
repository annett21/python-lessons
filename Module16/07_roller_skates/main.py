number_of_skates = int(input("Кол-во коньков: "))
skates_size = []

for i in range(1, number_of_skates + 1):
    size = int(input(f"Размер {i} пары: "))
    skates_size.append(size)

number_of_people = int(input("Кол-во людей: "))
legs_size = []

for n in range(1, number_of_people + 1):
    leg_size = int(input(f"Размер ноги {n} человека: "))
    legs_size.append(leg_size)

check = 0

for leg_size in legs_size:
    for skate_size in sorted(skates_size):
        if leg_size <= skate_size:
            check += 1
            skates_size.remove(skate_size)
            break

print("Наибольшее кол-во людей, которые могут взять ролики:", check)
