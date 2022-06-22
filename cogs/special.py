import discord
from discord.ext import commands
import datetime
import asyncio


# The frames
async def get_frame(number):
    with open(f'frames/frame-{number}.txt', 'r') as f:
        return f.read()


class Special(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def newyear(self, ctx):
        await ctx.reply(f"Check your dms {ctx.author.name}! [This command was for **1 January 2021**]")
        message1 = await ctx.author.send("Starting in 10 seconds...")

        for i in range(9, 1, -1):
            await asyncio.sleep(1)
            await message1.edit(content=f"Starting in {i} seconds...")

        await asyncio.sleep(1)
        await message1.edit(content="Starting in 1 second... Enjoy :3")
        await asyncio.sleep(1)
        await message1.delete()

        message = await ctx.author.send(await get_frame(1))

        for i in range(2, 39):
            await asyncio.sleep(0.5)
            await message.edit(content=await get_frame(i))

        await message.edit(content="**Best wishes for 2021 - The Shiba Dev Team <3**")
    
    @commands.command()
    async def gift(self, ctx):
        await ctx.reply(f"Check your dms {ctx.author.name}! [This command was for **25 Decemeber 2020**]")
        embed = discord.Embed(title='Here is your gift:', color=discord.Colour.blue())
        embed.set_image(url="https://images.unsplash.com/photo-1549465220-1a8b9238cd48?ixlib=rb-1.2.1&ixid"
                            "=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1324&q=80")
        embed.set_footer(text='Note from the Developers: we would like to thank you all for being a part of this '
                              'amazing journey and helping us to acheve what we have today ♥♥♥')
        await ctx.author.send(embed=embed)


def setup(client):
    client.add_cog(Special(client))
