from typing import Iterable


# def new_zip(a: Iterable, b: Iterable, i: int = 0) -> None:
#     print((a[i], b[i]))
#     if i == (len(a) - 1):
#         return
#     new_zip(a, b, i + 1)


# new_zip([1, 2, 3], "abc")


def new_zip_2(x: Iterable, y: Iterable, file: list = [], i: int = 0) -> list:
    file.append((x[i], y[i]))
    if len(file) == len(x):
        return
    new_zip_2(x, y, file, i + 1)
    return file


print(new_zip_2([1, 2, 3, 4], "abcd"))

# попробуй вместо принта сохранять кортежи в список и передавать
#  этот список через весь стек вызовов как i, и возвращать этот список
