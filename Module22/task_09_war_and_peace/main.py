import os
from collections import Counter
from zipfile import ZipFile


def extract_zip(file_path: str) -> str:
    dir_path = os.path.dirname(file_path)
    zip_name = os.path.basename(file_path)
    file_name = ".".join(zip_name.split(".")[:-1])

    extracted_dir_path = os.path.join(dir_path, file_name)

    with ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extracted_dir_path)

    return extracted_dir_path


def analyze_text(file_path: str) -> dict[str, float]:
    stats: dict[str, int] = {}

    with open(file_path, "r") as f:
        for line in f.read():
            for char, quantity in Counter(line).items():
                if char.isalpha():
                    stats[char] = stats.get(char, 0) + quantity

    all_letters_quantity = sum(stats.values())
    analyzed_stats: dict[str, float] = {}
    for char, quantity in stats.items():
        analyzed_stats[char] = round(quantity / all_letters_quantity, 6)

    return analyzed_stats


def print_stats(stats: dict[str, float]) -> None:
    sorted_stats = sorted(stats.items(), key=lambda i: i[1], reverse=True)
    pretty_stats = (" ".join((char, str(quantity))) for char, quantity in sorted_stats)
    print(*pretty_stats, sep="\n")


# def open_zip_file(file_path: str) -> None:
#     with ZipFile(file_path, "r") as zip_ref:
#         zip_ref.extractall("Module22/task_09_war_and_peace")


# zip_path = os.path.abspath("Module22/task_09_war_and_peace/voyna-i-mir.zip")
# open_zip_file(zip_path)

# text_path = os.path.abspath("Module22/task_09_war_and_peace/voyna-i-mir.txt")

# all_letters = {}

# with open(text_path) as f:
#     for line in f:
#         letters_in_line = Counter(line)
#         for letter in letters_in_line:
#             if not letter.isalpha():
#                 continue
#             letter_counter = all_letters.get(letter, 0)
#             all_letters[letter] = letter_counter + letters_in_line[letter]

# print(
#     *(
#         " ".join((letter, str(counter)))
#         for letter, counter in sorted(
#             list(all_letters.items()), key=lambda i: i[1]
#         )
#     ),
#     sep="\n"
# )


if __name__ == "__main__":
    zip_path = os.path.abspath("Module22/task_09_war_and_peace/voyna-i-mir.zip")
    dir_path = extract_zip(zip_path)
    file_path = os.path.join(dir_path, os.path.basename(dir_path) + ".txt")

    stats = analyze_text(file_path)
    print_stats(stats)
