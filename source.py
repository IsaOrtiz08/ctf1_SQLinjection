from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Flag for the challenge
FLAG = "flag{SQL_1nj3ct10n_success!}"

# Set up the database
def init_db():
    conn = sqlite3.connect("ctf.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'password123')")
    conn.commit()
    conn.close()

# Vulnerable login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Vulnerable SQL query
        conn = sqlite3.connect("ctf.db")
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("Executing query:", query)
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()

        if result:
            # Successful login
            return render_template("success.html", username=username, flag=FLAG)
        else:
            # Failed login
            return render_template("error.html")

    # Render the login page from index.html
    return render_template("index.html")

if __name__ == "__main__":
    init_db()  # Initialize the database with test data
    app.run(debug=True)
