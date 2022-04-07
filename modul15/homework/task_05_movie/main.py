def get_input_parameters():
    """
    Получаем список фильмов, которые пользователь хочет добавить в "любимые"
    
    :return: добавляемые фильмы, например: ["Леон", "Безумный Макс", "Мементо", "Царь горы"]
    :rtype: List[str]
    """
    new_favorite_films = []
    num = int(input("Сколько фильмов хотите добавить? "))
    for _ in range(num):
        film = input("Введите название фильма: ")
        new_favorite_films.append(film)
    
    return new_favorite_films



def display_result(favorite_films, errors):
    """
    Выводим список ошибок и список любимых фильмов
    
    :param favorite_films: список любимых фильмов, например: ["Леон", "Мементо"]
    :type favorite_films: List[str]
    :param errors: список ненайденных фильмов, например: ["Безумный Макс", "Царь горы"]
    :type errors: List[str]
    """
    print("Ошибка. Этих фильмов у нас нет:", errors)
    print("Ваш список любимых фильмов:", favorite_films)


def add_favorite_film(new_favorite_films, available_films):
    """
    Добавляем фильмы в список "любимых".
    
    :param new_favorite_films: фильмы, которые нужно добавить в "любимые", 
           например: ["Леон", "Безумный Макс", "Мементо", "Царь горы"]
    :type new_favorite_films: List[str]
    :param available_films: фильмы, которые есть на киносайте, 
           например: ["Леон", "Назад в будущее", "Мементо"] 
    :type available_films: List[str]
    
    :return: Список фильмов в списке "любимых" и список не найденных фильмов,
             например: (["Леон", "Мементо"], ["Безумный Макс", "Царь горы"])
    :rtype: Tuple[List[str], List[str]]
    """
    
    favorite_films = list(set(new_favorite_films) & set(available_films))
    errors = list(set(new_favorite_films).difference(set(favorite_films)))

    return favorite_films, errors


if __name__ == '__main__':
    available_films = [
        "Крепкий орешек", "Назад в будущее", "Таксист", 
        "Леон", "Богемская рапсодия", "Город грехов", 
        "Мементо", "Отступники", "Деревня"
    ]
    new_favorite_films = get_input_parameters()  
    favorite_films, errors = add_favorite_film(
        new_favorite_films,
        available_films
    )  
    display_result(favorite_films, errors) 