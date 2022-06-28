import os
from collections import Counter


def read_file(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()


def get_all_letters(text: str) -> list[str]:
    return [letter for letter in text.lower() if letter.isalpha()]


def analyse_data_content(letters: list[str]) -> list[tuple[str, float]]:
    counted_letters = dict(Counter(letters))
    return [
        (letter, round(counted_letters[letter] / len(letters), 3))
        for letter in counted_letters
    ]


def sort_stats(stats: list[tuple[str, float]]) -> list[tuple[str, float]]:
    def sorting(elem: tuple[str, float]) -> tuple[str, float]:
        return -elem[1], elem[0]

    return sorted(stats, key=sorting)


def make_pretty_stats(stats: list[tuple[str, float]]) -> str:
    return "\n".join([" ".join((elem[0], str(elem[1]))) for elem in stats])


def write_to_file(file_path: str, text: str) -> None:
    with open(file_path, "w") as f:
        f.write(text + "\n")


text_path = os.path.abspath("Module22/task_08_frequency_analysis/text.txt")
analysis_path = os.path.abspath(
    "Module22/task_08_frequency_analysis/analysis.txt"
)

text = read_file(text_path)
letters = get_all_letters(text)
stats_info = analyse_data_content(letters)
sorted_stats_info = sort_stats(stats_info)
pretty_line = make_pretty_stats(sorted_stats_info)
write_to_file(analysis_path, pretty_line)
