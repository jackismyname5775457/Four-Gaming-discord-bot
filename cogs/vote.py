
from discord.ext import commands,menus
import discord,os,json

from cogs.xp import server
class aa():
    async def heehee():
        with open('vote.json', 'r') as f:
            vote = json.load(f)
        tvote=vote['vote']
        qu=vote['qu']
        a1=vote['an1']
        annum1=vote['annum1']
        a2=vote['an2']
        annum2=vote['annum2']
        a3=vote['an3']
        annum3=vote['annum3']
        a4=vote['an4']
        annum4=vote['annum4']
        a5=vote['an5']
        annum5=vote['annum5']
        pa1= annum1/tvote*100
        pa2= annum2/tvote*100
        pa3= annum3/tvote*100
        pa4= annum4/tvote*100
        pa5= annum5/tvote*100
        embed = discord.Embed(color=discord.Colour.random())
        embed.add_field(name=qu, value=f"Tổng số phiếu: `{tvote}`--(`100%`)", inline=False)
        embed.add_field(name=(f'1️⃣. {a1}.'), value=f"Số phiếu: `{annum1}` / `{tvote}`--(`{pa1}%`)", inline=False)
        embed.add_field(name=(f'2️⃣. {a2}.'), value=f"Số phiếu: `{annum2}` / `{tvote}`--(`{pa2}%`)", inline=False)
        if a3 is not None:
            embed.add_field(name=(f'3️⃣. {a3}.'), value=f"Số phiếu: `{annum3}` / `{tvote}`--(`{pa3}%`)", inline=False)
        if a4 is not None:
            embed.add_field(name=(f'4️⃣. {a4}.'), value=f"Số phiếu: `{annum4}` / `{tvote}`--(`{pa4}%`)", inline=False)
        if a5 is not None:
            embed.add_field(name=(f'5️⃣. {a5}.'), value=f"Số phiếu: `{annum5}` / `{tvote}`--(`{pa5}%`)", inline=False)
        return embed
async def update_dataa(userss):
    userss['vote'] += 1

async def b1(userss):
    userss['annum1'] += 1

async def b2(userss):
    userss['annum2'] += 1

async def b3(userss):
    userss['annum3'] += 1

async def b4(userss):
    userss['annum4'] += 1

async def b5(userss):
    userss['annum5'] += 1

async def userr(userss,user,server):
    if not str(server) in userss['server']:
        userss['server'][str(server)] = {}
        if not str(user) in userss['server'][str(server)]:
            userss['server'][str(server)][str(user)] = {}
            userss['server'][str(server)][str(user)]['click'] = 0
    elif not str(user) in userss['server'][str(server)]:
            userss['server'][str(server)][str(user)] = {}
            userss['server'][str(server)][str(user)]['click'] = 0
        
async def aass(userss,server):
    userss['server'][str(server)] = {}

class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    with open('vote.json','r') as exppp:
        userss = json.load(exppp)
    @discord.ui.button( style=discord.ButtonStyle.primary, emoji="1️⃣") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_a1(self, interaction: discord.Interaction, button: discord.ui.Button):
        server= interaction.guild_id
        user= interaction.user.id
        
        with open('vote.json','r') as exppp:
            userss = json.load(exppp)
        await userr(userss,user,server)
        if userss['server'][str(server)][str(user)]['click'] >=1:
            await interaction.response.send_message('Tham lam vừa thôi bro!!!',ephemeral=True)  
            return
        userss['server'][str(server)][str(user)]['click']+=1
        await update_dataa(userss)
        await b1(userss)
        with open('vote.json','w') as exppp:
            json.dump(userss, exppp,indent=4)
        embed = await aa.heehee()
        await interaction.response.edit_message(embed=embed)


    @discord.ui.button( style=discord.ButtonStyle.primary, emoji="2️⃣") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_a2(self, interaction: discord.Interaction, button: discord.ui.Button):
        server= interaction.guild_id
        user= interaction.user.id
        
        with open('vote.json','r') as exppp:
            userss = json.load(exppp)
        await userr(userss,user,server)
        if userss['server'][str(server)][str(user)]['click'] >=1:
            await interaction.response.send_message('Tham lam vừa thôi bro!!!',ephemeral=True)  
            return
        userss['server'][str(server)][str(user)]['click']+=1
        await update_dataa(userss)
        await b2(userss)
        with open('vote.json','w') as exppp:
            json.dump(userss, exppp,indent=4)
        embed = await aa.heehee()
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button( style=discord.ButtonStyle.primary, emoji="3️⃣") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_a3(self, interaction: discord.Interaction, button: discord.ui.Button):
        server= interaction.guild_id
        user= interaction.user.id
        with open('vote.json','r') as exppp:
            userss = json.load(exppp)
        a=userss['an3']
        if a== None:
            button.style = discord.ButtonStyle.green
            button.disabled = True
        await userr(userss,user,server)
        if userss['server'][str(server)][str(user)]['click'] >=1:
            await interaction.response.send_message('Tham lam vừa thôi bro!!!',ephemeral=True)  
            return
        userss['server'][str(server)][str(user)]['click']+=1
        await update_dataa(userss)
        await b3(userss)
        with open('vote.json','w') as exppp:
            json.dump(userss, exppp,indent=4)
        embed = await aa.heehee()
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button( style=discord.ButtonStyle.primary, emoji="4️⃣") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_a4(self, interaction: discord.Interaction, button: discord.ui.Button):
        server= interaction.guild_id
        user= interaction.user.id
        
        with open('vote.json','r') as exppp:
            userss = json.load(exppp)
        await userr(userss,user,server)
        if userss['server'][str(server)][str(user)]['click'] >=1:
            await interaction.response.send_message('Tham lam vừa thôi bro!!!',ephemeral=True)  
            return
        userss['server'][str(server)][str(user)]['click']+=1
        await update_dataa(userss)
        await b4(userss)
        with open('vote.json','w') as exppp:
            json.dump(userss, exppp,indent=4)
        embed = await aa.heehee()
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(style=discord.ButtonStyle.primary, emoji="5️⃣") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_a5(self, interaction: discord.Interaction, button: discord.ui.Button):
        server= interaction.guild_id
        user= interaction.user.id
        
        with open('vote.json','r') as exppp:
            userss = json.load(exppp)
        await userr(userss,user,server)
        if userss['server'][str(server)][str(user)]['click'] >=1:
            await interaction.response.send_message('Tham lam vừa thôi bro!!!',ephemeral=True)  
            return
        userss['server'][str(server)][str(user)]['click']+=1
        await update_dataa(userss)
        await b5(userss)
        with open('vote.json','w') as exppp:
            json.dump(userss, exppp,indent=4)
        embed = await aa.heehee()
        await interaction.response.edit_message(embed=embed)



 
class vote(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command() # Create a slash command
    async def t(self,ctx,qu=None,a1=None,a2=None,a3=None,a4=None,a5=None,):
        with open('vote.json', 'r') as f:
            userss = json.load(f)
        server = ctx.guild.id
        userss['vote']=0
        userss['qu']= qu
        userss['an1']= a1
        userss['annum1']= 0
        userss['an2']= a2
        userss['annum2']= 0
        userss['an3']= a3
        userss['annum3']= 0
        userss['an4']= a4
        userss['annum4']= 0
        userss['an5']= a5
        userss['annum5']= 0
        await aass(userss,server)
        with open('vote.json','w') as votee:
            json.dump(userss, votee,indent=1)
        if qu==None:
            await ctx.send('nedd ques')
            return
        if a1==None: 
            await ctx.send('need an1')
            return
        if a2==None:
            await ctx.send('need an2')
            return
        if a1 and a2 and qu is not None:
            embed = discord.Embed(color=discord.Colour.random())
            embed.add_field(name=qu, value=f"-", inline=False)
            embed.add_field(name=(f'1️⃣. {a1}.'), value=f"-", inline=False)
            embed.add_field(name=(f'2️⃣. {a2}.'), value=f"-", inline=False)
            if a3 is not None:
                embed.add_field(name=(f'3️⃣. {a3}.'), value=f"-", inline=False)
            if a4 is not None:
                embed.add_field(name=(f'4️⃣. {a4}.'), value=f"-", inline=False)
            if a5 is not None:
                embed.add_field(name=(f'5️⃣. {a5}.'), value=f"-", inline=False)
            await ctx.send("here is your ques",embed=embed, view=MyView())

async def setup(bot):
    await bot.add_cog(vote(bot))


