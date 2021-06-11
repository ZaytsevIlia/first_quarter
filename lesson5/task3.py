from itertools import zip_longest


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

journal = (name for name in zip_longest(tutors, klasses, fillvalue=None))

print(next(journal))
print(next(journal))
print(next(journal))
print(next(journal))
print(next(journal))
print(next(journal))
print(next(journal))
print(next(journal))
