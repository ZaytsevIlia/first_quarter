duration = int(input('Введите количество секунд: '))


if duration < 60:
    print(duration, "сек")
elif (duration >= 60) and (duration < 3600):
    minutes = duration // 60
    seconds = duration % 60
    print(minutes, 'мин, ', seconds, 'сек')
elif (duration >= 3600) and (duration < 86400):
    hours = duration // 60 // 60
    minutes = (duration - hours * 3600) // 60
    seconds = duration - hours * 3600 - minutes * 60
    print(hours, 'час, ', minutes, 'мин, ', seconds, 'сек')
elif duration >= 86400:
    days = duration // 60 // 60 // 24
    hours = (duration - days * 86400) // 60 // 60
    minutes = (duration - days * 86400 - hours * 3600) // 60
    seconds = (duration - days * 86400 - hours * 3600 - minutes * 60) % 60
    print(days, 'дн, ', hours, 'час, ', minutes, 'мин, ', seconds, 'сек')