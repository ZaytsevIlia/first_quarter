def thesaurus_adv(*users):
    username_dict = {}
    for user in users:
        name = user.split()[0]
        surname = user.split()[1]
        key_surname = surname[:1]
        key_name = name[:1]
        username_dict.setdefault(key_surname, {})
        username_dict[key_surname].setdefault(key_name, [])
        username_dict[key_surname][key_name].append(user)
    return username_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", 'Татьяна Андреева',
                    'Ирина Петрова', 'Лариса Гузеева'))
