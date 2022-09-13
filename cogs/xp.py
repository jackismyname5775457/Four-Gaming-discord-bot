import discord,json,asyncio
from discord.ext import commands
import serverpingmodule
class server(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def ping(self,ctx,arg1):
        await ctx.message.delete()
        server = serverpingmodule.Server(arg1).get_status()
        embed = discord.Embed(title = 'Sever ip', description =arg1 ,color=discord.Colour.random())
        embed.add_field(name='Tên sever', value=server.name, inline=False)
        embed.add_field(name='Bản đồ', value=server.map, inline=False)
        embed.add_field(name='Số người chơi', value=server.players, inline=False)
        embed.add_field(name='Số đợt', value=server.wave, inline=False)
        embed.add_field(name='ping', value=server.ping, inline=False)
        embed.add_field(name='Thể loại', value=server.vertype, inline=False)
        embed.set_footer(text="⭐⭐⭐⭐⭐ • Supper Server") 
        msg=await ctx.send(embed=embed,delete_after=20)

    @commands.command()
    async def info(self,ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author

        async with ctx.typing():
            
            # import asyncio if you already have not
            await asyncio.sleep(1)

            info_embed = discord.Embed(title=f"{member.name}'s info", color=0x797d7f)

            info_embed.add_field(name='Username', value=(member.name), inline=True)
            info_embed.add_field(name='Display Name', value=(member.display_name), inline=True)
            info_embed.set_thumbnail(url=member.avatar)
            info_embed.set_footer(text=ctx.message.author.name, icon_url=ctx.message.author.avatar)

            await ctx.send(embed=info_embed,delete_after=5)
    @commands.command()
    async def rank(self,ctx, x=10):
        with open('users.json', 'r') as f:
            
            users = json.load(f)
            
        leaderboard = {}
        total=[]
        
        for user in list(users[str(ctx.guild.id)]):
            name = int(user)
            total_amt = users[str(ctx.guild.id)][str(user)]['exp']
            leaderboard[total_amt] = name
            total.append(total_amt)

        total = sorted(total,reverse=True)
        

        em = discord.Embed(
            title = f'Top {x} highest leveled members in {ctx.guild.name}',
            description = 'The highest leveled people in this server'
        )
        
        index = 1
        for amt in total:
            id = leaderboard[amt]

            namee = await self.client.fetch_user(int(id))           
            member = namee.name
            
            
            em.add_field(name = f'{index}: {member}', value = f'{amt}', inline=False)
            
            
            if index == x:
                break
            else:
                index += 1
            
        await ctx.send(embed = em,delete_after=15)



    @commands.command(aliases = ['lvl'])
    async def lv(self,ctx,member: discord.Member = None):
        if member ==None:
            user = ctx.message.author
            with open('users.json','r') as f:
                users = json.load(f)
            lvl = users[str(ctx.guild.id)][str(user.id)]['level']
            exp = users[str(ctx.guild.id)][str(user.id)]['exp']
            with open('spam.json','r') as f:
                users = json.load(f)
            mute = users[str(ctx.guild.id)][str(user.id)]['mute']
            endXP = ((lvl + 1) ** 4)+100

            embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP / {endXP} XP" ,color=discord.Colour.random())
            embed.set_author(name = ctx.author, icon_url = ctx.author.avatar)
            embed.add_field(name='Tổng số gậy', value=f"{mute} / 3", inline=True)
            await ctx.send(embed = embed,delete_after=15)
        else:
            with open('users.json','r') as f:
                users = json.load(f)
            lvl = users[str(ctx.guild.id)][str(member.id)]['level']
            exp = users[str(ctx.guild.id)][str(member.id)]['exp']
            with open('spam.json','r') as f:
                users = json.load(f)
            mute = users[str(ctx.guild.id)][str(member.id)]['mute']
            endXP = ((lvl + 1) ** 4)+100
            embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP / {endXP} XP" ,color=discord.Colour.random())
            embed.set_author(name = member, icon_url = member.avatar)
            embed.add_field(name='Tổng số gậy', value=f"{mute} / 3", inline=True)
            await ctx.send(embed = embed,delete_after=15)


async def setup(bot):
    await bot.add_cog(server(bot))
