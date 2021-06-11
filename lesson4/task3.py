from requests import get
from decimal import Decimal
import datetime


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
    data_index = response.find('Date="')
    response_date = datetime.date(int(response[data_index + 12: data_index + 16]),
                                  int(response[data_index + 9: data_index + 11]),
                                  int(response[data_index + 6: data_index + 8]),)
    answer = f'{rate_dec} {response_date}'
    return answer


print(currency_rates('USD'))
print(currency_rates('UsD'))
print(currency_rates('EUR'))
print(currency_rates('eur'))
print(currency_rates('qwe'))
