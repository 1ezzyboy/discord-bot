import discord
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

# A Client is an object that represents a connection to Discord
# A Client handles events, tracks state, and generally interacts
# with Discord APIs
client = discord.Client()
print(token)

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord")

client.run(token)
