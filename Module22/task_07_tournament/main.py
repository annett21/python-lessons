import os


# path = os.path.abspath("Module22/task_07_tournament/first_tour.txt")

# with open(path) as data:
#     max_point = int(data.readline())
#     people_points = data.read().split("\n")


# full_data = [
#     people.split() for people in people_points if int(people.split()[2]) > max_point
# ]
# # people is ["surname", "name", "point"]


# def get_point(people):
#     return int(people[2])


# sorted_full_data = sorted(full_data, key=get_point, reverse=True)


# def pretty_people(people):
#     surname, name, point = people
#     return f"{name[0]}. {surname} {point}"


# new_path = os.path.abspath("Module22/task_07_tournament/second_tour.txt")

# with open(new_path, "w") as f:
#     f.write(str(len(sorted_full_data)) + "\n")
#     for i, people in enumerate(sorted_full_data):
#         f.write(f"{i + 1}) " + pretty_people(people) + "\n")


def read_file(file_path: str) -> str:
    # Returns all text in file.
    pass


def write_file(file_path: str, data: str) -> None:
    # Writes the data to file.
    pass


def extract_passing_score(raw_data: str) -> int:
    # Returns passing score that is in the first line.
    pass


def extract_participants(raw_data: str) -> list[tuple[str, str, int]]:
    # Returns a list of people. A person is a tuple consisting of three string elements
    # ("Surname", "Name", "Score")
    pass


def filter_participants_by_score(
    participants: list[tuple[str, str, int]], min_score: int = 0
) -> list[tuple[str, str, int]]:
    # Filters participants who score is bigger than min_score.
    pass


def sort_participants_by_score(
    participants: list[tuple[str, str, int]]
) -> list[tuple[str, str, int]]:
    # Sorts the participants in descending order of score.
    pass


def prepare_to_write(participants: list[tuple[str, str, int]]) -> str:
    # Returns the all data that second_tour.txt file should include.
    # The first line is a length of participant list.
    pass


if __name__ == "__main__":
    first_tour_file_path = os.path.abspath("Module22/task_07_tournament/first_tour.txt")
    raw_data = read_file(first_tour_file_path)

    passing_score = extract_passing_score(raw_data)
    participants = extract_participants(raw_data)
    filtered_participants = filter_participants_by_score(participants, min_score=80)
    sorted_participants = sort_participants_by_score(filtered_participants)
    prepared_data = prepare_to_write(sorted_participants)

    second_tour_file_path = os.path.abspath(
        "Module22/task_07_tournament/second_tour.txt"
    )
    write_file(second_tour_file_path, prepared_data)
