import os
import sqlite3

def save_interaction(interaction, chat_id):
  connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), "aissistant.db"))
  connection.execute('''CREATE TABLE IF NOT EXISTS interactions
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    role TEXT,
                    content TEXT,
                    chat_id INTEGER,
                    FOREIGN KEY(chat_id) REFERENCES chats(id))''')
  connection.execute("INSERT INTO interactions (role, content, chat_id) VALUES (?, ?, ?)", (interaction["role"], interaction["content"], chat_id))
  connection.commit()
  connection.close()

def find_interactions_by_chat_id(chat_id):
  connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), "aissistant.db"))
  connection.execute('''CREATE TABLE IF NOT EXISTS interactions
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        role TEXT,
                        content TEXT,
                        chat_id INTEGER,
                        FOREIGN KEY(chat_id) REFERENCES chats(id))''')
  cursor = connection.cursor()
  cursor.execute("SELECT role, content FROM interactions WHERE chat_id = ?", (chat_id,))
  rows = cursor.fetchall()
  interactions = [{"role": row[0], "content": row[1]} for row in rows]
  connection.close()
  return interactions