import os

import discord
from discord import Interaction, app_commands

from nx_ai.discord_service.news_modal import NewsModal
from nx_ai.discord_service.recap_modal import RecapModal
from nx_ai.discord_service.quiz_modal import QuizModal
from nx_ai.openai_service.openai_api import (
        fetch_news_with_gpt_web_search,
        rewrite_summary_with_personal_style)


DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")

GUILD_ID = 1357783834208243864
DISCORD_BO_NEWS_FEED = 1407779612439613522
DISCORD_BO_NEWSROOM_IA = 1408853151733518376
DISCORD_BO_LE_RECAP = 1408121527433433221
DISCORD_BO_QUIZ = 1416441425238949988
DISCORD_BO_STYLE_TEXT = 1425854954194600017


class DiscordClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)
    
    async def setup_hook(self):
        guild = discord.Object(id=GUILD_ID)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)


def run_discord_bot():
    client = DiscordClient()
    
    @client.event
    async def on_ready():
        print(f"Bot connected as {client.user}")

    @client.tree.command(name="create_quiz", description="Créer un nouveau quiz à partir d'une fiche technique")
    async def create_quiz(interaction: Interaction):
        if interaction.channel_id != DISCORD_BO_QUIZ:
            await interaction.response.send_message(
                "❌ Cette commande n’est autorisée que dans le channel dédié.",
            )
            return
        
        await interaction.response.send_modal(QuizModal())
        
    @client.tree.command(name="create_recap", description="Créer un nouveau Le Recap")
    async def create_recap(interaction: Interaction):
        if interaction.channel_id != DISCORD_BO_LE_RECAP:
            await interaction.response.send_message(
                "❌ Cette commande n’est autorisée que dans le channel dédié.",
                ephemeral=True
            )
            return

        await interaction.response.send_modal(RecapModal())
    
    @client.tree.command(name="add_news", description="Créer une nouvelle news")
    async def create_news(interaction: Interaction):
        if interaction.channel_id != DISCORD_BO_NEWS_FEED:
            await interaction.response.send_message(
                "❌ Cette commande n’est autorisée que dans le channel dédié.",
                ephemeral=True
            )
            return
        
        await interaction.response.send_modal(NewsModal())
        
    @client.tree.command(name="fetch_news", description="Chercher des news sur Internet")
    @app_commands.describe(simulate="Si activé, renvoie des données mockées (simulate=True)")
    async def fetch_news(interaction: Interaction, simulate: bool = True):
        if interaction.channel_id != DISCORD_BO_NEWSROOM_IA:
            await interaction.response.send_message(
                "❌ Cette commande n’est autorisée que dans le channel dédié.",
                ephemeral=True
            )
            return
            
        await interaction.response.send_message(f"🔍 Recherche {'simulée' if simulate else 'réelle'} en cours...")
        
        news = fetch_news_with_gpt_web_search(simulate=simulate)
        
        for item in news.data["data"]:
            embed = discord.Embed(
                title=item["title"],
                description=item["content"],
                url=item["url"],
                color=0x3498db
            )
            await interaction.followup.send(embed=embed)
        await interaction.followup.send("✅ Travail terminé.")

    @client.tree.command(name="style-text",
                         description="Reécrire un texte avec mon style personnel")
    @app_commands.describe(simulate="Si activé, permet de simuler la reécriture")
    async def style_text(
            interaction: Interaction,
            simulate: bool = True):
        if interaction.channel_id != DISCORD_BO_STYLE_TEXT:
            await interaction.response.send_message(
                    content="❌ Cette commande n’est autorisée que dans le channel dédié.",
                    ephemeral=True
            )
            return

        await interaction.response.send_message(f"Écriture {'simulée' if
                                                simulate else 'réelle'} en cours...")

        styled_text = rewrite_summary_with_personal_style(
            simulate=simulate,
            raw_summary=""
        )

        await interaction.followup.send(f"voici le texte adapté à mon style: {styled_text.text}")
        await interaction.followup.send("✅ Travail terminé.")

    
    client.run(DISCORD_TOKEN)
