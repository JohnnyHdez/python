from flask import Flask
from datetime import datetime
from flask import render_template
from flask import request
import sqlite3
import os


app = Flask(__name__)

db = sqlite3.connect(os.path.join('static', 'blog_posts.db'))
cursor = db.cursor()
query = "SELECT title, comment FROM posts"
fetch = cursor.execute(query)
MY_TOKEN = "JohnnyHernandez2023+superWow4ever"

@app.route("/")
def home():
    title = request.form.get("title")
    comment = request.form.get("comment")
    return render_template("index.html", title=title, comment=comment)

@app.route("/add-post", methods=["POST", "GET"])
def add_post():
    return render_template("add-post.html")

@app.route("/crear", methods=["POST"])
def crear_post():
    title = request.form.get("title")
    comment = request.form.get("comment")
    return render_template("index.html", title=title, comment=comment)
if __name__ == "__main__":
    app.run(debug=True)
