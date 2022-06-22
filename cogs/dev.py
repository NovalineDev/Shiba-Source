import discord
from discord.ext import commands
from functions import *
import platform
import psutil
from hurry.filesize import size
import os
import sys


class Dev(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dm(self, ctx, member: discord.Member, *, msg=''):
        if str(ctx.author.id) in devs:
            await ctx.channel.purge(limit=1)
            await member.send(msg)
            await ctx.author.send('Dm successful.')

    @commands.is_owner()
    @commands.group()
    async def sudo(self, ctx):
        if ctx.subcommand_passed is None:
            command = self.client.get_command("sudo help")
            await ctx.invoke(command)
        elif ctx.invoked_subcommand is None:
            await ctx.message.add_reaction("❌")

    @sudo.command()
    async def help(self, ctx):
        prefix = prefix_grabber(ctx.guild.id)
        embed = discord.Embed(title='<:developer:736208652851085382> Sudo Commands:',
                              color=discord.Colour.blue())
        embed.add_field(name=f"{prefix}sudo reload cogs", value="```Reloads all cogs.```", inline=True)
        embed.add_field(name=f"{prefix}sudo reload status", value="```Reloads the playing status.```",
                        inline=True)
        embed.add_field(name=f"{prefix}sudo system", value="```Get all info about the hosting system.```",
                        inline=True)
        await ctx.reply(embed=embed)

    @sudo.command()
    async def reload(self, ctx, *args):
        if len(args) == 0:
            await ctx.reply("What do you want me to reload? (cogs/status)")
        elif args[0] == "cogs":
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    self.client.reload_extension(f'cogs.{filename[:-3]}')
            await ctx.message.add_reaction('<:okMAN:808395966175903798>')
        elif args[0] == "status":
            await self.client.change_presence(activity=discord.Streaming(name=f"@mention for help |"
                                                                              f" {(len(self.client.commands))}"
                                                                              " commands!",
                                                                         url=open("assets/status_video.txt",
                                                                                  "r").read()))
            await ctx.message.add_reaction('<:okMAN:808395966175903798>')

    @sudo.command()
    async def system(self, ctx):
        embed = discord.Embed(
            title="[DEV] Host System Information",
            colour=discord.Colour.blue()
        )

        embed.add_field(name="‎", value="**CPU**", inline=False)
        embed.add_field(name="CPU Usage", value=str(psutil.cpu_percent()) + "%")
        embed.add_field(name="Logical CPU Count", value=psutil.cpu_count())

        mem = psutil.virtual_memory()
        embed.add_field(name="‎", value="**Memory**", inline=False)
        embed.add_field(name="Total Memory", value=size(mem.total) + "B")
        embed.add_field(name="Available Memory", value=size(mem.available) + "B")
        embed.add_field(name="Memory Usage", value=str(mem.percent) + "%")

        disk = psutil.disk_usage("/")
        embed.add_field(name="‎", value="**Disk**", inline=False)
        embed.add_field(name="Total Space", value=size(disk.total) + "B")
        embed.add_field(name="Used Space", value=size(disk.used) + "B")
        embed.add_field(name="Free Space", value=size(disk.free) + "B")
        embed.add_field(name="Disk Usage", value=str(disk.percent) + "%")

        net = psutil.net_io_counters()
        embed.add_field(name="‎", value="**Network**", inline=False)
        embed.add_field(name="Packets Sent", value=net.packets_sent)
        embed.add_field(name="Packets Received", value=net.packets_recv)
        embed.add_field(name="Bytes Sent", value=size(net.bytes_sent) + "B")
        embed.add_field(name="Bytes Received", value=size(net.bytes_recv) + "B")

        embed.add_field(name="‎", value="**OS**", inline=False)
        embed.add_field(name="System", value=platform.system())
        if len(platform.release()) != 0:
            embed.add_field(name="Release", value=platform.release())
        else:
            embed.add_field(name="Release", value="???")
        if len(platform.version()) != 0:
            embed.add_field(name="Version", value=platform.version())
        else:
            embed.add_field(name="Release", value="???")

        await ctx.reply(embed=embed)
        
    @sudo.command()
    async def reboot(self, ctx):
        await ctx.message.add_reaction('<:okMAN:808395966175903798>')
        await ctx.send("Now rebooting!")
        os.execl(sys.executable, sys.executable, *sys.argv)
        sys.exit()    

    @commands.is_owner()
    @commands.command()
    async def dev_only(self, ctx):
        servers = list(self.client.guilds)
        await ctx.channel.purge(limit=1)
        await ctx.author.send("https://top.gg/api/widget/718769183885754380.svg")
        embed = discord.Embed(title='Check console!', color=discord.Colour.blue())
        embed.set_footer(text='[Dev Only Command]')
        await ctx.author.send(embed=embed)
        print(f"Connected on {str(len(self.client.guilds))} servers:")
        print('\n'.join(guild.name + ' (Member - ' + str(guild.member_count) + ')' for guild in servers))


def setup(client):
    client.add_cog(Dev(client))
