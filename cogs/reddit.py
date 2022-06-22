import discord
from discord.ext import tasks, commands

import random
import asyncio

import redditeasy

reddit_client_id = ''
reddit_client_secret = ''
reddit_user_agent = 'ShibaBot by AstroDev'

facepalm_gif = "https://media.discordapp.net/attachments/755131015751532584/818192626108727296/bruh.gif"


class Reddit(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def meme(self, ctx):
        async with ctx.channel.typing():
            errors = 0
            post = redditeasy.Subreddit()
            while True:
                try:
                    postoutput = post.get_post(subreddit="memes")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/memes/')
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
    async def shiba(self, ctx):
        errors = 0
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            while True:
                try:
                    postoutput = post.get_post(subreddit="shiba")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/shiba/')
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
    async def ihadastroke(self, ctx):
        errors = 0
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            while True:
                try:
                    postoutput = post.get_post(subreddit="ihadastroke")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/ihadastroke/')
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
    async def clouds(self, ctx):
        errors = 0
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            while True:
                try:
                    postoutput = post.get_post(subreddit="clouds")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/clouds/')
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
    async def backgrounds(self, ctx):
        errors = 0
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            while True:
                try:
                    postoutput = post.get_post(subreddit="backgrounds")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/backgrounds/')
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
    async def masterhacker(self, ctx):
        errors = 0
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            while True:
                try:
                    postoutput = post.get_post(subreddit="masterhacker")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/masterhacker/')
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
    async def starterpacks(self, ctx):
        errors = 0
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            while True:
                try:
                    postoutput = post.get_post(subreddit="starterpacks")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/starterpacks/')
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
    async def programmerhumor(self, ctx):
        errors = 0
        async with ctx.channel.typing():
            post = redditeasy.Subreddit()
            while True:
                try:
                    postoutput = post.get_post(subreddit="programmerhumor")
                    embed = discord.Embed(title=f'**{postoutput.title}**',
                                          color=discord.Colour.blue())
                    embed.add_field(name="Link:", value=f"[Click here]({postoutput.post_url})", inline=True)
                    embed.add_field(name="Author:", value=f"u/{postoutput.author}", inline=True)
                    embed.add_field(name="Upvotes:", value=f"{postoutput.score}", inline=True)
                    embed.set_image(url=postoutput.content)
                    embed.set_footer(text='www.reddit.com/r/programmerhumor/')
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


def setup(client):
    client.add_cog(Reddit(client))
