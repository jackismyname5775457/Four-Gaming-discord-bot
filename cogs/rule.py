from os import link
from discord.ext import commands
import discord,aiohttp,random,json


class rule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='rule')
    async def rule(self,ctx):
            embedVar = discord.Embed(title="**Luật lệ**", description="**Nhớ đọc kỹ trước khi bị ban!!!**", color=discord.Colour.random())
            embedVar.add_field(name="1️⃣", value="Không toxic, bắt nạt người khác.", inline=False)
            embedVar.add_field(name="2️⃣", value="Không spam, mention các vai trò tùy tiện.", inline=False)
            embedVar.add_field(name="3️⃣", value="Không NSFW, nội dung phản cảm, bạo lực.", inline=False)
            embedVar.add_field(name="4️⃣", value="Sử dụng các kênh, lệnh đúng cách.", inline=False)
            embedVar.add_field(name="5️⃣", value="Không tương tác với người người phá luật, thay vào đó hãy báo cáo họ.", inline=False)
            embedVar.add_field(name="6️⃣", value="Không nói về các vấn đề chính trị, tôn giáo, phân biệt chủng tộc, phân biệt giới tính.", inline=False)
            embedVar.add_field(name="7️⃣", value="Không mention(đề cập) các vai trò một cách bừa bãi.", inline=False)
            embedVar.add_field(name="Lưu ý", value="**Các hành vi phá hoại, không tuân thủ luật tùy mức độ sẽ bị xử phạt.**", inline=False)
            await ctx.send(embed=embedVar,delete_after=120)
    @commands.command(name='sever')
    async def sever(self,ctx):
        embedVar = discord.Embed(title="**ID**", description="**Fourgamingstudio.ddns.net**", color=discord.Colour.random())
        await ctx.send(embed=embedVar)


    @commands.command()
    async def embed(self,ctx, arg1, arg2):
        embedVar = discord.Embed(title=arg1, description=arg2, color=discord.Colour.random())
        await ctx.send(embed=embedVar)
    
    @commands.command(aliases=['av'])
    async def avatar(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author
        emb = discord.Embed(color=discord.Colour.random())
        emb.set_image(url=member.avatar)
        await ctx.send(embed=emb)

    @commands.command(pass_context=True)
    async def meme(self,ctx):
        embed = discord.Embed(title="", description="")

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)



async def setup(bot):
    await bot.add_cog(rule(bot))