# Mar's Self Bot 1.0

Welcome to **Mar's Self Bot 1.0**, a customizable self-bot for Discord! This bot is designed to automate reactions to your messages, making your Discord experience a bit more fun and interactive. Remember, this bot is intended solely for educational purposes and operates using your own Discord account.

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

## 🌟 Features 🌟

Mar's Self Bot comes with several handy features:

- **Automatic Reactions**: Add predefined reactions to your messages automatically.
- **Self-Bot Functionality**: Operates directly with your personal Discord account.
- **User-Friendly Setup**: Quick and straightforward installation and configuration.

## 🔧 Installation 🔧

### 🖥️ Executable Method

1. **Download the Executable**
   - Obtain the executable file from the [latest release](https://github.com/7cf/Discord-Self-React-Bot/releases/download/discordselfbot/selfreact.exe).

2. **Run the Application**
   - Launch the executable.
   - Enter your Discord token when prompted.
   - Click "Run" to start the bot.
   - If necessary, you can decode the executable if you encounter issues.

### 📦 Source Code Method

If you prefer working with the source code, follow these steps:

#### Prerequisites

Ensure you have the following:

- **Python 3.8** or higher
- **`discord.py-self`** library

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
   - Replace the placeholder token with your actual Discord user token:

    ```python
    TOKEN = 'your_discord_token_here'
    ```

## 🚀 Usage 🚀

### Running the Bot

1. **Executable File**
   - Simply run the executable file and click "Run" after entering your token.

2. **Python Script**
   - Execute the script from your terminal:

    ```sh
    python selfbot.py
    ```

3. **Verify Successful Login**
   - Check your terminal for a success message:

    ```sh
    Logged in as your_username
    ```

## ⚙️ Configuration ⚙️

### Script Overview

Here’s a brief look at the main script (`selfbot.py`):

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
