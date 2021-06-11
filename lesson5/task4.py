from time import perf_counter


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# Первый вариант

start = perf_counter()
new_list = []
for i in src[1:]:
    if i > src[src.index(i) - 1]:
        new_list.append(i)

print(new_list)
end = perf_counter()
print(end - start)

# Второй вариант с оптимизацией

start = perf_counter()
result = [i for i in src[1:] if i > src[src.index(i) - 1]]
print(result)
end = perf_counter()
print(end - start)
