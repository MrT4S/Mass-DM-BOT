import json
import discord
from discord import Intents
from discord.ext import commands
from concurrent.futures import ProcessPoolExecutor

with open('config.json', 'r') as config:
    get = json.load(config)
prefix = get['prefix']
token = get['token']
stats = get['status_name']
ints = discord.Intents.all()
client = commands.Bot(intents=ints, command_prefix=prefix)
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=f'{stats}'))
    print(f"=================\nLogged: {client.user} ({client.user.id})\n=================\nHelp: {prefix}help\n=================\nBy: github.com/DaddyTezzy\n=================")

@client.command(name='help')
async def _help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{client.user.name} | Prefix: {prefix} | Usage: {prefix}<>", description=f"**help** - Shows this message.\n> `Usage:` {prefix}help\n\n**massdm** - MassDM all users in the server the command is ran a custom message.\n> `Usage:` {prefix}massdm Hey, join the best community server for many giveaways: https://discord.gg/lobby\n\**nmassdmall** - MassDM all users in all servers the bot has access to a custom message.\n> `Usage:` {prefix}massdmall Hey, join the best pfp/icons server here: https://discord.gg/pfpz", color=0xf0f0f0)
    embed.set_footer(text="Made by https://github.com/DaddyTezzy | Please give credits.", icon_url=client.user.avatar_url)
    await ctx.author.send(ctx.author.mention, embed=embed)
    
@client.command(name='massdm')
async def _massdm(ctx, *, message):
    await ctx.message.delete()
    await ctx.author.send(embed = discord.Embed(description=f"Started `{prefix}massdm` !\n{ctx.guild.name}` guild | `{ctx.guild.member_count}` users", color=0xf0f0f0))
    for user in ctx.guild.members:
        global count
        try:
            await user.send(f"{message}\n\n- {user.mention}")
            count += 1
            print(f"Messaged: {user} ({count})")
        except:
            print(f"Failed: {user}")
    await ctx.author.send(embed = discord.Embed(description=f"Finished `{prefix}massdm` !", color=0xf0f0f0))

@client.command(name='massdmall')
async def _massdmall(ctx, *, message):
    await ctx.message.delete()
    await ctx.author.send(ctx.author.mention, embed = discord.Embed(description=f"Started `{prefix}massdmall` !\n`{len(client.guilds)}` guilds | `{len(client.users)}` users", color=0xf0f0f0))
    for user in client.guilds:
        global count
        try:
            await user.send(f"{message}\n\n- {user.mention}")
            count += 1
            print(f"Messaged: {user} ({count})")
        except:
            print(f"Failed: {user}")
    await ctx.author.send(ctx.author.mention, embed = discord.Embed(description=f"Finished `{prefix}massdmall` !", color=0xf0f0f0))
    
client.run(token, bot=True)
