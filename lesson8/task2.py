import re

DATA = re.compile(r'^(\d+.\d+.\d+.\d+) - - \[(\d{2}\/[A-Z][a-z]+\/\d{4}\:\d{2}\:\d{2}\:\d{2}\ \+\d{4})\] "([A-Z]+) '
                  r'(\/[a-z]+\/[a-z]+\_\d+) [A-Z]+\/\d+\.\d+\" (\d+) (\d+)')
DATA2 = re.compile(r'^([\w+\:+]+) - - \[(\d{2}\/[A-Z][a-z]+\/\d{4}\:\d{2}\:\d{2}\:\d{2}\ '
                   r'\+\d{4})\] "([A-Z]+) (\/[a-z]+\/[a-z]+\_\d+) [A-Z]+\/\d+\.\d+\" (\d+) (\d+)')

with open('nginx_logs.txt') as f:
    for line in f:
        try:
            print(DATA.findall(line)[0])
        except IndexError:
            print(DATA2.findall(line)[0])
