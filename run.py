import discord
import json
import os

from utilits import Utilits
from slots import Slot
from casino import Casino_Drawer
from buffering import Bufferisation
from dotenv import load_dotenv

intents = discord.Intents().all()
intents.members = True

load_dotenv()
bot = discord.Bot(intents = intents)

@bot.slash_command(name = 'server_info', description = 'Get some information about server')
async def server_info(ctx):
    data = Utilits.get_server_info(ctx.author.guild.id)
    if data:
        def check(n):
            if n:
                return "Активирован"
            else:
                return "Неактивен"
        done = discord.Embed(title = '**Информация о сервере**',
                             description = f'Количество сыгрыннх игр: {data[0]}\nКоличество игроков с премиумом: {data[1]}\nПремиум сервера:{check(data[2])}')
        await ctx.respond(embed = done)
    else:
        notd = discord.Embed(title = 'Возникла ошибка', description = 'Код ошибки 000. Обратитесь со скрином этого сообщения в поддержку бота или к администрации вашего сервера.')
        #добавить отправку сообщения в личные сообщения мне или кому-то из хелперов
        await ctx.respoond(embed = notd)