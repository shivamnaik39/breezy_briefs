from fastapi import FastAPI, Query, Path, Response
from captions import get_captions_url
from pydantic import BaseModel
from typing import Optional
import logging
import urllib.parse
import requests

logger = logging.getLogger()

app = FastAPI()


@app.get("/api/captions/{yt_id}")
def get_captions(yt_id: str = Query(title="Youtube URL", description="URL of the youtube video to fetch captions"),
                 language: str = Query(
                     default="en", title="Language", description="Language of the captions if multiple languages are available"),
                 type: str = Query(default="vtt", title="Subtitle Format", description="Format of the subtitles to be fetched")):

    caption_url_res = get_captions_url(
        video_url=yt_id, language=language, type=type)
    # If some error
    if caption_url_res['error'] is True:
        return caption_url_res

    # If no error
    caption_url = caption_url_res['caption_url']

    # Make a request to the URL returned by the youtube API
    response = requests.get(caption_url)

    # Return the response from the second API as the response of the parent API
    return Response(content=response.content, media_type=response.headers["Content-Type"])
