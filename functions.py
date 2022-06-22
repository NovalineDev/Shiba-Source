from discord_webhook import DiscordWebhook, DiscordEmbed

from pymongo import MongoClient
import json

import time

dbclient = MongoClient(
    "")
discorddb = dbclient.get_database('shiba_reborn')
prefixes = discorddb.prefix
languages = discorddb.language


def send_join_server_webhook(count):
    join_webhook = DiscordWebhook(
        url='',
        username="Shiba Server Log")

    embed = DiscordEmbed(title='I just joined a server', description=f':point_right::upside_down::point_left: less go',
                         color=0x00FF00)

    embed.set_footer(text=f'New server count: {int(count)}')
    embed.set_timestamp(time.time())

    join_webhook.add_embed(embed)
    join_webhook.execute()


def send_leave_server_webhook(count):
    print("hello I'm abouta send the hook lol")
    leave_webhook = DiscordWebhook(
        url='',
        username="Shiba Server Log")

    embed = DiscordEmbed(title='I just left a server', description=f':pensive: sadness', color=0xFF0000)

    embed.set_footer(text=f'New server count: {int(count)}')
    embed.set_timestamp(time.time())

    leave_webhook.add_embed(embed)
    leave_webhook.execute()


def prefix_grabber(id):
    try:
        var = prefixes.find_one({"id": id}, {"_id": False})
        var1 = str(var).replace("'", '"')
        prefix_json = json.loads(var1)
        return str(prefix_json[str("prefix")])

    except Exception:
        return "s?"
