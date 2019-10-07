# 3.3 Регулярные выражения в Python

# Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.

# Sample Input:
# I need to understand the human mind
# humanity

# Sample Output:
# I need to understand the computer mind
# computerity

import re, sys

[print(re.sub(r'human', 'computer', line).rstrip()) for line in sys.stdin]
