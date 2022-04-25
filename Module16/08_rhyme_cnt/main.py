people_quantity = int(input("Количество человек: "))
step = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {step} человек.")

people = list(range(1, people_quantity + 1))


def run_count(start_index=0):
    if len(people) == 1:
        return people[0]

    start_index = 0 if start_index == len(people) else start_index

    print("\nТекущий круг людей:", people)
    print("Начало счёта с номера", people[start_index])

    normalized_step = step % len(people)
    leaving_index = (start_index + normalized_step - 1) % len(people)
    print("Выбывает человек под номером", people[leaving_index])
    del people[leaving_index]

    return run_count(leaving_index)


remaining_person = run_count()

print("\nОстался человек под номером", remaining_person)
