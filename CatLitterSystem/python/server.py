from flask import Flask
from flask import request

app = Flask(__name__)

# START SERVER ROUTE AT /
@app.route("/")
def home():
    return "Server running"

# START POST ROUTE
@app.route("/upload", methods=["POST"])

def upload():
    return "upload received"

app.run(host="0.0.0.0", port=5000)
