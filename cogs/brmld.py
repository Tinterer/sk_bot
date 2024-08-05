import discord

from discord.ext import commands
from library.utilits import Utilits
from library.buffering import Bufferisation
from library.slots import Slot

class Cas(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name = 'fruitty_slotty', description = "Let's get some benefit from fruits!!")
    async def fruit_slot(self, ctx, value: int):

        userData = Utilits.get_user_info(ctx.author.id, ctx.author.guild.id)
        serverData = Utilits.get_server_info(ctx.author.guild.id)
        usBalance = round(userData['balance'], 2)
        svBalance = round(serverData['total_balance'], 2)

        if usBalance > value:

            q = Slot.fruit_slot(ctx.author.id, ctx.author.guild.id)
            k = q[3]

            if svBalance >= value * k:

                userData['balance'] = userData['balance'] - value + (value * k)
                file = discord.File(f"sources/{ctx.author.id}.png", filename = 'image.png')
                
                tp = ''
                tc = 0

                if k >= 1:
                    tp = 'Выигрыш'
                    tc = 1
                    serverData['total_balance'] -= (value * k - value)
                    serverData['total_wins'] += 1
                else:
                    tp = 'Проигрыш'
                    tc = 0
                    serverData['total_balance'] += value * k

                userData['total_lose'] += int(tc == 0)
                userData['total_win'] += int(tc != 0)
                userData['personal_counter'] += 1
                serverData['total_counter'] += 1

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

    @commands.slash_command(name = 'apple_slotte', description = 'What about some rich games?')
    async def apple_slott(self, ctx, value: int):

        userData = Utilits.get_user_info(ctx.author.id, ctx.author.guild.id)
        serverData = Utilits.get_server_info(ctx.author.guild.id)
        usBalance = round(userData['balance'], 2)
        svBalance = round(serverData['total_balance'], 2)

        if usBalance > value:

            q = Slot.apple_slot(ctx.author.id, ctx.author.guild.id)
            k = q[3]

            if svBalance >= value * k:

                userData['balance'] = userData['balance'] - value + (value * k)
                file = discord.File(f"sources/{ctx.author.id}.png", filename = 'image.png')
                
                tp = ''
                tc = 0

                if k >= 1:
                    tp = 'Выигрыш'
                    tc = 1
                    serverData['total_balance'] -= (value * k - value)
                    serverData['total_wins'] += 1
                else:
                    tp = 'Проигрыш'
                    tc = 0
                    serverData['total_balance'] += value * k

                userData['total_lose'] += int(tc == 0)
                userData['total_win'] += int(tc != 0)
                userData['personal_counter'] += 1
                serverData['total_counter'] += 1

                Utilits.user_dump(ctx.author.id, ctx.author.guild.id, userData)
                Utilits.server_dump(ctx.author.guild.id, serverData)

                res = discord.Embed(title = 'Яблочный розыгрыш')
                res.add_field(name = 'Ставка', value = f'{value}', inline = True)
                res.add_field(name = 'Коэффициент', value = f'{round(k, 2)}x',inline = True)
                res.add_field(name = f'{tp}', value = f'{round(abs(value - value * k), 2)}')
                res.set_image(url = 'attachment://image.png')

                await ctx.respond(file = file, embed = res)

            else:

                errw01 = discord.Embed(title = 'Возникла ошибка', description = 'Код ошибки w01. Ошибка локальная, не связана с работой бота, обратитесь к администрации вашего сервера или понизьте ставку.')

                await ctx.respond(embed = errw01)

        else: 

            errw00 = discord.Embed(title = 'Возникла ошибка', description = 'Код ошибки w00. На вашем счете недостаточно средств для совершения операции')

            await ctx.respond(embed = errw00)


def setup(bot):
    bot.add_cog(Cas(bot))