import discord
from discord.ext import commands
import redditeasy

reddit_client_id = ''
reddit_client_secret = ''
reddit_user_agent = 'ShibaBot by AstroDev'

facepalm_gif = "https://media.discordapp.net/attachments/755131015751532584/818192626108727296/bruh.gif"


class Nsfw(commands.Cog):
    @commands.command()
    @commands.is_nsfw()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ass(self, ctx):
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            errors = 0
            while True:
                try:
                    postoutput = post.get_post(subreddit="ass")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/ass/')
                    await ctx.reply(embed=embed)
                    break
                except Exception:
                    async with ctx.channel.typing():
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
    @commands.is_nsfw()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def boobs(self, ctx):
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            errors = 0
            while True:
                try:
                    postoutput = post.get_post(subreddit="boobs")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/boobs/')
                    await ctx.reply(embed=embed)
                    break
                except Exception:
                    async with ctx.channel.typing():
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
    @commands.is_nsfw()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def nsfw(self, ctx):
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            errors = 0
            while True:
                try:
                    postoutput = post.get_post(subreddit="nsfw")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/nsfw/')
                    await ctx.reply(embed=embed)
                    break
                except Exception:
                    async with ctx.channel.typing():
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
    @commands.is_nsfw()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def porngif(self, ctx):
        post = redditeasy.Subreddit()
        errors = 0
        while True:
            try:
                postoutput = post.get_post(subreddit="porngif")
                embed = discord.Embed(title=f'**{postoutput.title}**',
                                      color=discord.Colour.blue())
                embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                embed.set_image(url=postoutput.content)
                embed.set_footer(text='www.reddit.com/r/porngif/')
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
    @commands.is_nsfw()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hentai(self, ctx):
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            errors = 0
            while True:
                try:
                    postoutput = post.get_post(subreddit="hentai")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/hentai/')
                    await ctx.reply(embed=embed)
                    break
                except Exception:
                    async with ctx.channel.typing():
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
    @commands.is_nsfw()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def yuri(self, ctx):
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            errors = 0
            while True:
                try:
                    postoutput = post.get_post(subreddit="yuri")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/yuri/')
                    await ctx.reply(embed=embed)
                    break
                except Exception:
                    async with ctx.channel.typing():
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
    @commands.is_nsfw()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ecchi(self, ctx):
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            errors = 0
            while True:
                try:
                    postoutput = post.get_post(subreddit="ecchi")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/ecchi/')
                    await ctx.reply(embed=embed)
                    break
                except Exception:
                    async with ctx.channel.typing():
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
    @commands.is_nsfw()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def zerotwo(self, ctx):
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            errors = 0
            while True:
                try:
                    postoutput = post.get_post(subreddit="zerotwo")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/zerotwo/')
                    await ctx.reply(embed=embed)
                    break
                except Exception:
                    async with ctx.channel.typing():
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
    @commands.is_nsfw()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hayasaka(self, ctx):
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            errors = 0
            while True:
                try:
                    postoutput = post.get_post(subreddit="hayasaka")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/hayasaka/')
                    await ctx.reply(embed=embed)
                    break
                except Exception:
                    async with ctx.channel.typing():
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
    @commands.is_nsfw()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ichigo(self, ctx):
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            errors = 0
            while True:
                try:
                    postoutput = post.get_post(subreddit="onetrueichigo")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/hayasaka/')
                    await ctx.reply(embed=embed)
                    break
                except Exception:
                    async with ctx.channel.typing():
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
    @commands.is_nsfw()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def waifu(self, ctx):
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            errors = 0
            while True:
                try:
                    postoutput = post.get_post(subreddit="waifu")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/waifu/')
                    await ctx.reply(embed=embed)
                    break
                except Exception:
                    async with ctx.channel.typing():
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
    @commands.is_nsfw()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def waifus(self, ctx):
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            errors = 0
            while True:
                try:
                    postoutput = post.get_post(subreddit="waifus")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/waifus/')
                    await ctx.reply(embed=embed)
                    break
                except Exception:
                    async with ctx.channel.typing():
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


def setup(client):
    client.add_cog(Nsfw(client))
