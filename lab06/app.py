import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    return render_template("index.html")


# ВРАЗЛИВА ВЕРСІЯ
@app.route("/search_vulnerable", methods=["POST"])
def search_vulnerable():
    login = request.form.get("login")

    query = "SELECT * FROM users WHERE login = '" + login + "'"

    conn = get_db()
    try:
        users = conn.execute(query).fetchall()
    except sqlite3.Error:
        users = []
    conn.close()

    return render_template(
        "index.html",
        users=users,
        mode="Вразлива версія"
    )


# ЗАХИЩЕНА ВЕРСІЯ
@app.route("/search_secure", methods=["POST"])
def search_secure():
    login = request.form.get("login")

    query = "SELECT * FROM users WHERE login = ?"

    conn = get_db()
    users = conn.execute(query, (login,)).fetchall()
    conn.close()

    return render_template(
        "index.html",
        users=users,
        mode="Захищена версія"
    )


if __name__ == "__main__":
    app.run(debug=True)
