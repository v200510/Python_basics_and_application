#3.6 API

# В этой задаче вам необходимо воспользоваться API сайта artsy.net
# API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
# В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения,
# выведите их имена в лексикографическом порядке.

# Работа с API Artsy
# Полностью открытое и свободное API предоставляют совсем немногие проекты. В большинстве случаев, для получения доступа
# к API необходимо зарегистрироваться в проекте, создать свое приложение, и получить уникальный ключ (или токен), и в
# дальнейшем все запросы к API осуществляются при помощи этого ключа.
# Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу документации
# к API https://developers.artsy.net/start и выполнить необходимые шаги, а именно зарегистрироваться, создать приложение,
# и получить пару идентификаторов Client Id и Client Secret. Не публикуйте эти идентификаторы.
# После этого необходимо получить токен доступа к API. На стартовой странице документации есть примеры того, как можно
# выполнить запрос и как выглядит ответ сервера. Мы приведем пример запроса на Python.
# import requests
# import json
#
# client_id = '...'
# client_secret = '...'
#
# # инициируем запрос на получение токена
# r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
#                   data={
#                       "client_id": client_id,
#                       "client_secret": client_secret
#                   })
#
# # разбираем ответ сервера
# j = json.loads(r.text)
#
# # достаем токен
# token = j["token"]

# Примечание:
# ﻿В качестве имени художника используется параметр sortable_name в кодировке UTF-8.

# Пример входных данных:
# 4d8b92b34eb68a1b2c0003f4
# 537def3c139b21353f0006a6
# 4e2ed576477cc70001006f99

# Пример выходных данных:
# Abbott Mary
# Warhol Andy
# Abbas Hamra

import requests

client_id = '9c50cfb83763e9a80651'
client_secret = '68668291f7eda7057637a9290934a8cb'
token = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                      data={"client_id": client_id, "client_secret": client_secret}).json()["token"]
dash = []
with open(r'C:\Users\usr\Desktop\Shcool_Exercim\dataset_24476_4.txt') as file:
    for dashName in file:
        url = 'https://api.artsy.net/api/artists/{}'.format(dashName.strip())
        params = {'xapp_token': token}
        dt = requests.get(url, params=params).json()
        dash.append({'name': dt['sortable_name'], 'birthday': dt['birthday']})

[print(i['name']) for i in sorted(dash, key=lambda x: (x['birthday'], x['name']))]
