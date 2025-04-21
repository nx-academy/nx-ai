import discord
import os
from datetime import datetime


def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
    DISCORD_RECAP_CHANNEL = int(os.environ.get("DISCORD_RECAP_CHANNEL"))


    @client.event
    async def on_ready():
        print(f"Bot connected as {client.user}")

        channel_id = DISCORD_RECAP_CHANNEL
        channel = client.get_channel(channel_id)

        if not channel:
            print("Unabled to connect to the channel")
            await client.close()
            return
        
        after = datetime(2025, 4, 1)
        before = datetime(2025, 5, 1)

        print("Retrieving April messages")
        messages = []
        async for msg in channel.history(after=after, before=before, limit=None, oldest_first=True):
            messages.append(msg)


        print(f"{len(messages)} messages have been found")
        for m in messages:
            print(f"[{m.created_at}] {m.author}: {m.content}")

        await client.close()


    client.run(DISCORD_TOKEN)
