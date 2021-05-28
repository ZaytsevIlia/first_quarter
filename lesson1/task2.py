numbers = []

for i in range(1, 1000, 2):
    i **= 3
    numbers.append(i)

print(numbers)


# a) Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
print('Задание "a"')
my_sum = []

for number in numbers:
    sum_digits = 0
    num = number
    while num != 0:
        sum_digits += num % 10
        num = num // 10
    if sum_digits % 7 == 0:
        my_sum.append(number)

print(sum(my_sum))


# b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
#    сумма цифр которых делится нацело на 7.
print('Задание "b"')
new_number = []

for number in numbers:
    number += 17
    new_number.append(number)

print(new_number)

my_sum = 0

for number in new_number:
    sum_digits = 0
    num = number
    while num != 0:
        sum_digits += num % 10
        num = num // 10
    if sum_digits % 7 == 0:
        my_sum += number

print(my_sum)


# c) * Решить задачу под пунктом b, не создавая новый список.
print('Задание "c"')
my_sum = 0

for number in numbers:
    sum_digits = 0
    num = number
    while num != 0:
        sum_digits += num % 10
        num = num // 10
    if sum_digits % 7 == 0:
        my_sum += number

print(my_sum)
