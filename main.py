from webserver import keep_alive
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
        f'!html - Returns Emmet html boilerplate code \n'
        f'!css - Returns CSS boilerplate code \n'
        f'!cpp - Returns Cpp boilerplate code \n'
        f'!c - Returns C boilerplate code \n'
        f'!cppbasics - Returns a file containing basic Cpp concepts'
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
    if response["link"]:
        await ctx.send(

            f'{response["activity"]}\n'
            f'Link: {response["link"]}\n'
        )
    else:
        await ctx.send(

            f'{response["activity"]}\n'
        )


@bot.command()
async def html(ctx):
    file = discord.File("./index.html")
    await ctx.send(file=file, content="HTML Boilerplate")


@bot.command()
async def css(ctx):
    file = discord.File("./styles.css")
    await ctx.send(file=file, content="CSS Boilerplate")


@bot.command()
async def cpp(ctx):
    file = discord.File("./main.cpp")
    await ctx.send(file=file, content="Cpp Boilerplate")


@bot.command()
async def c(ctx):
    file = discord.File("./main.c")
    await ctx.send(file=file, content="C Boilerplate")


@bot.command()
async def loop(ctx, lang, type):
    start = "```"+lang
    end = "```"
    if(type == ('for' or 'For')):
        if (lang == 'python'):
            await ctx.send(
                f'''{start}       
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x){end} '''
            )


@bot.command()
async def cppbasics(ctx):
    file = discord.File("./cppbasics.txt")
    await ctx.send(file=file, content="Cpp Basics")


keep_alive()
bot.run(os.getenv("TOKEN"))
