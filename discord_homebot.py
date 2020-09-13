#!/usr/bin/python3
# coding: UTF-8

import discord
import os

client=discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content=='/neko':
        await message.channel.send('nyan')

    if message.content == '冷房オン':
        await message.channel.send('冷房をつけました！')

    if message.content == '暖房オン':
        await message.channel.send('暖房をつけました！')

    if message.content == 'エアコンオフ':
        await message.channel.send('エアコンを止めました！')


client.run(os.environ.get("discord_homebot_token"))