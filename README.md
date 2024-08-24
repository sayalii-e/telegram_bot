
# Telegram UUID Linker: Flask Web App & Bot Integration

This project consists of a simple Flask web application and a Telegram bot that work together. The Flask app generates unique user links using a UUID stored in a SQLite database. The Telegram bot interacts with users and adds their records to the database, assigning them unique UUIDs.

## Prerequisites

- Python 3.x

- Telegram Bot Token (Refer to Telegram BotFather to create your bot and obtain an API token)


## Installation

Clone the project

```bash
  git clone https://github.com/sayalii-e/telegram_bot
```

Create and Activate a Virtual Environment

```bash
  python3 -m venv venv
  source venv\Scripts\activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```


## Running the Telegram Bot

Start the bot by running the following command:

```bash
  python bot.py
```

## Running the Flask App

Start the Flask server

```bash
  python app.py
```

**Bot Username : trent3bot**

Open Telegram and search for bot using its username.

Interact with the bot:

- /start: Welcomes the user.
- /create: Creates a new record in the database with the user's first name, last name, and a unique UUID.

## Environment Variables

To run this project, you will need to add the following environment variables to your **config.py** file

`API_TOKEN`


## Using the Bot

**Bot Username : trent3bot**

- Start a conversation with the bot by searching for its username in Telegram.

- Use the **/start** command to get a welcome message.

- Use the **/create** command to generate a unique UUID. The bot will store your first name, last name, and UUID in the **user.db** SQLite database.

- The bot will respond with a message containing your unique UUID.

- Go to the Flask app (http://127.0.0.1:5000/link/<uuid>), replacing <uuid> with your generated UUID. You will see a message showing your Telegram details along with your UUID.

## Screenshots
1. **Bot username: trent3bot**
![bot_1](https://github.com/user-attachments/assets/80f513ab-d3a7-42ba-8585-909cd6f06905)

2. /start:
![bot_2](https://github.com/user-attachments/assets/b296bb39-9725-456f-945e-0d5d6ef77932)

3. /create:
![bot_3](https://github.com/user-attachments/assets/95cfcdec-4285-4202-b0a5-c519dce7068b)

4. Navigate to: http://127.0.0.1:5000/
![bot_4](https://github.com/user-attachments/assets/48376e0b-83a1-4c6a-b454-8f8d7bf684e2)

5. Navigate to: http://127.0.0.1:5000/link/c587844e-104f-4c22-80a1-4a5c64c0f853/
![bot_5](https://github.com/user-attachments/assets/0490a8c3-04a8-4f73-840c-a23a2b1137cd)
