def site_copy(name=0):
    site = {
        "html": {
            "head": {"title": f"Куплю/продам {name} недорого"},
            "body": {
                "h2": f"У нас самая низкая цена на {name}",
                "div": "Купить",
                "p": "продать",
            },
        }
    }
    return site


number_site = int(input("Сколько сайтов: "))
for i_site in range(number_site):
    new_name = input("Введите название продукта для нового сайта: ")
    print(f"Сайт для {new_name}:")
    print(site_copy(new_name))
    print()
