import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
import pip._vendor.requests as requests

load_dotenv()  # take environment variables from .env.


bot = commands.Bot(command_prefix='!')


#

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


@bot.command()
async def info(ctx):
    await ctx.send(

        f'Command Prefix : !\n'
        f'Commands: \n'
        f'!solve exp - exp is a numerical expression to be solved using python operators (+,-,/,*,**)\n'
        f'!ping      - returns pong\n'
        f'!gender name - name is the name of a person. This command will try to predict the gender based on the name entered\n'
        f'!fact        - Returns a Random Fact\n'
        f'!define word - Returns the definition of <word> \n'
        f'!bored - Returns an activity to cure your boredom \n'
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


@bot.command()
async def fact(ctx):
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    response = response.json()
    await ctx.send(

        f'Fact: {response["text"]}\n'
    )


@bot.command()
async def define(ctx, arg):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+arg
    response = requests.get(url)
    response = response.json()
    for res in response:

        await ctx.send(

            f'Word: {res["word"]}\n'
            f'Definition: {res["meanings"][0]["definitions"][0]["definition"]}\n'
            f'Phonetic: {res["phonetic"]}\n'
            # f'Origin: {res["origin"] or None}\n'
            f'Synonyms: {res["meanings"][0]["definitions"][0]["synonyms"]}\n'
        )


@bot.command()
async def bored(ctx):
    url = "http://www.boredapi.com/api/activity/"
    response = requests.get(url)
    response = response.json()

    await ctx.send(

        f'{response["activity"]}\n'
    )


bot.run(os.getenv("TOKEN"))
