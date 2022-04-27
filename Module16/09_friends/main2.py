number_of_friends = int(input("Кол-во друзей: "))
number_of_notes = int(input("Кол-во долговых расписок: "))

friends_list = list(range(1, number_of_friends + 1))

friends_list = [[item] for item in friends_list]

for number in range(1, number_of_notes + 1):
    print(f"{number} расписка: ")
    to_whom = int(input("Кому: "))
    from_whom = int(input("От кого: "))
    how_much = int(input("Сколько: "))
    friends_list[to_whom - 1].append(-how_much)
    friends_list[from_whom - 1].append(how_much)

print("Баланс:", friends_list)
