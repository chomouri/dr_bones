import discord
from discord.ext import commands

import config
import dice_roller as dr

client = commands.Bot(
    command_prefix='$',
    help_command=None,
    # TODO: fix intents to least priv
    intents=discord.Intents.all()
)

@client.event
async def on_ready() -> None:
    print("DISCORD: We have logged in as {0.user}".format(client))

@client.command()
async def roll(ctx):
    if ctx.message.content.startswith("$roll "):
        response = dr.parse_roll(ctx.message.content[6:])
    await ctx.send(response)

client.run(config.config(section="discord")["bones_token"])
