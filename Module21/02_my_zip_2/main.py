from typing import Iterable, Optional


def new_zip_2(
    x: Iterable, y: Iterable, file: Optional[list] = None, i: int = 0
) -> list:
    if file is None:
        file = []
    file.append((x[i], y[i]))
    if len(file) == len(x) or len(file) == len(y):
        return
    new_zip_2(x, y, file, i + 1)
    return file


print(new_zip_2([1, 2, 3], "abcd"))
print(new_zip_2("abctd", [1, 2, 3, 7, 4]))
print(new_zip_2([1, 2, 3, 4], "abc"))
