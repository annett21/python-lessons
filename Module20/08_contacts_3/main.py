def add_contact(contacts: dict):
    name, surname = input(
        "Введите имя и фамилию нового контакта (через пробел): "
    ).split()
    if (name, surname) in contacts:
        print("Такой человек уже есть в контактах.")
    else:
        phone_number = int(input("Введите номер телефона: "))
        contacts[(name, surname)] = phone_number
    print("Текущий словарь контактов: ", contacts)


def find_contacts(contacts: dict):
    search_surname = input("Введите фамилию для поиска: ").capitalize()
    for (name, surname) in contacts:
        if search_surname == surname:
            print(name, surname, contacts[(name, surname)])


contacts = {}
action = 0
text = (
    "Введите номер действия: 1. Добавить контакт 2. Найти человека 3. Выход\n"
)

while action != 3:
    action = int(input(text))
    if action == 1:
        add_contact(contacts)
    elif action == 2:
        find_contacts(contacts)
