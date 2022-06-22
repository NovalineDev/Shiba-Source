import discord
from discord.ext import commands

import time


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title='Invites:', color=discord.Colour.blue())
        embed.add_field(name=":link: Shiba:",
                        value="[Shiba Invite!](https://discord.com/api/oauth2/authorize?client_id=718769183885754380&permissions=8&scope=bot%20applications.commands)",
                        inline=True)
        await ctx.reply(embed=embed)

    @commands.command(pass_context=True)
    async def servers(self, ctx):
        embed = discord.Embed(title="I'm in " + str(len(self.client.guilds)) + " servers", color=discord.Colour.blue())
        await ctx.reply(embed=embed)

    @commands.command()
    async def info(self, ctx):
        newline = "\n"
        dev1 = [str(self.client.get_user(603635602809946113)).replace("None", "Lunah#3131"),
                str(self.client.get_user(350325552344858624)).replace("None", "Vuiizx#6969")]
        embed = discord.Embed(title='Shiba Info:', color=discord.Colour.blue())
        embed.add_field(name="<:developer:736208652851085382> Developers:",
                        value=f"{newline.join(dev1)}", inline=True)
        embed.add_field(name=":link: Links:",
                        value='[Shiba Invite](https://discord.com/api/oauth2/authorize?client_id=718769183885754380&permissions=8&scope=bot%20applications.commands)\n[Vote](https://top.gg/bot/718769183885754380/vote)\n['
                              'Support](https://discord.gg/xc6xGCY)')
        embed.add_field(name=":bar_chart: Stats",
                        value=f"Server count: {(len(self.client.guilds))}\nPing: {round(self.client.latency * 1000)}ms"
                              f"\nTotal members: {len(self.client.users)}\nTotal commands: "
                              f"{(len(self.client.commands))}")

        await ctx.reply(embed=embed)

    @commands.command()
    async def credits(self, ctx):
        newline = "\n"
        dev1 = [str(self.client.get_user(603635602809946113)).replace("None", "Lunah#3131"),
                str(self.client.get_user(350325552344858624)).replace("None", "Vuiizx#6969")]
        embed = discord.Embed(title='Shiba Credits:', color=discord.Colour.blue())
        embed.add_field(name="<:developer:736208652851085382> Developers:",
                        value=f"{newline.join(dev1)}", inline=True)
        embed.add_field(name=":desktop: Library:",
                        value='discord.py (python)')
        thanks2 = str(self.client.get_user(519417425993924618)).replace("None", "FourTOne5#8922")
        thanks3 = str(self.client.get_user(707654800904290376)).replace("None", "xX_Jay_Xx#0001")
        thanks4 = str(self.client.get_user(301731447046406145)).replace("None", "Syubhr#3220")
        thanks6 = str(self.client.get_user(444550944110149633)).replace("None", "MakufonSkifto#1414")
        thanks7 = str(self.client.get_user(429935667737264139)).replace("None", "IAmAHuman#6359")
        thanks9 = str(self.client.get_user(603635602809946113)).replace("None", "Lunah#3131")
        embed.add_field(name=":star: Special thanks:",
                        value=f"{thanks2}\n{thanks3}\n{thanks4}\n{thanks6}\n{thanks7}\n{thanks9}")
        embed.add_field(name=":heart: Note:",
                        value='And of course I cannot forget all the amazing people that have supported Shiba by '
                              'inviting her <3')
        await ctx.reply(embed=embed)

    @commands.command()
    async def vote(self, ctx):
        embed = discord.Embed(title='Vote:', color=discord.Colour.blue())
        embed.add_field(name=":link: You can vote once every 12 hours using this link:",
                        value="[Click here!](https://top.gg/bot/718769183885754380/vote)", inline=True)
        await ctx.reply(embed=embed)

    @commands.command()
    async def support(self, ctx):
        await ctx.reply(":white_check_mark: You can join our official support server here: https://discord.gg/xc6xGCY")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        async with ctx.channel.typing():
            t1 = time.perf_counter()
            await ctx.trigger_typing()
            t2 = time.perf_counter()
            res = round((t2 - t1) * 1000)
        await ctx.reply(embed=discord.Embed(title=":ping_pong: Pong!",
                                            description=f":white_small_square: Bot Latency: "
                                                        f"**{round(self.client.latency * 1000)}**ms\n"
                                                        f":white_small_square: API Latency: **{res}**ms",
                                            colour=discord.Colour.blue()))


def setup(client):
    client.add_cog(Info(client))
