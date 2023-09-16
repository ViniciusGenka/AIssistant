import os
import sqlite3

def find_chat_by_name(chat_name):
  connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), "aissistant.db"))
  connection.execute('''CREATE TABLE IF NOT EXISTS chats
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)''')
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM chats WHERE name = ?", (chat_name,))
  chat = cursor.fetchone()
  connection.close
  return chat

def save_chat(chat_name):
  connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), "aissistant.db"))
  connection.execute('''CREATE TABLE IF NOT EXISTS chats
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT)''')
  connection.execute("INSERT INTO chats (name) VALUES (?)", (chat_name,))
  chat = find_chat_by_name(chat_name)
  connection.commit()
  connection.close()
  return chat
