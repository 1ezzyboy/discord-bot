import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f"\n{bot.user.name} has connected to Discord!")
    print(f"{bot.user.name}'s user ID is {bot.user.id}")


bot.run(token)