import copy
import random
import re

import discord
from discord.ext import commands

import config
import dice_roller as dr

client = commands.Bot(
    command_prefix='$',
    help_command=None,
    intents=discord.Intents.all()
)

@client.event
async def on_ready() -> None:
    print("DISCORD: We have logged in as {0.user}".format(client))

# @client.event
# async def on_message(message) -> None:
#     if message.content.startswith("$roll "):
#         if message.content.startswith("$roll char"):
#             response = f"Offical:\n {dr.roll_char_stats()}"
#         else:
#             dice = message.content
#             response = f"Offical:\n {dr.parse_roll(dice)}"
#         await message.channel.send(response)

@client.command()
async def roll(ctx):
    print(f"Print to console {ctx.message.content}")
    if ctx.message.content.startswith("$roll char"):
        response = f"Offical:\n {dr.roll_char_stats()}"
    else:
        dice = ctx.message.content
        response = f"Offical:\n {dr.parse_roll(dice)}"
    await ctx.send(response)

client.run(config.config(section="discord")["bones_token"])
