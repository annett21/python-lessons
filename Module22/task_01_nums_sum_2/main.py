# def get_numbers_from_file(file_path):
#     with open(file_path, "r") as numbers:
#         return [int(i_num.strip()) for i_num in numbers if i_num.strip()]


# def write_sum_to_file(file_path, numbers):
#     with open(file_path, "a") as answer:
#         answer.write(str(sum(numbers)) + "\n")


# absolute_path = "/Users/anatarasevic/python_lessons/Module22/01_nums_sum_2/"
# answer_path = absolute_path + "answer.txt"
# number_path = absolute_path + "numbers.txt"

# write_sum_to_file(answer_path, get_numbers_from_file(number_path))


def read_file(file_path: str) -> str:
    pass


def normalize_file_data(file_data: str) -> list[int]:
    pass
