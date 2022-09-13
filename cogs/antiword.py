import asyncio
import os
from discord.ext import commands
from discord.ext.commands import bot
import discord




class anti(commands.Cog):
    def __init__(self, client):
        self.client = client
        self._last_member = None

    #when !maps is recieved run this:
    @commands.command(name='Mlist',aliases=['m','Maps','M'])
    async def Mlist(self,ctx):
        file = discord.File(os.path.join("D:\\downloand\\mindustry-server-unstable\\config\\maps\\Alloy.msav"))
        await ctx.send(file=file)
    @commands.command(name="check")
    async def check(self, ctx: commands.Context,id) -> None:
        """
        This command is actually used as an app command AND a message command.
        This means it is invoked with `?ping` and `/ping` (once synced, of course).
        """
        name = await self.client.fetch_user(int(id))
        await ctx.send(name.name)
    
    @commands.command()
    async def nonever(self,ctx):
        for file in os.listdir("D:/downloand/mindustry-server-unstable/config/maps/pvp"):
            if file.endswith(".msav"):
                file = discord.File(os.path.join("D:/downloand/mindustry-server-unstable/config/maps/pvp", file))
                await ctx.send(file=file)

    @commands.Cog.listener("on_message")
    async def bad(self,message):
        bad_word = ["dm", "DM", "Dm"]
        if message.content in bad_word:
            await message.delete()

    @commands.Cog.listener("on_message")
    async def greet(self,message):
        Cheers= ["Hi", "hi", "Hello", "hello"]
        if message.content in Cheers:
            await message.channel.send('Hello again',delete_after=5)

    @commands.Cog.listener("on_message")
    async def agree(self,message):
        Agree = ["yes", "yep", "ok"]
        if message.content in Agree:
            await message.channel.send('good!',delete_after=5)


    @commands.Cog.listener("on_message")
    async def dAgree(self,message):
        dAgree= ["no", "nope"]
        if message.content in dAgree:
            msg=await message.channel.send('why?',delete_after=5)

    @commands.command(name="sync")
    async def sync(self,ctx)-> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f'synced {len(fmt)} commands',delete_after=5)
    @commands.command(name="tr")
    async def tr(self,ctx):
        a=21
        b={
            21
        }
        if a in b:
            await ctx.send(b)
async def setup(bot):
    await bot.add_cog(anti(bot))
