import os
import yt_dlp
from flask import Flask, request, render_template, jsonify, send_file
from dotenv import load_dotenv
import threading
import uuid
import time

app = Flask(__name__)
load_dotenv()

DOWNLOAD_PATH = "downloads"
if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)

download_status = {}

def progress_hook(d, session_id):
    if d['status'] == 'downloading':
        percent = d.get('downloaded_bytes', 0) / d.get('total_bytes', 1) * 100
        speed = d.get('speed', 0) / 1024 / 1024  # MB/s
        download_status[session_id] = {
            'status': 'downloading',
            'percent': percent,
            'speed': speed
        }
    elif d['status'] == 'finished':
        download_status[session_id] = {'status': 'finished'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_qualities', methods=['POST'])
def get_qualities():
    url = request.form['url']
    try:
        ydl_opts = {
            'format': 'best',
            'cookiefile': 'cookies.txt',
            'http_timeout': 60,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'simulate': True  # Force metadata extraction
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])
            quality_options = []
            seen_resolutions = set()
            for f in formats:
                res = f.get('height') or f.get('resolution')
                if res and res not in seen_resolutions and f.get('ext') == 'mp4':
                    filesize = f.get('filesize') or f.get('filesize_approx', 0)
                    if filesize == 0:
                        filesize = 1  # Fallback to avoid division by zero
                    quality_options.append({
                        'format_id': f['format_id'],
                        'resolution': f"{res}p",
                        'size': filesize / 1024 / 1024  # MB
                    })
                    seen_resolutions.add(res)
            time.sleep(1)  # Add delay to avoid rate-limiting
            return jsonify({'qualities': sorted(quality_options, key=lambda x: x['size'])[:3]})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    format_id = request.form['format_id']
    session_id = str(uuid.uuid4())
    download_status[session_id] = {'status': 'starting'}

    def download_video():
        try:
            file_path = os.path.join(DOWNLOAD_PATH, f"video_{session_id}.mp4")
            ydl_opts = {
                'outtmpl': file_path,
                'format': format_id,
                'merge_output_format': 'mp4',
                'progress_hooks': [lambda d: progress_hook(d, session_id)],
                'retries': 5,
                'http_timeout': 60,
                'cookiefile': 'cookies.txt',
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            download_status[session_id]['file_path'] = file_path
        except Exception as e:
            download_status[session_id] = {'status': 'error', 'error': str(e)}

    threading.Thread(target=download_video).start()
    time.sleep(1)  # Add delay to avoid rate-limiting
    return jsonify({'session_id': session_id})

@app.route('/progress/<session_id>')
def progress(session_id):
    status = download_status.get(session_id, {'status': 'not_found'})
    return jsonify(status)

@app.route('/get_file/<session_id>')
def get_file(session_id):
    status = download_status.get(session_id, {})
    if status.get('status') == 'finished' and 'file_path' in status:
        file_path = status['file_path']
        if os.path.exists(file_path):
            response = send_file(file_path, as_attachment=True)
            threading.Thread(target=lambda: time.sleep(5) or os.remove(file_path)).start()  # Delay file deletion
            return response
    return jsonify({'error': 'File not ready or already downloaded'}), 400

if __name__ == '__main__':
    app.run(debug=True)
