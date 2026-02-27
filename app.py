from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    today = datetime.now().strftime("%d-%b-%Y")
    return render_template("index.html", today=today)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)