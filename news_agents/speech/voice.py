from queue import Queue
from typing import List
from elevenlabs import generate, play, stream
from elevenlabs import set_api_key
from environs import Env
env = Env()
env.read_env()
set_api_key(env("ELEVEN_API_KEY"))


class TextToSpeech:
    def __init__(self, voices: List[str], stream: bool = False):
        self.queue = Queue()
        self.voices = voices
        self.is_playing = False
        self.stream = stream

    def add_to_queue(self, text: str, voice_index: int):
        voice = self.voices[voice_index]
        self.queue.put((text, voice))

    def start(self):
        if not self.is_playing:
            self.is_playing = True
            self._play_queue()

    def stop(self):
        self.is_playing = False

    def _play_queue(self):
        while self.is_playing and not self.queue.empty():
            text, voice = self.queue.get()

            if self.stream:
                audio_stream = generate(text=text, voice=voice, stream=True)
                stream(audio_stream)
            else:
                audio = generate(text=text, voice=voice)
                play(audio)

            self.queue.task_done()

        self.is_playing = False


# voices_list = ["Arnold", "Bella"]
# tts = TextToSpeech(voices_list, stream=True)

# import time


# tts.add_to_queue("Good evening, I'm Sarah Chen. We have a lot on the agenda tonight, but first, the groundbreaking news that's gripping the globe. NASA has just announced a successful landing on Mars, setting a new chapter in human exploration of the Red Planet. This is absolutely insane in the membrane.", 0)
# tts.add_to_queue("Absolutely, Sarah. It's a momentous occasion for all of humanity. We've been following this mission since its launch, with bated breath and anticipation, and it's truly an emotional moment to hear about the successful landing.", 1)

# # start counting time
# start = time.time()
# tts.start()  # This will play all queued items in order
# # print time taken
# print("Time taken: {} seconds".format(time.time() - start))

