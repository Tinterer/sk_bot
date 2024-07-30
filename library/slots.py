import random
from library.casino import Casino_Drawer

class Slot():

    def __init__(self, TGame, TLose, TWin):
        self.slot1(TGame, TLose, TWin)

    def slot3k(TGame, TWin, TLose):
        
        x1 = 1 + (TGame + 1/ 10)
        x2 = 10 / (TWin + 1)
        x3 = TLose / 100

        k = x1 + x2 * x3

        return k
    
    def fruit_slot(user_id, guild_id):

        user_id = str(user_id)
        code1 = random.randint(1, 10)
        code2 = random.randint(1, 10)
        code3 = random.randint(1, 10)

        if code1 == code2 == code3: #мегамэтч
            k = code1 + code2 + code3
        elif code1 == 1 and code2 == 2 and code3 == 3: #яблочный спас
            k = code1 * code2 * code3
        elif code1 == 7 and code2 == 8 and code3 == 10:
            k = 7 * 8 / 10
        elif (code1 + code2 + code3) % 2 == 1:
            k = max(code1, code2, code3) / (100  * code2 * code3)
        elif (code1 + code2 + code3) % 2 == 0:
            k = max(code1, code2, code3) / (10 * (code2 + code3))

        else:
            k = code1 / 10 * code2

        q = [code1, code2, code3, k]

        Casino_Drawer.test_r3(user_id, guild_id, 'r3', 'fs', code1, code2, code3, k)

        return q
    
            
            
