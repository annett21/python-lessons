from random import randint


def create_and_fill_list(length: int, list_name: str) -> list[int]:
    new_list = []

    for number in range(1, length + 1):
        user_input = input(f"Enter the {number} number for {list_name} list: ")
        try:
            new_list.append(int(user_input))
        except ValueError:
            new_list.append(randint(1, 10))

    return new_list


first_list = create_and_fill_list(3, "first")
second_list = create_and_fill_list(7, "second")

print("\nThe first list:", first_list)
print("The second list:", second_list)

first_list.extend(second_list)
for number in first_list:
    while first_list.count(number) > 1:
        first_list.remove(number)

print("\nThe new first list:", first_list)
