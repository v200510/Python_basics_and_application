# 3.3 Регулярные выражения в Python

# Вам дана последовательность строк.
# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w.

# Sample Input:
# this is a text
# "this' !is. ?n1ce,

# Sample Output:
# htis si a etxt
# "htis' !si. ?1nce,

import re, sys

[print(re.sub(r'\b(\w)(\w)', r'\2\1', line), end="") for line in sys.stdin]
