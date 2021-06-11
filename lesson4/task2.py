from requests import get
from decimal import Decimal


def currency_rates(currency_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    currency_code = currency_code.upper()
    currency_index = response.find(currency_code)

    if currency_index == -1:
        return None

    response_for_currency = response[currency_index:]
    rate = (response_for_currency[response_for_currency.find('<Value>') + 7:response_for_currency.find('<Value>') + 14])
    rate_dec = Decimal(rate.replace(',', '.'))
    rate_dec = rate_dec.quantize(Decimal('1.0000'))
    return rate_dec


print(currency_rates('USD'))
print(currency_rates('UsD'))
print(currency_rates('EUR'))
print(currency_rates('eur'))
print(currency_rates('qwe'))
