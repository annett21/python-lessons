from random import randint
from typing import List


def get_input_parameters() -> List[int]:
    """
    Gets a list of numbers.
    A user enters the length of the list. The list will generate randomly.
    """
    while True:
        user_input = input("Enter the length of the list: ")

        try:
            list_length = int(user_input)
        except ValueError:
            print("Enter an integer number.")
            continue

        if list_length < 2 or list_length > 100:
            print("Enter a number between 2 and 100 inclusive.")
            continue

        break

    random_list = [randint(-100, 100) for _ in range(list_length)]
    print("The original list:", random_list)
    return random_list


def display_result(sorted_list: List[int]) -> None:
    """
    Prints the sorted list.
    """
    print("The sorted list:", sorted_list)


def sort_list(original_list: List[int]) -> List[int]:
    """
    Sorts the list by ascending.
    """
    # return sorted(original_list)

    for index in range(1, len(original_list)):
        moving_index = index
        while original_list[moving_index] < original_list[moving_index - 1]:
            # swapping the numbers
            original_list.insert(moving_index - 1, original_list.pop(moving_index))

            moving_index -= 1
            if not moving_index:
                break

    return original_list


if __name__ == "__main__":
    original_list = get_input_parameters()
    sorted_list = sort_list(original_list)
    display_result(sorted_list)
