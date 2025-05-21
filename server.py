from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig
from flask import Flask
from dotenv import load_dotenv
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/url/<video_id>', methods=['GET'])
def home(video_id):
    ytt_api = YouTubeTranscriptApi(
    proxy_config=WebshareProxyConfig(
        proxy_username=os.getenv("USERNAME"),
        proxy_password=os.getenv("PASSWORD"),
    )
)
    fetched_transcript = ytt_api.fetch(video_id)
    text_transcript = ""
    for snippet in fetched_transcript:
        text_transcript += snippet.text

    return text_transcript

