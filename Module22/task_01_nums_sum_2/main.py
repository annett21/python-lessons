import os


def read_file(file_path: str) -> str:
    with open(file_path) as numbers:
        return numbers.read()


def normalize_file_data(file_data: str) -> list[int]:
    return [int(i_num.strip()) for i_num in file_data if i_num.strip()]


def write_file(file_path: str, text: str) -> None:
    with open(file_path, "w") as answer:
        answer.write(text)


if __name__ == "__main__":
    answer_path = os.path.abspath("Module22/task_01_nums_sum_2/answer.txt")
    numbers_path = os.path.abspath("Module22/task_01_nums_sum_2/numbers.txt")

    file_data = read_file(numbers_path)
    normalized_data = normalize_file_data(file_data)
    sum_of_numbers = str(sum(normalized_data))
    write_file(answer_path, sum_of_numbers)
