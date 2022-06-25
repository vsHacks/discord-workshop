from discord.ext import commands


# A commands.Cog is a collection of related commands and event listeners.
# Commands in separate cogs will show up in different sections when users
# run the help command.
class System(commands.Cog):
	"""Core commands relating to the bot."""
	def __init__(self, bot):
		self.bot = bot

	# Similar to @bot.event, @commands.command is a decorator
	# that marks the method as a command. 
	@commands.command()
	@commands.cooldown(1, 1000) # Only allow the command to be used once per second.
	async def ping(self, ctx):
		"""Check if the bot is online."""
		await ctx.send("Pong!")

def setup(bot):
	# Tell Discord.py to add this cog and all its commands when this extension is added.
	bot.add_cog(System(bot))
