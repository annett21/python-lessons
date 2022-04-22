def get_input_parameters():
    """
    Получаем сдвиг и начальны список
    
    :return: например: (3, [1, 4, -3, 0, 10])
    :rtype: Tuple[int, List[int]]
    """
    shift = int(input("Сдвиг: "))
    elements = int(input("Введите число элементов: "))

    original_list = []

    for _ in range(elements):
        number = int(input("Введите число для списка: "))
        original_list.append(number)

    return shift, original_list



def display_result(shifted_list):
    """
    Выводим получившиеся список
    
    :param shifted_list: сдвинутый список, например: [5, 1, 2, 3, 4]
    :type shifted_list: List[int]
    """
    return print("Сдвинутый список:", shifted_list)
   


def shift_list(shift, original_list):
    """
    Сдвигаем список на определённое количество элементов в право
    
    :param shift: сдвиг: 3
    :type shift: int
    :param original_list: Исходный список: [1, 4, -3, 0, 10]
    :type original_list: List[int]
    
    :return: сдвинутый список, например: [5, 1, 2, 3, 4]
    :rtype: List[int]
    """
    
    for _ in range(shift % len(original_list)):
        original_list.insert(0, original_list.pop())
    
    return original_list


if __name__ == '__main__':
    shift, original_list = get_input_parameters()  
    shifted_list = shift_list(shift, original_list)
    display_result(shifted_list)