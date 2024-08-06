# Mar's Self Bot 1.0

Mar's Self Bot 1.0 is a self-bot for Discord designed to automatically react to your messages. This bot is intended for educational purposes only and interacts with your messages by adding default reactions.

## 📚 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Customization](#customization)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## 🌟 **Features** 🌟

- **Automatic Reactions**: Automatically adds reactions to your messages.
- **Self-Bot**: Operates using your own Discord account.
- **Easy to Use**: Simple setup and configuration.

## 🔧 **Installation** 🔧

### 🖥️ **Exe Method**

- Download the executable from the [latest release](https://github.com/7cf/Discord-Self-React-Bot/releases/download/discordselfbot/selfreact.exe).
- Run the application, enter your token, and click "Run" to start the bot.
- If needed, decode it if you want.

### 📦 **Source Code Method**

#### Prerequisites

- Python 3.8 or higher
- `discord.py-self` library

#### Step-by-Step Guide

1. **Clone the Repository**
    ```sh
    git clone https://github.com/7cf/Discord-Self-React-Bot.git
    cd Discord-Self-React-Bot
    ```

2. **Install Dependencies**
    ```sh
    pip install discord.py-self
    ```

3. **Edit the Script**
    - Download the Python script from the [latest release](https://github.com/7cf/Discord-Self-React-Bot/releases/download/discordselfbot/selfbot.py).
    - Open `selfbot.py` in your preferred text editor.
    - Replace the placeholder token with your actual Discord user token.

    ```python
    TOKEN = 'your_discord_token_here'
    ```

## 🚀 **Usage** 🚀

1. **Run the Bot**

    For the executable, just run it and click "Run" after entering your token.

    For the Python script:

    ```sh
    python selfbot.py
    ```

2. **Check for Successful Login**
    - You should see a message in your terminal indicating that you have logged in successfully.

    ```sh
    Logged in as your_username
    ```

## ⚙️ **Configuration** ⚙️

### Script Overview

The main script (`selfbot.py`) looks like this:

```python
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
            await message.add_reaction('💚')
            await message.add_reaction('🍍')
        except Exception as e:
            print(f'Error adding reactions: {e}')
    
    await client.process_commands(message)  # Process other commands

client.run(TOKEN)
