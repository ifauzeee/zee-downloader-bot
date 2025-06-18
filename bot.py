import os
import time
import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import yt_dlp
from dotenv import load_dotenv

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DOWNLOAD_PATH = "downloads"

if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)

async def start(update, context):
    await update.message.reply_text("Kirim link YouTube/TikTok untuk unduh video.")

async def progress_hook(d, context, chat_id, message_id, last_update):
    if d['status'] == 'downloading':
        percent = d.get('downloaded_bytes', 0) / d.get('total_bytes', 1) * 100
        speed = d.get('speed', 0) / 1024 / 1024  # MB/s
        eta = d.get('eta', 0)  # Detik
        current_time = time.time()
        # Update setiap 2 detik atau setiap 5% progres
        if current_time - last_update[0] >= 2 or percent - last_update[1] >= 5:
            logger.info(f"Progress: {percent:.1f}% at {speed:.2f} MB/s, ETA {eta}s")
            await context.bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=f"Downloading: {percent:.1f}% ({speed:.2f} MB/s, ETA {eta//60:02d}:{eta%60:02d})"
            )
            last_update[0] = current_time
            last_update[1] = percent
    elif d['status'] == 'finished':
        logger.info("Download finished")
        await context.bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="Download selesai, memproses..."
        )

async def get_quality_options(url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Prioritaskan 4K
        'cookiefile': '/home/zee/zee-downloader-bot/cookies.txt',  # Path lengkap cookies
        'http_chunk_size': 10485760,  # 10 MB chunks
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        formats = info.get('formats', [])
        quality_options = []
        seen_resolutions = set()
        for f in sorted(formats, key=lambda x: x.get('height', 0) or 0, reverse=True):
            res = f.get('height')
            if res and isinstance(res, int) and res not in seen_resolutions and f.get('ext') == 'mp4':
                quality_options.append({
                    'format_id': f['format_id'],
                    'resolution': f"{res}p",
                    'size': f.get('filesize', 0) / 1024 / 1024 or 'N/A'
                })
                seen_resolutions.add(res)
        return quality_options[:3]  # Batasi 3 opsi

async def download_video(update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    chat_id = update.message.chat_id
    context.user_data['url'] = url
    try:
        quality_options = await get_quality_options(url)
        if not quality_options:
            await update.message.reply_text("Tidak ada opsi kualitas tersedia.")
            return

        keyboard = [[InlineKeyboardButton(
            f"{q['resolution']} (~{q['size'] if q['size'] != 'N/A' else 'ukuran tidak diketahui'} MB)",
            callback_data=q['format_id']
        )] for q in quality_options]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Pilih kualitas video:", reply_markup=reply_markup)
    except Exception as e:
        logger.error(f"Error in download_video: {str(e)}")
        await update.message.reply_text(f"Error: {str(e)}")

async def quality_selected(update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    chat_id = query.message.chat_id
    format_id = query.data
    url = context.user_data.get('url')

    try:
        message = await context.bot.send_message(chat_id=chat_id, text="Sabar ya derrr")
        last_update = [time.time(), 0]  # [last_update_time, last_percent]
        ydl_opts = {
            'outtmpl': f'{DOWNLOAD_PATH}/%(title)s.%(ext)s',
            'format': f'{format_id}+bestaudio[ext=m4a]/best[ext=mp4]',
            'merge_output_format': 'mp4',
            'progress_hooks': [lambda d: progress_hook(d, context, chat_id, message.message_id, last_update)],
            'retries': 5,
            'http_timeout': 30,
            'retry_sleep': 10,
            'cookiefile': '/home/zee/zee-downloader-bot/cookies.txt',
            'http_chunk_size': 10485760,  # 10 MB chunks
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)
        with open(file_path, 'rb') as video:
            await context.bot.send_document(chat_id=chat_id, document=video)
        os.remove(file_path)
        await context.bot.send_message(chat_id=chat_id, text="Download selesai!")
    except Exception as e:
        logger.error(f"Error in quality_selected: {str(e)}")
        await context.bot.send_message(chat_id=chat_id, text=f"Error: {str(e)}")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))
    app.add_handler(CallbackQueryHandler(quality_selected))
    app.run_polling()

if __name__ == "__main__":
    main()
