# -*- coding: utf8 -*-

from pprint import pprint
import json


import requests

TOKEN = "73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1"

user_id = input('Введите id пользователя или его screen name')

class User:

    def __init__(self, TOKEN):
        self.access_token = TOKEN


    def get_params(self):
        return {
            "access_token": self.access_token,
            "v": 5.101,
            "extended": 1,
            "fields": "members_count", #"deactivated"
            'user_ids': user_id
        }

    def get_info(self):
        params = self.get_params()
        response = requests.get(
            "https://api.vk.com/method/users.get",
            params
        )
        return response.json()

    def get_friends(self):
        params = self.get_params()
        response = requests.get(
            "https://api.vk.com/method/friends.get",
            params
        )
        return response.json()

    def get_group(self):
        params = self.get_params()
        response = requests.get(
            "https://api.vk.com/method/groups.get",
            params
        )
        return response.json()

user = User(TOKEN)
user_info = user.get_info()
#pprint(user_info)

#множество друзей пользователя
user_info_friends = user.get_friends()
friend_id_set = set()
for n, index_friend in enumerate(user_info_friends['response']["items"]):
    print('-')
    friend_id_set.add(index_friend['id'])

print(friend_id_set)


info_group = user.get_group()
#печатает состав групп
group_ide = []
user_group_id = set()
for i, index in enumerate(info_group['response']["items"]):
    #print('-')
    #print(news['name'])
    #word.append(news['name'])
    group_name = index['name']
    group_id = index['id']
    members_count = index['members_count']
    groups = {'group_name': group_name, 'group_id': group_id, 'members_count': members_count}
    #group_id.append(index['id'])
    group_ide.append(groups)
    user_group_id.add(index['id'])

#print(group_ide)
print(user_group_id)

group_id = 4100014

def get_group_members():
    params = {
        "access_token": TOKEN,
        "v": 5.101,
        "extended": 1,
        "fields": "members_count",
        #"count": 0,
        #"offset": 0,
        "group_id": group_id
    }
    response = requests.get(
        "https://api.vk.com/method/groups.getMembers",
        params
    )
    return response.json()
offset = 0
count = 0
array = []
group_set_user = set()
while True:
    resp = get_group_members()
    array += resp['response']["items"]
    offset += 1000
    #group_set_user = set()
    for id_user_friend in resp['response']["items"]:
         if offset > id_user_friend["id"]:
             break
    for user_friend in array:
        group_set_user.add(user_friend['id'])
    print(type(group_set_user))
