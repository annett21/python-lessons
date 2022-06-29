import os
from collections import Counter
from zipfile import ZipFile


def open_zip_file(file_path: str) -> None:
    with ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall("Module22/task_09_war_and_peace")


zip_path = os.path.abspath("Module22/task_09_war_and_peace/voyna-i-mir.zip")
open_zip_file(zip_path)

text_path = os.path.abspath("Module22/task_09_war_and_peace/voyna-i-mir.txt")


all_letters = {}

with open(text_path) as f:
    for line in f:
        letters_in_line = Counter(line)
        for letter in letters_in_line:
            if not letter.isalpha():
                continue
            letter_counter = all_letters.get(letter, 0)
            all_letters[letter] = letter_counter + letters_in_line[letter]

print(
    *(
        " ".join((letter, str(counter)))
        for letter, counter in sorted(
            list(all_letters.items()), key=lambda i: i[1]
        )
    ),
    sep="\n"
)
