import os


def read_file(file_path: str) -> str:
    with open(file_path) as text:
        return text.read()


def reverse_lines(text: str) -> str:
    return "\n".join(reversed(text.split("\n")))


if __name__ == "__main__":
    path_to_zen = os.path.abspath("Module22/task_02_zen_of_python/zen.txt")
    zen_of_python = read_file(path_to_zen)
    reversed_zen = reverse_lines(zen_of_python)
    print(reversed_zen)
