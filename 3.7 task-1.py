# 3.7 XML, библиотека ElementTree, библиотека lxml

# Вам дано описание пирамиды из кубиков в формате XML. Кубики могут быть трех цветов: красный (red), зеленый (green)
# и синий (blue﻿). Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

# Пример:
# <cube color="blue">
#   <cube color="red">
#     <cube color="green">
#     </cube>
#   </cube>
#   <cube color="red">
#   </cube>
# </cube>

# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1.
# Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками,
# имеют ценность 3. И т. д. Ценность цвета равна сумме ценностей всех кубиков этого цвета. Выведите через пробел
# три числа: ценности красного, зеленого и синего цветов.

# Sample Input:
# <cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>

# Sample Output:
# 4 3 1

import xml.sax as sax
import xml.sax.handler as saxhandler

src = input()

class TreeBuilder(saxhandler.ContentHandler):
    def __init__(self):
        self.level = 0
        self.rez = {'red': 0, 'green': 0, 'blue': 0}

    def startElement(self, name, attrs):
        self.level += 1
        self.rez[attrs["color"]] += self.level

    def endElement(self, name):
        self.level -= 1

    def print_rez(self):
        print(f'{self.rez["red"]} {self.rez["green"]} {self.rez["blue"]}')

builder = TreeBuilder()
sax.parseString(src, builder)
builder.print_rez()
