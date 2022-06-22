import discord
from discord.ext import commands
import asyncio

import time
from pymongo import MongoClient
import json
import datetime

msg_ = None
msg2_ = None


def prefix_grabber(id):
    var = prefixes.find_one({"id": id}, {"_id": False})
    var1 = str(var).replace("'", '"')
    prefix_json = json.loads(var1)
    return str(prefix_json[str("prefix")])


dbclient = MongoClient(
    "")
discorddb = dbclient.get_database('discord')
prefixes = discorddb.prefix

snipeDB = discorddb.snipe
editsnipeDB = discorddb.editsnipe


class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount + 1)
        embed = discord.Embed(title="Cleared " + str(amount) + ' messages.', color=discord.Colour.blue())
        message = await ctx.send(embed=embed)
        await asyncio.sleep(2)
        await message.delete()

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason=None):
        await member.kick(reason=f'{reason} | by {ctx.author.name}')
        embed = discord.Embed(title=f"{member.name} got kicked by {ctx.author.name}", color=discord.Colour.blue())
        embed.add_field(name=f"Reason: **{reason}**!", inline=True)
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        await member.ban(reason=f'{reason} | by {ctx.author.name}')
        embed = discord.Embed(title=f"{member.name} got banned by {ctx.author.name}", color=discord.Colour.blue())
        embed.set_image(url="https://media.discordapp.net/attachments/755131015751532584/823221277807476826/banned.gif")
        embed.add_field(name="Reason", value=f"**{reason}**", inline=True)
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, *, response):
        response = response.replace("(", "")
        response = response.replace(")", "")
        await ctx.reply(response)

    @commands.command()
    async def id(self, ctx, user: discord.Member = None):
        avatar = self.client.user.avatar_url
        embed = discord.Embed(colour=discord.Colour(0x62ff))

        embed.set_thumbnail(url=f"{avatar}")
        embed.set_author(name="Shiba User ID Grabber", icon_url=f"{avatar}")

        if user is None:
            id = ctx.author.id
            embed.add_field(
                name=f"{ctx.author.name} your user ID is", value=f"```{id}```", inline=True)
        elif ctx.author.id == user.id:
            id = user.id
            embed.add_field(
                name=f"{user.name} your user ID is", value=f"```{id}```", inline=True)
        else:
            id = user.id
            embed.add_field(
                name=f"The User ID of {user.name} is",
                value=f"```{id}```",
                inline=True)
        await ctx.reply(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles if role.name != '@everyone']

        embed = discord.Embed(color=discord.Colour.blue())

        embed.set_author(name=f"User info - {member}")
        embed.set_thumbnail(url=member.avatar_url)

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Nickname:", value=member.display_name)

        embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(
            name=f"Roles ({len(roles)})",
            value=" ".join(role.mention for role in roles),
        )

        embed.add_field(name="Top role:", value=member.top_role.mention)

        await ctx.reply(content=f"<:info:856882672508469259> | information about **{member}**.", embed=embed)

    @commands.command()
    async def serverinfo(self, ctx):
        find_bots = sum(1 for member in ctx.guild.members if member.bot)

        embed = discord.Embed(color=discord.Colour.blue())

        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon_url)
        if ctx.guild.banner:
            embed.set_image(url=ctx.guild.banner_url_as(format="png"))

        embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
        embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
        embed.add_field(name="Members", value=ctx.guild.member_count, inline=True)
        embed.add_field(name="Bots", value=find_bots, inline=True)
        embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
        embed.add_field(name="Region", value=ctx.guild.region, inline=True)
        date = ctx.guild.created_at.strftime("%d/%m/%Y, %H:%M (D/M/Y, H:M)")
        embed.add_field(name="Created", value=date, inline=True)

        await ctx.reply(content=f"<:info:856882672508469259> | information about **{ctx.guild.name}**.", embed=embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        prefix = prefix_grabber(message.guild.id)
        if f"{prefix}snipe" not in message.content and not message.author.bot:
            try:
                var = snipeDB.find_one({"id": int(message.guild.id)}, {"_id": False})
                var1 = str(var).replace("'", '"')
                json.loads(var1)
                updates = {
                    'pfp': str(message.author.avatar_url),
                    'msg': str(message.content).replace("'", "").replace('"', ''),
                    'author': str(message.author.name).replace("'", "").replace('"', ''),
                    'time': str(datetime.datetime.now().strftime('%d %b %Y %H:%M'))
                }
                snipeDB.update_one({'id': int(message.guild.id)}, {'$set': updates})

            except Exception:
                new_document = {
                    'id': int(message.guild.id),
                    'pfp': str(message.author.avatar_url),
                    'server': str(message.guild.name).replace("'", "").replace('"', ''),
                    'msg': str(message.content).replace("'", "").replace('"', ''),
                    'author': str(message.author.name).replace("'", "").replace('"', ''),
                    'time': str(datetime.datetime.now().strftime('%d %b %Y %H:%M'))
                }
                snipeDB.insert_one(new_document)

    @commands.command()
    @commands.guild_only()
    async def snipe(self, ctx):
        try:
            var = snipeDB.find_one({"id": int(ctx.guild.id)}, {"_id": False})
            var1 = str(var).replace("'", '"')
            snipe_db_json = json.loads(var1)
            e = discord.Embed(description=str(snipe_db_json[str("msg")]),
                              color=discord.Colour.blue())
            e.set_author(name=f'{str(snipe_db_json[str("author")])} said...',
                         icon_url=f'{str(snipe_db_json[str("pfp")])}')
            time = str(snipe_db_json[str("time")])
            e.set_footer(text=f"Message sent at {time} (GMT)")
            await ctx.reply(embed=e)
        except Exception:
            e = discord.Embed(description=f"There is nothing to snipe!",
                              color=0xff0000)
            e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
            e.set_footer(text=f"Command: {ctx.command}")
            await ctx.reply(embed=e)

    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
        print(message_after)  # me when pycharm
        if not message_before.author.bot:
            try:
                var = editsnipeDB.find_one({"id": int(message_before.guild.id)}, {"_id": False})
                var1 = str(var).replace("'", '"')
                json.loads(var1)
                updates = {
                    'pfp': str(message_before.author.avatar_url),
                    'msg': str(message_before.content).replace("'", "").replace('"', ''),
                    'author': str(message_before.author.name).replace("'", "").replace('"', ''),
                    'time': str(datetime.datetime.now().strftime('%d %b %Y %H:%M'))
                }
                editsnipeDB.update_one({'id': int(message_before.guild.id)}, {'$set': updates})

            except Exception:
                new_document = {
                    'id': int(message_before.guild.id),
                    'pfp': str(message_before.author.avatar_url),
                    'server': str(message_before.guild.name).replace("'", "").replace('"', ''),
                    'msg': str(message_before.content).replace("'", "").replace('"', ''),
                    'author': str(message_before.author.name).replace("'", "").replace('"', ''),
                    'time': str(datetime.datetime.now().strftime('%d %b %Y %H:%M'))
                }
                editsnipeDB.insert_one(new_document)

    @commands.command()
    @commands.guild_only()
    async def editsnipe(self, ctx):
        try:
            var = editsnipeDB.find_one({"id": int(ctx.guild.id)}, {"_id": False})
            var1 = str(var).replace("'", '"')
            editsnipe_db_json = json.loads(var1)
            e = discord.Embed(description=str(editsnipe_db_json[str("msg")]),
                              color=discord.Colour.blue())
            e.set_author(name=f'{str(editsnipe_db_json[str("author")])} said...',
                         icon_url=f'{str(editsnipe_db_json[str("pfp")])}')
            time = str(editsnipe_db_json[str("time")])
            e.set_footer(text=f"Message sent at {time} (GMT)")
            await ctx.reply(embed=e)
        except Exception:
            e = discord.Embed(description=f"There is nothing to snipe!",
                              color=0xff0000)
            e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
            e.set_footer(text=f"Command: {ctx.command}")
            await ctx.reply(embed=e)

    @commands.Cog.listener()
    async def on_ready(self):
        editsnipeDB.remove({})
        snipeDB.remove({})


def setup(client):
    client.add_cog(Mod(client))
