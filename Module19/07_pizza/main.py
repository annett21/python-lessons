orders = int(input("Enter the number of orders: "))

pizza_time_data = {}

for i in range(1, orders + 1):
    order = input(f"{i} order (Surname Pizza amount): ").split()
    if order[0] not in pizza_time_data:
        pizza_time_data[order[0]] = {}
    if order[1] in pizza_time_data[order[0]]:
        pizza_time_data[order[0]][order[1]] += int(order[2])
    else:
        pizza_time_data[order[0]][order[1]] = int(order[2])


def get_pizza_name(item):
    return item[0]


for client_name in sorted(pizza_time_data.keys()):
    print(f"{client_name}:")
    for pizza, pizza_amount in sorted(
        pizza_time_data[client_name].items(), key=get_pizza_name
    ):
        print(f"\t{pizza}: {pizza_amount}")
