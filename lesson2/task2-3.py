my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

print(my_list)

for element in my_list:
    if element.isdigit():
        var = int(my_list[my_list.index(element)])
        my_list.insert(my_list.index(element), f'{var:02d}')
        my_list.remove(element)
    for i in element:
        if i == '+' or i == '-':
            var = int(my_list[my_list.index(element)])
            my_list.insert(my_list.index(element), f'+{var:02d}')
            my_list.remove(element)

print(my_list)

for element in reversed(my_list):
    if element.isdigit():
        di = my_list.index(element)
        my_list.insert(di, '"')
        my_list.insert(di + 2, '"')
    for i in element:
        if i == '+' or i == '-':
            di = my_list.index(element)
            my_list.insert(di, '"')
            my_list.insert(di + 2, '"')

print(my_list)

print(' '.join(my_list))

# Чтобы убрать пробелы придумал только один способ, совсем неэффективный это с методом .replace, просто, например,
# брать '" 05 " и менять на '"05"', но не думаю что именно такого от нас требует задание
