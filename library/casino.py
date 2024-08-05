import json

from PIL import Image, ImageDraw, ImageFont
from library.utilits import Utilits

class Casino_Drawer():

    def __init__(self, user_id, title, coef, key1, key2, key3):
        self.test_r3(user_id, type, title, key1, key2, key3, coef)

    '''def fruitSlot_dr(key1, key2, key3, coef):

        with open('types.json', 'r', encoding = 'utf-8') as file:
            frslData = json.load(file)
        
        img1 = Image.open(frslData['fs'][f'{key1}'])
        img2 = Image.open(frslData['fs'][f'{key2}']) 
        img3 = Image.open(frslData['fs'][f'{key3}'])

        background = Image.open('frames/fr_sl.png')
        maxsize = (350, 350)
        img1.thumbnail(maxsize)
        img2.thumbnail(maxsize)
        img3.thumbnail(maxsize)
        
        background.paste(img1, (217 + 50, 400), mask=img1.convert('RGBA'))
        background.paste(img2, (int(217.5 * 2 + 350), 400), mask=img2.convert('RGBA'))
        background.paste(img3, (int(217.5 * 3 + 350 * 2) - 50, 400), mask=img3.convert('RGBA'))

        im = ImageDraw.Draw(background)
        font = ImageFont.truetype('fonts/Ramona-Bold.ttf' ,70)
        im.text((int(217.5 * 3 + 350 * 2) - 200, 875), str(coef), fill=(145, 222, 207), font = font)



        background.save('back.png')'''

    def test_r3(user_id, guild_id, type, title, key1, key2, key3, coef):

        with open('types.json', 'r', encoding = 'utf-8') as file:
            data = json.load(file)

        userData = Utilits.get_user_info(user_id, guild_id)

        img1 = Image.open(data[f'{type}'][f'{title}'][f'{key1}'])
        img2 = Image.open(data[f'{type}'][f'{title}'][f'{key2}'])
        img3 = Image.open(data[f'{type}'][f'{title}'][f'{key3}'])

        background = Image.open(f'types/{type}/{title}/{title}_bg.png')
        maxsize = (350, 350)
        img1.thumbnail(maxsize)
        img2.thumbnail(maxsize)
        img3.thumbnail(maxsize)

        background.paste(img1, (217 + 50, 400), mask=img1.convert('RGBA'))
        background.paste(img2, (int(217.5 * 2 + 350), 400), mask=img2.convert('RGBA'))
        background.paste(img3, (int(217.5 * 3 + 350 * 2) - 50, 400), mask=img3.convert('RGBA'))

        im = ImageDraw.Draw(background)
        font = ImageFont.truetype('fonts/Ramona-Bold.ttf' ,70)
        im.text((int(217.5 * 3 + 350 * 2) - 200, 875), str(round(coef, 2)), fill=(145, 222, 207), font = font)

        background.save(f"sources/{user_id}.png")


