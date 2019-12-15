# -*- coding: utf8 -*-

from pprint import pprint
import json
import requests

TOKEN = "73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1"

class User:

    def __init__(self, access_token):
        self.access_token = access_token

    def get_params(self):
        return {
            "access_token": self.access_token,
            "v": 5.101,
            "extended": 1,
            "fields": "members_count"
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

evgeny = User(TOKEN)

user_info = evgeny.get_info()
#pprint(user_info)


info_group = evgeny.get_group()
#print('Количество групп:', info_group['response']["count"])

for i, index_group in enumerate(info_group['response']["items"]):
    #print('-')
    group_name = index_group['name']
    group_id = index_group['id']
    members_count = index_group['members_count']
    groups = {'group_name': group_name, 'group_id': group_id, 'members_count': members_count}

    #print(group_id)


    def get_group_members():
        params = {
            "access_token": TOKEN,
            "v": 5.101,
            "extended": 1,
            "fields": "members_count",
            "group_id": 8564
        }
        response = requests.get(
            "https://api.vk.com/method/groups.getMembers",
            params
        )
        return response.json()

    #print(type(groups))

    info_2 = get_group_members()
    for id in info_2['response']["items"]:
        group_set = set()
        group_set.add(id['id'])

        pprint(group_set)
