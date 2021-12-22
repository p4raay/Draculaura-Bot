import discord
from discord.ext import commands
bot_channel = 111111111111111111 #Bot channel

class utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['aide'])
    async def help(self, ctx):
        if ctx.channel.id == bot_channel:
            embed=discord.Embed(color=0xa91e6f, title="Help command")
            embed.set_author(name="Draculaura is here.", icon_url="https://i.pinimg.com/originals/b3/ac/d4/b3acd47dba7723610fc4a06975c11ef7.jpg")
            embed.set_thumbnail(url="https://64.media.tumblr.com/5980bf83f3cb753f3612137ade8ce4e1/tumblr_mncuvjfaQ21remqmko1_250.gif")
            embed.add_field(name="``XP system``", value=f" ``+rank`` *Show informations about your XP.* \n ``+leaderboard`` *Show the server's leaderboard.*", inline=False)
            embed.add_field(name="``Utilities``", value="``+pp`` *Show the avatar of a member.*", inline=False)
            embed.add_field(name="``Moderation``", value="``+lock`` *Used to lock a channel.*\n ``+unlock`` *Used to unlock a channel.*", inline=False)
            await ctx.channel.send(embed=embed)

    @commands.command(aliases=['pp', 'pfp'])
    async def avatar(self, ctx: commands.Context, member: discord.Member = None):
      if ctx.channel.id == bot_channel:
        if member:
            m = member
        else:
            m = ctx.author
        av_embed = discord.Embed(title=f"Here's the avatar of {m}", color=0xa91e6f)
        av_embed.set_image(url=m.avatar_url)
        await ctx.send(embed=av_embed)
def setup(client):
    client.add_cog(utils(client))
