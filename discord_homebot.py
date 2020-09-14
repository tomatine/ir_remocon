#!/usr/bin/python3
# coding: UTF-8

import discord
import os
import re
import logging
from mojimoji import zen_to_han#半角を全角に変換するメソッド
from send_ir import fetch_code, send
from set_timer import timer

#ログ取り用スニペットのコピペ（discord.logに出力）
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s'))
logger.addHandler(handler)


client = discord.Client()
#クーラーオン、ヒーターオン、エアコンオフなどの、赤外線コードの入ったファイル名を変数指定
cooler_on_filename='cooler_on_25.txt'
heater_on_filename = 'heater_on_22.txt'
aircon_off_filename = 'aircon_stop.txt'
light_on_filename = 'light_on.txt'
light_off_filename = 'light_off.txt'
light_night_filename='light_night.txt'#常夜灯


#タイマーセット用関数（function_nameは暖房、冷房、オフなど、タイマーの名前）
async def timer_conversation(message, filename, function_name: str):
    try:
        time=re.findall('[0-9]+', zen_to_han(message.content))
        hour = int(time[0])
        minute = int(time[1])
        if hour < 0 or hour > 23 or minute < 0 or minute > 59:
            raise IndexError
        else:
            timer(hour,minute,filename)
            await message.channel.send('{0}:{1}に'.format(hour, minute)+function_name+'タイマーをセットしました！')
    except (IndexError):
        await message.channel.send('正しい形式の時刻を入力して！')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    game = discord.Game('\'ヘルプ\'と入力するとコマンド一覧を表示します')
    await client.change_presence(activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('ヘルプ'):
        help_message ='ライトオン---ライトを点けます\n\
ライトオフ---ライトを消します\n\
常夜灯---常夜灯にします\n\
冷房オン---25度で冷房をつけます\n\
暖房オン---22度で暖房をつけます\n\
エアコンオフ---エアコンを止めます\n\
冷房タイマー22:30---22:30に冷房をつけます\n\
暖房タイマー22:30---22:30に暖房をつけます\n\
オフタイマー22:30---22:30にエアコンを止めます\n\
'
        e = discord.Embed(title='ヘルプ',description=help_message,colour=0x206694)#colourをランダムで選べるようにしたい
        await message.channel.send(embed=e)

    if message.content == '/neko':
        await message.channel.send('nyan')

    if message.content == 'ありがとう':
        await message.channel.send('どういたしまして😁')

    if message.content == '冷房オン':
        code = fetch_code(cooler_on_filename)
        send(code)
        await message.channel.send('冷房をつけました！')

    if message.content == '暖房オン':
        code = fetch_code(heater_on_filename)
        send(code)
        await message.channel.send('暖房をつけました！')

    if message.content == 'エアコンオフ':
        code = fetch_code(aircon_off_filename)
        send(code)
        await message.channel.send('エアコンを止めました！')

    if message.content == 'ライトオン':
        code = fetch_code(light_on_filename)
        send(code)
        await message.channel.send('ライトを点けました！')

    if message.content == 'ライトオフ':
        code = fetch_code(light_off_filename)
        send(code)
        await message.channel.send('ライトを消しました！')
    
    if message.content == '常夜灯':
        code = fetch_code(light_night_filename)
        send(code)
        await message.channel.send('常夜灯にしました！')

    if message.content.startswith('冷房タイマー'):
        await timer_conversation(message, cooler_on_filename, '冷房')

    if message.content.startswith('暖房タイマー'):
        await timer_conversation(message, heater_on_filename, '暖房')

    if message.content.startswith('オフタイマー'):
        await timer_conversation(message, aircon_off_filename, 'オフ')

#環境変数からdiscordbotのトークンを取得
client.run(os.environ.get("discord_homebot_token"))