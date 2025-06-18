Zee Downloader Bot 🚀
A powerful Telegram bot for downloading YouTube and TikTok videos with support for multiple quality options (up to 4K) and real-time progress updates.
Table of Contents

Features
Prerequisites
Installation
Usage
Example Commands
Dependencies
Contributing
License
Acknowledgments

Features

📹 Download Videos: Download from YouTube and TikTok with a single command.
🎥 Multiple Quality Options: Choose from various video qualities, up to 4K.
⏳ Real-Time Progress: Track download progress with percentage, speed, and ETA.
🔒 Secure Data Handling: Manage API tokens and cookies via environment variables and .gitignore.
🐍 Python-Powered: Built with Python, leveraging yt-dlp for robust downloading.

Prerequisites

Python 3.8 or higher
Telegram bot token from BotFather
Cookies file for YouTube/TikTok authentication (Netscape format)

Installation

Clone the repository:
git clone https://github.com/ifauzeee/zee-downloader-bot.git
cd zee-downloader-bot


Set up a virtual environment:
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt


Create .env file:
echo "TELEGRAM_BOT_TOKEN=your_bot_token_here" > .env

Replace your_bot_token_here with your Telegram bot token.

Prepare cookies:

Export cookies for youtube.com and tiktok.com using a browser extension (e.g., EditThisCookie).
Save as cookies.txt in the project root (ensure listed in .gitignore).


Run the bot:
python3 bot.py



Usage

Start the bot on Telegram with /start.
Send a YouTube or TikTok video URL.
Select desired video quality from options.
Wait for the bot to download and send the video in MP4 format.

Example Commands

/start - Initialize the bot and view welcome message.
Send a link like https://www.youtube.com/watch?v=iVrjwy0foF4 to start downloading.

Dependencies

yt-dlp: For video downloads.
python-telegram-bot: For Telegram API interactions.
python-dotenv: For secure environment variable management.

Install with:
pip install yt-dlp python-telegram-bot python-dotenv

Contributing

Fork the repository.
Create a new branch:git checkout -b feature/your-feature


Commit changes:git commit -m "Add your feature"


Push to the branch:git push origin feature/your-feature


Open a Pull Request on GitHub.

Ensure code adheres to project style and includes tests.
License
Licensed under the MIT License.
Acknowledgments

yt-dlp for robust video downloading.
python-telegram-bot for seamless Telegram API integration.
Built with ❤️ by ifauzeee.

Happy downloading! 🎉
