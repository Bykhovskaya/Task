# -*- coding: utf8 -*-
#
from collections import Counter

import json

with open('newsafr.json', encoding='utf-8-sig') as f:
    json_data = json.load(f)
    lenght = 6
    word = []
    for news in json_data["rss"]["channel"]["items"]:
        word.extend(word.lower() for word in news["description"].split() if len(word) > lenght)
    counter = Counter(word)
    print('Топ 10 слов в новостях:')
    for i in counter.most_common(10):
         print('слово',"'"+i[0]+"'",'встречалось', i[1],'раз')
