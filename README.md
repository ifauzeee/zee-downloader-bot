Zee Downloader Bot 🚀
A powerful Telegram bot designed to download videos from YouTube and TikTok with ease. Supports multiple quality options (up to 4K), real-time progress updates, and a seamless user experience.
 
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

Features ✨

📹 Download videos from YouTube and TikTok with a single command.
🎥 Select from multiple video quality options, including up to 4K when available.
⏳ Real-time download progress with percentage, speed, and estimated time of arrival (ETA).
🔒 Securely handles sensitive data (API tokens and cookies) via environment variables and .gitignore.
🐍 Built with Python, leveraging yt-dlp for robust video downloading.

Prerequisites 🛠️
Before running the bot, ensure you have:

Python 3.8 or higher
A Telegram bot token from BotFather
Cookies file for YouTube/TikTok authentication in Netscape format

Installation 📥
Follow these steps to set up the bot:

Clone the repository:
git clone https://github.com/ifauzeee/zee-downloader-bot.git
cd zee-downloader-bot


Set up a virtual environment:
python3 -m venv venv
source venv/bin/activate


Install dependencies:
pip install -r requirements.txt


Create .env file:
echo "TELEGRAM_BOT_TOKEN=your_bot_token_here" > .env

Replace your_bot_token_here with your Telegram bot token.

Prepare cookies:

Export cookies for youtube.com and tiktok.com using a browser extension like EditThisCookie.
Save the cookies as cookies.txt in the project root (ensure it’s listed in .gitignore).


Run the bot:
python3 bot.py



Usage 📖

Start the bot on Telegram by sending /start.
Send a YouTube or TikTok video URL.
Choose the desired video quality from the provided options.
Wait for the bot to download and send the video file in MP4 format.

Example Commands

/start - Initialize the bot and display a welcome message.
Send a link like https://www.youtube.com/watch?v=iVrjwy0foF4 to start the download process.

Dependencies 📦

yt-dlp: For downloading videos from YouTube and TikTok.
python-telegram-bot: For interacting with the Telegram API.
python-dotenv: For managing environment variables securely.

Install them using:
pip install yt-dlp python-telegram-bot python-dotenv

Contributing 🤝
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch:git checkout -b feature/your-feature


Commit your changes:git commit -m "Add your feature"


Push to the branch:git push origin feature/your-feature


Open a Pull Request on GitHub.

Please ensure your code follows the project’s style and includes appropriate tests.
License 📝
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments 🙌

yt-dlp for its robust video downloading capabilities.
python-telegram-bot for seamless Telegram API integration.
Built with ❤️ by ifauzeee.


Happy downloading! 🎉
