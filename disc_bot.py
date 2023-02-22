"""Main Script for Discord Bot"""
__lver__ = '1.1.0'

# Built-in Imports
import sys

# Third-Party Imports
import discord
from discord.ext import commands
imports_others = [str(m) for m in sys.modules]

# Local Imports
import config
import dice_roller as dr
imports_all = [str(m) for m in sys.modules]
imports_mine = [m for m in imports_all if not m in imports_others]

class ModuleVersioning:
    def __init__(self, name, lver):
        self.name = name
        self.lver = lver
    def __repr__(self):
        return f"{self.name}: {self.lver}"

def get_project_version(imports_mine):
    """Compiles version information from project modules"""
    local_versioning = []
    for module_name in imports_mine:
        module = sys.modules[module_name]
        try:
            local_versioning.append(ModuleVersioning(module_name, module.__lver__))
        except AttributeError:
            if module.__name__ == 'configparser':
                pass
            else:
                print(f"Local Version number not found for {module.__name__}")
    project_version = local_versioning
    return project_version

project_version = get_project_version(imports_mine)

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
