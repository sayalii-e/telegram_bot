from config import API_TOKEN
import telebot
import uuid
import sqlite3

bot = telebot.TeleBot(token=API_TOKEN)

# /start
@bot.message_handler(commands=['start'])
def welcome(message):
    welcome_text = f'User {message.from_user.first_name}, Welcome to the Bot!'
    bot.send_message(message.chat.id, welcome_text)

# Create the database
with sqlite3.connect('user.db') as connection:
    cursor = connection.cursor()
    create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            uuid TEXT
        );
    """
    cursor.execute(create_table_query)

# /create
@bot.message_handler(commands=['create'])
def create_user(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_uuid = str(uuid.uuid4())  # Generate a new UUID

    with sqlite3.connect('user.db') as connection:
        cursor = connection.cursor()
        insert_data_query = """
            INSERT INTO users (first_name, last_name, uuid)
            VALUES (?, ?, ?)
        """
        cursor.execute(insert_data_query, (first_name, last_name, user_uuid))

    bot.send_message(message.chat.id, f"User {first_name}, your unique ID has been created: {user_uuid}")

bot.polling()
