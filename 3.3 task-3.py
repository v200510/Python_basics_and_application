# 3.3 Регулярные выражения в Python

# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.

# Sample Input:
# zabcz
# zzz
# zzxzz
# zz
# zxz
# zzxzxxz

# Sample Output:
# zabcz
# zzxzz

import re, sys

[print(line.rstrip()) for line in sys.stdin if re.search(r'z.{3}z', line)]
