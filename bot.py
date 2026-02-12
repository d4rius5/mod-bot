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
    
    with open("cases_number.json", "r") as f:
        data = json.load(f)

    if "cases" not in data:
        data["cases"] = 0

    data["cases"] += 1

    with open("cases_number.json", "w") as f:
        json.dump(data, f, indent=4)

    print(data)

bot.run(TOKEN)
