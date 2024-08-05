import random

WALK_PATTERNS = {
    "1": {
        'description': 'На прогулке вы встретили злую собаку и убегая от нее потеряли половину своих денег.',
        'k': 0.5,
        'summ': 0
    },
    "2": {
        'description': 'Вы решили проехаться на автобусе и мошенники с терминалом сняли все деньги с вашей карточки в рюкзаке.',
        'k': 0,
        'summ': 0
    },
    "3": {
        'description': 'Гуляя по парку вы нашли 5000, на 1000 рублей вы поели в Шоколаднице, поэтому домой принесли только 4000.',
        'k': 1,
        'summ': 4000
    }
}

class Econ():

    def __init__(self):
        self.walk()

    def walk():
        
        q = random.randint(1, len(WALK_PATTERNS.keys()))
        return WALK_PATTERNS[str(q)]
