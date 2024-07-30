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

admin = bot.get_user(825422631704068166)

@bot.slash_command(name = 'server_info', description = 'Get some information about server')
async def server_info(ctx):

    data = Utilits.get_server_info(ctx.author.guild.id)
    admin = bot.get_user(825422631704068166)
    helper = bot.get_user(402184234430758914)
    guild = bot.get_guild(ctx.author.guild.id)

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

@bot.slash_command(name = 'fruitty_slotty', description = "Let's get some benefit from fruits!!")
async def fruit_slot(ctx, value: int):

    userData = Utilits.get_user_info(ctx.author.id, ctx.author.guild.id)
    serverData = Utilits.get_server_info(ctx.author.guild.id)
    usBalance = round(userData['balance'], 2)
    svBalance = round(serverData['total_balance'], 2)

    if usBalance > value:

        q = Slot.fruit_slot(ctx.author.id, ctx.author.guild.id)
        k = q[3]

        if svBalance >= value * k:

            userData['balance'] = userData['balance'] - value + (value * k)
            file = discord.File(f"sources/{ctx.author.id}_{userData['personal_counter']}.png", filename = 'image.png')
            userData['personal_counter'] += 1
            tp = ''
            tc = 0

            if k >= 1:
                tp = 'Выигрыш'
                tc = 1
                serverData['total_balance'] -= (value * k)
            else:
                tp = 'Проигрыш'
                tc = 0

            userData['total_lose'] += int(tc == 0)
            userData['total_win'] += int(tc != 0)
            #serverData['total_balance'] -= (value * k)
            Utilits.user_dump(ctx.author.id, ctx.author.guild.id, userData)
            Utilits.server_dump(ctx.author.guild.id, serverData)

            res = discord.Embed(title = 'Фруктовый слот')
            res.add_field(name = 'Ставка', value = f'{value}', inline = True)
            res.add_field(name = 'Коэффициент', value = f'{round(k, 2)}x',inline = True)
            res.add_field(name = f'{tp}', value = f'{round(abs(value - value * k), 2)}')
            res.set_image(url = 'attachment://image.png')

            await ctx.respond(file = file, embed = res)

        else:

            errw01 = discord.Embed(title = 'Возникла ошибка', description = 'Код ошибки w01. Ошибка локальная, не связанная с работой бота, обратитесь к администрации вашего сервера или понизьте ставку.')

            await ctx.respond(embed = errw01)

    else: 

        errw00 = discord.Embed(title = 'Возникла ошибка', description = 'Код ошибки w00. На вашем счете недостаточно средств для совершения операции')

        await ctx.respond(embed = errw00)

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

@bot.slash_command(name = 'balance', description = 'Do you wanna watch your balance?')
async def balance(ctx):

    userData = Utilits.get_user_info(ctx.author.id, ctx.author.guild.id)
    balce = discord.Embed(title = f'**Баланс {ctx.author.name}**', description = f">  **Валюта:**\n**`       {userData['balance']}       `**")
    balce.set_thumbnail(url = f'{ctx.author.avatar.url}')

    await ctx.respond(embed = balce)

bot.run(os.getenv('token'))