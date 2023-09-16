import sys, pyperclip
from configs.config import get_config
from repositories.chatRepository import find_chat_by_name, save_chat
from services.chatgptService import ChatgptService
from services.wakeWordService import WakeWordService
from services.dialogService import DialogService

config = get_config()
if not find_chat_by_name(config["chatgpt"]["chat_name"]):
  save_chat(config["chatgpt"]["chat_name"])
question_counter = 0
wake_word_service = WakeWordService()
dialog_service = DialogService()
chatgpt_service = ChatgptService()
print("""
  ___  _____        _     _              _   
 / _ \|_   _|      (_)   | |            | |  
/ /_\ \ | | ___ ___ _ ___| |_ __ _ _ __ | |_ 
|  _  | | |/ __/ __| / __| __/ _` | '_ \| __|
| | | |_| |\__ \__ \ \__ \ || (_| | | | | |_ 
\_| |_/\___/___/___/_|___/\__\__,_|_| |_|\__|               
        """)
print("To ask a question, say either 'computer' for regular questions or 'jarvis' for clipboard-based questions.")
while True:
  try:
    wake_word = wake_word_service.listen_wakeword()
    question = dialog_service.listen() if wake_word == "computer" else dialog_service.listen() + ": " + pyperclip.paste()
    if question is None:
       continue
    question_counter += 1
    print(f"{question_counter}th Question: {question}")
    chatgpt_response = chatgpt_service.ask_chatgpt(question)
    print("Answer:", chatgpt_response)
    dialog_service.speak(chatgpt_response)
    print("-------------------------------------------")
  except KeyboardInterrupt:
      wake_word_service.stop()
      print("Turning off AIssistant.")
      sys.exit(0)