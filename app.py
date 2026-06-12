from flask import Flask, render_template, request, redirect, session, flash
import sqlite3
import bcrypt
import re
from database import init_db
import os
app = Flask(__name__)

# Secret Key for Session Management
app.config["SECRET_KEY"] = os.environ.get(
    "SECRET_KEY",
    "fallback-secret-key"
)
# Initialize Database
init_db()

def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn


# Home Route
@app.route("/")
def home():
    if "user_id" in session:
        return redirect("/dashboard")
    return redirect("/login")


# Register Route
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"].strip()
        email = request.form["email"].strip()
        password = request.form["password"]

        # Username Validation
        if len(username) < 3:
            flash("Username must be at least 3 characters", "danger")
            return redirect("/register")

        # Email Validation
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(email_pattern, email):
            flash("Invalid email format", "danger")
            return redirect("/register")

        # Password Validation
        if (
            len(password) < 8 or
            not re.search(r"[A-Z]", password) or
            not re.search(r"[a-z]", password) or
            not re.search(r"\d", password)
        ):
            flash(
                "Password must contain at least 8 characters, one uppercase letter, one lowercase letter and one number",
                "danger"
            )
            return redirect("/register")

        # Hash Password
        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                INSERT INTO users
                (username, email, password_hash)
                VALUES (?, ?, ?)
                """,
                (username, email, hashed_password)
            )

            conn.commit()

            flash("Registration successful. Please login.", "success")

        except sqlite3.IntegrityError:
            flash("Email already registered.", "danger")

        finally:
            conn.close()

        return redirect("/login")

    return render_template("register.html")


# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"].strip()
        password = request.form["password"]

        conn = get_db_connection()

        user = conn.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        ).fetchone()

        conn.close()

        if user:

            stored_hash = user["password_hash"]

            if bcrypt.checkpw(
                password.encode("utf-8"),
                stored_hash
            ):
                session["user_id"] = user["id"]
                session["username"] = user["username"]

                flash("Login successful.", "success")

                return redirect("/dashboard")

        flash("Invalid email or password.", "danger")

        return redirect("/login")

    return render_template("login.html")


# Protected Dashboard
@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        flash("Please login first.", "warning")
        return redirect("/login")

    return render_template(
        "dashboard.html",
        username=session["username"]
    )


# Logout Route
@app.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully.", "info")

    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)