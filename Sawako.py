import discord
from discord.ext.commands import Bot
import string
import json

client = discord.Client()
BOT_PREFIX = '!'

with open("../venv/Scripts/config.json", "r") as f:
    config=json.load(f)
TOKEN = config["Token"]

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    game = discord.Game("tricks on you")
    await client.change_presence(activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'I am':
        await message.channel.send('Degen!')
    if message.content == 'Kazehaya':
        await message.channel.send(file=discord.File('../venv/Resources/GIFs/blush_1.gif'))
    if message.content == 'Sadako':
        await message.channel.send(file = discord.File('../venv/Resources/GIFs/sadako_1.gif'))
    if message.content.startswith('Vaibhav'):
        await message.channel.send('Futa lover!')
    if message.content.startswith('Guardian'):
        await message.channel.send('Computer is gone!')

async def hello(context):
    await context.send(content = ("Hello" + ", " + context.message.author.mention))

client.run(TOKEN)