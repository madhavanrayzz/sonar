import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()

# Function to insert user input into the database (vulnerable to SQLi)
def insert_user(username, password):
    # Vulnerable: Directly concatenating user input into SQL query
    query = "INSERT INTO users (username, password) VALUES ('" + username + "', '" + password + "')"
    cursor.execute(query)
    conn.commit()
    print("User inserted successfully.")

# Example usage: Get input from user
user_input_username = input("Enter username: ")
user_input_password = input("Enter password: ")

# Call the vulnerable function
insert_user(user_input_username, user_input_password)

# Close the connection
conn.close()
