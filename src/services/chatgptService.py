import openai
from configs.config import get_config
from repositories.chatRepository import find_chat_by_name
from repositories.interactionRepository import find_interactions_by_chat_id, save_interaction

class ChatgptService():
  def __init__(self):
    self.config = get_config()
    self.chat_name = self.config["chatgpt"]["chat_name"]
    self.context_threshold = int(self.config["chatgpt"]["context_threshold"])
    self.gpt_model = self.config["chatgpt"]["gpt_model"]
    self.aditional_prompt = self.config["chatgpt"]["aditional_prompt"] + " " if self.config["chatgpt"]["aditional_prompt"] != "" else ""
    openai.api_key = self.config["access"]["openai_api_key"]

  def ask_chatgpt(self, question):
    prompt = self.aditional_prompt + question
    print(prompt)
    chat = find_chat_by_name(self.chat_name)
    context = find_interactions_by_chat_id(chat[0])
    context.append(
      {"role": "user", "content": prompt}
    )
    save_interaction(context[-1], chat[0])
    chatgpt_context_slice = context[-(self.context_threshold * 2 + 1):]
    completion = openai.ChatCompletion.create(
        model = self.gpt_model,
        messages = chatgpt_context_slice
    )
    answer = completion['choices'][0]['message']['content']
    context.append(
      {"role": "assistant", "content": answer},
    )
    save_interaction(context[-1], chat[0])
    return answer