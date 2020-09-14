#!/usr/bin/python3
# coding: UTF-8

import discord
import os
from send_ir import fetch_code, send

client=discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == 'ヘルプ':
        help_message='\n冷房オン：25度で冷房をつけます\n暖房オン：暖房をつけます\nエアコンオフ：エアコンを止めます\n'
        await message.channel.send(help_message)

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


client.run(os.environ.get("discord_homebot_token"))