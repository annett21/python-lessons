def get_input_parameters() -> str:
    """
    Gets the input word.
    """
    return input("Enter the word: ")


def display_result(is_palindrome: bool) -> None:
    """
    Prints the information the input word is a palindrome or isn't.
    """
    print(f"The word {'is' if is_palindrome else 'is not'} a palindrome.")


def check_palindrome(word: str) -> bool:
    """
    Checks if the word is a palindrome.
    """
    return word == word[::-1]


if __name__ == "__main__":
    word = get_input_parameters()
    is_palindrome = check_palindrome(word)
    display_result(is_palindrome)
