def get_input_parameters():
    """
    Получаем входное слово
    
    :return: входное слово, например: "привет"
    :rtype: str
    """
    word = input("Введите слово: ")
    return word


def display_result(number_unique_letters):
    """
    Выводим количество уникальных букв в слове
    
    :param number_unique_letters: количество уникальных букв в слове, например: 6
    :type number_unique_letters: int
    """
    print("Кол-во уникальных букв:", number_unique_letters)


def count_number_unique_letters(word):
    """
    Считаем количество уникальных букв в слове.
    
    :param word: входное слово, например: "привет"
    :type word: str
    
    :return: количество уникальных букв в слове, например: 6
    :rtype: int
    """
    
    number_unique_letters = 0

    for letter in word:
        if word.count(letter) == 1:
            number_unique_letters += 1

    return number_unique_letters
    


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    number_unique_letters = count_number_unique_letters(word)  # считаем количество уникальных букв.
    display_result(number_unique_letters)  # выводим результат