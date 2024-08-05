import discord
import json

from discord.ext import commands
from library.utilits import Utilits
from discord.ui import Select, View
from library.buffering import Bufferisation
from library.slots import Slot
from library.economy import Econ

class Economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    '''@commands.slash_command(name = 'job_info', description = 'Перестань уже сидеть на шее у родителей')
    async def job_info(self, ctx):

        userData = Utilits.get_user_info(ctx.author.id, ctx.author.guild.id)
        serverData = Utilits.get_server_info(ctx.author.guild.id)

        info = discord.Embed(title = '**Немного о работе**', description = 'Вы можете прокачиваться в разных ветках, строить бизнес и изучать этот мир больших денег')
        info.add_field(name = 'Ваша работа', value = f"{userData['actual_job']}", inline = True)
        info.add_field(name = 'Количество рабочих сессий', value = f"{userData['work_sessions']}", inline = True)
        info.add_field(name = 'Всего было работ', value = f"{userData['jobs']}", inline = True)

        await ctx.respond(embed = info)'''

    #доп доход

    @commands.slash_command(name = 'погулять')
    async def walk(self, ctx):

        userData = Utilits.get_user_info(ctx.author.id, ctx.author.guild.id)
        q = Econ.walk()

        if q['k'] == 1:
            userData['balance'] = userData['balance'] + q['summ']
        else:
            userData['balance'] = userData['balance'] * q['k']

        userData['exp'] += 0.01
        userData['walks_counter'] += 1
        Utilits.user_dump(ctx.author.id, ctx.author.guild.id, userData)

        walk = discord.Embed(title = 'Вы вышли прогуляться', description = f"{q['description']}")

        await ctx.respond(embed = walk)

    #желто-салатовая ветка

    @commands.slash_command(name = 'работа', description = 'поработаем немного?')
    async def works(self, ctx):
        select = Select(placeholder = 'Выберите ветку прокачки', options = [
            discord.SelectOption(label = "Желтая", description = 'Поработайте на желтой ветке'),
            discord.SelectOption(label = 'Оранжевая', description = 'А может на оранжевой?')
            ])
        view = View()
        view.add_item(select)

        async def my_callback(interaction):
            if select.values[0] == 'Желтая':
                jobs = Select(options = [
                    discord.SelectOption(
                        label = 'Дворник', 
                        description = 'Зарплата 1000, а трудоустройство стоит 550'),
                    discord.SelectOption(
                        label = 'Рабочий по благоустройству', 
                        description = 'Зарплата 1350, но из-за большой конкуренции трудоустройство стоит 700'),
                ])

                async def cb(interaction):
                    if jobs.values[0] == 'Дворник':
                        userData = Utilits.get_user_info(ctx.author.id, ctx.author.guild.id)
                        serverData = Utilits.get_server_info(ctx.author.guild.id)
                        if userData['actual_job'] != 'Дворник' and userData['balance'] >= 550:
                            userData['actual_job'] = 'Дворник'
                            userData['balance'] -= 550
                            userData['exp'] += 0.5
                            userData['jobs'] += 1
                            serverData['workers_counter'] += 1

                            Utilits.user_dump(ctx.author.id, ctx.author.guild.id, userData)
                            Utilits.server_dump(ctx.author.guild.id, serverData)

                            gjob = discord.Embed(title = 'Вы устроились на работу!', description = 'Вы устроились дворником. Вы накрыли поляну в честь этого и потратили 500. Для того, чтобы работать пишите `/work`. Для получения подробной информации напишите `/job_info`')
                            print('ok')
                            await interaction.response.send_message(embed = gjob, ephemeral = True)

                        else:

                            gjob = discord.Embed(title = 'Ошибка', description = 'Зачем вам вторая работа дворником?')

                    if jobs.values[0] == 'Рабочий по благоустройству':
                        userData = Utilits.get_user_info(ctx.author.id, ctx.author.guild.id)
                        serverData = Utilits.get_server_info(ctx.author.guild.id)
                        if userData['actual_job'] != 'Рабочий по благоустройству' and userData['balance'] >= 550:
                            userData['actual_job'] = 'Рабочий по благоустройству'
                            userData['balance'] -= 700
                            userData['exp'] += 0.6
                            userData['jobs'] += 1
                            serverData['workers_counter'] += 1

                            Utilits.user_dump(ctx.author.id, ctx.author.guild.id, userData)
                            Utilits.server_dump(ctx.author.guild.id, serverData)

                            gjob = discord.Embed(title = 'Вы устроились на работу!', description = 'Вы устроились рабочим по благоустройству территории. Была большая конкуренция и пришлось дать взятку девочкам из бухгалтерии в виде коробки конфет и шампанского, вы потратили 700. Для того, чтобы работать пишите `/work`. Для получения подробной информации напишите `/job_info`')

                            await interaction.response.send_message(embed = gjob, ephemeral = True)

                        else:

                            gjob = discord.Embed(title = 'Ошибка', description = 'Зачем сменять работу на точно такую же?')
                        
                jobs.callback = cb

                view1 = View()
                view1.add_item(jobs)

                await interaction.response.send_message('Выберите начальную работу', view = view1, ephemeral = True)

            if select.values[0] == 'Оранжевая':
                jobs = Select()

        select.callback = my_callback

        await ctx.respond('Выбирайте', view = view, ephemeral = True)


    @commands.slash_command(name = 'job_info', description = 'Узнайте побольше о работе')
    async def job_info(self, ctx):

        job_menu = Select(placeholder = 'Выберите ветку', options = [
            discord.SelectOption(
                label = 'Желтая', 
                description = 'Попробуйте себя в роли простого рабочего'
            ),
            discord.SelectOption(
                label = 'Оранжевая',
                description = 'Пробейтесь с самого нуля до элиты.'
            ),
            discord.SelectOption(
                label = 'Зеленая',
                description = 'Попробуйте себя в гос структурах.'
            )
        ])

        async def lines_callback(interaction):
            if job_menu.values[0] == 'Желтая':

                yellow = Select(placeholder = 'Выберите работу', options = [
                    discord.SelectOption(label = 'Дворник', description = ''),
                    discord.SelectOption(label = 'Рабочий по благоустройству территории', description = ''),
                    discord.SelectOption(label = 'Таксист', description = ''),
                    discord.SelectOption(label = 'Бригадир уборщиков', description = ''),
                    discord.SelectOption(label = 'Менеджер таксистов', description = ''),
                    discord.SelectOption(label = 'Зам директора ЖКХ', description = ''),
                    discord.SelectOption(label = 'Руководитель таксопарка', description = ''),
                    discord.SelectOption(label = 'Директор ЖКХ', description = ''),
                    discord.SelectOption(label = 'Владелец таксопарка', description = '')
                ])

                async def yellow_cb(interaction):
                    with open('jobs.json', 'r', encoding = 'utf-8') as file:
                        data = json.load(file)

                    ycb = discord.Embed(title = f'{yellow.values[0]}', description = f"{data['yellow'][yellow.values[0]]['Описание']}")
                    ycb.add_field(name = 'Зарплата', value = f"{data['yellow'][yellow.values[0]]['Зарплата']}")
                    ycb.add_field(name = 'Необходимое количество рабочих смен', value = f"{data['yellow'][yellow.values[0]]['Переход']}")

                    await interaction.response.send_message(embed = ycb, ephemeral = True)

                yellow.callback = yellow_cb
                yellow_view = View()
                yellow_view.add_item(yellow)

                await interaction.response.send_message(view = yellow_view, ephemeral = True)

            else:

                await interaction.response.send_message('Информация появится после 22 августа.', ephemeral = True)

        job_menu.callback = lines_callback
        lines_view = View()
        lines_view.add_item(job_menu)

        await ctx.respond(view = lines_view, ephemeral = True)

    @commands.slash_command(name = 'work', description = 'Надо зарабатывать деньги')
    async def work(ctx):

        userData = Utilits.get_user_info(ctx.author.id, ctx.author.guild.id)
        serverData = Utilits.get_server_info(ctx.author.guild.id)

        job = userData['actual_job']

        jobem = discord.Embed(title = 'Работа', description = '')


def setup(bot):
    bot.add_cog(Economy(bot))