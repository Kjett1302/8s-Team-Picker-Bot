import random
import numpy as np
import discord
import os

from discord import message
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.all()
load_dotenv()
bot = commands.Bot(command_prefix='!', intents=intents)
token = os.getenv('TOKEN')

playerPool = []
team1 = []
team2 = []


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')


@bot.command(name='listCommands')
async def ping(ctx):
    await ctx.send('Picker Commands: addMe, viewPool, viewTeam1, viewTeam2, clearPool, makeTeams, remove <Name> EX: !remove Bob, ping')


@bot.command(name='viewPool')
async def viewPool(ctx):
    await ctx.send("Player Pool: " + str(playerPool))


@bot.command(name='viewTeam1')
async def viewTeam1(ctx):
    await ctx.send("Team 1: " + str(team1))


@bot.command(name='viewTeam2')
async def viewTeam2(ctx):
    await ctx.send("Team 2: " + str(team2))


@bot.command(name='clearPool')
async def clearPool(ctx):
    playerPool.clear()
    await ctx.send('Player Pool Clear!')


@bot.command(name='addMe')
async def addToPool(ctx):
    author = ctx.message.author
    userName = author.name
    playerPool.append(userName)
    await ctx.send(userName + " has been added to player pool!")


@bot.command(name='makeTeams')
async def makeTeams(ctx):
    if len(team1) or len(team2) != 0:
        team1.clear()
        team2.clear()
        await ctx.send('Old teams cleared!')
    playerCount = len(playerPool)
    if playerCount >= 8:
        randomNums = list(random.sample(range(playerCount), 8))
        randomNumsArray = np.array(randomNums)
        team1.append(playerPool[randomNumsArray[0]])
        team1.append(playerPool[randomNumsArray[1]])
        team1.append(playerPool[randomNumsArray[2]])
        team1.append(playerPool[randomNumsArray[3]])
        team2.append(playerPool[randomNumsArray[4]])
        team2.append(playerPool[randomNumsArray[5]])
        team2.append(playerPool[randomNumsArray[6]])
        team2.append(playerPool[randomNumsArray[7]])
        await ctx.send('Teams Made!')
    if playerCount < 8:
        missing = 8 - playerCount
        await ctx.send("Need " + str(missing) + " more players!")


@bot.command(name='remove')
async def removePlayer(ctx):
    TF = False
    userNameUnparsed = ctx.message.content
    userNameParsed = userNameUnparsed.replace('!remove ', '')
    for player in playerPool:
        if player == userNameParsed:
            TF = True

    if TF == True:
        playerPool.remove(userNameParsed)
        await ctx.send(userNameParsed + " has been removed from player pool!")

    if TF == False:
        await ctx.send(userNameParsed + " has NOT been removed, please verify player pool for spelling.")


bot.run(token)
