import discord
from discord.ext import commands
import json
from pymongo import MongoClient
import asyncio
import random

haveBeenAsked = []


def partner_grabber(id):
    var = partners.find_one({"id": id}, {"_id": False})
    var1 = str(var).replace("'", '"')
    partner_json = json.loads(var1)
    return str(partner_json[str("partner_id")])


def check_partner(id):
    try:
        var = partners.find_one({"id": id}, {"_id": False})
        var1 = str(var).replace("'", '"')
        partner_json = json.loads(var1)
        return str(partner_json[str("partner_id")])

    except Exception:
        new_document = {
            'id': id,
            'partner_id': int(0)
        }
        partners.insert_one(new_document)
        var = partners.find_one({"id": id}, {"_id": False})
        var1 = str(var).replace("'", '"')
        partner_json = json.loads(var1)
        return str(partner_json[str("partner_id")])


def check_asked(id):
    var = askedByDB.find_one({"haveBeenAsked": id}, {"_id": False})
    var1 = str(var).replace("'", '"')
    asked_by_db_json = json.loads(var1)
    return str(asked_by_db_json[str("askedBy")])


dbclient = MongoClient(
    "")
discorddb = dbclient.get_database('discord')
partners = discorddb.partner
askedByDB = discorddb.askedBy

rose_gifs = ["https://media1.tenor.com/images/a27ffcb97c97875cc894601c5a8a5335/tenor.gif",
             "https://media1.tenor.com/images/092b8d0da857f1ecfcb5cbac57b1ff62/tenor.gif",
             "https://media1.tenor.com/images/b3ca272aa1cb91728a6774e863633bf3/tenor.gif"]

chocolate_gids = ["https://media1.tenor.com/images/37178d20f48bb581c7bf44b904da7fb7/tenor.gif",
                  "https://media1.tenor.com/images/9585bc5b9904f9eb1ea3c9e855bfd929/tenor.gif"]


class Marriage(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def test_partner_db(self, ctx):
        try:
            await ctx.send(partner_grabber(ctx.author.id))

        except Exception:
            new_document = {
                'id': ctx.author.id,
                'partner_id': int(0)
            }
            partners.insert_one(new_document)

            await ctx.send(str(partner_grabber(ctx.author.id)))

    @commands.command()
    async def marriage(self, ctx):
        message = await ctx.send(f"<a:loading:802883106868428801> | {ctx.author.mention} loading your data.")
        partner = check_partner(ctx.author.id)
        if partner == "0":
            await message.edit(
                content=f":broken_heart: | {ctx.author.mention}, I'm sorry but you don't have a fiancé..")
        else:
            await message.edit(content=f":hearts: | {ctx.author.mention}, <@{partner}> is your fiancé!")

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def marry(self, ctx, member: discord.Member = None):
        message = await ctx.send(f"<a:loading:802883106868428801> | {ctx.author.mention} loading data...")
        try:
            check_asked(member.id)
            await message.edit(
                content=f":thinking: | {ctx.author.mention}, {member.mention} already asked someone else to be their "
                        f"fiancé...")
        except Exception:
            if not member:
                await message.edit(
                    content=f":thinking: | {ctx.author.mention}, please mention someone to ask! `s?ask @user`")
            else:
                partner = check_partner(ctx.author.id)
                if partner != "0":
                    await message.edit(content=f":thinking: | {ctx.author.mention}, you already have a fiancé!")
                elif member.id == ctx.author.id:
                    await message.edit(content=f":thinking: | {ctx.author.mention}, you can't be your own fiancé...")
                else:
                    partner = check_partner(member.id)
                    if partner != "0":
                        await message.edit(
                            content=f":broken_heart: | {ctx.author.mention}, {member.name} already has a fiancé...")
                    else:
                        await message.delete()
                        message = await ctx.send(
                            f":eyes: | {member.mention}, {ctx.author.mention} asked to be your fiancé, do you accept?")
                        haveBeenAsked.append(f"{member.id}")
                        new_document = {
                            'haveBeenAsked': member.id,
                            'askedBy': ctx.author.id
                        }
                        askedByDB.insert_one(new_document)
                        await message.add_reaction("✅")
                        await message.add_reaction("❎")
                        await asyncio.sleep(60)
                        try:
                            askedByDB.delete_one({'haveBeenAsked': member.id})
                            haveBeenAsked.remove(f"{member.id}")
                        except Exception:
                            pass
                        try:
                            await message.clear_reaction("✅")
                            await message.clear_reaction("❎")
                            await message.edit(content=f":alarm_clock: | This marriage proposal has expired.")
                        except Exception:
                            pass

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.message.author.id != self.client.user.id:
            return
        if reaction.emoji == '✅':
            if str(user.id) in haveBeenAsked:
                try:
                    asked_by = check_asked(user.id)
                    haveBeenAsked.remove(f"{user.id}")
                    askedByDB.delete_one({'haveBeenAsked': user.id})
                    await reaction.message.delete()

                    message = await reaction.message.channel.send(
                        f"<a:loading:802883106868428801> | Updating database please wait...")

                    updates = {
                        "partner_id": int(user.id)
                    }
                    partners.update_one({'id': int(asked_by)}, {'$set': updates})

                    updates = {
                        "partner_id": int(asked_by)
                    }
                    partners.update_one({'id': user.id}, {'$set': updates})

                    await message.delete()
                    await reaction.message.channel.send(
                        f"<a:animated_hearts:809060094456496145> | <@{asked_by}>, {user.mention} said yes! "
                        f"<:Cute:809117636742086676> *How cute! :3*")

                except Exception:
                    await reaction.message.delete()
                    await reaction.message.channel.send(
                        f":sob: | I'm sorry but it looks like something went wrong, please try again...")

        elif reaction.emoji == '❎':
            if str(user.id) in haveBeenAsked:
                try:
                    asked_by = check_asked(user.id)
                    haveBeenAsked.remove(f"{user.id}")
                    askedByDB.delete_one({'haveBeenAsked': user.id})
                    await reaction.message.delete()
                    await reaction.message.channel.send(
                        f":broken_heart: | <@{asked_by}>, I'm sorry but {user.mention} said no...")

                except Exception:
                    await reaction.message.delete()
                    await reaction.message.channel.send(
                        f":sob: | I'm sorry but it looks like something went wrong, please try again...")

    @commands.command()
    async def leave(self, ctx, *args):
        if len(args) == 0:
            await ctx.send(
                f":broken_heart: | {ctx.author.mention}, use `s?leave confirm` to confirm leaving your marriage.")

        elif args[0] == "confirm":
            message = await ctx.send(f"<a:loading:802883106868428801> | {ctx.author.mention} loading data...")
            partner = check_partner(ctx.author.id)
            if partner != "0":
                await message.edit(content=f"<a:loading:802883106868428801> | Updating database please wait...")
                updates = {
                    "partner_id": int(0)
                }
                partners.update_one({'id': int(partner)}, {'$set': updates})
                updates = {
                    "partner_id": int(0)
                }
                partners.update_one({'id': ctx.author.id}, {'$set': updates})
                await message.delete()
                await ctx.send(
                    f":broken_heart: | {ctx.author.mention}, you have successfully left your marriage *sad violin "
                    f"noises*...")
            else:
                await message.edit(content=f":thinking: | {ctx.author.mention}, you are not in a marriage...")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def rose(self, ctx, member: discord.Member = None):
        if not member:
            embed = discord.Embed(title=f'{ctx.author.name}, who do you want to give a rose to? :pleading_face:',
                                  colour=discord.Colour.blue())
        else:
            embed = discord.Embed(title=f'{ctx.author.name} gives {member.name} a rose, how sweet! :rose:',
                                  colour=discord.Colour.blue())
            embed.set_image(url=random.choice(rose_gifs))
        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def chocolate(self, ctx, member: discord.Member = None):
        if not member:
            embed = discord.Embed(
                title=f'{ctx.author.name}, who do you want to give a a box of chocolate to? :pleading_face:',
                colour=discord.Colour.blue())
        else:
            embed = discord.Embed(
                title=f'{ctx.author.name} gives {member.name} a box of chocolate, how cute! '
                      '<:Adore:809121605540118538>',
                colour=discord.Colour.blue())
            embed.set_image(url=random.choice(chocolate_gids))
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        askedByDB.remove({})


def setup(client):
    client.add_cog(Marriage(client))
