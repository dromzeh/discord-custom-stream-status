# importing required modules
try:
    import time
    import discord
    import asyncio
    from discord.ext import commands
    import json
    from colorama import init, Fore, Back, Style
except ModuleNotFoundError:
    print('You are missing the required module(s) to run this program.\n Please install them from requirements.txt and try running the program again.')

init(autoreset=True) # allowing colorama to properly display on windows

# loading config
with open("config.json") as data:
    config = json.load(data)

token = config["token"]
prefix = config["prefix"]
streamurl = config["streamurl"]
streamname = config["streamname"]

bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    print(f"{Fore.YELLOW}[!] Running Discord Custom Stream Status - https://github.com/dromzeh/discord-custom-stream-status")
    print(f"\n{Fore.YELLOW}[!] Licensed under MIT - Read https://mit.dromzeh.dev/ for more information")
    print(f"\n{Fore.GREEN}[+] Logged in as [{bot.user.id}] {bot.user.name}")
    try:
        await bot.change_presence(activity=discord.Streaming(name=streamname, url=streamurl))
        print(f'\n{Fore.GREEN}[+] Streaming status enabled: \nStream Name: {streamname} \nStream Url: {streamurl}')
    except Exception as e:
        print(f'\n{Fore.RED}[-] Failed to start streaming status - {e}')

@bot.command()
async def stop(ctx):
    print(f"\n{Fore.RED}[-] Bot shutdown requested, shutting down...")
    await bot.close()
    time.sleep(3)

bot.run(token, bot = False)
