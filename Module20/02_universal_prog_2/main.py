import math


def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(num))
    for i in range(3, 1 + max_divisor, 2):
        if num % i == 0:
            return False
    return True


def crypto(iterable_object):
    return [
        element
        for index, element in enumerate(iterable_object)
        if is_prime(index)
    ]


print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto("О Дивный Новый мир!"))
