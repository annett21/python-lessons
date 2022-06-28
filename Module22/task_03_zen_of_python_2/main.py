import os
from collections import Counter


def read_file(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()


def count_letters(text: str) -> int:
    return len([char for char in text if char.isalpha()])


def count_words(text: str) -> int:
    return len(
        [word for word in text.split() if any([l.isalpha() for l in word])]
    )


def count_lines(text: str) -> int:
    return len(text.split("\n"))


def find_most_rare_letter(text: str) -> str:
    c = Counter([letter for letter in text.lower() if letter.isalpha()])
    return c.most_common()[-1][0]


if __name__ == "__main__":
    pass
    abs_path_zen = os.path.abspath("Module22/task_02_zen_of_python/zen.txt")
    zen_of_python = read_file(abs_path_zen)

    letters_quantity = count_letters(zen_of_python)
    words_quantity = count_words(zen_of_python)
    lines_quantity = count_lines(zen_of_python)
    most_rare_letter = find_most_rare_letter(zen_of_python)

    print("Количество букв в файле: ", letters_quantity)
    print("Количество слов в файле: ", words_quantity)
    print("Количество строк в файле:", lines_quantity)
    print("Наиболее редкая буква: ", most_rare_letter)
