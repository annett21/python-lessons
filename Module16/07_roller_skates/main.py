from random import randint


def create_and_fill_list() -> list[int]:
    list_length = 3

    for _ in range(3):
        user_input = input("Enter the length of the list: ")
        try:
            list_length = int(user_input)
            if list_length > 10 or list_length < 1:
                list_length = 3
                raise ValueError
        except ValueError:
            print("Enter an integer number between 1 and 10.")
            continue
        else:
            break

    print("The length of the list:", list_length)

    result_list = []

    for index in range(1, list_length + 1):
        user_input = input(f"{index} value: ")
        try:
            result_list.append(int(user_input))
        except ValueError:
            rand_value = randint(39, 47)
            result_list.append(rand_value)
            print(f"{index} value: {rand_value}")

    return result_list


print("\nSkates:")
skates = sorted(create_and_fill_list())

print("\nPeople:")
people = sorted(create_and_fill_list())

initial_skates = skates.copy()
initial_people = people.copy()

for _ in range(len(skates)):
    if not people:
        break
    skate = skates.pop()
    for _ in range(len(people)):
        if skate >= people.pop():
            break

max_people_with_skates = len(initial_skates) - len(skates)

print("\nPeople whit skates:", max_people_with_skates)
