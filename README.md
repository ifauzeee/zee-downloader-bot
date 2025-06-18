Tentu! Berikut adalah isi `README.md` dalam satu kotak agar mudah disalin:

````
# Zee Downloader Bot

A sleek Telegram bot for downloading YouTube and TikTok videos effortlessly. Choose from multiple quality options (up to 4K), track progress in real-time, and enjoy a smooth user experience.

---

## 📋 Overview

- **Platform**: Telegram  
- **Tech Stack**: Python, yt-dlp, python-telegram-bot, python-dotenv  
- **Features**: Video downloads, quality selection, progress tracking, secure configuration  
- **License**: MIT License

---

## 🚀 Features

- Download videos from **YouTube** and **TikTok** with ease.
- Select video quality up to **4K** (when available).
- Real-time progress updates: percentage, speed, and ETA.
- Secure handling of sensitive data via `.env` and `.gitignore`.
- Lightweight and easy to deploy.

---

## 🛠️ Requirements

- **Python** 3.8+
- **Telegram bot token** from BotFather
- **Cookies file** for YouTube/TikTok (Netscape format)

---

## 🔧 Installation

### 1. Clone the repository:

```bash
git clone https://github.com/ifauzeee/zee-downloader-bot.git
cd zee-downloader-bot
````

### 2. Set up a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Configure `.env` file:

Create a `.env` file with your Telegram bot token:

```bash
echo "TELEGRAM_BOT_TOKEN=your_bot_token_here" > .env
```

> Replace `your_bot_token_here` with your **Telegram bot token** from [BotFather](https://core.telegram.org/bots#botfather).

### 5. Prepare cookies:

* Export cookies for **youtube.com** and **tiktok.com** using [EditThisCookie](https://www.editthiscookie.com/).
* Save the cookies as `cookies.txt` in the project root (ensure it’s listed in `.gitignore`).

### 6. Run the bot:

```bash
python3 bot.py
```

---

## 🎮 Usage

1. Send `/start` to initialize the bot on Telegram.
2. Share a YouTube or TikTok video URL.
3. Choose the video quality from the options.
4. Receive the downloaded MP4 video.

**Example:**

* `/start` → Welcome message
* `https://www.youtube.com/watch?v=iVrjwy0foF4` → Quality selection → Download

---

## 📦 Dependencies

| Package               | Purpose                         |
| --------------------- | ------------------------------- |
| `yt-dlp`              | Video downloading               |
| `python-telegram-bot` | Telegram API integration        |
| `python-dotenv`       | Environment variable management |

Install dependencies with:

```bash
pip install yt-dlp python-telegram-bot python-dotenv
```

---

## 🤝 Contributing

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

5. Submit a **Pull Request**.

---

## 📜 License

Licensed under the **MIT License**.

---

## 🙏 Acknowledgments

* [yt-dlp](https://github.com/yt-dlp/yt-dlp)
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
* Created by **ifauzeee**

---

**Enjoy downloading!** 🎥

```

Silakan salin seluruh isi di atas. Jika ada hal lain yang perlu diperbaiki atau ditambahkan, beri tahu saya ya!
```
