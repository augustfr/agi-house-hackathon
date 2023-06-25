from queue import Queue
from elevenlabs import generate, play

class SpeechSynthesizer:
    def __init__(self):
        self.queue = Queue()
        self.playing = False
        self.stop_requested = False

    def add_to_queue(self, text: str):
        audio = generate(text)
        duration = len(audio) / 44100  # Assuming sample rate is 44100 Hz
        self.queue.put((audio, duration))

    def start(self):
        if not self.playing:
            self.playing = True
            self.stop_requested = False
            self._play_queue()

    def stop(self):
        self.stop_requested = True

    def _play_queue(self):
        while not self.queue.empty() and not self.stop_requested:
            audio, duration = self.queue.get()
            print(f"Playing audio for {duration} seconds")
            play(audio)
        self.playing = False

# Usage example:
synthesizer = SpeechSynthesizer()
synthesizer.add_to_queue("Hello, this is the first message.")
synthesizer.add_to_queue("And this is the second message.")
synthesizer.start()

