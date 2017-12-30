import discord
from discord.ext import commands
import json as jason
import datetime
import asyncio

bot = commands.Bot(command_prefix='b!', description='A bot for managing birthdays!')
token = ""

@bot.event
async def on_ready():
    print("Bot Is Online.")
    
async def check_for_birthday(self):
    await self.wait_until_ready()
    now = datetime.datetime.now()
    curmonth = now.month
    curday = now.day
    
    while not self.is_closed():
        # TODO loop through birthdays.json and check for matches
        # TODO send birthday wish
        await asyncio.sleep(86400) # task runs every day

# on_guild_join is modified from CreeperBot
@bot.event
async def on_guild_join(guild):
    # Loop through all channels until a good channel is found. Implemented due to removal of default channel
    success = False
    index = 0
    while not success:
        try:
            await guild.channels[index].send("Hello! I'm BirthdayBot, a bot for tracking your birthdays! Get started with `b!help` and `b!setbirthday`.")
        except discord.Forbidden:
            index += 1
        except AttributeError:
            index += 1
        except IndexError:
            # if the server has no channels, doesn't let the bot talk, or all vc/categories
            pass
        else:
            success = True
            
@bot.command()
async def ping(ctx):
    '''Check if bot is working.'''
    await ctx.send("Pong. I work.")
    
@bot.command()
async def setbirthday(ctx):
    '''Set a birthday.'''
    member = ctx.message.author.id
    await ctx.send("What is your birthday? Please use MM/DD format.")
    def check(user):
        return user == ctx.message.author and user == ctx.message.channel
    msg = await bot.wait_for('message', check=check)
    try:
        list = msg.split("/")
        if list[0] > 13 or list[0] < 1:
            await ctx.send("Invalid date.")
            await ctx.send("Aborting...")
            return
        else:
            pass
            
        if list[0] in (1, 3, 5, 7, 8, 10, 12):
            if list[1] > 31 or list[1] < 1:
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
            else:
                pass
        elif list[0] in (4, 6, 9, 11):
            if list[1] > 30 or list[1] < 1:
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
            else:
                pass
        elif list[0] == 2:
            if list[1] > 29 or list[1] < 1:
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
            else:
                pass
        else:
            await ctx.send("Invalid date.")
            await ctx.send("Aborting...")
            return
    except:
        await ctx.send("Invalid date.")
        await ctx.send("Aborting...")
        return
    
    list = msg.split("/")
    month = list[0]
    day = list[1]
    
    date[member] = {'month': month, 'day': day}
    
    with open('./birthdays.json', 'r+') as f:
        jason.dump(date, f, indent=4)

if __name__ == "__main__":
    bot.run(token)
    self.bg_task = self.loop.create_task(self.check_for_birthday())
    
