import discord
from discord.ext import commands
from pymongo import MongoClient

 
bot_channel = 111111111111111111 #Command's channel
talk_channels = [111111111111111111] #The channels where you can earn XP


level = ["Role"] #Here are the roles you want to give
levelnum = [10] #Here are the levels
 
cluster = MongoClient("your mangodb url")
 
collection_name = cluster["collec1"]["collec 2"] #Your collections in mangodb
 
class levels(commands.Cog):
    def __init__(self, client):
        self.client = client
 
    @commands.Cog.listener()
    async def on_ready(self):
      print("Online!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id in talk_channels:
            stats = collection_name.find_one({"id":message.author.id})
            if not message.author.bot:
                if stats is None:
                    newuser = {"id" : message.author.id, "xp" : 0}
                    collection_name.insert_one(newuser)
                else:
                    xp = stats["xp"] + 1
                    collection_name.update_one({"id":message.author.id}, {"$set":{"xp":xp}}) 
                    lvl = 0
                    while True:
                        if xp < ((50*(lvl**2))+(50*lvl)):
                            break
                        lvl += 1
                    xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                    if xp == 0:
                        await message.xpchan.send(f"Congratulations ! {message.author.mention} ! You are now **level : {lvl}** !")
                        for i in range(len(level)):
                            if lvl == levelnum[i]:
                                await message.author.add_roles(discord.utils.get(message.author.guild.roles, name=level[i]))
                                embed = discord.Embed(color = 0xce9fd7, description=f"{message.author.mention}. You got a new role : **{level[i]}** !!!")
                                embed.set_thumbnail(url=message.author.avatar_url)
                                await message.channel.send(embed=embed)
 
    @commands.command(aliases=['xp', 'level'])
    async def rank(self, ctx):
        if ctx.channel.id == bot_channel:
            stats = collection_name.find_one({"id" : ctx.author.id})
            if stats is None:
                embed = discord.Embed(color=0x9f2c65,description="No message = No XP")
                await ctx.channel.send(embed=embed)
            else:
                xp = stats["xp"]
                lvl = 0
                rank = 0
                while True:
                        if xp < ((50*(lvl**2))+(50*lvl)):
                            break
                        lvl += 1
                xp -= ((50*((lvl-1)**2))+(50*(lvl-1)))
                boxes = int((xp/(200*((1/2) * lvl)))*20)
                rankings = collection_name.find().sort("xp",-1) 
                for x in rankings:
                    rank += 1
                    if stats["id"] == x["id"]:
                        break
                embed = discord.Embed(color=0xe6b8f3,title="Information sur l'XP de {}".format(ctx.author.name))
                embed.add_field(name="Username", value=ctx.author.mention, inline=True)
                embed.add_field(name="XP", value=f"{xp}/{int(200*((1/2)*lvl))}", inline=True)
                embed.add_field(name="Level", value=f"{lvl}", inline=True)
                embed.add_field(name="Progress bar :", value=boxes * ":blue_square:" + (20-boxes) * ":white_large_square:", inline=False)
                embed.set_thumbnail(url=ctx.author.avatar_url)
                await ctx.channel.send(embed=embed)

    @commands.command(aliases=['lb', 'classement'])
    async def leaderboard(self, ctx):
        if (ctx.channel.id == bot_channel):
            rankings = collection_name.find().sort("xp",-1) 
            i = 1
            embed = discord.Embed(color=0xba5186,title="Server's leaderboard :")
            for x in rankings:
                try:
                    temp = ctx.guild.get_member(x["id"])
                    tempxp = x["xp"]
                    embed.add_field(name=f"``⭐ {i} :`` {temp.name}", value=f"*Total XP :* {tempxp}", inline=False)
                    i += 1
                except:
                    pass
                if i == 11:
                    break
            await ctx.channel.send(embed=embed)

    

def setup(client):
    client.add_cog(levels(client))
