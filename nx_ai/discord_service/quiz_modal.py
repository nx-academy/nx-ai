import discord
from discord.ui import Modal, TextInput

from nx_ai.utils.url_checker import is_url_valid


class QuizModal(Modal, title="Créer un nouveau quiz"):
    title_input = TextInput(
        label="Nom du fichier",
        placeholder="Par exemple, artefact-github-actions",
        max_length=255
    )
    cheatsheet_url = TextInput(
        label="URL de la fiche technique",
        placeholder="https://nx.academy/drafts/artefact-github-actions/"
    )

    async def on_submit(self, interaction: discord.Interaction):
        title_input = str(self.title_input).strip()
        cheatsheet_url = str(self.cheatsheet_url).strip()

        if not is_url_valid(cheatsheet_url):
            await interaction.response.send_message(
                "❌ URL invalide. Utiliser un lien http(s).",
                ephemeral=True
            )
            return
        
        await interaction.response.send_message(f"Construction du Quiz {title_input} en cours...")
