from flask import Flask
import sqlite3

app = Flask(__name__)

# Create the web server routes
@app.route('/')
def index():
    return "<h1>Go to the bot to get your unique link!</h1>"

@app.route('/link/<uuid>')
def link(uuid):
    # Connect to the SQLite database
    with sqlite3.connect('user.db') as connection:
        cursor = connection.cursor()
        # Query the database to get the user's information based on the UUID
        cursor.execute("SELECT first_name, last_name FROM users WHERE uuid = ?", (uuid,))
        user = cursor.fetchone()
        
        if user:
            first_name, last_name = user
            return f"<h1>{first_name} {last_name}'s Telegram ID is associated with UUID: {uuid}</h1>"
        else:
            return "<h1>Invalid UUID or user not found!</h1>", 404

if __name__ == '__main__':
    app.run(debug=True)