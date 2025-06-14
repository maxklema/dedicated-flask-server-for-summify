from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig
from flask import Flask
# from dotenv import load_dotenv
# import os
from flask_cors import CORS
from requests import session
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route('/<video_id>', methods=['GET'])
def home(video_id):

    url = "https://youtube-transcriptor.p.rapidapi.com/transcript?video_id=" + video_id + "&lang=en" # Replace with your target URL

    headers = {
        'x-rapidapi-host': 'youtube-transcriptor.p.rapidapi.com',
        'x-rapidapi-key': ''
    }

    session = requests.Session()
    response = session.get(url, headers=headers)

    responseRaw = (response.text)[1:(len(response.text)-1)] # remove enclosed brackets
    responseJSON = json.loads(responseRaw)

    return responseJSON["transcriptionAsText"]

