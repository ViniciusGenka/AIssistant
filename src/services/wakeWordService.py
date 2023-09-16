import struct
import pyaudio, pvporcupine
from configs.config import get_config

class WakeWordService():
  def __init__(self):
    self.config = get_config()
    self.porcupine_computer = pvporcupine.create(keywords=["computer"], access_key=self.config["access"]["picovoice_access_key"])
    self.porcupine_jarvis = pvporcupine.create(keywords=["jarvis"], access_key=self.config["access"]["picovoice_access_key"])
    self.pa = pyaudio.PyAudio()
    self.audio_stream = self.pa.open(
                  rate=self.porcupine_computer.sample_rate,
                  channels=1,
                  format=pyaudio.paInt16,
                  input=True,
                  frames_per_buffer=self.porcupine_computer.frame_length)

  def listen_wakeword(self):
    print("Waiting for the wake word...")
    while True:
      pcm = self.audio_stream.read(self.porcupine_computer.frame_length)
      pcm = struct.unpack_from("h" * self.porcupine_computer.frame_length, pcm)
      keyword_index = self.porcupine_computer.process(pcm)
      if keyword_index >= 0:
        return "computer"

      keyword_index = self.porcupine_jarvis.process(pcm)
      if keyword_index >= 0:
        return "jarvis"
  
  def stop(self):
    self.audio_stream.close()
    self.pa.terminate()
    self.porcupine_computer.delete()
    self.porcupine_jarvis.delete()