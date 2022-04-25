from typing import Any


shop: list[list[Any]] = [
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

handy_shop: dict[str, list[int]] = {stuff[0]: [0, 0] for stuff in shop}
for stuff in shop:
    handy_shop[stuff[0]][0] += 1
    handy_shop[stuff[0]][1] += stuff[1]

print("Print 'exit' to exit.")
while True:
    name_of_stuff = input("Enter the name of stuff: ")

    if name_of_stuff == "exit":
        break

    if name_of_stuff not in handy_shop:
        print("This product is out of stock.")
        continue

    print("Number of products:", handy_shop[name_of_stuff][0])
    print("The total price:", handy_shop[name_of_stuff][1])
