nice_list = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
]

# list = [[elements - element[item]]]

new_list = [item for elements in nice_list for element in elements for item in element]

print(new_list)
