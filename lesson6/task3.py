from itertools import zip_longest
import json

with open("users.csv") as f_users, open("hobby.csv") as f_hobby, open('result_task3.json', 'w') as f:
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
    json.dump(my_dict, f)
