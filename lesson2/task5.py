#   A. Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
# получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).

print()
print('A.')
prices = [54.34, 43.06, 123.7, 2500, 2.55, 560.8, 783.44, 1145.99, 4208.21, 2224.5, 43.01, 12.12, 1478.23, 984.30]

new_prices = []
for price in prices:
    price_split = str(price).split('.')
    if len(price_split) == 1:
        rub = price_split[0]
        penny = 00
        new_prices.append(f'{rub} руб {penny:02d} коп')
    else:
        rub = price_split[0]
        penny = int(price_split[1])
        new_prices.append(f'{rub} руб {penny:02d} коп')

print(", ".join(new_prices))

#  B.  Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после
# сортировки остался тот же).

print()
print('B.')
print(id(prices))
prices.sort()
print(prices)
print(id(prices))

#  C.  Создать новый список, содержащий те же цены, но отсортированные по убыванию.

print()
print('C.')
print(list(reversed(sorted(prices))))

#  D.  Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию,
# написав минимум кода?

print()
print('D.')
print(list(reversed(sorted(prices)))[:5])

