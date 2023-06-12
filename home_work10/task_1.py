# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


from random import choice, randint
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(choice(letters) for i in range(length))
    return random_string


def generate_random_name():
    while True:
        str1 = generate_random_string(randint(1, 15))
        str2 = generate_random_string(randint(1, 15))
        yield f'{str1} {str2}'

#    l1, l2 = (choice(letter) for _ in randint(1, 15))
#    print(l1, l2, sep=' ')

gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
