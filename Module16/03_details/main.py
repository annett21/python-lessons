

shop = [
    ["каретка", 1200],
    ["шатун", 1000],
    ["седло", 300],
    ["педаль", 100],
    ["седло", 1500],
    ["рама", 12000],
    ["обод", 2000],
    ["шатун", 200],
    ["седло", 2700],
]

detail = input("Название детали: ")
price = 0
number = 0

for i in range(0, len(shop)):
    for item in shop[i]:
        if item == detail:
            number += 1
            price += shop[i][1]

print("Кол-во деталей -", number)
print("Общая стоимость -", price)
