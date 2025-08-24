import discord
from discord.ui import Modal, TextInput, button

from nx_ai.utils.url_checker import is_url_valid
from nx_ai.workflows.generate_recap import generate_recap_beta


class RecapModal(Modal, title="Créer un nouveau Le Recap"):
    title_input = TextInput(
        label="Nom du fichier",
        placeholder="Par exemple, le-recap-aout-2025 ou le-recap-septembre-2025",
        max_length=255
    )
    first_article = TextInput(
        label="URL de l'article 1",
        placeholder="https://"
    )
    second_article = TextInput(
        label="URL de l'article 2",
        placeholder="https://"
    )
    third_article = TextInput(
        label="URL de l'article 3",
        placeholder="https://"
    )
    fourth_article = TextInput(
        label="URL de l'article 4",
        placeholder="https://"
    )
    
    async def on_submit(self, interaction: discord.Interaction):
        title_input = str(self.title_input).strip()
        first_article = str(self.first_article).strip()
        second_article = str(self.second_article).strip()
        third_article = str(self.third_article).strip()
        fourth_article = str(self.fourth_article).strip()
        
        urls = [first_article, second_article, third_article, fourth_article]
        for url in urls:
            if not is_url_valid(url):
                await interaction.response.send_message("❌ URL invalide. Utiliser un lien http(s).", ephemeral=True)
                return
        
        await interaction.response.send_message(f"Construction du Recap {title_input} en cours...")
        
        generate_recap_beta(urls=urls, filename=title_input, simulate=True)
        
        await interaction.followup.send("✅ Travail terminé.")
