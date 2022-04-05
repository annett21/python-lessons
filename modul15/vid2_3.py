dogs = int(input('Сколько собак участвует? '))

amount_of_points = []

for dog in range(dogs):
    points = int(input('Сколько очков у собаки? '))
    amount_of_points.append(points)

print(amount_of_points)

max_point = max(amount_of_points)
min_point = min(amount_of_points)

ndex_1 = amount_of_points.index(max_point)
ndex_2 = amount_of_points.index(min_point)

amount_of_points[ndex_1], amount_of_points[ndex_2] = amount_of_points[ndex_2], amount_of_points[ndex_1]

print(amount_of_points)