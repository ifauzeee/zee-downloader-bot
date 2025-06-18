
# Zee Downloader Bot 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Issues](https://img.shields.io/github/issues/ifauzeee/zee-downloader-bot)](https://github.com/ifauzeee/zee-downloader-bot/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/ifauzeee/zee-downloader-bot/pulls)

A powerful Telegram bot for downloading videos from YouTube and TikTok, supporting up to 4K quality with real-time progress updates.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example Commands](#example-commands)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features
- 📹 Download videos from YouTube and TikTok with a single command.
- 🎥 Choose from multiple video quality options, up to 4K when available.
- ⏳ Real-time download progress with percentage, speed, and ETA.
- 🔒 Secure handling of API tokens and cookies using environment variables and `.gitignore`.
- 🐍 Built with Python, powered by `yt-dlp` for robust video downloading.

## Prerequisites
Before running the bot, ensure you have:
- Python 3.8 or higher
- A Telegram bot token from [BotFather](https://t.me/BotFather)
- Cookies file for YouTube/TikTok authentication in Netscape format

## Installation
Follow these steps to set up the bot locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ifauzeee/zee-downloader-bot.git
   cd zee-downloader-bot
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   - Create a `.env` file in the project root:
     ```bash
     echo "TELEGRAM_BOT_TOKEN=your_bot_token_here" > .env
     ```
   - Replace `your_bot_token_here` with your Telegram bot token from BotFather.

5. **Prepare cookies file**:
   - Export cookies for `youtube.com` and `tiktok.com` using a browser extension (e.g., [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie)).
   - Save as `cookies.txt` in the project root.
   - Ensure `cookies.txt` is listed in `.gitignore` to prevent accidental commits.

6. **Run the bot**:
   ```bash
   python3 bot.py
   ```

## Usage
1. Open Telegram and start the bot by sending `/start`.
2. Send a YouTube or TikTok video URL (e.g., `https://www.youtube.com/watch?v=iVrjwy0foF4`).
3. Select the desired video quality from the inline options.
4. Wait for the bot to process and send the video in MP4 format.

## Example Commands
- `/start`: Initializes the bot and displays a welcome message.
- Send a URL: `https://www.tiktok.com/@user/video/123456789` to trigger a download.

## Dependencies
The bot relies on the following Python libraries:
- `yt-dlp`: For downloading videos from YouTube and TikTok.
- `python-telegram-bot`: For interacting with the Telegram API.
- `python-dotenv`: For managing environment variables.

Install them using:
```bash
pip install yt-dlp python-telegram-bot python-dotenv
```

## Contributing
We welcome contributions! To get started:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature
   ```
5. Open a Pull Request on GitHub.

Please ensure your code follows the project's style guidelines and includes tests. See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Code of Conduct
This project adheres to the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/). By participating, you are expected to uphold this code.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for powerful video downloading capabilities.
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) for seamless Telegram API integration.
- Built with ❤️ by [ifauzeee](https://github.com/ifauzeee).

Happy downloading! 🎉
