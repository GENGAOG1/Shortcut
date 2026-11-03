
import os
from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def home():
    icloud_link = os.environ.get("ICLOUD_LINK")

    if not icloud_link:
        return "Shortcut-Link ist nicht konfiguriert.", 500

    return redirect(icloud_link)

if __name__ == "__main__":
    app.run()
