def slicer(any_tuple, element):
    if element not in any_tuple:
        return ()
    if any_tuple.count(element) > 1:
        first_index = any_tuple.index(element)
        second_index = any_tuple.index(element, first_index + 1) + 1
        return any_tuple[first_index:second_index]
    else:
        return any_tuple[any_tuple.index(element) :]
