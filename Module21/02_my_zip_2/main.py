from typing import Iterable


def new_zip(a: Iterable, b: Iterable, i=0) -> None:
    print((a[i], b[i]))
    if i == (len(a) - 1):
        return
    new_zip(a, b, i + 1)


new_zip([1, 2, 3], "abc")
