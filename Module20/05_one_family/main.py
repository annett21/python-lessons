def is_women(string):
    return string[-1] == "а"


family = {
    ("Сидоров", "Никита"): 35,
    ("Сидорова", "Алина"): 34,
    ("Сидоров", "Павел"): 10,
    ("Иванов", "Дмитрий"): 15,
    ("Иванова", "Алиса"): 18,
    ("Смирнов", "Кирилл"): 25,
}

surname_search = input("Введите фамилию: ").capitalize()
print()


for (surname, name), ages in family.items():
    if surname == surname_search:
        print(surname, name, ages)
    elif is_women(surname):
        if surname[:-1] == surname_search:
            print(surname, name, ages)
    elif is_women(surname_search):
        if surname == surname_search[:-1]:
            print(surname, name, ages)
