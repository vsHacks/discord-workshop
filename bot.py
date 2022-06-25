import os
import sys

import discord
import dotenv
from discord.ext import commands

# Load variables from the .env file.
# This isn't necessary on Replit, but is needed elsewhere.
dotenv.load_dotenv()

# Create a new bot instance with the prefix "!" and all intents enabled.
# Remember to enable all intents for your bot in the Discord developer portal as well.
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# @bot.event registers the on_ready function with Discord.py so it'll be called
# when the bot receives the ready event from Discord.
#
# Read more about Python decorators here: https://realpython.com/primer-on-python-decorators/.
# For a list of all supported events, see https://discordpy.readthedocs.io/en/stable/api.html#event-reference.
@bot.event
async def on_ready():
	print(f"successfully logged in as {bot.user}")

@bot.event
async def on_message(msg):
	await bot.process_commands(msg)

@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, (commands.CommandOnCooldown, commands.UserInputError)):
		await ctx.send(str(error))

# A list of extensions to register when the bot is started.
# Each entry in this list corresponds to a Python module;
# for example, cogs.system corresponds to cogs/system.py.
#
# When you write a new cog, remember to add it to this list;
# otherwise, its commands and listeners won't be registered.
initial_exts = ["cogs.fun", "cogs.system", "cogs.utility"]

def main():
	token = os.getenv("DISCORD_TOKEN")
	if not token:
		print("no token specified; make sure you have a .env file with a DISCORD_TOKEN entry")
		sys.exit(1)
	
	for ext in initial_exts:
		bot.load_extension(ext)
	bot.run(token)

if __name__ == "__main__":
	main()
