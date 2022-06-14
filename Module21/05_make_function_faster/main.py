def recur_factorial(n: int) -> int:
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


def calculating_math_func(data: int) -> int:
    result = recur_factorial(data)
    result /= data**3
    result = result**10
    return result


print(calculating_math_func(5))
