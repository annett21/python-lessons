def get_input_parameters():
    """
    Получаем список видеокарт
    
    :return: набор клеток, например: [3070, 2060, 3090, 3070, 3090]
    :rtype: List[int]
    """
    old_video_cards = []

    cards = int(input("Кол-во видеокарт: "))

    for i in range(1, cards + 1):
        card = int(input(f"{i} Видеокарта: "))
        old_video_cards.append(card)

    return old_video_cards

def display_result(old_video_cards, new_video_cards):
    """
    Выводим список оставшихся видеокарт
    
    :param old_video_cards: старый набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :type old_video_cards: List[int]
    :param new_video_cards: новый набор видеокарт, например: [3070, 2060, 3070]
    :type new_video_cards: List[int]
    """
    print("Старый список видеокарт:", old_video_cards)
    print("Новый список видеокарт:", new_video_cards)


def select_video_cards(old_video_cards):
    """
    Удаляем из списка видеокарт наибольшие элементы.
    
    :param video_cards: набор видеокарт, например: [3070, 2060, 3090, 3070, 3090]
    :type video_cards: List[int]
    
    :return: набор оставшихся видеокарт, например: [3070, 2060, 3070]
    :rtype: List[int]
    """
    
    new_video_cards = old_video_cards.copy()
    max_card = max(old_video_cards)
    # for card in old_video_cards:
    #     if max_card == card:
    #         new_video_cards.remove(card)
    while max_card in new_video_cards:
        new_video_cards.remove(max_card)

    
    return new_video_cards


if __name__ == '__main__':
    video_cards = get_input_parameters() 
    result_video_cards = select_video_cards(video_cards)  # удаляет наибольшие элементы.
    display_result(video_cards, result_video_cards)  # выводим результат