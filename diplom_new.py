# -*- coding: utf8 -*-

import json
import time

import requests

TOKEN = "73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1"

class User:

    def __init__(self, TOKEN):
        self.access_token = TOKEN

    def get_params(self):
        return {
            "access_token": self.access_token,
            "v": 5.101,
            "extended": 1,
            "fields": "members_count",
            'user_id': user_name
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

    def get_friends_list(self):
        params = self.get_params()
        response = requests.get(
            "https://api.vk.com/method/friends.getLists",
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

def only_user_group(user_name):
    user = User(TOKEN)

# определяем множество друзей пользователя
    user_info_friends = user.get_friends()
    friend_sit = []
    for index_friend in user_info_friends['response']["items"]:
        if index_friend.get('id') > 0:
            friend_sit.append(index_friend.get('id'))

    info_group = user.get_group()

    group_ide = []
    user_group_id = set()
    for index in info_group['response']["items"]:
        group_name = index['name']
        group_id = index['id']
        members_count = index['members_count']
        groups = {'group_name': group_name, 'group_id': group_id, 'members_count': members_count}
        group_ide.append(groups)
        user_group_id.add(index['id'])

    new_list_group = []
    for number_group in user_group_id:
        for a in friend_sit:
            def get_is_group_members():
                params = {
                    "access_token": TOKEN,
                    "v": 5.101,
                    "extended": 0,
                    "group_id": number_group,
                    "user_ids": a
                }
                response = requests.get(
                    "https://api.vk.com/method/groups.isMember",
                    params
                )
                return response.json()

            is_user = get_is_group_members()
            time.sleep(0.42)
            try:
                for mem_is in is_user.get('response'):
                    print('-')
                    if mem_is['member'] == 1:
                        if number_group not in new_list_group:
                            new_list_group.append(number_group)
                            
            except TypeError:
                print('Объект не найден')

    group_ide_new = []
    for elem in group_ide:
        if elem['group_id'] not in new_list_group:
            group_name = elem['group_name']
            group_id = elem['group_id']
            members_count = elem['members_count']
            ide_new = {'group_name': group_name, 'group_id': group_id, 'members_count': members_count}
            group_ide_new.append(ide_new)

    with open('groups.json', "w", encoding='cp1251') as f:
        json.dump(group_ide_new, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    user_name = input('Введите id пользователя или его screen name')
only_user_group(user_name)
