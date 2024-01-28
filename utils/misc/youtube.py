import asyncio
import io
import logging
from concurrent.futures import ThreadPoolExecutor

from pytube import YouTube


class Youtube(YouTube):
    @property
    def get_video_preview(self):
        return f"https://img.youtube.com/vi/{self.video_id}/maxresdefault.jpg"

    async def download_video(self) -> bytes | None:
        result = None
        try:
            with io.BytesIO() as output:
                streams = self.streams.get_highest_resolution()
                loop = asyncio.get_event_loop()
                with ThreadPoolExecutor() as pool:
                    await loop.run_in_executor(pool, streams.stream_to_buffer, output)
                result = output.getvalue()
        except Exception as error:
            logging.error(error)
        return result

    async def download_audio(self) -> bytes | None:
        result = None
        try:
            with io.BytesIO() as output:
                streams = self.streams.get_audio_only()
                loop = asyncio.get_event_loop()
                with ThreadPoolExecutor() as pool:
                    await loop.run_in_executor(pool, streams.stream_to_buffer, output)
                result = output.getvalue()
        except Exception as error:
            logging.error(error)
        return result
