import discord
from discord.ext import commands
from pymongo import MongoClient
import json
import datetime

dbclient = MongoClient(
    "")
discorddb = dbclient.get_database('discord')
prefixes = discorddb.prefix


def prefix_grabber(id):
    var = prefixes.find_one({"id": id}, {"_id": False})
    var1 = str(var).replace("'", '"')
    prefix_json = json.loads(var1)
    return str(prefix_json[str("prefix")])


class Other(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(aliases=["help"])
    async def _help(self, ctx):
        if ctx.invoked_subcommand is None or ctx.subcommand_passed is None:
            prefix = prefix_grabber(ctx.guild.id)
            embed = discord.Embed(title='Please specify a page.', color=discord.Colour.blue())
            embed.add_field(name=f":tools: {prefix}help mod", value="```Get a list of the moderation commands.```",
                            inline=True)
            embed.add_field(name=f":joy: {prefix}help fun", value="```Get a list of the fun commands.```", inline=True)
            embed.add_field(name=f"<:reddit:802510404570972161> {prefix}help reddit",
                            value="```Get a list of the reddit commands.```", inline=True)
            embed.add_field(name=f":revolving_hearts: {prefix}help marriage",
                            value="```Get a list of the marriage commands.```",
                            inline=True)
            embed.add_field(name=f":grey_question: {prefix}help info", value="```Get a list of the info commands.```",
                            inline=True)
            embed.add_field(name=f":hugging: {prefix}help roleplay", value="```Get a list of the roleplay commands.```",
                            inline=True)
            embed.add_field(name=f":wrench: {prefix}help settings", value="```Get a list of the server settings.```",
                            inline=True)
            embed.add_field(name=f":underage: {prefix}help nsfw", value="```Get a list of the nsfw commands.```",
                            inline=True)
            embed.add_field(name=f":gift: {prefix}help special", value="```Get a list of the special commands.```",
                            inline=True)
            if ctx.author.id in self.client.owner_ids:
                embed.add_field(name=f"<:developer:736208652851085382> {prefix}help dev",
                                value="```Get a list of developer commands.```",
                                inline=True)
            embed.add_field(name=":white_check_mark: Join our official support server here:",
                            value="https://discord.gg/xc6xGCY", inline=False)
            await ctx.reply(embed=embed)

    @_help.command()
    async def mod(self, ctx):
        prefix = prefix_grabber(ctx.guild.id)
        embed = discord.Embed(title=':tools: Moderation Commands:', color=discord.Colour.blue())
        embed.add_field(name=f"{prefix}clear [amount]", value="```Clear a given amount of messages.```", inline=True)
        embed.add_field(name=f"{prefix}say [message]",
                        value="```Make the bot say a given message.```",
                        inline=True)
        embed.add_field(name=f"{prefix}userinfo @member",
                        value="```Make the bot give a list of info about a member.```",
                        inline=True)
        embed.add_field(name=f"{prefix}kick @member [reason]",
                        value="```Make the bot kick a member for a given reason.```",
                        inline=True)
        embed.add_field(name=f"{prefix}ban @member [reason]",
                        value="```Make the bot ban a member for a given reason.```",
                        inline=True)
        embed.add_field(name=f"{prefix}id @member", value="```Get a users id.```", inline=True)
        embed.add_field(name=f"{prefix}snipe", value="```Snipe a deleted message.```", inline=True)
        embed.add_field(name=f"{prefix}editsnipe", value="```Editsnipe a deleted message.```", inline=True)
        await ctx.reply(embed=embed)

    @_help.command()
    async def fun(self, ctx):
        prefix = prefix_grabber(ctx.guild.id)
        embed = discord.Embed(title=':joy: Fun Commands:', color=discord.Colour.blue())
        embed.add_field(name=f"{prefix}flip", value="```Flip a coin.```", inline=True)
        embed.add_field(name=f"{prefix}8ball [question]", value="```Ask the 8ball a question.```", inline=True)
        embed.add_field(name=f"{prefix}cat", value="```Kittens!```", inline=True)
        embed.add_field(name=f"{prefix}dog", value="```Doggos!```", inline=True)
        embed.add_field(name=f"{prefix}mock [text]", value="```Make Shiba mock at something.```", inline=True)
        embed.add_field(name=f"{prefix}enlarge [emoji]", value="```Enlarge an emoji.```", inline=True)
        embed.add_field(name=f"{prefix}respects", value="```Pay some respects.```", inline=True)
        embed.add_field(name=f"{prefix}owoify", value="```OwOify something.```", inline=True)
        embed.add_field(name=f"{prefix}owo", value="```OwO```", inline=True)
        embed.add_field(name=f"{prefix}iq @member", value="```Calculate someone's iq.```", inline=True)
        embed.add_field(name=f"{prefix}howgay @member", value="```Calculate how gay someone is.```", inline=True)
        embed.add_field(name=f"{prefix}urban [word]", value="```Search for the definition of a word.```", inline=True)
        embed.add_field(name=f"{prefix}skin [username]", value="```Grab the skin of any Minecraft player!```",
                        inline=True)
        await ctx.reply(embed=embed)

    @_help.command()
    async def reddit(self, ctx):
        prefix = prefix_grabber(ctx.guild.id)
        embed = discord.Embed(title='<:reddit:802510404570972161> Reddit Commands:', color=discord.Colour.blue())
        embed.add_field(name=f"{prefix}meme", value="```Get a random reddit meme.```", inline=True)
        embed.add_field(name=f"{prefix}shiba", value="```Shiba's!```", inline=True)
        embed.add_field(name=f"{prefix}ihadastroke", value="```Get a random post from r/ihadastroke.```", inline=True)
        embed.add_field(name=f"{prefix}clouds", value="```Get a random post from r/clouds.```", inline=True)
        embed.add_field(name=f"{prefix}backgrounds", value="```Get a random post from r/backgrounds.```", inline=True)
        embed.add_field(name=f"{prefix}starterpacks", value="```Get a random post from r/starterpacks.```", inline=True)
        embed.add_field(name=f"{prefix}programmerhumor", value="```Get a random post from r/programmerhumor.```",
                        inline=True)
        embed.add_field(name=f"{prefix}masterhacker", value="```Get a random post from r/masterhacker.```", inline=True)
        await ctx.reply(embed=embed)

    @_help.command(aliases=["info"])
    async def _info(self, ctx):
        prefix = prefix_grabber(ctx.guild.id)
        embed = discord.Embed(title=':grey_question: Info Commands:', color=discord.Colour.blue())
        embed.add_field(name=f"{prefix}credits",
                        value="```Get a list of all the amazing people that have helped Shiba!```", inline=True)
        embed.add_field(name=f"{prefix}info", value="```Find all the info about the bot.```", inline=True)
        embed.add_field(name=f"{prefix}servers", value="```Check in how many servers the bot is added.```", inline=True)
        embed.add_field(name=f"{prefix}invite", value="```Get the bot's invite link.```", inline=True)
        embed.add_field(name=f"{prefix}vote", value="```Get the bot's vote link.```", inline=True)
        embed.add_field(name=f"{prefix}ping", value="```Get the bot's latency.```", inline=True)
        embed.add_field(name=f"{prefix}support", value="```Get an invite into the support server.```", inline=True)
        await ctx.reply(embed=embed)

    @_help.command()
    async def roleplay(self, ctx):
        prefix = prefix_grabber(ctx.guild.id)
        embed = discord.Embed(title=':hugging: Roleplay Commands:', color=discord.Colour.blue())
        embed.add_field(name=f"{prefix}bite @member", value="```Bite someone.```", inline=True)
        embed.add_field(name=f"{prefix}blush", value="```Blush.```", inline=True)
        embed.add_field(name=f"{prefix}bonk @member", value="```Bonk someone.```", inline=True)
        embed.add_field(name=f"{prefix}clap", value="```Clap.```", inline=True)
        embed.add_field(name=f"{prefix}confused", value="```Express your confusion.```", inline=True)
        embed.add_field(name=f"{prefix}cry", value="```Cry.```", inline=True)
        embed.add_field(name=f"{prefix}chocolate @user", value="```Give someone a box of chocolate! :3```", inline=True)
        embed.add_field(name=f"{prefix}cuddle @member", value="```Cuddle with someone.```", inline=True)
        embed.add_field(name=f"{prefix}dance", value="```Dance.```", inline=True)
        embed.add_field(name=f"{prefix}die", value="```Die.```", inline=True)
        embed.add_field(name=f"{prefix}facepalm", value="```Facepalm.```", inline=True)
        embed.add_field(name=f"{prefix}glare", value="```Glare.```", inline=True)
        embed.add_field(name=f"{prefix}greet", value="```Greet.```", inline=True)
        embed.add_field(name=f"{prefix}highfive @member", value="```Highfive someone.```", inline=True)
        embed.add_field(name=f"{prefix}hug @member", value="```Hug someone.```", inline=True)
        embed.add_field(name=f"{prefix}kiss @member", value="```Kiss someone.```", inline=True)
        embed.add_field(name=f"{prefix}laugh", value="```Laugh.```", inline=True)
        embed.add_field(name=f"{prefix}lick @member", value="```Lick someone.```", inline=True)
        embed.add_field(name=f"{prefix}pat @member", value="```Pat someone.```", inline=True)
        embed.add_field(name=f"{prefix}poke @memner", value="```Poke someone.```", inline=True)
        embed.add_field(name=f"{prefix}pout", value="```Pout.```", inline=True)
        embed.add_field(name=f"{prefix}punch @member", value="```Punch someone.```", inline=True)
        embed.add_field(name=f"{prefix}purr @member", value="```Purr at someone.```", inline=True)
        embed.add_field(name=f"{prefix}run", value="```Run out of there.```", inline=True)
        embed.add_field(name=f"{prefix}sad", value="```Makes you sad.```", inline=True)
        embed.add_field(name=f"{prefix}shoot @member", value="```Shoot someone.```", inline=True)
        embed.add_field(name=f"{prefix}shrug", value="```Shrug.```", inline=True)
        embed.add_field(name=f"{prefix}shy", value="```Become shy.```", inline=True)
        embed.add_field(name=f"{prefix}slap @member", value="```Slap someone.```", inline=True)
        embed.add_field(name=f"{prefix}poke @memner", value="```Poke someone.```", inline=True)
        embed.add_field(name=f"{prefix}smile", value="```Smile.```", inline=True)
        embed.add_field(name=f"{prefix}stare @member", value="```Stare at someone.```", inline=True)
        embed.add_field(name=f"{prefix}stomp @member", value="```Stomp someone.```", inline=True)
        embed.add_field(name=f"{prefix}wag", value="```Wag.```", inline=True)
        embed.add_field(name=f"{prefix}wiggle", value="```Wiggle.```", inline=True)
        embed.add_field(name=f"{prefix}rose @user", value="```Give someone a rose! :D```", inline=True)
        await ctx.reply(embed=embed)

    @_help.command()
    async def settings(self, ctx):
        prefix = prefix_grabber(ctx.guild.id)
        embed = discord.Embed(title=':wrench: Server Settings:', color=discord.Colour.blue())
        embed.add_field(name=f"{prefix}changeprefix [prefix]", value="```Change Shiba's prefix.```", inline=True)
        await ctx.reply(embed=embed)

    @_help.command()
    async def nsfw(self, ctx):
        prefix = prefix_grabber(ctx.guild.id)
        embed = discord.Embed(title=':underage: Nsfw Commands:', color=discord.Colour.blue())
        embed.add_field(name=f"{prefix}ass", value="```Gives you a random post from r/ass.```", inline=True)
        embed.add_field(name=f"{prefix}boobs", value="```Gives you a random post from r/boobs.```", inline=True)
        embed.add_field(name=f"{prefix}nsfw", value="```Gives you a random post from r/nsfw.```", inline=True)
        embed.add_field(name=f"{prefix}porngif", value="```Gives you a random post from r/porngif.```", inline=True)
        embed.add_field(name=f"{prefix}hentai", value="```Gives you a random post from r/hentai.```", inline=True)
        embed.add_field(name=f"{prefix}yuri", value="```Gives you a random post from r/yuri.```", inline=True)
        embed.add_field(name=f"{prefix}ecchi", value="```Gives you a random post from r/ecchi.```", inline=True)
        embed.add_field(name=f"{prefix}zerotwo", value="```Gives you a random post from r/zerotwo.```", inline=True)
        embed.add_field(name=f"{prefix}hayasaka", value="```Gives you a random post from r/hayasaka.```", inline=True)
        embed.add_field(name=f"{prefix}ichigo", value="```Gives you a random post from r/onetrueichigo.```",
                        inline=True)
        embed.add_field(name=f"{prefix}waifu", value="```Gives you a random post from r/waifu.```", inline=True)
        embed.add_field(name=f"{prefix}waifus", value="```Gives you a random post from r/waifus.```", inline=True)
        await ctx.reply(embed=embed)

    @_help.command()
    async def marriage(self, ctx):
        prefix = prefix_grabber(ctx.guild.id)
        embed = discord.Embed(title=':revolving_hearts: Marriage Commands:', color=discord.Colour.blue())
        embed.add_field(name=f"{prefix}marriage", value="```Shows you who your fiancé is.```", inline=True)
        embed.add_field(name=f"{prefix}marry @user", value="```Ask someone if they want to be your fiancé.```",
                        inline=True)
        embed.add_field(name=f"{prefix}leave", value="```Leave your fiancé... Don't...```", inline=True)
        await ctx.reply(embed=embed)

    @_help.command()
    async def special(self, ctx):
        prefix = prefix_grabber(ctx.guild.id)
        embed = discord.Embed(title=':gift: Special Commands:', color=discord.Colour.blue())
        embed.add_field(name=f"{prefix}gift", value="```Special gift command from 25 December 2020.```", inline=True)
        embed.add_field(name=f"{prefix}newyear", value="```Special new year command from 1 January 2021.```",
                        inline=True)
        await ctx.reply(embed=embed)

    @_help.command()
    async def dev(self, ctx):
        prefix = prefix_grabber(ctx.guild.id)
        if ctx.author.id in self.client.owner_ids:
            embed = discord.Embed(title='<:developer:736208652851085382> Developer Commands:',
                                  color=discord.Colour.blue())
            embed.add_field(name="Only Developers can use these.", value="```Yeah lol```", inline=True)
            embed.add_field(name=f"{prefix}dm @member [message]", value="```Dm a given member a given message.```",
                            inline=True)
            embed.add_field(name=f"{prefix}dev_only", value="```Just some dev info.```", inline=True)
            embed.add_field(name=f"{prefix}sudo help", value="```Get help about all the sudo commands.```", inline=True)
            await ctx.reply(embed=embed)
        else:
            e = discord.Embed(description="Help page not found.", color=0xff0000)
            e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
            await ctx.reply(embed=e)

    @commands.command()
    async def the(self, ctx, *args):
        if args[0] == "war":
            embed = discord.Embed(title='the war', color=discord.Colour.blue())
            await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Other(client))
