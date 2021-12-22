import discord
from discord.ext import commands


class moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, channel : discord.TextChannel = None):
      guild = ctx.guild
      role = discord.utils.get(guild.roles,name=" the role after checking the rules")
      if channel is None:
        channel = ctx.message.channel
      await channel.set_permissions(role, send_messages=False)
      lockembed = discord.Embed(color=0xa91e6f, description="🔒 • Channel locked !")
      await ctx.send(embed=lockembed)

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx, channel : discord.TextChannel = None):
      guild = ctx.guild
      role = discord.utils.get(guild.roles,name="the role after checking the rules")
      if channel is None:
        channel = ctx.message.channel
      await channel.set_permissions(role, send_messages=True)
      unlockembed = discord.Embed(color=0x9f2c65, description="🔓 • Channel unlocked !")
      await ctx.send(embed=unlockembed)

def setup(client):
    client.add_cog(moderation(client))
