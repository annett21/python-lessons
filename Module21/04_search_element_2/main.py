from typing import Any

site = {
    "html": {
        "head": {"title": "Мой сайт"},
        "body": {
            "h2": "Здесь будет мой заголовок",
            "div": "Тут, наверное, какой-то блок",
            "p": "А вот здесь новый абзац",
        },
    }
}


def find_key(data: dict, key: str, i: int = 1) -> Any:
    if key in data:
        return data[key]

    for i_data in data.values():
        if isinstance(i_data, dict):
            i += 1
            result = find_key(i_data, key)
            if result:
                break
    else:
        result = None

    return result, i


search_key = input("Введите искомый ключ: ").lower()
search_parametr = input("Хотите ввести максимальную глубину? y/n: ")
if search_parametr == "y":
    depth = input("Введите максимальную глубину: ")
    # print(find_key(site, search_key, depth))

print(find_key(site, search_key))
