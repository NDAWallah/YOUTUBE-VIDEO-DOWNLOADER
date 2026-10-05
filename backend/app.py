import os

from flask import Flask, request, jsonify
from flask_cors import CORS

import yt_dlp


app = Flask(__name__)

CORS(app)


@app.route("/")
def home():

    return jsonify({
        "status": "online",
        "service": "NDA Wallah YouTube Downloader"
    })


@app.route("/api/info")
def video_info():

    url = request.args.get("url", "").strip()

    if not url:

        return jsonify({
            "error": "YouTube URL is required"
        }), 400


    options = {

        "quiet": True,

        "no_warnings": True,

        "skip_download": True,

        "noplaylist": True

    }


    try:

        with yt_dlp.YoutubeDL(options) as ydl:

            info = ydl.extract_info(
                url,
                download=False
            )


        return jsonify({

            "title": info.get("title"),

            "uploader": info.get("uploader"),

            "duration": info.get("duration"),

            "thumbnail": info.get("thumbnail"),

            "webpage_url":
                info.get("webpage_url", url)

        })


    except Exception as error:

        return jsonify({

            "error": str(error)

        }), 500


if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            10000
        )
    )

    app.run(
        host="0.0.0.0",
        port=port
    )