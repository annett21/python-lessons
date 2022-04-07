from typing import List


def get_input_parameters() -> int:
    """
    Asks to input number and return it.
    """
    while True:
        user_input = input("Enter a number: ")

        try:
            number = int(user_input)
        except ValueError:
            print("Enter an integer number.")
            continue

        if number < 1:
            print("Enter a number greater than 1.")
            continue

        return number


def display_result(odd_numbers: List[int]) -> None:
    """
    Prints list of odd numbers.
    """
    print("List of odd numbers:", odd_numbers)


def get_odd_numbers(number: int) -> List[int]:
    """
    Returns a list of odd numbers from 1 to `number` sorted by ascending.
    """
    return list(range(1, number + 1, 2))


if __name__ == "__main__":
    number = get_input_parameters()
    odd_numbers = get_odd_numbers(number)
    display_result(odd_numbers)
