# 🤓 **Mar's Self Bot 1.0** 🤓

Mar's Self Bot 1.0 is a self-bot for Discord that automatically reacts to your messages. This bot is designed for educational purposes only. It adds default reactions to all messages sent by the user.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## 🌟 **Features** 🌟

- **Automatic Reactions**: Automatically adds reactions to your messages.
- **Self-Bot**: Operates using your own Discord account.
- **Easy to Use**: Simple setup and configuration.

## 🔧 **Installation** 🔧

### Prerequisites

- Python 3.8 or higher
- `discord.py-self` library

### Step-by-Step Guide

1. **Clone the Repository**

    ```sh
    git clone https://github.com/your-username/mars-self-bot.git
    cd mars-self-bot
    ```

2. **Install Dependencies**

    ```sh
    pip install discord.py-self
    ```

3. **Edit the Script**

    - Open `selfbot.py` in your preferred text editor.
    - Replace the placeholder token with your actual Discord user token.

    ```python
    TOKEN = 'your_discord_token_here'
    ```

## 📄 **Usage** 📄

1. **Run the Bot**

    ```sh
    python selfbot.py
    ```

2. **Check for Successful Login**

    - You should see a message in your terminal indicating that you have logged in successfully.

    ```sh
    Logged in as your_username
    ```

## 📜 **Configuration** 📜

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
🎉 selfreact.exe 🎉
For those who prefer a more user-friendly approach, we have provided a compiled executable version named selfreact.exe. This version offers a simple graphical interface where you can enter your token and start or stop the self-bot with the click of a button.

💻 Commands 💻
!addreaction
Manually add a reaction to your messages.

!removereaction
Remove a reaction from your messages.

🤝 Contributing 🤝
We welcome contributions! If you would like to contribute, please fork the repository and submit a pull request.

For any questions, feel free to reach out to me on Discord: #unvilged.

📄 License 📄
This project is licensed under the MIT License. See the LICENSE file for details.

⚠️ Disclaimer ⚠️
Please be cautious! This project is intended for educational purposes only. Using self-bots is against Discord's Terms of Service and can lead to your account being banned. We do not take any responsibility for any actions taken against your account as a result of using this self-bot.

Happy coding! 🌟
