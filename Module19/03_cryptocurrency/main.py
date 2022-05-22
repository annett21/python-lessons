python_data = {
    "address": "0x544444444444",
    "ETH": {"balance": 444, "totalIn": 444, "totalOut": 4},
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
                "price": False,
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0,
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
                "price": False,
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0,
        },
    ],
}

print(python_data.keys())
print()
print(python_data.values())

python_data["ETH"]["total_diff"] = 100

python_data["tokens"][0]["fst_token_info"]["name"] = "doge"

for data in python_data["tokens"]:
    python_data["ETH"]["total_out"] = data.pop("total_out")


python_data["tokens"][1]["sec_token_info"]["total_price"] = python_data["tokens"][1][
    "sec_token_info"
].pop("price")
