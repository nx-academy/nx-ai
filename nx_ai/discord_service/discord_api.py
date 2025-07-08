import discord
import os


DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
DISCORD_RECAP_CHANNEL = int(os.environ.get("DISCORD_RECAP_CHANNEL"))


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f"Bot connected as {client.user}")
        
        channel_id = DISCORD_RECAP_CHANNEL
        channel = client.get_channel(channel_id)
        
        if not channel:
            print("Unabled to connect to the channel")
            await client.close()
            return
    
        
    client.run(DISCORD_TOKEN)
    
    
