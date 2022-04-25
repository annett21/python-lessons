from random import randint


def int_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Введите целое число.")


friends_quantity = int_input("Количество друзей: ")
debts_quantity = int_input("Долговых расписок: ")


debts = []
for number_debt in range(1, debts_quantity + 1):
    print(f"\n{number_debt} расписка")

    to_friend = int_input("Кто должен: ")
    if to_friend < 1 or to_friend > friends_quantity:
        to_friend = randint(1, friends_quantity)
        print("Кто должен:", to_friend)

    from_friend = int_input("Кто отдолжил: ")
    if from_friend < 1 or from_friend > friends_quantity:
        from_friend = randint(1, friends_quantity)
        print("Кто отдолжил:", to_friend)

    price = int_input("Сколько: ")
    if price < 0:
        price = randint(1, 100)
        print("Сколько:", price)

    debts.append((to_friend, from_friend, price))


balances = {k: 0 for k in range(1, friends_quantity + 1)}
for debt in debts:
    balances[debt[0]] -= debt[2]
    balances[debt[1]] += debt[2]

print("\nБаланс друзей:")
for friend, balance in balances.items():
    print(friend, ":", balance)
