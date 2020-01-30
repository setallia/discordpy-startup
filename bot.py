#coding:UTF-8
import discord
from discord.ext import tasks
from datetime import datetime 

TOKEN = "NjcyNTM5OTU5NzY0NDUxMzU5.XjNYbg.xRE2wwympijRKOYPXj0Yvvz66Oc" #トークン
CHANNEL_ID = 662647436119900183 #チャンネルID
# 接続に必要なオブジェクトを生成
client = discord.Client()

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    if now == '07:30':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('おはよう')  

#ループ処理実行
loop.start()
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
