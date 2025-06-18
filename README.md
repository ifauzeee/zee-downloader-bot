Zee Downloader Bot 🚀
A powerful Telegram bot for downloading YouTube and TikTok videos with ease. Supports multiple quality options up to 4K, real-time progress updates, and a seamless user experience.
 
Features ✨

📹 Download videos from YouTube and TikTok.
🎥 Choose from multiple video qualities (up to 4K when available).
⏳ Real-time download progress with percentage, speed, and ETA.
🔒 Secure handling of sensitive data (API tokens and cookies).
🐍 Built with Python, yt-dlp, and python-telegram-bot.

Prerequisites 🛠️
Before running the bot, ensure you have:

Python 3.8+
A Telegram bot token from BotFather
Cookies file for YouTube/TikTok authentication (Netscape format)

Installation 📥

Clone the repository:git clone https://github.com/ifauzeee/zee-downloader-bot.git
cd zee-downloader-bot


Set up a virtual environment:python3 -m venv venv
source venv/bin/activate


Install dependencies:pip install -r requirements.txt


Create .env file:echo "TELEGRAM_BOT_TOKEN=your_bot_token_here" > .env

Replace your_bot_token_here with your Telegram bot token.
Prepare cookies:
Export cookies for youtube.com and tiktok.com using a browser extension (e.g., EditThisCookie).
Save as cookies.txt in the project root (ensure listed in .gitignore).


Run the bot:python3 bot.py



Usage 📖

Start the bot on Telegram by sending /start.
Send a YouTube or TikTok video URL.
Choose the desired video quality from the provided options.
Wait for the bot to download and send the video file.

Example Commands

/start - Initialize the bot.
Send a link like https://www.youtube.com/watch?v=iVrjwy0foF4 to start downloading.

Dependencies 📦

yt-dlp: For video downloading.
python-telegram-bot: For Telegram API integration.
python-dotenv: For environment variable management.

Contributing 🤝
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a Pull Request.

License 📝
This project is licensed under the MIT License. See LICENSE for details.
Acknowledgments 🙌

yt-dlp for video downloading capabilities.
python-telegram-bot for Telegram integration.
Built with ❤️ by ifauzeee.


Happy downloading! 🎉
