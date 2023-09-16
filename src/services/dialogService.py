import os, pyttsx3, speech_recognition as sr
import threading
from playsound import playsound
from configs.config import get_config

class DialogService:
  def __init__(self):
    self.config = get_config()
    self.recognizer = sr.Recognizer()
    self.recognizer.pause_threshold = float(self.config["voice"]["input_voice_pause_threshold"])
    self.recognizer.dynamic_energy_threshold = bool(self.config["voice"]["input_dynamic_energy_threshold"])
    self.recognizer.energy_threshold = int(self.config["voice"]["input_energy_threshold"])
    self.engine = pyttsx3.init()
    self.voices = self.engine.getProperty('voices')
    self.engine.setProperty('voice', self.voices[int(self.config["voice"]["output_voice_index"])].id)
    self.engine.setProperty('rate', int(self.config["voice"]["output_voice_speed"]))
    self.engine.setProperty('volume', float(self.config["voice"]["output_voice_volume"]))

  def listen(self):
    with sr.Microphone() as source:
      if self.config["voice"]["input_adjust_for_ambient_noise"] == 'True':
        self.recognizer.adjust_for_ambient_noise(source)
      threading.Timer(0.1, playsound, (os.path.join(os.path.dirname(__file__), "../resources/listening.wav"),)).start()
      threading.Timer(0.1, print, ("I'm listening, ask your question.",)).start()
      audio = self.recognizer.listen(source)
      try:
        question = self.recognizer.recognize_google(audio, language=self.config["voice"]["input_voice_language"])
        return question
      except sr.UnknownValueError:
        print("Couldn't recognize the question.")
      except sr.RequestError as e:
        print(f"Request error: {e}")
  
  def speak(self, text):
    self.engine.say(text)
    self.engine.runAndWait()
    self.engine.stop()