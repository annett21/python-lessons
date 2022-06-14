nice_list = [
    1,
    2,
    [3, 4],
    [[5, 6, 7], [8, 9, 10]],
    [[11, 12, 13], [14, 15], [16, 17, 18]],
]


def open_list(data: list) -> list:
    if data == []:
        return data
    if isinstance(data[0], list):
        return open_list(data[0]) + open_list(data[1:])
    return data[:1] + open_list(data[1:])


print(open_list(nice_list))
