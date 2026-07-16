from flask import Flask, render_template, request, send_from_directory
from pymongo import MongoClient
import os

app = Flask(
    __name__,
    template_folder=".",
    static_folder="."
)

# MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mobile_showroom"]
orders = db["orders"]

# Serve HTML files
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/order")
def order():
    return render_template("order.html")

# Serve CSS & images (IMPORTANT FIX)
@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(".", filename)

# Form submit
@app.route("/submit", methods=["POST"])
def submit():
    orders.insert_one({
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "address": request.form["address"],
        "payment": request.form["payment"]
    })
    return "<h2>✅ Order placed successfully!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
