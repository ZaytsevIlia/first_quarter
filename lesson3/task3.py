def thesaurus(*names):
    alphabet_names = sorted(names)
    names_dict = {}
    for name in alphabet_names:
        names_dict.setdefault(name[:1], []).append(name)
    return names_dict


my_dict = thesaurus('Иван', 'Мария', 'Петр', 'Илья', 'Сергей', 'Татьяна', 'Ксения', 'Андрей', 'Алексей', 'Александр')
print(my_dict)
