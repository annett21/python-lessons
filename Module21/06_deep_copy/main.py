def site_copy(name):
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
for _ in range(number_site):
    new_name = input("Введите название продукта для нового сайта: ")
    print(f"Сайт для {new_name}:")
    print(site_copy(new_name))
    print()
