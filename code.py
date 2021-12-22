import discord
from discord.ext import commands
bot_channel = 111111111111111111 #Commands channel

class code(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def code(self, ctx):
    if (ctx.channel.id == bot_channel):
        codepfp = discord.Embed(color=0xa91e6f)
        codepfp.set_author(name="Code's github (click me dummy)", url="https://github.com/p4raay/Draculaura-Bot/tree/main")
        await ctx.send(embed=codepfp)

def setup(client):
    client.add_cog(code(client))
