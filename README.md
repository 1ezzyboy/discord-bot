# discord-bot
This is a readme file for the discord bot
Currently working on transferring code to python

# Features currently implemented
- Can create text channels
- Can create voice channels

# Bot functionality ideas
1. Twitter webhooking to pull profiles and maybe posts
2. E621 webhooking to pull pictures based on searching tags
3. Music bot features (YouTube linking to play music)


# Notes from the python file (for personal reference)
A Client is an object that represents a connection to Discord. A Client handles events, tracks state, and generally interacts with Discord APIs: https://discordpy.readthedocs.io/en/latest/api.html#client

Client events use coroutines and are used to perform actions: https://discordpy.readthedocs.io/en/latest/api.html#event-reference

The run function abstracts the event loop initialization and starts the bot: https://discordpy.readthedocs.io/en/latest/api.html#discord.Client.run