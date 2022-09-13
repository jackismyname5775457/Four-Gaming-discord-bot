from datetime import datetime
import discord,asyncio
from discord.ext import commands
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

class raedy(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener("on_ready")
    async def on_ready(self):
        while True:
            print(f"cleared {current_time}")
            await asyncio.sleep(15)
            with open("spam-bank.txt", "r+") as file:
                file.truncate(0)
    
async def setup(bot):
    await bot.add_cog(raedy(bot))
