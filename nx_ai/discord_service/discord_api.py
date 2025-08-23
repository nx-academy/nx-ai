import os

import discord
from discord import app_commands
from discord.ui import Modal, TextInput, View, button

from nx_ai.utils.slugify import slugify_title
from nx_ai.utils.url_checker import is_url_valid
from nx_ai.turso_service.turso_api import insert_news_in_db
from nx_ai.github_service.github_api import trigger_gh_rebuild


DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

GUILD_ID = 1357783834208243864
DISCORD_BO_NEWS_FEED = 1407779612439613522


class PreviewNewsView(View):
    def __init__(self, *, title: str, content: str, url: str):
        super().__init__(timeout=600)
        self.title = title
        self.content = content
        self.url = url
        self.slug = slugify_title(title)
    
    @button(label="Publier", style=discord.ButtonStyle.success)
    async def publish(self, interaction: discord.Interaction, button: discord.ui.Button):
        try:
            await insert_news_in_db(
                title=self.title,
                content=self.content,
                url=self.url,
                slug=self.slug
            )
            
            await interaction.response.edit_message(
                content="✅ News publiée et ajoutée à la base de données !",
                view=None
            )
            trigger_gh_rebuild()
        
        except Exception as e:
            await interaction.response.send_message(
                f"❌ Erreur lors de la publication : {e}",
                ephemeral=True
            )
    
    @button(label="Rejeter", style=discord.ButtonStyle.danger)
    async def reject(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.message.delete()


class NewsModal(Modal, title="Créer une nouvelle news"):
    title_input = TextInput(label="Titre", placeholder="Titre de la news", max_length=255)
    content_input = TextInput(
        label="Contenu",
        style=discord.TextStyle.paragraph,
        placeholder="Contenu de la news",
        max_length=500)
    url_input = TextInput(label="URL", placeholder="https://...")
    
    async def on_submit(self, interaction: discord.Interaction):
        title = str(self.title_input).strip()
        content = str(self.content_input).strip()
        url = str(self.url_input).strip()
        
        if not is_url_valid(url):
            await interaction.response.send_message("❌ URL invalide. Utiliser un lien http(s).", ephemeral=True)
            return
        
        embed = discord.Embed(
            title=title,
            description=content,
            color=discord.Color.blurple()
        )
        embed.add_field(name="Lien", value=url, inline=False)
        embed.add_field(name="Slug", value=slugify_title(title), inline=True)
        
        view = PreviewNewsView(
            title=title,
            content=content,
            url=url
        )
        
        await interaction.response.send_message(
            embed=embed,
            view=view,
            ephemeral=False
        )


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
        if interaction.channel_id != DISCORD_BO_NEWS_FEED:
            await interaction.response.send_message(
                "❌ Cette commande n’est autorisée que dans le channel dédié.",
                ephemeral=True
            )
            return
        
        await interaction.response.send_modal(NewsModal())
    
    client.run(DISCORD_TOKEN)
