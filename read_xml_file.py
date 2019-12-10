# -*- coding: utf8 -*-

from collections import Counter
import xml.etree.ElementTree as ET
#
tree = ET.parse('newsafr.xml')
root = tree.getroot()
items = root.findall("channel/item/description")

lenght = 6
word = []
for element in items:
     word.extend(word.lower() for word in element.text.split() if len(word) > lenght)
counter = Counter(word)
print('Топ 10 слов в новостях:')
for i in counter.most_common(10):
    print('слово', "'" + i[0] + "'", 'встречалось', i[1], 'раз')
