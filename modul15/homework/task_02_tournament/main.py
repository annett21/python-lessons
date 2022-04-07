def display_result(participants_names):
    """
    Выводим список имён участников в первый день
    
    :param participants_names: список имён участников, например: ["Артемий", "Влад", "Дима", "Женя"]
    :type participants_names: List[str]
    """
    print("Первый день:", participants_names)


def get_participants_names(names):
    """
    Получаем элементы списка только с чётными индексами.
    
    :param names: список имён, например: ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    :type names: List[str]
    
    :return: список имён с чётными индексами , например: ["Артемий", "Влад", "Дима", "Женя"]
    :rtype: List[str]
    """
    participants_names = []
    for i in range(0, len(names), 2):
        participants_names.append(names[i])

    return participants_names



if __name__ == '__main__':
    participants_names = get_participants_names(
        ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
        )
    display_result(participants_names)