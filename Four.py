 
import discord,logging,logging.handlers,os,asyncio, discord,json,sys,random,math
from discord.ext import commands,menus
from discord import ui
#---------------------------------------------------------#
with open('Config.json', 'r') as f:
    Config = json.load(f)
prefix = Config['prefix']
token = Config['token']
bot_client_id = Config['bot_client_id']
channel_for_anti_and_exp=set(Config['channel_for_anti_and_exp'])
#---------------------------------------------------------#
activity = discord.Activity(name='Four Gaming Studio', type=discord.ActivityType.watching)
client = commands.Bot(command_prefix=prefix, activity=activity, status=discord.Status.idle, intents=discord.Intents.all(),application_id=bot_client_id)
#client.remove_command('help')
#client.remove_command('help')
#---------------------------------------------------------#
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='discord.log',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

#---------------------------------------------------------#

class MyMenuPages(ui.View, menus.MenuPages):
    def __init__(self, source):
        super().__init__(timeout=60)
        self._source = source
        self.current_page = 0
        self.ctx = None
        self.message = None

    async def start(self, ctx, *, channel=None, wait=False):
        # We wont be using wait/channel, you can implement them yourself. This is to match the MenuPages signature.
        await self._source._prepare_once()
        self.ctx = ctx
        self.message = await self.send_initial_message(ctx, ctx.channel)

    async def _get_kwargs_from_page(self, page):
        """This method calls ListPageSource.format_page class"""
        value = await super()._get_kwargs_from_page(page)
        if 'view' not in value:
            value.update({'view': self})
        return value

    async def interaction_check(self, interaction):
        """Only allow the author that invoke the command to be able to use the interaction"""
        return interaction.user == self.ctx.author

    # This is extremely similar to Custom MenuPages(I will not explain these)
    @discord.ui.button(emoji='⏪', style=discord.ButtonStyle.blurple)
    async def first_page(ctx,self, button, interaction):
        await self.show_page(0)
    @discord.ui.button(emoji='⬅️', style=discord.ButtonStyle.blurple)
    async def before_page(self, button, interaction):
        await self.show_checked_page(self.current_page - 1)

    @discord.ui.button(emoji='➡️', style=discord.ButtonStyle.blurple)
    async def next_page(self, button, interaction):
        await self.show_checked_page(self.current_page + 1)

    @discord.ui.button(emoji='⏩', style=discord.ButtonStyle.blurple)
    async def last_page(self, button, interaction):
        await self.show_page(self._source.get_max_pages() - 1)

class MySource(menus.ListPageSource):
    async def format_page(self, menu, entries):
        if entries==1:
            embed = discord.Embed(description=f"This is number {entries}.", color=discord.Colour.random())
            embed.add_field(name="Play <tên bài hát hoặc ulr>", value="Chơi nhạc.", inline=False)
            embed.add_field(name="stop", value="Dừng phát bài hát và xóa hết danh sách chờ.", inline=False)
            embed.add_field(name="skip", value="Bỏ qua bài hát.", inline=False)
            embed.add_field(name="remove <Số thứ tự bài hát>", value="Xóa Bài hát từ danh sách.", inline=False)
            embed.add_field(name="now", value="Hiển thị bài hát đang phát.", inline=False)
            embed.add_field(name="queue", value="Hiển thị danh sách phát.", inline=False)
            embed.add_field(name="join", value="Tham gia phòng trò chuyện.", inline=False)
            embed.set_footer(text=f"Requested by {menu.ctx.author}")
            return embed
        if entries==2:
            embed = discord.Embed(description=f"This is number {entries}.", color=discord.Colour.random())
            embed.add_field(name="loop ", value="Phát lại bài hát.", inline=False)
            embed.add_field(name="shuffle", value="Đảo trộn danh sách phát.", inline=False)
            embed.add_field(name="summon", value="Triệu hồi bot.", inline=False)
            embed.add_field(name="pause", value="Dừng bài hát đang phát.", inline=False)
            embed.add_field(name="resume", value="Hiển thị bài hát đang phát.", inline=False)
            embed.add_field(name="test", value="Hiển thị tốc độ kết nối với bot.", inline=False)
            embed.add_field(name="sync", value="Kiểm tra có bao nhiêu lệnh nhanh.", inline=False)
            embed.set_footer(text=f"Requested by {menu.ctx.author}")
            return embed
        if entries>=3:
            embed = discord.Embed(description=f"This is number {entries}.", color=discord.Colour.random())
            embed.add_field(name="rule ", value="Hiển thị danh sách luật sever.", inline=False)
            embed.add_field(name="sever", value="Hiển thị ID sever.", inline=False)
            embed.add_field(name="tic", value="Bắt đầu trò chơi XO.", inline=False)
            embed.add_field(name="help", value="Hiển thị tất cả lệnh.", inline=False)
            embed.add_field(name="help2", value="Hiển thị tất cả lệnh chi tiết.", inline=False)
            embed.add_field(name="info", value="Hiển thị thông tin sever.", inline=False)
            embed.add_field(name="Clear <số tin nhắn muốn xóa>", value="Xóa tin nhắn.", inline=False)
            embed.set_footer(text=f"Requested by {menu.ctx.author}")
            return embed


@client.command()
async def help2(ctx):
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,1000]
    formatter = MySource(data, per_page=1) # MySource came from Custom MenuPages subtopic. [Please refer to that]
    menu = MyMenuPages(formatter)
    await menu.start(ctx)

#---------------------------------------------------------#

#---------------------------------------------------------#
class NewHelpName(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page,color=discord.Colour.random())
            await destination.send(embed=emby,delete_after=60)
client.help_command = NewHelpName()
#---------------------------------------------------------#
@client.command()
async def infoserver(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name} Info", description="Information of this Server", color=discord.Colour.random())
    embed.add_field(name='🆔Server ID', value=f"{ctx.guild.id}", inline=True)
    embed.add_field(name='📆Created On', value=ctx.guild.created_at.strftime("%b %d %Y"), inline=True)
    embed.add_field(name='👑Owner', value=f"{ctx.guild.owner}", inline=True)
    embed.add_field(name='👥Members', value=f'{ctx.guild.member_count} Members', inline=True)
    embed.add_field(name='💬Channels', value=f'{len(ctx.guild.text_channels)} Text | {len(ctx.guild.voice_channels)} Voice', inline=True)
    embed.add_field(name='🌎Region', value=f'{ctx.guild.description}', inline=True)
    embed.set_thumbnail(url=ctx.guild.icon) 
    embed.set_footer(text="⭐⭐⭐⭐⭐ • Supper Server")    
    embed.set_author(name=f'{ctx.author.name}' ,icon_url=ctx.author.avatar.url)

    await ctx.send(embed=embed,delete_after=15)
#---------------------------------------------------------#
@client.event
async def on_command_error(ctx, error):
    await ctx.message.delete()
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("**Sai lệnh. Thử sử dụng** `help` **để tìm ra lệnh bạn đang hướng tới!**",delete_after=5)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('**Thiếu từ khóa.**',delete_after=5)
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("**Bạn không có quyền để sử dụng lệnh này!! :angry:**",delete_after=5)

#---------------------------------------------------------#

@client.command()
async def check1(ctx, user: discord.Member):
    if user.nick == None:
        await ctx.send(f"Display name: {user.display_name}",delete_after=15)
    else:
        await ctx.send(f"Nickname: {user.nick}",delete_after=15)
#---------------------------------------------------------#
#---------------------------------------------------------#
async def Four():
    async with client:
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
            # cut off the .py from the file name
                await client.load_extension(f"cogs.{filename[:-3]}")
                print(f'load {filename[:-3]} susess')
            else:
                print(f'Unable to load {filename[:-3]}')
        await client.start(token)

asyncio.run(Four())
#---------------------------------------------------------#
