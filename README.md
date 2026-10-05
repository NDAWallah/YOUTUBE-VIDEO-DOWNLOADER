YouTube Video Downloader
A simple web app (Flask + yt-dlp) to download YouTube videos as MP4 or audio as MP3.
Requirements
Python 3.9+
FFmpeg installed and on your PATH (needed to merge video/audio and make MP3)
Setup
git clone https://github.com/NDAWallah/YOUTUBE-VIDEO-DOWNLOADER.git
cd YOUTUBE-VIDEO-DOWNLOADER
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
Open http://127.0.0.1:5000
Usage
Paste a YouTube link and click Fetch.
Choose Video (MP4) with a quality, or Audio (MP3).
Click Download.
Tips
If downloads stop working, update yt-dlp: pip install -U yt-dlp
Playlists are not supported (single videos only).
Disclaimer
For personal use only. Download only content you own or have permission to save, and respect YouTube's Terms of Service and copyright law.
License
MIT