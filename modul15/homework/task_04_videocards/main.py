def get_input_parameters():
    """
    Получаем список видеокарт
    
    :return: набор клеток, например: [3070, 2060, 3090, 3070, 3090]
    :rtype: List[int]
    """
    # TODO: в этой функции пишем весь необходимый код для 
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    pass


def display_result(old_video_cards, new_video_cards):
    """
    Выводим список оставшихся видеокарт
    
    :param old_video_cards: старый набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :type old_video_cards: List[int]
    :param new_video_cards: новый набор видеокарт, например: [3070, 2060, 3070]
    :type new_video_cards: List[int]
    """
    # TODO: в этой функции пишем весь необходимый код 
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    pass


def select_video_cards(video_cards):
    """
    Удаляем из списка видеокарт наибольшие элементы.
    
    :param video_cards: набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :type video_cards: List[int]
    
    :return: набор оставшихся видеокарт, например: [3070, 2060, 3070]
    :rtype: List[int]
    """
    # TODO: в этой функции пишем логику удаление из списка видеокарт наибольшие элементы. 
    #  print'ов и input'ов тут не должно быть. 
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    video_cards = get_input_parameters()  # получаем параметры
    result_video_cards = select_video_cards(video_cards)  # удаляет наибольшие элементы.
    display_result(video_cards, result_video_cards)  # выводим результат