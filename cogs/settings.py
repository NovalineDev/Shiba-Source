import discord
from discord.ext import commands
import json
from pymongo import MongoClient


def prefix_grabber(_id):
    var = prefixes.find_one({"id": _id}, {"_id": False})
    var1 = str(var).replace("'", '"')
    prefix_json = json.loads(var1)
    return str(prefix_json[str("prefix")])


dbclient = MongoClient(
    "")
discorddb = dbclient.get_database('discord')
prefixes = discorddb.prefix


class Settings(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["prefix"])
    @commands.cooldown(1, 25, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    async def changeprefix(self, ctx, prefix):
        old_prefix = prefix_grabber(ctx.guild.id)
        updates = {
            "prefix": prefix
        }
        prefixes.update_one({'id': ctx.guild.id}, {'$set': updates})
        await ctx.reply(f"Prefix changed from {old_prefix} to {prefix}")


def setup(client):
    client.add_cog(Settings(client))
