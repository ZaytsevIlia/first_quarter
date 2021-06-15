from sys import argv
from itertools import zip_longest

program, users, hobby, users_hobby = argv
try:
    with open(users) as f_users, open(hobby) as f_hobby, open(users_hobby, 'x') as f:
        my_dict = {}
        sum_lines_user = 0
        sum_lines_hobby = 0

        for line in f_users:
            sum_lines_user += 1

        for line in f_hobby:
            sum_lines_hobby += 1

        if sum_lines_hobby > sum_lines_user:
            exit(1)

        f_users.seek(0)
        f_hobby.seek(0)

        for line_f_users, line_f_hobby in zip_longest(f_users, f_hobby):
            if line_f_hobby is not None:
                my_dict[line_f_users.strip().replace(',', ' ')] = line_f_hobby.strip()
            else:
                my_dict[line_f_users.strip().replace(',', ' ')] = line_f_hobby
        for user, hobby in my_dict.items():
            f.write(f'{user}: {hobby}\n')
except FileExistsError:
    print('Исходный файл с таким названием уже существует.')
