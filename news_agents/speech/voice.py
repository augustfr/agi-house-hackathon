from queue import Queue
from typing import List
from elevenlabs import generate, stream
from elevenlabs import set_api_key
from environs import Env

env = Env()
env.read_env()
set_api_key(env("ELEVEN_API_KEY"))

from threading import Thread


class SpeechQueue:
    def __init__(self):
        self.queue = Queue()
        self.playing = False
        self.stop_flag = False
        self.current_thread = None

    def add_text(self, text: str, voice: str):
        self.queue.put((text, voice))

    def start(self):
        if not self.playing:
            self.playing = True
            self.stop_flag = False
            self.current_thread = Thread(target=self._play_queue)
            self.current_thread.start()

    def stop(self):
        self.stop_flag = True
        if self.current_thread is not None:
            self.current_thread.join()
            self.current_thread = None
        self.playing = False

    def _play_queue(self):
        while not self.stop_flag and not self.queue.empty():
            text, voice = self.queue.get()
            audio_stream = generate(text, voice=voice, stream=True)
            stream(audio_stream)
            self.queue.task_done()
        self.playing = False


# speech_queue = SpeechQueue()
# speech_queue.add_text("Hello, this is Arnold speaking.", "Arnold")
# speech_queue.add_text("Now, this is Bella.", "Bella")

# speech_queue.add_text("Sup man", "Bella")
