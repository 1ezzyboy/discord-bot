import discord
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
client = discord.Client()

@client.event
async def on_ready():
    print(f"\n{client.user.name} has connected to Discord!")
    print(f"{client.user.name}'s user ID is {client.user.id}")


client.run(token)