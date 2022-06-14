from functools import lru_cache


@lru_cache(maxsize=1000)
def fobinacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fobinacci(n - 1) + fobinacci(n - 2)


num_pos = int(input("Введите позицию числа в ряде Фибоначчи: "))

print("Число:", fobinacci(num_pos))
