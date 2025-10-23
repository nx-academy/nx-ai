import discord
from discord.ui import Modal, TextInput

from nx_ai.openai_service.openai_api import rewrite_summary_with_personal_style


class SummaryModal(Modal, title="Générer un résumé personnalisé"):
    text_input: TextInput = TextInput(
        label="Texte à personnaliser",
        placeholder="Ceci est un super texte d'exemple qui n'a pas été écrit par moi.",
        style=discord.TextStyle.paragraph,
        max_length=500
    )

    async def on_submit(self, interaction: discord.Interaction) :
        text_input = str(self.text_input).strip()

        await interaction.followup.send("Résumé en cours de réalisation...")

        styled_text = rewrite_summary_with_personal_style(
            simulate=False,
            raw_summary=text_input
        )

        await interaction,followup.send(f"Voici le texte reformulée: {styled_text.text}")

        await interaction.followup.send("✅ Travail terminé.")

