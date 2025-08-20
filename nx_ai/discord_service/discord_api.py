import discord
from discord import app_commands
from discord.ui import Modal, TextInput
import os


DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
GUILD_ID = 1357783834208243864
DISCORD_RECAP_CHANNEL = int(os.environ.get("DISCORD_RECAP_CHANNEL"))


class NewsFeedClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)
    
    async def setup_hook(self):
        guild = discord.Object(id=GUILD_ID)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)


client = NewsFeedClient()

def run_discord_bot():
    @client.event
    async def on_ready():
        print(f"Bot connected as {client.user}")
    
    @client.tree.command(name="add_news", description="Créer une nouvelle news")
    async def create_news(interaction: discord.Interaction):
        print("====")
        print("====")
        print("====")
    
    client.run(DISCORD_TOKEN)
