#ir a net ver do preço da bitcoin e com info do terminal saber o numero de bitcois

import requests
import sys

try:
    number_coins=float(sys.argv[1])
    bitcoin_info=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    bitcoin_info=bitcoin_info.json()
    price_bitcoin=bitcoin_info["bpi"]["EUR"]["rate_float"]
    amount=number_coins*price_bitcoin
    print(f"{amount:,.4f}€")


except IndexError:
    sys.exit("Missing command-line argument   ")

except ValueError:
    sys.exit("Command-line argument is not a number")