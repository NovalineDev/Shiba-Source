import discord
from discord.ext import commands
import random
import aiohttp
import asyncio
import redditeasy
import urbanpython
import skingrabber
from skingrabber import skingrabber

facepalm_gif = "https://media.discordapp.net/attachments/755131015751532584/818192626108727296/bruh.gif"

urban = urbanpython.Urban("")

sg = skingrabber()

reddit_client_id = ''
reddit_client_secret = ''
reddit_user_agent = 'ShibaBot by AstroDev'


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def reply_test(self, ctx):
        await ctx.reply('Hello!')

    @commands.command()
    async def owo(self, ctx):
        await ctx.send("<:OwO:736586006597337182>")

    @commands.command(aliases=["8ball"])
    async def _8ball(self, ctx, *, ques):
        response = [
            "As I see it, yes.", "Without a doubt.", "Yes.", "It is certain.",
            "It is decidedly so.", "Most likely.", "Outlook good.",
            "Signs point to yes."
            "Don’t count on it.", "My reply is no.", "My sources say no.",
            "Outlook not so good."
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Reply hazy, try again.",
            "Very doubtful.",
        ]

        ans = random.choice(response)

        embed = discord.Embed(
            title="Shiba 8Ball",
            color=discord.Colour.blue()
        )
        embed.set_footer(
            text=f"Shiba",
            icon_url="https://media.discordapp.net/attachments/755131015751532584/823185561950879765/Shiba_PFP.png"
        )
        embed.set_thumbnail(
            url="https://media.discordapp.net/attachments/733379390196416663/736206921643589724/8ball.png"
        )
        embed.add_field(name=f"Question: {ques}", value=f"Answer: {ans}")
        await ctx.reply(embed=embed)

    @commands.command()
    async def flip(self, ctx):
        result = None
        value = random.randint(1, 2)
        if value == 1:
            result = "It's heads!"
        elif value == 2:
            result = "It's tails!"
        message = await ctx.reply("Flipping Coin..")
        await asyncio.sleep(0.5)
        await message.edit(content=f"{result}")

    @commands.command(aliases=["c"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cat(self, ctx):
        async with ctx.channel.typing():
            errors = 0
            post = redditeasy.Subreddit(subreddit="cats",  # Subreddit name
                                        client_id=reddit_client_id,  # Your client ID
                                        client_secret=reddit_client_secret,  # Your client secret
                                        user_agent=reddit_user_agent
                                        # Your user agent (ex: ClientName/0.1 by YourUsername")
                                        )
            while True:
                try:
                    postoutput = post.get_post()
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/cat/')
                    await ctx.reply(embed=embed)
                    break
                except Exception:
                    errors += 1
                    if errors == 10:
                        e = discord.Embed(
                            description=f"**You can report the error here:** [support server]("
                                        f"https://discord.gg/xc6xGCY)\n```py\nIt looks like something went wrong with "
                                        f"reddit... I've tried {errors} times.```",
                            color=0xff0000)
                        e.set_author(name='Command raised exception | Please try again',
                                     icon_url="https://i.imgur.com/OyDaCvd.png")
                        e.set_image(url=facepalm_gif)
                        e.set_footer(text=f"Command: {ctx.command}")
                        await ctx.reply(embed=e)
                        break

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dog(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title=":dog: Woof",
        )
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://random.dog/woof.json") as r:
                    data = await r.json()
                    embed.set_image(url=data['url'])
        embed.set_footer(text="https://random.dog/")
        await ctx.reply(embed=embed)

    @commands.command()
    async def owoify(self, ctx, *, text=None):
        if text is None:
            e = discord.Embed(description=f"Please include what you want to owoify in the command!",
                              color=0xff0000)
            e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
            e.set_footer(text=f"Command: {ctx.command.name}")
            await ctx.reply(embed=e)
        else:
            old = text
            text = text.replace("R", "W")
            text = text.replace("r", "w")
            text = text.replace("l", "w")
            text = text.replace("L", "W")
            text = text.replace("O", "U")

            embed = discord.Embed(
                title="<:100owo:808404681784557669> OWOifier 3000",
                description=text,
                colour=discord.Colour.blue()
            )
            embed.set_footer(text=f'Translated from "{old}"')
            await ctx.reply(embed=embed)

    @commands.command()
    async def enlarge(self, ctx, emoji: discord.PartialEmoji = None):
        if not emoji:
            e = discord.Embed(description=f"Please provide an emoji!",
                              color=0xff0000)
            e.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
            e.set_footer(text=f"Command: {ctx.command.name}")
            await ctx.reply(embed=e)
        else:
            await ctx.reply(emoji.url)

    @commands.command()
    async def respects(self, ctx):
        message = await ctx.reply("Press <:f_emoji:802527960523079711> to pay respects.")
        await message.add_reaction('<:f_emoji:802527960523079711>')

    @commands.command()
    async def iq(self, ctx, member: discord.Member = None):
        if not member:
            if ctx.author.id == 350325552344858624:  # Me (Arno)
                iq = "*I N F I N I T E*"
            elif ctx.author.id == 603635602809946113:  # Lunah
                iq = "h"
            elif ctx.author.id == 301731447046406145:  # Syubhr (Caleb)
                iq = "200"
            elif ctx.author.id == 686972977891508258:  # showman (VZ)
                iq = "0"
            else:
                iq = random.randint(15, 130)
            embed = discord.Embed(title='IQ Calculator', description=f"{ctx.author.name}'s IQ is **{iq}** :brain:",
                                  color=discord.Colour.blue())
        else:
            if member.id == 350325552344858624:  # Me (Arno)
                iq = "*I N F I N I T E*"
            elif member.id == 603635602809946113:  # Lunah
                iq = "h"
            elif member.id == 301731447046406145:  # Syubhr (Caleb)
                iq = "200"
            elif member.id == 686972977891508258:  # showman (VZ)
                iq = "0"
            else:
                iq = random.randint(15, 130)
            embed = discord.Embed(title='IQ Calculator', description=f"{member.name}'s IQ is **{iq}** :brain:",
                                  color=discord.Colour.blue())
        await ctx.reply(embed=embed)

    @commands.command()
    async def howgay(self, ctx, member: discord.Member = None):
        if not member:
            if ctx.author.id == 350325552344858624:  # Me (Arno)
                rate = "not "
            elif ctx.author.id == 301731447046406145:  # Syubhr (Caleb)
                rate = "no u "
            elif ctx.author.id == 707654800904290376:  # Syubhr (Caleb)
                rate = "not "
            else:
                rate = random.randint(1, 100)
            embed = discord.Embed(title='Gay Rate Calculator',
                                  description=f"{ctx.author.name} is **{rate}**% gay :gay_pride_flag:",
                                  color=discord.Colour.blue())
        else:
            if (
                    member.id == 350325552344858624
                    or member.id != 301731447046406145
                    and member.id == 707654800904290376
            ):
                rate = "not "
            elif member.id == 301731447046406145:
                rate = "no u "
            else:
                rate = random.randint(1, 100)
            embed = discord.Embed(title='Gay Rate Calculator',
                                  description=f"{member.name} is **{rate}**% gay :gay_pride_flag:",
                                  color=discord.Colour.blue())
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def urban(self, ctx, *args):
        if len(args[0]) == 0:
            async with ctx.channel.typing():
                embed = discord.Embed(description=f"Please provide something to urban!",
                                      color=0xff0000)
                embed.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                embed.set_footer(text=f"MissingRequiredArgument | Command: {ctx.command}")
        else:
            async with ctx.channel.typing():
                result = urban.search(' '.join(str(x) for x in args))
                embed = discord.Embed(title=f"Results for: {' '.join(str(x) for x in args)}",
                                      color=discord.Colour.blue())
                embed.add_field(name="Definition(s):", value=f"{result.definition}", inline=False)
                embed.add_field(name="Link:", value=f"[Click here]({result.permalink})", inline=True)
                embed.add_field(name="Author:", value=f"{result.author}", inline=True)
                embed.add_field(name="Thumbs up:", value=f"{result.thumbs_up}", inline=True)
                embed.add_field(name="Example(s):", value=f"{result.example}", inline=False)
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def skin(self, ctx, *args):
        if len(args) == 0:
            async with ctx.channel.typing():
                embed = discord.Embed(description=f"Please provide a username to fetch the skin from!",
                                      color=0xff0000)
                embed.set_author(name='Error', icon_url="https://i.imgur.com/OyDaCvd.png")
                embed.set_footer(text=f"MissingRequiredArgument | Command: {ctx.command}")
        else:
            async with ctx.channel.typing():
                skin = skingrabber().get_skin(user=args[0])
                skin_rendered = skingrabber().get_skin_rendered(user=args[0])
                uuid = skingrabber().get_uuid(args[0])
                embed = discord.Embed(title=f'Skin of: {args[0]}',
                                      color=discord.Colour.blue())
                embed.add_field(name="Download Link:", value=f"[Click here]({skin})", inline=True)
                embed.set_image(url=skin_rendered)
                embed.set_footer(text=f"{args[0]}'s UUID: {uuid}\nSkin API by Crafatar - https://crafatar.com/")
        await ctx.reply(embed=embed)

    @commands.command()
    async def mock(self, ctx, *, args):
        mock = ''.join(x + y for x, y in zip(args[0::2].upper(), args[1::2].lower()))
        await ctx.reply(mock, file=discord.File('assets/mock.gif'))
        

def setup(client):
    client.add_cog(Fun(client))
