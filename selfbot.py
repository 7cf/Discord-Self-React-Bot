import discord
from discord.ext import commands

# Replace with your actual user token
TOKEN = 'your_discord_token_here'

client = commands.Bot(command_prefix='!', self_bot=True)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Check if the message is sent by the bot itself
    if message.author.id == client.user.id:
        try:
            await message.add_reaction('☠️')
            await message.add_reaction('💀')
        except Exception as e:
            print(f'Error adding reactions: {e}')
    
    await client.process_commands(message)  # Process other commands

client.run(TOKEN)
