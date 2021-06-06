def num_translate_adv(word, translate_dict):
    if word.istitle():
        low_word = word.lower()
        return translate_dict[low_word].title()
    else:
        return translate_dict[word]


eng_rus_dict = {'one': 'один',
                'two': 'два',
                'three': 'три',
                'four': 'четыре',
                'five': 'пять',
                'six': 'шесть',
                'seven': 'семь',
                'eight': 'восемь',
                'nine': 'девять',
                'ten': 'десять'}

user_word = input('Введите слово: ')
print(num_translate_adv(user_word, eng_rus_dict))
