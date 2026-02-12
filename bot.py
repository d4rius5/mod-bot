import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import json

# load .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="r!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command
async def warn(ctx, user: discord.Member, *, reason: str = "No reason provided"):
    if reason == "No reason provided":
        return
    
    

bot.run(TOKEN)
