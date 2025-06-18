Zee Downloader Bot 🚀
 A powerful Telegram bot for downloading YouTube and TikTok videos with ease. Supports multiple quality options up to 4K, real-time progress updates, and a seamless user experience.

 ![Bot Demo](https://via.placeholder.com/800x400.png?text=Zee+Downloader+Bot+Demo) <!-- Ganti dengan screenshot bot jika ada -->

 ## Features ✨
 - 📹 Download videos from YouTube and TikTok.
 - 🎥 Choose from multiple video qualities (up to 4K when available).
 - ⏳ Real-time download progress with percentage, speed, and ETA.
 - 🔒 Secure handling of sensitive data (API tokens and cookies).
 - 🐍 Built with Python, `yt-dlp`, and `python-telegram-bot`.

 ## Prerequisites 🛠️
 Before running the bot, ensure you have:
 - Python 3.8+
 - A Telegram bot token from [BotFather](https://t.me/BotFather)
 - Cookies file for YouTube/TikTok authentication (Netscape format)

 ## Installation 📥
 1. **Clone the repository**:
    ```bash
    git clone https://github.com/ifauzeee/zee-downloader-bot.git
    cd zee-downloader-bot
    ```
 2. **Set up a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
 3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
 4. **Create `.env` file**:
    ```bash
    echo "TELEGRAM_BOT_TOKEN=your_bot_token_here" > .env
    ```
    Replace `your_bot_token_here` with your Telegram bot token.
 5. **Prepare cookies**:
    - Export cookies for `youtube.com` and `tiktok.com` using a browser extension (e.g., [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg)).
    - Save as `cookies.txt` in the project root (ensure listed in `.gitignore`).
 6. **Run the bot**:
    ```bash
    python3 bot.py
    ```

 ## Usage 📖
 1. Start the bot on Telegram by sending `/start`.
 2. Send a YouTube or TikTok video URL.
 3. Choose the desired video quality from the provided options.
 4. Wait for the bot to download and send the video file.

 ## Example Commands
 - `/start` - Initialize the bot.
 - Send a link like `https://www.youtube.com/watch?v=iVrjwy0foF4` to start downloading.

 ## Dependencies 📦
 - `yt-dlp`: For video downloading.
 - `python-telegram-bot`: For Telegram API integration.
 - `python-dotenv`: For environment variable management.

 ## Contributing 🤝
 Contributions are welcome! To contribute:
 1. Fork the repository.
 2. Create a new branch (`git checkout -b feature/your-feature`).
 3. Commit your changes (`git commit -m "Add your feature"`).
 4. Push to the branch (`git push origin feature/your-feature`).
 5. Open a Pull Request.

 ## License 📝
 This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

 ## Acknowledgments 🙌
 - [yt-dlp](https://github.com/yt-dlp/yt-dlp) for video downloading capabilities.
 - [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) for Telegram integration.
 - Built with ❤️ by [ifauzeee](https://github.com/ifauzeee).

 ---

 **Happy downloading!** 🎉

