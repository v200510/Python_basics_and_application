# 3.5 Распространённые форматы текстовых файлов: CSV, JSON

# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле
# name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

# ﻿Эквивалент на Python:
# class A:
#     pass
#
# class B(A, C):
#     pass
#
# class C(A):
#     pass

# Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от
# одного класса более одного раза.
# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
# <имя класса> : <количество потомков>
# Выводить классы следует в лексикографическом порядке.

# Sample Input:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

# Sample Output:
# A : 3
# B : 1
# C : 2

import json


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


dd, buf = {}, []
mss = json.loads(input())
for i in range(len(mss)):
    dd[mss[i]["name"]] = set(mss[i]["parents"])
for str in dd:
    s = 1
    for stp in dd:
        if list(dfs_paths(dd, stp, str)):
            s += 1
    buf.append([str, s])
buf = sorted(buf)
[print(f"{buf[ind][0]} : {buf[ind][1]}") for ind in range(len(buf))]
