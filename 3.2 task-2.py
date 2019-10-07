# 3.2 Стандартные методы и функции для строк

# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
# Выведите одно число – количество вхождений строки t в строку s.

# Пример:
# s = "abababa"
# t = "aba"
# Вхождения строки t в строку s:
# abababa
# abababa
# abababa

# Sample Input 1:
# abababa
# aba

# Sample Output 1:
# 3

s, t = (input() for i in range(2))
n = 0
for i in range(len(s)):
    if s[i:i + (len(t))] == t: n += 1
print(n)
