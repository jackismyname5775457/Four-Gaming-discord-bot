
from socket import timeout
import discord,datetime,asyncio,humanfriendly
from discord.ext import commands
from discord import app_commands


class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label='Chấp nhận!', style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Chấp nhận thành công!!!', ephemeral=True)
        self.value = True
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='Hủy bỏ!', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Hủy bỏ thành công!!!', ephemeral=True)
        self.value = False
        self.stop()
        
class ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self,ctx: commands.Context, member:discord.Member, *, reason = None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("Chỉ có thằng ngu mới ban chính mình?",delete_after=5)
            return
        try:
            view = Confirm()
            await ctx.send(f'Bạn có chắc chắn ban {member.mention} chứ???', view=view,delete_after=60)
            if view.value is None:
                print('Timed out...')
                await ctx.author.send(f'Hết thời gian đợi chấp nhận ban.',delete_after=5)
            elif view.value:
                print('Confirmed...')
                await member.ban(reason = reason)
                unban= discord.Embed(title=f'Thành viên này đã bị ban!', description='', color=discord.Colour.random())
                unban.add_field(name='Admin:', value=f'`{ctx.author}`', inline=True)
                unban.add_field(name='Thành viên', value=f'`{member.mention}`', inline=True)
                unban.add_field(name='Hành động:', value='`BAN`', inline=True)
                unban.set_author(name=f'{ctx.guild}', icon_url=ctx.guild.icon)
                unban.set_thumbnail(url=member.avatar)
                unban.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=unban,delete_after=30)
            else:
                await ctx.author.send(f'Hủy lệnh ban.',delete_after=5)
        except Exception:
            await ctx.channel.send(f"Bot không có đủ quyền để ban bố ơi!!!!!",delete_after=5)

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, id: int):
        try:
            view = Confirm()
            msg=await ctx.send(f'Bạn có chắc chắn unban chứ???', view=view,delete_after=60)
            await view.wait()
            try:
                user = await self.client.fetch_user(id)
                await ctx.guild.unban(user)
                unban= discord.Embed(title=f'A moderation action has been performed!', description='', color=discord.Colour.random())
                unban.add_field(name='Moderator Name:', value=f'`{ctx.author}`', inline=True)
                unban.add_field(name='Moderator ID:', value=f'`{ctx.author.id}`', inline=True)
                unban.add_field(name='Action Performed:', value='`UnBan`', inline=True)
                unban.set_author(name=f'{ctx.guild}', icon_url=ctx.guild.icon)
                unban.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=unban)
            except:
                ctx.send("ID sai hoặc thành viên này chưa bị ban.",delete_after=30)
        except Exception:
            await ctx.channel.send(f"Bot không có đủ quyền để unban bố ơi!!!!!",delete_after=5)

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self,ctx: commands.Context, member:discord.Member, *, reason = None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("Chỉ có thằng ngu mới kick chính mình?",delete_after=5)
            return
        try:
            view = Confirm()
            await ctx.send(f'Bạn có chắc chắn kick {member.mention} chứ???', view=view,delete_after=60)
            await view.wait()

            if view.value is None:
                print('Timed out...')
                await ctx.author.send(f'Hết thời gian đợi chấp nhận kick.',delete_after=5)
            elif view.value:
                print('Confirmed...')
                await member.kick(reason = reason)
                unban= discord.Embed(title=f'Thành viên này đã bị kick!', description='', color=discord.Colour.random())
                unban.add_field(name='Admin:', value=f'`{ctx.author}`', inline=True)
                unban.add_field(name='Thành viên', value=f'`{member.mention}`', inline=True)
                unban.add_field(name='Hành động:', value='`Kick`', inline=True)
                unban.set_author(name=f'{ctx.guild}', icon_url=ctx.guild.icon)
                unban.set_thumbnail(url=member.avatar)
                unban.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=unban,delete_after=30)
            else:
                await ctx.author.send(f'Hủy lệnh Kick.',delete_after=5)

        except Exception:
            await ctx.channel.send(f"Bot không có đủ quyền để Kich bố ơi!!!!!",delete_after=5)
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def mute(self,ctx: commands.Context, member:discord.Member,time, *, reason = None):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("Chỉ có thằng ngu mới mute chính mình?",delete_after=5)
            return
        try:
            view = Confirm()
            await ctx.send(f'Bạn có chắc chắn mute {member.mention} chứ???', view=view,delete_after=60)
            await view.wait()

            if view.value is None:
                print('Timed out...')
                await ctx.author.send(f'Hết thời gian đợi chấp nhận mute.',delete_after=5)
            elif view.value:
                print('Confirmed...')
                time1= humanfriendly.parse_timespan(time)
                await member.timeout(discord.utils.utcnow()+datetime.timedelta(seconds=time1))
                unban= discord.Embed(title=f'Thành viên này đã bị mute!', description='', color=discord.Colour.random())
                unban.add_field(name='Admin:', value=f'`{ctx.author}`', inline=True)
                unban.add_field(name='Thành viên', value=f'`{member.mention}`', inline=True)
                unban.add_field(name='Hành động:', value='`mute`', inline=True)
                unban.set_author(name=f'{ctx.guild}', icon_url=ctx.guild.icon)
                unban.set_thumbnail(url=member.avatar)
                unban.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=unban,delete_after=30)
            else:
                await ctx.author.send(f'Hủy lệnh mute.',delete_after=5)

        except Exception:
            await ctx.channel.ssend(f"Bot không có đủ quyền để mute bố ơi!!!!!",delete_after=5)
    
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def unmute(self,ctx: commands.Context, member:discord.Member,*, reason = None):
        try:
            view = Confirm()
            await ctx.send(f'Bạn có chắc chắn unmute chứ???', view=view,delete_after=60)
            await view.wait()
            try:
                await member.timeout(discord.utils.utcnow()+datetime.timedelta(seconds=0))
                unban= discord.Embed(title=f'A moderation action has been performed!', description='', color=discord.Colour.random())
                unban.add_field(name='Moderator Name:', value=f'`{ctx.author}`', inline=True)
                unban.add_field(name='Moderator ID:', value=f'`{ctx.author.id}`', inline=True)
                unban.add_field(name='Action Performed:', value='`UnMute`', inline=True)
                unban.set_author(name=f'{ctx.guild}', icon_url=ctx.guild.icon)
                unban.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=unban,delete_after=30)
            except:
                ctx.send("Thành viên này chưa bị mute.",delete_after=5)
        except Exception:
            await ctx.channel.send(f"Bot không có đủ quyền để unmute bố ơi!!!!!",delete_after=5)

async def setup(bot):
    await bot.add_cog(ban(bot))
