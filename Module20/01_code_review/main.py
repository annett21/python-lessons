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

print("Список пар 'ID студента — возраст':", end=" ")
print([(student_id, students[student_id]["age"]) for student_id in students])


def check_data(dict):
    len_surname = sum([len(st["surname"]) for st in students.values()])
    all_interests = set(
        [i for st in students.values() for i in st["interests"]]
    )
    # for i_student in students:
    #     all_interests.update(students[i_student]["interests"])
    #     len_surname += len(students[i_student]["surname"])
    return all_interests, len_surname


result = check_data(students)
print("Полный список интересов всех студентов:", result[0])
print("Общая длина всех фамилий студентов:", result[1])
