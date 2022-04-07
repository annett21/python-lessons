def get_input_parameters() -> str:
    """
    Gets word using input.
    """
    return input("Enter a word: ")


def display_result(number_unique_letters: int) -> None:
    """
    Prints result. Suddenly.
    """
    print("Count of unique letters is", number_unique_letters)


def count_number_unique_letters(word: str) -> int:
    """
    Counts number of unique letters in `word`. Suddenly again :)
    """
    return len(set(word))


if __name__ == "__main__":
    word = get_input_parameters()
    number_unique_letters = count_number_unique_letters(word)
    display_result(number_unique_letters)
