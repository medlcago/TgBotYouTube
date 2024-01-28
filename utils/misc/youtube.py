import io
import logging

from pytube import YouTube


class Youtube(YouTube):
    @property
    def get_video_preview(self):
        return f"https://img.youtube.com/vi/{self.video_id}/maxresdefault.jpg"

    def download_video(self) -> bytes | None:
        result = None
        try:
            with io.BytesIO() as output:
                streams = self.streams.get_highest_resolution()
                streams.stream_to_buffer(output)
                result = output.getvalue()
        except Exception as error:
            logging.error(error)
        return result

    def download_audio(self) -> bytes | None:
        result = None
        try:
            with io.BytesIO() as output:
                streams = self.streams.get_audio_only()
                streams.stream_to_buffer(output)
                result = output.getvalue()
        except Exception as error:
            logging.error(error)
        return result
