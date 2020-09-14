#!/usr/bin/python3
# coding: UTF-8

import discord
import os
import logging
from send_ir import fetch_code, send

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)


client=discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game('\'ヘルプ\'と入力するとコマンド一覧を表示します')
    await client.change_presence(activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == 'ヘルプ':
        help_message = '冷房オン---25度で冷房をつけます\n\
暖房オン---暖房をつけます\n\
エアコンオフ---エアコンを止めます\n\
冷房タイマー22:30---22:30に冷房をつけます\n\
暖房タイマー22:30---22:30に暖房をつけます\n\
オフタイマー22:30---22:30にエアコンを止めます\n\
'
        e = discord.Embed(title='ヘルプ',description=help_message,colour=0x206694)#colourをランダムで選べるようにしたい
        await message.channel.send(embed=e)

    if message.content == '/neko':
        await message.channel.send('nyan')

    if message.content == '冷房オン':
        code = fetch_code('cooler_on_25.txt')
        send(code)
        await message.channel.send('冷房をつけました！')

    if message.content == '暖房オン':
        await message.channel.send('暖房をつけました！')

    if message.content == 'エアコンオフ':
        code = fetch_code('aircon_stop.txt')
        send(code)
        await message.channel.send('エアコンを止めました！')

    if message.content.startswith('冷房タイマー'):
        
        await message.channel.send('{0}:{1}にタイマーをセットしました！'.format(hour,minute))

client.run(os.environ.get("discord_homebot_token"))