import asyncio,discord,math,random,json,datetime
from discord.ext import commands

time_window_milliseconds = 10000
max_msg_per_window = 5
timemute =60
author_msg_times = {}

async def cheeck(users, user, channel, server):
    mute = users[str(user.guild.id)][str(user.id)]['mute']
    endmute = 3
    timemute = 60
    if mute >=endmute:
        users[str(server.id)][str(user.id)]['mute'] = 0
        await channel.send(f"You have been muted in {user.mention} for spamming | You'll be unmuted in 1 minutes.",delete_after=3)
        await user.timeout(discord.utils.utcnow()+datetime.timedelta(seconds=timemute))
        msg = []
        msg = await channel.purge(user)
        await msg.delete()
       

async def add_mute(users, user, channel, server):
    counter = 0
    with open("spam-bank.txt", "r+") as file:
        for lines in file:
            if lines.strip("\n") == str(user.id):
                counter+=1
        
        file.writelines(f"{str(user.id)}\n")
        if counter > 7:
            await channel.send(f"{user.mention} stop spamming or i will mute you 😡",delete_after=3)
            users[str(user.guild.id)][str(user.id)]['mute'] += 1
            msg=[]
            limit=6
            async for m in channel.history():
                if len(msg) == limit:
                    break
                if m.author == user:
                    msg.append(m)
            await channel.delete_messages(msg)

async def update_data_spam(users, user,server):
    if not str(server.id) in users:
        users[str(server.id)] = {}
        if not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['mute'] = 0
    elif not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['mute'] = 0

async def update_data(users, user,server):
    if not str(server.id) in users:
        users[str(server.id)] = {}
        if not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['exp'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1
    elif not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['exp'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1

async def add_experience(users, user, server):
  users[str(user.guild.id)][str(user.id)]['exp'] += random.randint(1,10)

async def level_up(users, user, channel, server):
    exp = users[str(user.guild.id)][str(user.id)]['exp']
    lvl_start = users[str(user.guild.id)][str(user.id)]['level']
    lvl_end = int(exp ** (1/4))
    if lvl_start < lvl_end:
        msg=await channel.send('{} has leveled up to Level {}'.format(user.mention, lvl_end),delete_after=5)
        users[str(user.guild.id)][str(user.id)]['level'] = lvl_end
with open('Config.json', 'r') as f:
    Config = json.load(f)
channel_for_anti_and_exp=set(Config['channel_for_anti_and_exp'])

class onmess(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener("on_message")
    async def on_message(self,message):
        if not message.author.bot:
            if message.channel.id in channel_for_anti_and_exp:
                with open('users.json','r') as expp:
                    users = json.load(expp)
                await update_data(users, message.author,message.guild)
                await add_experience(users, message.author, message.guild)
                await level_up(users, message.author,message.channel, message.guild)

                with open('users.json','w') as expp:
                    json.dump(users, expp,indent=4)

                with open('spam.json','r') as antii:
                    users = json.load(antii)
                await update_data_spam(users, message.author,message.guild)
                await add_mute(users, message.author,message.channel, message.guild)
                await cheeck(users, message.author,message.channel, message.guild)
                with open('spam.json','w') as antii:
                    json.dump(users, antii,indent=4)



async def setup(bot):
    await bot.add_cog(onmess(bot))

