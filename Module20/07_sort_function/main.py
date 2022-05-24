def tpl_sort(any_tuple):
    for element in any_tuple:
        if not isinstance(element, int):
            return any_tuple
    return sorted(any_tuple)


print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))
