contacts = {}

action = 0

while action != 3:
    action = int(
        input(
            "Введите номер действия: 1. Добавить контакт 2. Найти человека"
            " 3. Выход\n"
        )
    )
    if action == 1:
        name, surname = input(
            "Введите имя и фамилию нового контакта (через пробел): "
        ).split()
        if (name, surname) in contacts.keys():
            print("Такой человек уже есть в контактах.")
        else:
            phone_number = int(input("Введите номер телефона: "))
            contacts[(name, surname)] = phone_number
        print("Текущий словарь контактов: ", contacts)

    if action == 2:
        search_surname = input("Введите фамилию для поиска: ").capitalize()
        for (name, surname) in contacts.keys():
            if search_surname == surname:
                print(name, surname, contacts[(name, surname)])
