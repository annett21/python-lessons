def get_input_parameters():
    """
    Получаем неотсортированный список чисел
    
    :return: неотсортированный список чисел, например: [1, 4, -3, 0, 10]
    :rtype: List[int]
    """
    return [1, 4, -3, 0, 10]


def display_result(sorted_list):
    """
    Выводим отсортированный список
    
    :param sorted_list: отсортированный список, например: [-3, 0, 1, 4, 10]
    :type sorted_list: List[int]
    """
    print("Отсортированный список: ", sorted_list)


def sort_list(original_list):
    """
    Сортируем список
    
    :param original_list: Исходный список: [1, 4, -3, 0, 10]
    :type original_list: List[int]
    
    :return: отсортированный, например: [-3, 0, 1, 4, 10]
    :rtype: List[int]
    """
    original_list.sort()
    return original_list
   
    # if len(original_list) < 2:
    #     return original_list
    # else:
    #     pivot = original_list[0]
    #     less = [i for i in original_list[1:] if i <= pivot]
    #     greater = [i for i in original_list[1:] if i > pivot]
    #     return sort_list(less) + [pivot] + sort_list(greater)


if __name__ == '__main__':
    original_list = get_input_parameters() 
    sorted_list = sort_list(original_list) 
    display_result(sorted_list) 