import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
import pip._vendor.requests as requests

load_dotenv()  # take environment variables from .env.


client = discord.Client()
bot = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Bot is online')


@client.event
async def on_message(message):
    if message.author == client.user:  # If it is not the bot that reacted
        return

    if message.content == 'hello' or message.content == 'Hello':
        await message.channel.send(
            f'{message.author}, welcome to the Testing Grounds'
        )

    if message.content == 'cool':
        await message.add_reaction('\U0001F60E')


@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} changed {before.content} to {after.content}'
    )


@client.event
async def on_reaction_add(reaction, user):

    if(reaction.message.author != client.user):  # If it is not the bot that reacted
        await reaction.message.channel.send(
            f'{user} reacted with {reaction.emoji}'
        )


@bot.event
async def on_ready():
    print('Bot command is online')


@bot.command()
async def solve(ctx, *arg):
    # ans = eval(arg)
    s = ''
    arg = s.join(arg)
    await ctx.send(
        f'{arg} : \n'

        f'{eval(arg)}\n'

    )
    # await ctx.send(f'Response : {eval(arg)}')


@bot.command()
async def info(ctx):
    await ctx.send(

        f'Command Prefix : !\n'
        f'Commands: \n'
        f'!solve exp - exp is a numerical expression to be solved using python operators (+,-,/,*,**)\n'
        f'!ping      - returns pong\n'
        f'!gender name - name is the name of a person. This command will try to predict the gender based on the name entered\n'
    )


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def gender(ctx, arg):
    url = "https://api.genderize.io/?name="+arg
    response = requests.get(url)
    response = response.json()
    await ctx.send(

        f'Name: {response["name"]}\n'
        f'Gender: {response["gender"]}\n'
        f'Probability: {response["probability"]}\n'
    )


# client.run(os.getenv("TOKEN"))
bot.run(os.getenv("TOKEN"))
