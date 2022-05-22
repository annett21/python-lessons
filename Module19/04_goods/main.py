goods = {
    "Лампа": "12345",
    "Стол": "23456",
    "Диван": "34567",
    "Стул": "45678",
}
inverted_goods = {value: key for key, value in goods.items()}

store = {
    "12345": [
        {"quantity": 27, "price": 42},
    ],
    "23456": [
        {"quantity": 22, "price": 510},
        {"quantity": 32, "price": 520},
    ],
    "34567": [
        {"quantity": 2, "price": 1200},
        {"quantity": 1, "price": 1150},
    ],
    "45678": [
        {"quantity": 50, "price": 100},
        {"quantity": 12, "price": 95},
        {"quantity": 43, "price": 97},
    ],
}

data_needed = {}
total_amount = 0
total_price = 0

for key in store:
    for record in store[key]:
        current_price = record["quantity"] * record["price"]
        total_price += current_price
        total_amount += record["quantity"]
    data_needed[inverted_goods[key]] = total_amount, total_price
    total_amount = 0
    total_price = 0

print(data_needed)
for good_name in data_needed:
    print(
        f"{good_name} — {data_needed[good_name][0]} штук, стоимость "
        f"{data_needed[good_name][1]} рубл(я/ей)"
    )
