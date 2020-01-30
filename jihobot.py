import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = "NjcyNTM5OTU5NzY0NDUxMzU5.XjNQ2Q.Lxn-VO8c64SYdc0oOzBfUkVDvN0"
CHANNEL_ID = 662647436119900183
client = discord.Client()

@tasks.loop(seconds=60)
async def loop():
    now = datetime.now().strftime('%H:%M')
    if now == '07:25':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはよう')  

loop.start()
client.run(TOKEN)
