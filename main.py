from fastapi import FastAPI, Query, Path, Response
from subtitles import get_subtitles
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

    return subtitles
