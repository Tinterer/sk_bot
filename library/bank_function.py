import json

from library.utilits import Utilits

PERSONAL_INFO_DEFAULT = {
    'balance': 0,
    'personal_status': '',
    'personal_theme': 'dark',
    'personal_counter': 0,
    'total_lose': 0,
    'total_win': 0,
    'premium': 0
}

class Bank:

    def __init__(self, user_id, guild_id, amount, member_id):
        self.user_id = user_id
        self.guild_id = guild_id
        self.amount = amount
        self.member_id = member_id
        self.replenish_balance(user_id, guild_id, amount)
        
    def replenish_balance(user_id, guild_id, amount):

        user_id = str(user_id)
        print(Utilits.check_server(guild_id))

        with open(f'users_lobby/s{guild_id}.json', 'r', encoding='utf-8') as file_info:
            users_info = json.load(file_info)

        if user_id not in users_info.keys():
            users_info[user_id] = PERSONAL_INFO_DEFAULT

        with open(f'users_lobby/s{guild_id}.json', 'w') as file_info:
            json.dump(users_info, file_info)   

        users_info[user_id]['balance'] = int(users_info[user_id]['balance']) + int(amount)
        
        with open(f'users_lobby/s{guild_id}.json', 'w') as file:
            json.dump(users_info, file)
            
        return users_info[user_id]['balance']