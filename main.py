from discord.ext import commands
import discord
import levels
import utils
import moderation
import code
from webserver import keep_alive

token = "yourtoken"
cogs = [levels, utils, moderation, code] 

client = commands.Bot(command_prefix='+', intents = discord.Intents.all(), activity = discord.Game(name="+help for help"))

client.remove_command("help")


for i in range(len(cogs)):
    cogs[i].setup(client)
    print('Setup successful.')
    
keep_alive()
client.run(token)
