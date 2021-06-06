import random


def get_jokes(quantity_jokes):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    while quantity_jokes > len(nouns):
        quantity_jokes = int(input(f'Введите количество шуток от 1 до {len(nouns)}: '))

    jokes_list = []
    for jokes in range(0, quantity_jokes):
        nouns_for_joke = random.choice(nouns)
        adverbs_for_joke = random.choice(adverbs)
        adjectives_for_joke = random.choice(adjectives)
        joke = f'{nouns_for_joke} {adverbs_for_joke} {adjectives_for_joke}'
        jokes_list.append(joke)
        nouns.remove(nouns_for_joke)
        adverbs.remove(adverbs_for_joke)
        adjectives.remove(adjectives_for_joke)
    return jokes_list


user_quantity_jokes = int(input('Введите количетво шуток: '))
print(get_jokes(user_quantity_jokes))
