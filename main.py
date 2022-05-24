import sys
import time

import discord
from discord.ext import commands

from cogs import bot_commands

from rich import print
from rich.console import Console
from rich.table import Table

from config import settings

print(f"[b yellow]Python {sys.version}")

bot = commands.Bot(command_prefix = settings['prefix'], intents=discord.Intents.all())
bot.remove_command('help')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        content = ctx.message.content
        await ctx.message.delete()
        print(f"[yellow]{ctx.author} tried to use undefined command ({content})!")
    elif isinstance(error, commands.CommandInvokeError):
        print(f"[red]Bot doesn't have permissions to execute a command :(")
    elif isinstance(error, commands.CheckFailure):
        print(f"[yellow]{ctx.author} is not in whitelist!")
    else:
        raise error

@bot.event
async def on_ready():
    pref = settings["prefix"]
    print(f"[b green]Bot is ready! \n"
          f"Prefix: {pref}")

    table = Table(title="Bot Commands List")

    table.add_column("Command", justify="left", style="cyan", no_wrap=True)
    table.add_column("Description", justify="right", style="green")

    table.add_row(f"{pref}ban",                "Banning members. Arguments: @member, reason")
    table.add_row(f"{pref}ban_all",            "Banning all members.")
    table.add_row(f"{pref}spam_roles",         "Creates a lot of roles. Args: count, name_of_the_roles")
    table.add_row(f"{pref}delete_all",         "Deletes all channels on the server.")
    table.add_row(f"{pref}spam_channel",       "Creates a lot of the channels. Args: name_of_the_channels, count")
    table.add_row(f"{pref}spam",               "Spamming in all channels. Args: count, message_text")

    console = Console()
    console.print(table)

if __name__ == '__main__':
    bot_commands.setup(bot)
    bot.run(settings['token'])