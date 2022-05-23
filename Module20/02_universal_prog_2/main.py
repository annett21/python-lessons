def is_prime(num):
    if num == 0:
        return False
    for i in range(2, (num // 2) + 1):
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
