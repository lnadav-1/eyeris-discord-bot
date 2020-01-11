import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')



def addfunc(a,b):
	return(a+b)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def echo(ctx, message: str):
    await ctx.send(message)

@bot.command()
async def foo(ctx, warp: str):
	if warp == "oof":
		await ctx.send("bloop")
	else:
		await ctx.send("blarp")

@bot.command()
async def add(ctx, a:int, b:int):
	
	await ctx.send(addfunc(a,b))

bot.run('NDk2MzUxMDcwNTA3NzYxNjY1.Xfvqcw.vml7GMsFr6DhVMhAJjvdlqPbOjo')