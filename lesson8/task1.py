import re

EMAIL = re.compile(r'^([(\w\#\$\%\&\'\*\+\-\/\\\=\?\^\_\`\{\|\}\~\.]{0,})@(\w{0,}.[a-z]{2,3})')  # Не нашёл как
# ограничить, чтобы точка не повторялась больше одного раза подряд


def email_parse(email_address):
    data = EMAIL.findall(email_address)
    if len(data) == 1:
        email_dict = {'username': data[0][0], 'domain': data[0][1]}
        return email_dict
    else:
        raise ValueError(f'wrong email: {email_address}')


print(email_parse('support@geekbrains.ru'))
print(email_parse('!support@geekbrains.sdfru'))


