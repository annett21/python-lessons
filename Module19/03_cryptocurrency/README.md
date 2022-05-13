## Задача 3. Криптовалюта
### Что нужно сделать
При работе с API (application programming interface) сайта биржи по криптовалюте вы получили вот такие данные в виде словаря:

```python
data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}
```

Теперь вам предстоит немного обработать эти данные.

Напишите программу, которая выполняет следующий алгоритм действий:

1. Вывести списки ключей и значений словаря.
1. В “ETH” добавить ключ “total_diff” со значением 100.
1. Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”.
1. Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”.
1. Внутри "sec_token_info" изменить название ключа “price” на “total_price”.

После выполнения алгоритма выводить результат (словарь) не нужно.
### Что оценивается
- Результат вычислений корректен.
- В коде соблюдается порядок действий алгоритма.
- Не используется других переменных, кроме data.
