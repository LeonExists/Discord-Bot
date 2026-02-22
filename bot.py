# --- Libraries ---
import discord
from discord.ext import commands
from discord import app_commands
import os
from dotenv import load_dotenv

load_dotenv()


# --- Game ---
from game import Game
games = {}



# --- Bot ---
class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)

    async def setup_hook(self):
        await self.tree.sync()
        print(f"Synced slash commands for {self.user}")

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

bot = MyBot()

 

# --- Commands ---
@bot.tree.command(name="start", description="Start a game.")
async def start(interaction: discord.Interaction):
    # create game message
    msg = await interaction.response.send_message(f"{interaction.user.mention}'s Game...")
    
    # create new game & store game under user id
    user_id = interaction.user.id
    game = Game(msg)
    games[user_id] = game

    # debugging - games
    print(f"Games: \n {games}")

@bot.tree.command(name="test", description="A testing command.")
async def test(interaction: discord.Interaction):
    # get user_id & game
    user_id = interaction.user.id
    game = games[user_id]

    # test
    game.render()

 


# --- Start ---
if __name__ == "__main__":
    TOKEN = os.getenv('DISCORD_TOKEN')
    if not TOKEN:
        raise ValueError("DISCORD_TOKEN not found in environment variables")
    bot.run(TOKEN)
