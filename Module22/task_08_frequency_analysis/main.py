import os
from collections import Counter
from string import ascii_lowercase


def read_file(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()


def get_all_letters(text: str) -> str:
    return "".join((letter for letter in text.lower() if letter in ascii_lowercase))


def analyse_letters(letters: str) -> dict[str, float]:
    counted_letters = dict(Counter(letters))

    return {
        letter: round(counted_letters[letter] / len(letters), 3)
        for letter in counted_letters
    }


def sort_stats(stats: dict[str, float]) -> list[tuple[str, float]]:
    def sorting(elem: tuple[str, float]) -> tuple[str, float]:
        return -elem[1], elem[0]

    return sorted(stats.items(), key=sorting)


def make_pretty_stats(stats: list[tuple[str, float]]) -> str:
    return "\n".join([f"{elem[0]} {elem[1]}" for elem in stats])


def write_file(file_path: str, text: str) -> None:
    with open(file_path, "w") as f:
        f.write(text)


if __name__ == "__main__":
    text_path = os.path.abspath("Module22/task_08_frequency_analysis/text.txt")
    analysis_path = os.path.abspath("Module22/task_08_frequency_analysis/analysis.txt")

    text = read_file(text_path)
    only_letters = get_all_letters(text)
    stats_info = analyse_letters(only_letters)
    sorted_stats_info = sort_stats(stats_info)
    pretty_result = make_pretty_stats(sorted_stats_info)
    write_file(analysis_path, pretty_result)
