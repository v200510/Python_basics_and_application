# 3.6 API

# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
# Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.
# Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

# Пример запроса к интересному числу:
# http://numbersapi.com/31/math?json=true
# Пример запроса к скучному числу:
# http://numbersapi.com/999/math?json=true

# Пример входного файла:
# 31
# 999
# 1024
# 502

# ﻿Пример выходного файла:
# Interesting
# Boring
# Interesting
# Boring

import requests
f = open('dataset_24476.txt', 'r')
lns = f.read().splitlines()
for num in lns:
    r = requests.get(r"http://numbersapi.com/" + num + r"/math?json=false").json()
    print("Interesting") if r['found'] else print("Boring")
