'''from discord.ext.commands import Bot
from discord import File, Game


BOT_PREFIX = '!'
TOKEN = 'NjA4MjkzOTExNjI2MTIxMjI2.XUmGCg.cnkYjJeiqtyp-DBNKEnselzsrIw'
client = Bot(command_prefix = BOT_PREFIX)

@client.command(name='hello',
                description="Greets you back.",
                brief="Greets you back.",
                aliases=['Hello'],
                pass_context=True)
async def hello(context):
    await context.send(content = ("Hello" + ", " + context.message.author.mention))

@client.command(name='dance',
                description="Da Vinci Dance!",
                brief="Da Vinci Dance!",
                aliases=['Dance'],
                pass_context=True)
async def dance(context):
    await context.send(file = File('../venv/Resources/GIFs/DaVincidance.gif'))

@client.command(name='sadako',
                description="Sadako",
                brief="Sadako",
                aliases=['Sadako'],
                pass_context=True)
async def sadako(context):
    await context.send(file = File('../venv/Resources/GIFs/sadako_1.gif'))


@client.event
async def on_ready():
    game = Game("With the code")
    await client.change_presence(activity=game)
    print("Logged in as " + client.user.name)


client.run(TOKEN)
'''

import discord
from discord.ext.commands import Bot
import string
import _json

client = discord.Client()
BOT_PREFIX = '!'

f = open(config.json)

TOKEN = _json.load(f)

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
        await message.channel.send(file = discord.File('../venv/Resources/GIFs/blush_1.gif'))
    if message.content.startswith('Vaibhav'):
        await message.channel.send('Futa lover!')
    if message.content.startswith('Guardian'):
        await message.channel.send('Autistic!')

client.run(TOKEN)