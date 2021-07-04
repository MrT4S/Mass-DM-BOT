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
client = commands.Bot(intents=ints, command_prefix=prefix, description='MassDM client by github.com/DaddyTezzy')
client.remove_command('help')

@client.event
async def on_ready():
    print(f"=================\nLogged: {client.user} ({client.user.id})\n=================\nHelp: {prefix}help\n=================\nBy: github.com/DaddyTezzy\n=================")
    await client.change_presence(activity=discord.Game(name=f'{stats}'))

@client.command(name='massdm')
async def _massdm(ctx, *, message):
    await ctx.message.delete()
    await ctx.author.send(f"> Started MassDMing! (`{prefix}massdm`)\n`{ctx.guild.name}` guild | `{ctx.guild.member_count}` users")
    for user in ctx.guild.members:
        global count
        try:
            await user.send(f"{message}\n\n- {user.mention}")
            count += 1
            print(f"Messaged: {user} ({count})")
        except:
            print(f"Failed: {user}")
    await ctx.author.send(f"> Finished MassDMing! (`{prefix}massdm`)")

@client.command(name='massdmall')
async def _massdmall(ctx, *, message):
    await ctx.message.delete()
    await ctx.author.send(f"> Started MassDMing! (`{prefix}massdmall`)\n`{len(client.guilds)}` guilds | `{len(client.users)}` users")
    for guilds in client.guilds:
        for user in guilds:
            global count
            try:
                await user.send(f"{message}\n\n- {user.mention}")
                count += 1
                print(f"Messaged: {user} ({count})")
            except:
                print(f"Failed: {user}")
    await ctx.author.send(f"> Finished MassDMing! (`{prefix}massdmall`)")

@client.command(name='help')
async def _help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{client.user} | Prefix: {prefix} | Usage: {prefix}<>", description=f"help - Shows this message.\n> `Usage:` {prefix}help\n\nmassdm - MassDM all users in the server the command is ran a custom message.\n> `Usage:` {prefix}massdm Hey, make sure to join our new server: https://discord.gg/lobby\n\nmassdmall - MassDM all users in all servers the bot has access to a custom message.\n> `Usage:` {prefix}massdmall Hey, make sure to join our new server: https://discord.gg/pfpz", color=0xf0f0f0)
    embed.set_footer(text="Made by https://github.com/DaddyTezzy | Please give credits.", icon_url=client.user.avatar_url)
    await ctx.author.send(ctx.author.mention, embed=embed)
    
client.run(token, bot=True)
