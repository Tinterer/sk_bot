import datetime
import shutil
import json

PERSONAL_INFO_DEFAULT = {
    'balance': 50,
    'personal_status': '',
    'personal_theme': 'dark',
    'personal_counter': 0,
    'total_lose': 0,
    'total_win': 0,
    'premium': 0,
    '3k_use': 0
}

MAIN_SERVER_INFO = {
    'total_counter': 0,
    'total_balance': 0,
    'total_wins': 0,
    'ppremium_counter': 0,
    'premium_status': 0,
    'registered_users': 0
}

class Utilits:

    def __init__(self, user_id, guild_id, user_info, server_info):
        self.user_id = user_id
        self.guild_id = guild_id
        self.user_info = user_info
        self.server_info = server_info
        self.get_user_info(user_id, guild_id)
        self.get_server_info(guild_id)
        self.check_server(guild_id)
        self.user_dump(user_id, guild_id, user_info)
        self.server_dumo(guild_id, server_info)

    def check_server(guild_id):
        name = 's' + str(guild_id)
        with open ('servers.json', 'r', encoding = 'utf-8') as file:
            serv = json.load(file)
        if guild_id not in serv.keys():
            shutil.copyfile('users_lobby/example.json', f'users_lobby/{name}.json')
        

    def get_user_info(user_id, guild_id):

        user_id = str(user_id)
        guild_id = str(guild_id)

        Utilits.check_server(guild_id)

        with open(f'users_lobby/s{guild_id}.json', 'r', encoding='utf-8') as file_info:
            users_info = json.load(file_info)
        
        if user_id not in users_info.keys():
            users_info[user_id] = PERSONAL_INFO_DEFAULT

        with open(f'users_lobby/s{guild_id}.json', 'w') as file_info:
            json.dump(users_info, file_info)
        
        return users_info[user_id]
    
    def get_server_info(guild_id):

        Utilits.check_server(guild_id)
        guild_id = str(guild_id)

        with open('servers.json', 'r', encoding='utf-8') as file_info:
            servers_info = json.load(file_info)

        if guild_id not in servers_info.keys():
            servers_info[guild_id] = MAIN_SERVER_INFO
        
        with open('servers.json', 'w') as file_info:
            json.dump(servers_info, file_info)

        return servers_info[guild_id]
    
    def user_dump(user_id, guild_id, user_info):

        user_id = str(user_id)

        Utilits.check_server(guild_id)

        with open(f'users_lobby/s{guild_id}.json', 'r', encoding='utf-8') as file_info:
            users_info = json.load(file_info)

        users_info[user_id] = user_info

        with open(f'users_lobby/s{guild_id}.json', 'w') as file_info:
            json.dump(users_info, file_info)


    def server_dump(guild_id, server_info):

        guild_id = str(guild_id)

        with open('servers.json', 'r', encoding='utf-8') as file_info:
            servers_info = json.load(file_info)

        servers_info[guild_id] = server_info
        
        with open('servers.json', 'w') as file_info:
            json.dump(servers_info, file_info)

    def kd3k(user_id, guild_id):

        user_id = str(user_id)
        guild_id = str(guild_id)
        time_now = int(datetime.datetime.now().timestamp())

        with open(f'users_lobby/s{guild_id}.json', 'r', encoding = 'utf-8') as file:
            users_info = json.load(file)

        users_info[user_id]['3k_use'] = time_now

        with open(f'users_lobby/s{guild_id}.json', 'w', encoding = 'utf-8') as file:
            json.dump(users_info, file)