from youtube_transcript_api import YouTubeTranscriptApi
from flask import Flask

app = Flask(__name__)

@app.route('/url/<video_id>', methods=['GET'])
def home(video_id):
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(video_id)
    text_transcript = ""
    for snippet in fetched_transcript:
        text_transcript += snippet.text

    return text_transcript

