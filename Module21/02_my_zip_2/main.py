from typing import Optional, Sequence


def new_zip_2(x: Sequence, y: Sequence, file: Optional[list] = None) -> list:
    if file is None:
        file = []
    if not x or not y:
        return []
    file.append((x[0], y[0]))
    new_zip_2(x[1:], y[1:], file)
    return file


print(new_zip_2([1, 2, 3], "abcd"))
print(new_zip_2("abctd", [1, 2, 3, 7, 4]))
print(new_zip_2([1, 2, 3, 4], "abc"))
