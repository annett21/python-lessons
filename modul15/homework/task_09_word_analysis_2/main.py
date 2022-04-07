def get_input_parameters():
    """
    Получаем входное слово
    
    :return: например: abccba
    :rtype: str
    """
    # TODO: в этой функции пишем весь необходимый код для 
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    pass


def display_result(is_palindrome):
    """
    Выводим список оставшихся видеокарт
    
    :param is_palindrome: является ли палиндромом, например: True
    :type is_palindrome: bool
    """
    # TODO: в этой функции пишем весь необходимый код 
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    pass


def check_palindrome(word):
    """
    Проверяем является ли слово палиндромом.
    
    :param word: слово, например: abccba
    :type word: str
    
    :return: является ли слово палиндром, например: True
    :rtype: bool
    """
    # TODO: в этой функции пишем логику проверки строки на палиндром. 
    #  print'ов и input'ов тут не должно быть. 
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    is_palindrome = check_palindrome(word)  # является ли слово палиндромом.
    display_result(is_palindrome)  # выводим результат