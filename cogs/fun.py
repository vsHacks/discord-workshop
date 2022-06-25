import random

from discord.ext import commands


class Fun(commands.Cog):
    """Fun commands."""
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.Listener is just like @bot.event, except it's usable in cogs.
    # In this case, we are telling Discord.py to run this method whenever
    # a message is sent.
    @commands.Cog.listener()
    async def on_message(self, msg):
        # Don't respond to bots.
        if msg.author.bot:
            return

        if msg.content.startswith("I'm"):
            name = msg.content.removeprefix("I'm").strip()
            await msg.reply(f"Hi {name}, I'm Dad!")

    @commands.command()
    async def rps(self, ctx, choice):
        """Play rock-paper-scissors against the bot."""
        CHOICES = ("rock", "paper", "scissors")
        WINNING_PAIRS = (("rock", "scissors"), ("scissors", "paper"), ("paper", "rock"))

        user_choice = choice.lower()
        if user_choice in CHOICES:
            bot_choice = random.choice(CHOICES)
            if bot_choice == user_choice:
                await ctx.send(f"I chose {user_choice} too, so it appears we're tied!")
            elif (user_choice, bot_choice) in WINNING_PAIRS:
                await ctx.send(
                    f"You chose {user_choice}, which beats my choice of {bot_choice}, so it appears you win."
                )
            else:
                await ctx.send(
                    f"I chose {bot_choice}, and that beats your choice of {user_choice}. Good game!"
                )
        else:
            await ctx.send("Choose one of rock, paper, or scissors.")

def setup(bot):
    bot.add_cog(Fun(bot))
