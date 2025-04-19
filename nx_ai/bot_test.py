import discord
import os


def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")


    @client.event
    async def on_ready():
        print(f"Bot connected as {client.user}")


    client.run(DISCORD_TOKEN)
