from fastapi import FastAPI, Query, Path
from fastapi.responses import JSONResponse
from utils.subtitles import get_subtitles
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


@app.get("/api/captions/{yt_id}")
def get_captions(yt_id: str = Query(title="Youtube URL", description="URL of the youtube video to fetch captions"),
                 language: str = Query(
                     default="en", title="Language", description="Language of the captions if multiple languages are available"),
                 type: str = Query(default="vtt", title="Subtitle Format", description="Format of the subtitles to be fetched")):

    subtitles = get_subtitles(
        video_url=yt_id, language=language, type=type)

    if subtitles['error']:
        return JSONResponse(subtitles, 400)

    else:
        return JSONResponse(subtitles, 200)
