# importing required packages
import time
import discord
import asyncio
from discord.ext import commands

# customize settings
prefix = '!!' # edit the bot prefix for the command
streamname = "dromzeh.best" # set the name of your stream (for example,, will appear as "Streaming dromzeh.best")
streamurl = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # set the url that the "watch" button redirects to, has to be twitch or youtube only

# do not modify / edit the rest of this if you have little to no python / discord.py knowledge
bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event  
async def on_ready():
    print(f"logged in as {bot.user.id} / {bot.user.name}")
    await bot.change_presence(activity=discord.Streaming(name=streamname, url=streamurl)) # sets presence to streaming
    print("streaming status enabled, may take some time to show up on your profile.")

@bot.command()
async def stop(ctx): # stops the streaming status and closes down
    if bot.user.id == ctx.message.author.id: # makes it so only you are able to shut down the bot
        print("bot shutdown requested")
        await bot.close()
        time.sleep(3)

bot.run('TOKEN', bot = False) # enter your token where it says TOKEN
