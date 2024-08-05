import discord
import json
import os
import random

from discord.ext import commands
from library.utilits import Utilits
from library.slots import Slot
from library.casino import Casino_Drawer
from library.buffering import Bufferisation
from library.bank_function import Bank
from dotenv import load_dotenv

intents = discord.Intents().all()
intents.members = True

load_dotenv()
bot = discord.Bot(intents = intents)

bot.load_extension('cogs.brmld')
bot.load_extension('cogs.eco')

admin = bot.get_user(825422631704068166)

@bot.slash_command(name = 'info', description = 'What is it?')
async def info(ctx):
    info = discord.Embed(title = '**Добро пожаловать!!**', description = '  Мtz.eco - это бот, ')

@bot.slash_command(name = 'server_info', description = 'Get some information about server')
async def server_info(ctx):

    data = Utilits.get_server_info(ctx.author.guild.id)

    print(data)
    admin = bot.get_user(825422631704068166)
    helper = bot.get_user(402184234430758914)

    if data:
        def check(n):

            if n:
                return "Активирован"
            else:
                return "Неактивен"
            
        done = discord.Embed(title = '**Информация о сервере**')
                             #description = f"Количество сыгранных игр: {data['total_counter']}\nКоличество игроков с премиумом: {data['ppremium_counter']}\nПремиум статус сервера: {check(data['premium_status'])}\nКоличество зарегистрированных пользователей: {Utilits.get_count(ctx.author.guild.id)}\nОбщий баланс сервера: {data['total_balance']}")
        
        done.add_field(name = 'Баланс сервера', value = f"{round(data['total_balance'], 2)}", inline = True).add_field(name = 'Зарегистрированные пользователи', value = f'{Utilits.get_count(ctx.author.guild.id)}', inline = True).add_field(name = 'Сыгранные игры', value = f"{data['total_counter']}", inline = True)
        done.add_field(name = 'Количестов премиум пользователей', value = f"{data['ppremium_counter']}", inline = True).add_field(name = 'Премиум статус сервера', value = f"{check(data['premium_status'])}", inline = True)

        done.set_author(name = f'{ctx.author.name}', url=f'{ctx.author.avatar}').set_thumbnail(url=f'{ctx.guild.icon}')
        
        await ctx.respond(embed = done)


    else:

        notd = discord.Embed(title = 'Возникла ошибка', description = 'Код ошибки x00. Обратитесь со скрином этого сообщения в поддержку бота или к администрации вашего сервера.')
        #общую сумму выигранных денег за все время на сервере
        #попробовать представить все эти данные в виде графики(проверить оптимизацию)
        await ctx.respoond(embed = notd)
        await admin.send(f'Обнаружена ошибка в работе команды `server_info`!\nGuild_id: {ctx.author.guild.id}\nGuild_name:{ctx.author.guild.name}\nUser_mention: {ctx.author.mention}')
        await helper.send(f'Обнаружена ошибка в работе команды `server_info`!\nGuild_id: {ctx.author.guild.id}\nGuild_name:{ctx.author.guild.name}\nUser_mention: {ctx.author.mention}')




@bot.slash_command(name = 'top_up', description = "top up your balance if you're chosen one")
@commands.has_permissions(administrator = True)
async def top_up(ctx, amount: int):

    x = random.randint(90, 99)

    userData = Utilits.get_user_info(ctx.author.id, ctx.author.guild.id)

    Bank.replenish_balance(ctx.author.id, ctx.author.guild.id, amount * (x / 100))
    Bank.replenish_sbalance(ctx.author.guild.id, amount * (1 - (x / 100)))

    top_up = discord.Embed(title = '**Вы пополнили баланс**')
    top_up.add_field(name = 'Ваш баланс', value = f"{round(userData['balance'], 2) + amount * (x / 100)}", inline = True)
    top_up.add_field(name = 'Сумма пополнения', value = f'{amount}', inline = True)
    top_up.add_field(name = 'Комиссия', value = f'{round(amount * (1 - (x / 100)), 2)}', inline = True)

    await ctx.respond(embed = top_up)

@bot.slash_command(name = 'balance')
async def bbalance(ctx, user: discord.Member = None):

    if user:

        userData = Utilits.get_user_info(user.id, ctx.guild.id)
        balce = discord.Embed(title = f'**Баланс {user.name}**', description = f">  **Валюта:**\n**`       {userData['balance']}       `**")
        balce.set_thumbnail(url = f'{user.avatar.url}')

    else:

        userData = Utilits.get_user_info(ctx.author.id, ctx.author.guild.id)
        balce = discord.Embed(title = f'**Баланс {ctx.author.name}**', description = f">  **Валюта:**\n**`       {userData['balance']}       `**")
        balce.set_thumbnail(url = f'{ctx.author.avatar.url}')

    await ctx.respond(embed = balce)
    

bot.run(os.getenv('token'))