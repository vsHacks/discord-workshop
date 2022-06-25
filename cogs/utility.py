import discord
from discord.ext import commands


class Utility(commands.Cog):
    """Useful utility commands for Discord."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def embed(self, ctx, title, desc):
        """Create a simple embed with a title and description."""
        embed = discord.Embed(title=title, description=desc)
        await ctx.send(embed=embed)

    @commands.command()
    async def react(self, ctx, emoji):
        """React with an emoji."""
        try:
            await ctx.message.add_reaction(emoji)
        except discord.HTTPException:
            await ctx.send("Not a valid emoji.")

    @commands.command()
    # Only allow this command to be used by members with permission to manage messages.   
    @commands.has_permissions(manage_messages=True)
    # The ": int" after amount is a type annotation, and tells Discord.py what sort of input
    # can be provided to this command. If a non-integer value is provided, Discord.py
    # will throw an exception for us, which will then be shown to the user.
    async def clear(self, ctx, amount: int):
        """Delete messages from the channel in bulk."""
        limit = amount + 1  # also delete triggering message
        if limit > 100:
            await ctx.send("The amount of messages to delete must be less than 100.")
        elif amount <= 0:
            await ctx.send("The amount of messages to delete must be greater than 0.")

        await ctx.channel.purge(limit=limit)
        msg = await ctx.send(f"Purged {amount} messages!")
        await msg.delete(delay=1)

def setup(bot):
    bot.add_cog(Utility(bot))
