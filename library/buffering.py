import json
import datetime

PERSON = {
    'LastTimeOnline': 0,
    'TotalGames': 0,
    'TotalLose': 1,
    'TotalWin': 1,
    'TotalGameTime': 0
}

class Bufferisation:

    def __init__(self, user_id, result):
        self.user_id = user_id   
        self.resilt = result

    def checkInBuffer(user_id):

        user_id = str(user_id)
        
        with open('buffer.json', 'r', encoding = 'utf-8') as file:
            buffer = json.load(file)

        if user_id not in buffer:
            buffer[user_id] = PERSON
        with open('buffer.json', 'w', encoding = 'utf-8') as file:
            json.dump(buffer, file)            
        
            
    def backToZero(user_id):
        
        user_id = str(user_id)

        with open('buffer.json', 'r', encoding = 'utf-8') as file:
            buffer = json.load(file)

        if user_id not in buffer:
            buffer[user_id] = PERSON

        buffer[user_id]['LastTimeOnline'] = 0

        with open('buffer.json', 'w', encoding = 'utf-8') as file:
            json.dump(buffer, file)

    def TotalGames(user_id):

        user_id = str(user_id)

        with open('buffer.json', 'r', encoding = 'utf-8') as file:
            buffer = json.load(file)

        if user_id not in buffer:
            buffer[user_id] = PERSON

        buffer[user_id]['TotalGames'] += 1

        with open('buffer.json', 'w', encoding = 'utf-8') as file:
            json.dump(buffer, file)

    def addResult(user_id, result):
        
        user_id = str(user_id)

        with open('buffer.json', 'r', encoding = 'utf-8') as file:
            buffer = json.load(file)

        if user_id not in buffer:
            buffer[user_id] = PERSON

        if result == 1:
            buffer[user_id]['TotalWin'] += 1
        else:
            buffer[user_id]['TotalLose'] += 1

        with open('buffer.json', 'w', encoding = 'utf-8') as file:
            json.dump(buffer, file) 

    def delUser(user_id):
        
        user_id = str(user_id)

        with open('buffer.json', 'r', encoding = 'utf-8') as file:
            buffer = json.load(file)

        buffer.pop(f'{user_id}')

        with open('buffer.json', 'w', encoding = 'utf-8') as file:
            json.dump(buffer, file)

    def setTime(user_id):
        
        user_id = str(user_id)
        time_now = int(datetime.datetime.now().timestamp())

        with open('buffer.json', 'r', encoding = 'utf-8') as file:
            buffer = json.load(file)

        if user_id not in buffer:
            buffer[user_id] = PERSON

        buffer[user_id]['LastTimeOnline'] = time_now

        with open('buffer.json', 'w', encoding = 'utf-8') as file:
            json.dump(buffer, file)

    def getUserInfo(user_id):
        
        user_id = str(user_id)

        with open('buffer.json', 'r', encoding = 'utf-8') as file:
            buffer = json.load(file)

        if user_id not in buffer:
            buffer[user_id] = PERSON

        with open('buffer.json', 'w', encoding = 'utf-8') as file:
            json.dump(buffer, file)

        return buffer[user_id]

        


        


        
            
    