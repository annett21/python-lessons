def slicer(any_tuple, element):
    quantity = any_tuple.count(element)
    if quantity == 0:
        return ()
    if quantity == 1:
        return any_tuple[any_tuple.index(element) :]

    first_index = any_tuple.index(element)
    second_index = any_tuple.index(element, first_index + 1) + 1
    return any_tuple[first_index:second_index]
