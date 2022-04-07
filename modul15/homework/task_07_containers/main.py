def get_input_parameters():
    """
    Получаем список весов контейнеров и вес нового контейнера
    Незабываем проверит данные: все числа целые и не превышают 200.
    
    :return: список весов контейнеров и вес нового контейнера,
             например: ([165, 163, 160, 160, 157, 157, 155, 154], 162)
    :rtype: Tuple[List[int], int]
    """
    list_container_weights = []
    num = int(input("Кол-во контейнеров: "))

    while len(list_container_weights) != num:
        weight = int(input("Введите вес контейнера: "))
        if 0 < weight < 200:
            list_container_weights.append(weight)
        else:
            print("Неверный вес")

    new_container_weight = int(input("Введите вес нового контенера: "))
    
    return list_container_weights, new_container_weight


def display_result(serial_number_new_container):
    """
    Выводим порядковый номер нового контейнера.
    
    :param serial_number_new_container: порядковый номер нового контейнера, например: 3
    :type serial_number_new_container: int
    """
    print("Номер, куда встанет новый контейнер:", serial_number_new_container)


def search_serial_number_new_container(list_container_weights, new_container_weight):
    """
    Ищем куда вставим новый контейнер.
    
    :param list_container_weights: список весов контейнеров, например: [165, 163, 160, 160, 157, 157, 155, 154]
    :type list_container_weights: List[int]
    :param new_container_weight: вес нового контейнера, например: 166
    :type new_container_weight: int
    
    :return: порядковый номер нового контейнера, например: 3
    :rtype: int
    """
    list_container_weights.append(int(new_container_weight))

    list_container_weights.sort(reverse=True)
    
    return len(list_container_weights) - list_container_weights[::-1].index(new_container_weight)

    
if __name__ == '__main__':
    list_container_weights, new_container_weight = get_input_parameters()
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)  
    display_result(serial_number_new_container)