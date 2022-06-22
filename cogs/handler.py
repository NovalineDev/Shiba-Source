import discord
from discord.ext import commands
import math
from difflib import SequenceMatcher

import json
from pymongo import MongoClient

facepalm_gif = "https://media.discordapp.net/attachments/755131015751532584/818192626108727296/bruh.gif"

dbclient = MongoClient(
    "")
discorddb = dbclient.get_database('discord')
prefixes = discorddb.prefix


def prefix_grabber(id):
    var = prefixes.find_one({"id": id}, {"_id": False})
    var1 = str(var).replace("'", '"')
    prefix_json = json.loads(var1)
    return str(prefix_json[str("prefix")])


class Handler(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):  # sourcery no-metrics
        if isinstance(error, commands.CommandNotFound):
            prefix = prefix_grabber(ctx.guild.id)
            suggestion = None
            for command in self.client.all_commands:
                if self.client.all_commands[command].enabled and not self.client.all_commands[command].hidden:
                    ratio = round(SequenceMatcher(a=ctx.invoked_with, b=command).ratio(),
                                  1)
                    if ratio >= 0.7:
                        suggestion = command
                        break
            if suggestion is None:
                e = discord.Embed(colour=0xff0000,
                                  description=f"That command doesn't exist! Use `{prefix}help` for a list of commands.")
            else:
                e = discord.Embed(colour=0xff0000,
                                  description="That command doesn't exist! Did you perhaps mean "
                                              f"`{prefix}{suggestion}`?")
            e.set_author(name='Command not found', icon_url="https://i.imgur.com/OyDaCvd.png")
            await ctx.reply(embed=e)

        # client - command disabled
        if isinstance(error, commands.DisabledCommand):
            e = discord.Embed(description="This command has been disabled.",
                              color=0xff0000)
            e.set_author(name='Disabled', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.reply(embed=e, delete_after=10)

        elif isinstance(error, commands.CommandOnCooldown):
            e = discord.Embed(
                description=f"You are ratelimited. Please try again in {math.ceil(error.retry_after)} seconds.",
                color=0xff0000)
            e.set_author(name='Ratelimited', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.reply(embed=e, delete_after=10)

        elif isinstance(error, commands.MissingPermissions):
            if ctx.command.name == "kick":
                e = discord.Embed(description="You need the `kick members` permissions to use this command.",
                                  color=0xff0000)
                e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                return await ctx.reply(embed=e)

            elif ctx.command.name == "ban":
                e = discord.Embed(description="You need the `ban members` permissions to use this command.",
                                  color=0xff0000)
                e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                return await ctx.reply(embed=e)

            else:
                e = discord.Embed(description=f"You can't use this command.", color=0xff0000)
                e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                return await ctx.reply(embed=e, delete_after=10)

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                e = discord.Embed(description=f"You can't use this command in DMs.",
                                  color=0xff0000)
                e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                return await ctx.author.send(embed=e, delete_after=10)
            except discord.Forbidden:
                return

        elif isinstance(error, commands.errors.NSFWChannelRequired):

            if ctx.command.cog_name == "Nsfw":
                e = discord.Embed(description=f"Nsfw channel is required for this command :upside_down:",
                                  color=0xff0000)
                e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
            else:
                e = discord.Embed(description=f"```py\n{error}```",
                                  color=0xff0000)
                e.set_author(name='Nsfw channel is required', icon_url="https://i.imgur.com/OyDaCvd.png")
            e.set_footer(text=f"{error.__class__.__name__} | Command: {ctx.command}")
            return await ctx.reply(embed=e)

        elif isinstance(error, commands.CheckFailure):
            e = discord.Embed(description=f"You can't use this command.", color=0xff0000)
            e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
            return await ctx.reply(embed=e, delete_after=10)

        elif isinstance(error, Exception):
            try:
                if ctx.command.name == "skin":
                    e = discord.Embed(description=f"Player does not exist!",
                                      color=0xff0000)
                    e.set_author(name='Error fetching skin', icon_url="https://i.imgur.com/OyDaCvd.png")
                    e.set_footer(text=f"{error.__class__.__name__} | Command: {ctx.command}")
                elif ctx.command.name == "mock":
                    e = discord.Embed(description=f"Please give me something to mock at... :smile:",
                                      color=0xff0000)
                    e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                    e.set_footer(text=f"{error.__class__.__name__} | Command: {ctx.command}")
                elif ctx.command.name == "_8ball":
                    e = discord.Embed(description=f"Please ask the 8ball a question!",
                                      color=0xff0000)
                    e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                    e.set_footer(
                        text=f"{error.__class__.__name__} | Command: {ctx.command.replace('_8ball', '8ball')}")
                elif ctx.command.name == "urban":
                    e = discord.Embed(description=f"Word was not found in the urbandictionary.",
                                      color=0xff0000)
                    e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                    e.set_footer(text=f"{error.__class__.__name__} | Command: {ctx.command}")
                elif ctx.command.name == "say":
                    e = discord.Embed(description=f"Please provide something to say!",
                                      color=0xff0000)
                    e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                    e.set_footer(text=f"{error.__class__.__name__} | Command: {ctx.command}")
                elif ctx.command.name == "changeprefix":
                    e = discord.Embed(description=f"Please provide a new prefix!",
                                      color=0xff0000)
                    e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                    e.set_footer(text=f"{error.__class__.__name__} | Command: {ctx.command}")
                elif ctx.command.name == "the":
                    e = discord.Embed(description=f"```The what?```",
                                      color=0xff0000)
                    e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                    e.set_footer(text=f"{error.__class__.__name__} | Command: {ctx.command}")
                elif ctx.command.name == "ban":
                    e = discord.Embed(
                        description=f"I don't have permission to ban this person or you didn't give me "
                                    f"anyone to ban...",
                        color=0xff0000)
                    e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                    e.set_footer(text=f"{error.__class__.__name__} | Command: {ctx.command}")
                elif ctx.command.name == "kick":
                    e = discord.Embed(
                        description=f"I don't have permission to kick this person or you didn't give me "
                                    f"anyone to kick...",
                        color=0xff0000)
                    e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                    e.set_footer(text=f"{error.__class__.__name__} | Command: {ctx.command}")
                elif ctx.command.name == "enlarge":
                    e = discord.Embed(
                        description=f"Please provide a custom emoji for me to enlarge.. regular emojis don't work.",
                        color=0xff0000)
                    e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                    e.set_footer(text=f"{error.__class__.__name__} | Command: {ctx.command}")
                else:
                    e = discord.Embed(
                        description=f"**You can report the error here:** [support server]("
                                    f"https://discord.gg/xc6xGCY)\n```py\n{error}```",
                        color=0xff0000)
                    e.set_author(name='Command raised exception | Please try again',
                                 icon_url="https://i.imgur.com/OyDaCvd.png")
                    e.set_image(url=facepalm_gif)
                    e.set_footer(text=f"{error.__class__.__name__} | Command: {ctx.command}")
                return await ctx.reply(embed=e)

            except AttributeError:
                pass

        else:
            return


def setup(client):
    client.add_cog(Handler(client))
