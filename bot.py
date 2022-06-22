import os
import discord
import datetime
from discord.ext import commands, tasks
import asyncio
from pymongo import MongoClient
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
import random
from functions import *
import warnings

TOKEN = ""

class BugWarning(UserWarning):
    pass

intents = discord.Intents.default()
intents.members = True

dbclient = MongoClient(
    "")
discorddb = dbclient.get_database('discord')
prefixes = discorddb.prefix

async def get_prefix(bot, message):
    try:
        var = prefixes.find_one({"id": message.guild.id}, {"_id": False})
        var1 = str(var).replace("'", '"')
        prefix_json = json.loads(var1)
        return str(prefix_json["prefix"])
    except Exception:
        new_document = {
            "id": message.guild.id,
            'prefix': 's?'
        }
        prefixes.insert_one(new_document)
        return "s?"



client = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=intents,
                      owner_ids=[350325552344858624, 301731447046406145, 603635602809946113])
client.remove_command("help")


# Changing status
@tasks.loop(minutes=60)
async def loop():
    await client.change_presence(
        activity=discord.Streaming(name=f"@mention for help | {(len(client.commands))} commands!",
                                   url=open("assets/status_video.txt", "r").read()))

    
@client.event
async def on_connect():
    print(f"Bot Starting...!")
    print("-------------------")
    print(f'Client Name: {client.user.name}')
    print(f'Ping: {round(client.latency * 1000)}ms')
    print(f'Server Count: {len(client.guilds)}')
    print("-------------------")
    print("All Cogs:")
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
            print(f"| {filename}")
            
@client.event
async def on_ready():
    start_logs = DiscordWebhook(
        url='',
        username="Shiba Start Logs")

    embed = DiscordEmbed(title=f'Shiba Bot Started.', color=242424)

    embed.set_footer(text=f'Started at')
    embed.set_timestamp()

    start_logs.add_embed(embed)
    start_logs.execute()

    loop.start()


@client.event
async def on_message(message):
    await client.process_commands(message)
    if not message.author.bot and client.user in message.mentions:
        prefix = prefix_grabber(message.guild.id)
        channel = message.channel
        await channel.send(f'Woof woof, use {prefix}help for help.')
    if message.channel.id == 747486937539149936:
        await message.add_reaction('<a:yes_tick:747482909472063570>')
        await message.add_reaction('<a:no_tick:747482930271617184>')


@client.event
async def on_command(ctx):
    print(f"{datetime.datetime.now().strftime('%m:%d @ %H:%M')} | {ctx.message.content}")


@client.event
async def on_guild_join(guild):
    send_join_server_webhook(len(client.guilds))

    server_count = DiscordWebhook(
        url='',
        username="Shiba Server Log")

    embed = DiscordEmbed(title='I just joined a server!', description=f'```fix\n{guild.name}```', color="00FF00")

    embed.set_footer(text='Added to the server at')
    embed.set_timestamp()

    embed.set_thumbnail(url=f'{guild.icon_url}')
    embed.add_embed_field(name="Statistics:", value="**――――――――――――――――――――――――――――**", inline=False)
    embed.add_embed_field(name="Server Count:", value=f'```yaml\n{len(client.guilds)}```')
    embed.add_embed_field(name="Member Count:", value=f'```yaml\n{len(client.users)}```')
    embed.add_embed_field(name="Bot Ping:", value=f'```yaml\n{round(client.latency * 1000)}ms```')

    embed.add_embed_field(name="Guild Info:", value="**――――――――――――――――――――――――――――**", inline=False)
    embed.add_embed_field(name='Name:', value=f'```yaml\n{guild.name}```')
    embed.add_embed_field(name='Owner:', value=f'```yaml\n{str(guild.owner)}```')
    embed.add_embed_field(name='ID:', value=f'```yaml\n{guild.id}```')
    embed.add_embed_field(name='Total Members:', value=f'```yaml\n{len(guild.members)}```')
    embed.add_embed_field(name='Humans:',
                          value=f'```yaml\n{len([member.bot for member in guild.members if member.bot is not True])}'
                                '```')
    embed.add_embed_field(name='Bots:',
                          value=f'```yaml\n{len([member.bot for member in guild.members if member.bot is True])}'
                                '```')

    server_count.add_embed(embed)
    server_count.execute()


@client.event
async def on_guild_remove(guild):
    if guild.name is None:
        warnings.warn('A bug has been detected', BugWarning)
        return
    send_leave_server_webhook(len(client.guilds))

    server_count = DiscordWebhook(
        url='',
        username="Shiba Server Log")

    embed = DiscordEmbed(title='I just left a server :pensive:', description=f'```fix\n{guild.name}```', color="FF0000")

    embed.set_footer(text='Removed from the server at')
    embed.set_timestamp()

    embed.set_thumbnail(url=f'{guild.icon_url}')
    embed.add_embed_field(name="Statistics:", value="**――――――――――――――――――――――――――――**", inline=False)
    embed.add_embed_field(name="Server Count:", value=f'```yaml\n{len(client.guilds)}```')
    embed.add_embed_field(name="Member Count:", value=f'```yaml\n{len(client.users)}```')
    embed.add_embed_field(name="Bot Ping:", value=f'```yaml\n{round(client.latency * 1000)}ms```')

    embed.add_embed_field(name="Guild Info:", value="**――――――――――――――――――――――――――――**", inline=False)
    embed.add_embed_field(name='Name:', value=f'```yaml\n{guild.name}```')
    embed.add_embed_field(name='Owner:', value=f'```yaml\n{str(guild.owner)}```')
    embed.add_embed_field(name='ID:', value=f'```yaml\n{guild.id}```')
    embed.add_embed_field(name='Total Members:', value=f'```yaml\n{len(guild.members)}```')
    embed.add_embed_field(name='Humans:',
                          value=f'```yaml\n{len([member.bot for member in guild.members if member.bot is not True])}'
                                '```')
    embed.add_embed_field(name='Bots:',
                          value=f'```yaml\n{len([member.bot for member in guild.members if member.bot is True])}'
                                '```')

    server_count.add_embed(embed)
    server_count.execute()

client.run(TOKEN, reconnect=True)
