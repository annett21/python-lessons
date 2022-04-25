heights_in_first_class = list(range(160, 177, 2))
heights_in_second_class = list(range(162, 181, 3))

all_heights = heights_in_first_class + heights_in_second_class
all_heights.sort()

print("The sorted list of heights from two class:", all_heights)
