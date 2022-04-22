def get_input_parameters():
    """
    Получаем входное слово
    
    :return: например: abccba
    :rtype: str
    """
    return input("Введите слово: ")


def display_result(is_palindrome):
    """
    Выводим список оставшихся видеокарт
    
    :param is_palindrome: является ли палиндромом, например: True
    :type is_palindrome: bool
    """
    if is_palindrome:
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")


def check_palindrome(word):
    """
    Проверяем является ли слово палиндромом.
    
    :param word: слово, например: abccba
    :type word: str
    
    :return: является ли слово палиндром, например: True
    :rtype: bool
    """
    return word[::-1] == word



if __name__ == '__main__':
    word = get_input_parameters() 
    is_palindrome = check_palindrome(word)  
    display_result(is_palindrome)