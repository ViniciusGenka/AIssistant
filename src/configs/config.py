from configparser import ConfigParser
import sys
import os

def get_config():
  config = ConfigParser()
  config.read(os.path.join(os.path.dirname(__file__), "../../config.ini"))
  section_key_configs = {
      "access": ["openai_api_key", "picovoice_access_key"],
      "voice": ["input_voice_language", "output_voice_index", "output_voice_speed", "output_voice_volume","input_adjust_for_ambient_noise", "input_voice_pause_threshold", "input_energy_threshold", "input_dynamic_energy_threshold"],
      "chatgpt": ["gpt_model", "context_threshold", "chat_name", "aditional_prompt"]
  }
  for section, keys in section_key_configs.items():
    for key in keys:
      if not config.has_section(section) or not config.has_option(section, key) or (key != "aditional_prompt" and not config[section][key]):
        print(f"Missing '{key}' in the '{section}' section of the config file.")
        sys.exit(1)
  return config