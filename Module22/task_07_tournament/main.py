import os


path = os.path.abspath("Module22/task_07_tournament/first_tour.txt")

with open(path) as data:
    max_point = int(data.readline())
    people_points = data.read().split("\n")


full_data = [
    people.split()
    for people in people_points
    if int(people.split()[2]) > max_point
]
# people is ["surname", "name", "point"]


def get_point(people):
    return int(people[2])


sorted_full_data = sorted(full_data, key=get_point, reverse=True)


def pretty_people(people):
    surname, name, point = people
    return f"{name[0]}. {surname} {point}"


new_path = os.path.abspath("Module22/task_07_tournament/second_tour.txt")

with open(new_path, "w") as f:
    f.write(str(len(sorted_full_data)) + "\n")
    for i, people in enumerate(sorted_full_data):
        f.write(f"{i + 1}) " + pretty_people(people) + "\n")
