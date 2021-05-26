number = int(input('Введите число: '))

if (number >= 11) and (number <= 14):
    print(number, 'процентов')
elif number % 10 == 1:
    print(number, 'процент')
elif (number % 10 >= 2) and (number % 10 <= 4):
    print(number, 'процента')
elif (number % 10 >= 5) and (number % 10 <= 9):
    print(number, 'процентов')
elif number % 10 == 0:
    print(number, 'процентов')