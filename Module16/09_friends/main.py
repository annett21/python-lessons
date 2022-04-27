N = int(input("Кол-во друзей: "))
K = int(input("Кол-во долговых расписок: "))
friends_list = []

for _ in range(N):
    friends_list.append(0)

for number in range(1, K + 1):
    print(f"{number} расписка: ")
    to_whom = int(input("Кому: "))
    from_whom = int(input("От кого: "))
    how_much = int(input("Сколько: "))
    friends_list[from_whom - 1] += how_much
    friends_list[to_whom - 1] -= how_much

print("Баланс друзей: ")
for index in range(len(friends_list)):
    print(index + 1, ": ", friends_list[index])
