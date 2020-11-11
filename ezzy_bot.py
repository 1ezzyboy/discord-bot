import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
token = os.getenv("DISCORD_TOKEN")
guild = os.getenv("DISCORD_GUILD")
bot = commands.Bot(command_prefix='!')
client = discord.Client()

@bot.event
async def on_ready():
    print(f"\n{bot.user.name} has connected to Discord!")
    print(f"{bot.user.name}'s user ID is {bot.user.id}")


@bot.command(name="idiot-check", help="tells you if you are an idiot")
async def retard_check(ctx):
    retard_list = [
        "You are an idiot, sorry about your luck buddy",
        "You are a genius, don't tell anyone or they might"
        "try to steal your IQ points!"
    ]
    response = random.choice(retard_list)
    await ctx.send(response)


@bot.command(name="create-text-channel", help="creates a text channel")
@commands.has_role("moron")
async def create_text_channel(ctx, channel_name="new-text-channel"):
    guild = ctx.guild
    category = discord.utils.get(ctx.guild.categories, name="Text Channels")
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f"Creating a new text channel named '{channel_name}'")
        await guild.create_text_channel(channel_name, category=category)


@bot.command(name="create-voice-channel", help="creates a voice channel")
@commands.has_role("moron")
async def create_voice_channel(ctx, channel_name="new voice channel"):
    guild = ctx.guild
    category = discord.utils.get(ctx.guild.categories, name="Voice Channels")
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f"Creating a new voice channel named '{channel_name}'")
        await guild.create_voice_channel(channel_name, category=category)

bot.run(token)