# 🌈 **Self Bot 1.0** 🌈

Welcome to the **Self Bot 1.0** repository! This project is designed for educational purposes and demonstrates how to create a self-bot using Python and Discord's API. **Please note that using self-bots is against Discord's Terms of Service. Proceed with caution.**

## 🌟 **Features** 🌟

- Automatically reacts to your messages with 💚 and 🍍
- Simple to set up and run

## 🔧 **Requirements** 🔧

- Python 3.x
- `discord.py-self` library

## 📝 **Installation** 📝

1. **Clone the Repository**

    ```sh
    git clone https://github.com/yourusername/self-bot.git
    cd self-bot
    ```

2. **Install the Required Libraries**

    ```sh
    pip install discord.py-self
    ```

3. **Run the Bot**

    ```sh
    python selfbot.py
    ```

## 📄 **Usage** 📄

Replace the placeholder token in `selfbot.py` with your actual Discord token:

```python
import discord
from discord.ext import commands

# Replace with your actual user token
TOKEN = 'YOUR_DISCORD_TOKEN'

client = commands.Bot(command_prefix='!', self_bot=True)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Check if the message is sent by the bot itself
    if message.author.id == client.user.id:
        try:
            await message.add_reaction('💚')
            await message.add_reaction('🍍')
        except Exception as e:
            print(f'Error adding reactions: {e}')
    
    await client.process_commands(message)  # Process other commands

client.run(TOKEN)
