# SERVER IMPORTS
from flask import Flask
from flask import request

# FILE IMPORTS
from datetime import datetime
from pathlib import Path

app = Flask(__name__)

# CHECK FILE SAVING DIRECTORY
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True);
    
# START SERVER ROUTE AT /
@app.route("/")
def home():
    return "Server running"

# START POST ROUTE
@app.route("/upload", methods=["POST"])
def upload():
    data = request.data
    
    if len(data) == 0:
        return "No Data Received", 400
    
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.jpg")
    path = UPLOAD_DIR / filename
    
    with open(path, "wb") as file:
        file.write(data)
        
    print (f"Saved {path}")
    
    return f"Saved {filename}"
    
    # print("Received Bytes: ", len(data))
    # return f"Received{len(data)} bytes"

app.run(host="0.0.0.0", port=5000)
