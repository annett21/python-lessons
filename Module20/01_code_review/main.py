students = {
    1: {
        "name": "Bob",
        "surname": "Vazovski",
        "age": 23,
        "interests": ["biology", "swimming"],
    },
    2: {
        "name": "Rob",
        "surname": "Stepanov",
        "age": 24,
        "interests": ["math", "computer games", "running"],
    },
    3: {
        "name": "Alexander",
        "surname": "Krug",
        "age": 22,
        "interests": ["languages", "health food"],
    },
}

print("Список пар \"ID студента — возраст\":", end=" ")
print([(student_id, students[student_id]["age"]) for student_id in students])


def parse_students_data(data):
    len_surname = sum([len(st["surname"]) for st in data.values()])
    all_interests = set(
        [i for st in data.values() for i in st["interests"]]
    )
    return all_interests, len_surname

all_interests, len_surname = parse_students_data(students)
print("Полный список интересов всех студентов:", all_interests)
print("Общая длина всех фамилий студентов:", len_surname)
