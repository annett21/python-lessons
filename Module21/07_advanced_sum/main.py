from typing import Any, Iterable


def new_sum(*args: Any) -> int:
    return sum(
        new_sum(*arg) if isinstance(arg, Iterable) else arg for arg in args
    )


print(new_sum([[1, 2, [3]], [1], 3]))
print(new_sum(1, 2, 3, 4, 5))
