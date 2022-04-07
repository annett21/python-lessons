from random import randint
from typing import List, Tuple


def get_input_parameters() -> Tuple[int, List[int]]:
    """
    Gets the shift and the list of integer numbers.
    """
    while True:
        user_input = input("Enter the shift: ")
        try:
            shift = int(user_input)
        except ValueError:
            print("The shift should be an integer number.")
            continue
        break

    original_list = [randint(-10, 10) for _ in range(5)]
    print("The original list:", original_list)

    return shift, original_list


def display_result(shifted_list: List[int]) -> None:
    """
    Prints the resulted list.
    """
    print("The shifted list:", shifted_list)


def shift_list(shift: int, original_list: List[int]) -> List[int]:
    """
    Shifts the list.
    Shifts to right if the shift is positive and to left if the shift is negative.
    """
    shift = shift % len(original_list)
    return original_list[-shift:] + original_list[:-shift]


if __name__ == "__main__":
    shift, original_list = get_input_parameters()
    shifted_list = shift_list(shift, original_list)
    display_result(shifted_list)
