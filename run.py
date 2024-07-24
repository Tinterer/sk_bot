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

admin = bot.get_user(825422631704068166)

@bot.slash_command(name = 'server_info', description = 'Get some information about server')
async def server_info(ctx):
    data = Utilits.get_server_info(ctx.author.guild.id)
    admin = bot.get_user(825422631704068166)
    helper = bot.get_user(402184234430758914)

    if data:
        def check(n):
            if n:
                return "Активирован"
            else:
                return "Неактивен"
        done = discord.Embed(title = '**Информация о сервере**',
                             description = f"Количество сыгранных игр: {data['total_counter']}\nКоличество игроков с премиумом: {data['premium_counter']}\nПремиум статус сервера: {check(data['premium_status'])}")
        await ctx.respond(embed = done)
        await admin.send(f'Обнаружена ошибка в работе команды `server_info`\nGuild_id: {ctx.author.guild.id}\nGuild_name: {ctx.author.guild.name}\nUser_mention: {ctx.author.mention}\nError: x00')
        await helper.send(f'Обнаружена ошибка в работе команды `server_info`\nGuild_id: {ctx.author.guild.id}\nGuild_name: {ctx.author.guild.name}\nUser_mention: {ctx.author.mention}\nError: x00')
    else:
        notd = discord.Embed(title = 'Возникла ошибка', description = 'Код ошибки x00. Обратитесь со скрином этого сообщения в поддержку бота или к администрации вашего сервера.')
        #общий баланс сервера, количество пользователей, зарегестрированных в системе
        #общую сумму выигранных денег за все время на сервере
        #вывод аватарки сервера в эмбеде
        #попробовать представить все эти данные в виде графики(проверить оптимизацию)
        await ctx.respoond(embed = notd)
        await admin.send(f'Обнаружена ошибка в работе команды `server_info`!\nGuild_id: {ctx.author.guild.id}\nGuild_name:{ctx.author.guild.name}\nUser_mention: {ctx.author.mention}')

@bot.slash_command(name = 'fruitty_slotty', description = "Let's get some benefit from fruits!!")
async def fruit_slot(ctx):

    userData = Utilits.get_user_info(ctx.author.id, ctx.author.guild.id)
    serverData = Utilits.get_server_info(ctx.author.guild.id)
    usBalance = round(userData['balance'], 2)
    svBalance = round(serverData['total_balance'], 2)

    

bot.run(os.getenv('token'))