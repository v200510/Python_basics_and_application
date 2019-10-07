# 3.4 Обзорно об интернете: http-запросы, html-страницы и requests

# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">,
# возможно с дополнительными параметрами внутри тега. Из A можно перейти в B за два перехода если существует такой
# документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

# Sample Input 1:
# https://stepic.org/media/attachments/lesson/24472/sample0.html
# https://stepic.org/media/attachments/lesson/24472/sample2.html

# Sample Output 1:
# Yes

# Sample Input 2:
# https://stepic.org/media/attachments/lesson/24472/sample0.html
# https://stepic.org/media/attachments/lesson/24472/sample1.html

import re, sys, requests as rq

def GetContent(url):
    try:
        res = rq.get(url.rstrip())
        return re.findall(r'<a.*href="([^"]*)"', res.text)
    except:
        return []

fl = False
urls = [i for i in sys.stdin]
url1 = GetContent(urls[0])
for lineUrl in url1:
    if urls[1] in GetContent(lineUrl):
        fl = True
        break
print("Yes" if fl else "No")
