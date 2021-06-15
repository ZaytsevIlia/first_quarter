my_list = []

with open('nginx_logs.txt') as f:
    for line in f:
        my_list.append((line[:line.find(' ')], line[line.find('"') + 1:line.find(' ', line.find('"'))],
                        line[line.find(' ', line.find('"')) + 1: line.find(' ', line.find('_'))]))

for i in my_list[:50]:
    print(i)
