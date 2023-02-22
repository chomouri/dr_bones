import discord
from discord.ext import commands

import config
import dice_roller as dr

meta = {'version': '1.0.0'}
project_version = config.get_project_version(meta)

client = commands.Bot(
    command_prefix='$',
    help_command=None,
    # TODO: fix intents to least priv
    intents=discord.Intents.all()
)

@client.event
async def on_ready() -> None:
    print(f"DISCORD BOT: We have logged in as {client.user} using {project_version}")

@client.command()
async def roll(ctx):
    if ctx.message.content.startswith("$roll "):
        response = dr.parse_roll(ctx.message.content[6:])
    await ctx.send(response)

client.run(config.config(section="discord")["bones_token"])
