from discord.ext import commands
import random
import discord
import requests
import json

bonk_gifs = ["https://media1.tenor.com/images/a60518ab2154d61e99251b11ec52f65c/tenor.gif?itemid=17402810",
             "https://cdn.discordapp.com/attachments/747486937539149936/801849216053805176/image0.gif",
             "https://media1.tenor.com/images/dc4329d27745a6707219cb658f5b2c46/tenor.gif?itemid=18191826",
             "https://media1.tenor.com/images/544fecdfc2d904cf9b1e36994d3a007d/tenor.gif?itemid=19740955",
             "https://media1.tenor.com/images/778f74d0b677ce017a8b618fdf494df6/tenor.gif?itemid=19187992"]

tenor_apikey = ""


class Roleplay(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Hug Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hug(self, ctx, member: discord.Member = None):
        search_term = "anime hugs"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        if not member:
            embed = discord.Embed(title=f'{ctx.author.name} hugs Shiba!',
                                  colour=discord.Colour.blue())
        else:
            embed = discord.Embed(title=f'{ctx.author.name} hugs {member.name}!',
                                  colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Kiss Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kiss(self, ctx, member: discord.Member = None):
        search_term = "anime kiss"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        if not member:
            embed = discord.Embed(title=f'{ctx.author.name} please mention someone to kiss.',
                                  colour=discord.Colour.blue())
        else:
            embed = discord.Embed(title=f'{ctx.author.name} kisses {member.name}!',
                                  colour=discord.Colour.blue())
            embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Cuddle Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cuddle(self, ctx, member: discord.Member = None):
        search_term = "anime cuddles"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        if not member:
            embed = discord.Embed(title=f'{ctx.author.name} please mention someone to cuddle.',
                                  colour=discord.Colour.blue())
        else:
            embed = discord.Embed(title=f'{ctx.author.name} cuddles {member.name}!',
                                  colour=discord.Colour.blue())
            embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Lick Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lick(self, ctx, member: discord.Member = None):
        search_term = "anime lick"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        if not member:
            embed = discord.Embed(title=f'{ctx.author.name} please mention someone to lick.',
                                  colour=discord.Colour.blue())
        else:
            embed = discord.Embed(title=f'{ctx.author.name} licks {member.name}!',
                                  colour=discord.Colour.blue())
            embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Pat Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pat(self, ctx, member: discord.Member = None):
        search_term = "anime pat"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        if not member:
            embed = discord.Embed(title=f'{ctx.author.name} pats Shiba!',
                                  colour=discord.Colour.blue())
        else:
            embed = discord.Embed(title=f'{ctx.author.name} pats {member.name}!',
                                  colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Shoot Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def shoot(self, ctx, member: discord.Member = None):
        search_term = "anime shoot"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        if not member:
            embed = discord.Embed(title=f'{ctx.author.name} please mention someone to shoot :smiling_imp:',
                                  colour=discord.Colour.blue())
        else:
            embed = discord.Embed(title=f'{ctx.author.name} shoots {member.name}! :smiling_imp:',
                                  colour=discord.Colour.blue())
            embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Bite Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bite(self, ctx, member: discord.Member = None):
        search_term = "anime bite"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        if not member:
            embed = discord.Embed(title=f'{ctx.author.name} please mention someone to bite.',
                                  colour=discord.Colour.blue())
        else:
            embed = discord.Embed(title=f'{ctx.author.name} bites {member.name}!', colour=discord.Colour.blue())
            embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Clap Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clap(self, ctx):
        search_term = "anime clap"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} claps!', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Cry Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cry(self, ctx):
        search_term = "anime cry"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} cries... :c', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Dance Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dance(self, ctx):
        search_term = "anime dance"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} dances!', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Die Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def die(self, ctx):
        embed = discord.Embed(title=f'{ctx.author.name} dies :c', colour=discord.Colour.blue())
        embed.set_image(url="https://media.discordapp.net/attachments/705473716955512963/774298267545763867/tenor.gif")
        await ctx.send(embed=embed)

    # Facepalm Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def facepalm(self, ctx):
        search_term = "anime facepalm"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} facepalms...', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Glare Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def glare(self, ctx):
        search_term = "anime glare"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} glares', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Greet Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def greet(self, ctx):
        search_term = "anime greet"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} greets!', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Highfive Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def highfive(self, ctx, member: discord.Member = None):
        search_term = "anime highfive"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        if not member:
            embed = discord.Embed(title=f'{ctx.author.name} highfives!',
                                  colour=discord.Colour.blue())
        else:
            embed = discord.Embed(title=f'{ctx.author.name} highfives {member.name}!', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Laugh Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def laugh(self, ctx):
        search_term = "anime laugh"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} laughs!', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Poke Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def poke(self, ctx, member: discord.Member = None):
        search_term = "anime poke"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        if not member:
            embed = discord.Embed(title=f'{ctx.author.name} please mention someone to poke!',
                                  colour=discord.Colour.blue())
        else:
            embed = discord.Embed(title=f'{ctx.author.name} pokes {member.name}!', colour=discord.Colour.blue())
            embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Pout Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pout(self, ctx):
        search_term = "anime pout"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} pouts...', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Punch Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def punch(self, ctx, member: discord.Member = None):
        search_term = "anime punch"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        if not member:
            embed = discord.Embed(title=f'{ctx.author.name} please mention someone to punch!',
                                  colour=discord.Colour.blue())
        else:
            embed = discord.Embed(title=f'{ctx.author.name} punch {member.name}!', colour=discord.Colour.blue())
            embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Purr Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def purr(self, ctx, member: discord.Member = None):
        if not member:
            embed = discord.Embed(title=f'{ctx.author.name} please mention someone to purr at!',
                                  colour=discord.Colour.blue())
        else:
            embed = discord.Embed(title=f'{ctx.author.name} purrs at {member.name}!', colour=discord.Colour.blue())
            embed.set_image(
                url="https://media.discordapp.net/attachments/705473716955512963/774308215227285534/tenor.gif")
        await ctx.send(embed=embed)

    # Run Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def run(self, ctx):
        search_term = "anime run"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} runs away... aaaaa', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Sad Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sad(self, ctx):
        search_term = "anime sad"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} is sad... :c', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Shrug Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def shrug(self, ctx):
        search_term = "anime shrug"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} shrugs', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Shy Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def shy(self, ctx):
        search_term = "anime shy"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} is shy OvO', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Slap Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slap(self, ctx, member: discord.Member = None):
        search_term = "anime slap"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        if not member:
            embed = discord.Embed(title=f'{ctx.author.name} please mention someone to slap!',
                                  colour=discord.Colour.blue())
        else:
            embed = discord.Embed(title=f'{ctx.author.name} slaps {member.name}!', colour=discord.Colour.blue())
            embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Smile Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def smile(self, ctx):
        search_term = "anime smile"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} smiles', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Stare Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def stare(self, ctx, member: discord.Member = None):
        search_term = "anime stare"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        if not member:
            embed = discord.Embed(title=f'{ctx.author.name} please mention someone to stare at.',
                                  colour=discord.Colour.blue())
        else:
            embed = discord.Embed(title=f'{ctx.author.name} stares at {member.name} :eyes:',
                                  colour=discord.Colour.blue())
            embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Stomp Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def stomp(self, ctx, member: discord.Member = None):
        search_term = "anime stomp"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        if not member:
            embed = discord.Embed(title=f'{ctx.author.name} please mention someone to stomp.',
                                  colour=discord.Colour.blue())
        else:
            embed = discord.Embed(title=f'{ctx.author.name} stomps {member.name} o-o', colour=discord.Colour.blue())
            embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Wag Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wag(self, ctx):
        search_term = "anime wag"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} wags :D', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Wiggle Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def wiggle(self, ctx):
        search_term = "anime wiggle"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} wiggles O.o', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Blush Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def blush(self, ctx):
        search_term = "anime blush"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} blushes~ how cute', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Confused Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def confused(self, ctx):
        search_term = "anime confused"
        r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, tenor_apikey, "1"))

        gifs = json.loads(r.content) if r.status_code == 200 else None
        embed = discord.Embed(title=f'{ctx.author.name} is confused O.o', colour=discord.Colour.blue())
        embed.set_image(url=gifs["results"][0]["media"][0]["mediumgif"]["url"])
        await ctx.send(embed=embed)

    # Bonk Command
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bonk(self, ctx, member: discord.Member = None):
        gif = random.choice(bonk_gifs)
        if not member:
            embed = discord.Embed(title=f'{ctx.author.name}, who we bonking?', colour=discord.Colour.blue())
        else:
            embed = discord.Embed(title=f'{ctx.author.name} bonks {member.name} <a:bonkcat:801872305469915177>',
                                  colour=discord.Colour.blue())
            embed.set_image(url=gif)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Roleplay(client))
