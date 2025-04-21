import discord
import os


def run_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
    DISCORD_RECAP_CHANNEL = os.environ.get("DISCORD_RECAP_CHANNEL")


    @client.event
    async def on_ready():
        print(f"Bot connected as {client.user}")

        channel_id = DISCORD_RECAP_CHANNEL
        channel = client.get_channel(channel_id)

        if channel:
            await channel.send("Hello World depuis le bot")
            print("Message has been successfully sent.")
        else:
            print("Something went wrong when sending the message.")


    client.run(DISCORD_TOKEN)
