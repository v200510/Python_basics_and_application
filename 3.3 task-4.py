# 3.3 Регулярные выражения в Python

# Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш "\﻿".

# Sample Input:
# \w denotes word character
# No slashes here

# Sample Output:
# \w denotes word character

import re, sys

[print(line.rstrip()) for line in sys.stdin if re.search(r'\\', line)]
