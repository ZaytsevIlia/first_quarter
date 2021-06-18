# Нерабочий код, пока не знаю как сделать, разбор на видео не смотрел, в свободное время постараюсь сделать.
from sys import argv

with open('bakery.csv', 'r+') as f:
    for i, line in enumerate(f, 1):
        if i == argv[1]:
            f.writelines(f'{argv[2]}\n')
        else:
            f.writelines(line)
