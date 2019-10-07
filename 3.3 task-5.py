# 3.3 Регулярные выражения в Python

# Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).

# Sample Input:
# blabla is a tandem repetition
# 123123 is good too
# go go
# aaa

# Sample Output:
# blabla is a tandem repetition
# 123123 is good too

import re, sys

[print(line.rstrip()) for line in sys.stdin if re.search(r'\b(.+)\1\b', line)]
