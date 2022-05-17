num = int(input("Количество стран: "))
countries = dict()

for i in range(1, num + 1):
    country = input(f"{i} страна: ")
    country = country.split()
    countries[country[0]] = country[1:]


for j in range(1, 4):
    city = input(f"{j} город: ")
    for country in countries.keys():
        if city in countries[country]:
            print(f"Город {city} расположен в стране {country}.")
            break
    else:
        print(f"По городу {city} данных нет.")
