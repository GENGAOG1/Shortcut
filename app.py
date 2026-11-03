
import os
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

ICLOUD_LINK = os.environ.get("ICLOUD_LINK", "")

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>System Access</title>

<style>
* {
    box-sizing: border-box;
}

body {
    background: #030303;
    color: #00ff41;
    font-family: monospace;
    margin: 0;
    padding: 20px;
    min-height: 100vh;
    overflow: hidden;
}

.container {
    max-width: 700px;
    margin: 60px auto;
}

h1 {
    color: #ff3333;
    font-size: 28px;
    text-shadow: 0 0 15px red;
    animation: glitch 1s infinite;
}

.terminal {
    border: 1px solid #00ff41;
    padding: 20px;
    box-shadow: 0 0 20px #00ff4133;
    background: #050505;
    min-height: 280px;
}

.line {
    margin: 12px 0;
    opacity: 0;
    animation: appear 0.3s forwards;
}

.warning {
    color: red;
}

.progress {
    width: 100%;
    height: 8px;
    background: #111;
    margin-top: 20px;
}

.bar {
    width: 0%;
    height: 100%;
    background: #00ff41;
    box-shadow: 0 0 10px #00ff41;
    transition: width 0.2s;
}

.final {
    margin-top: 30px;
    color: red;
    font-size: 22px;
    display: none;
    text-align: center;
    animation: glitch 0.5s infinite;
}

@keyframes appear {
    to { opacity: 1; }
}

@keyframes glitch {
    0%, 100% { transform: translateX(0); }
    20% { transform: translateX(-2px); }
    40% { transform: translateX(2px); }
    60% { transform: translateX(-1px); }
}

@media(max-width: 600px) {
    .container {
        margin-top: 30px;
    }

    h1 {
        font-size: 22px;
    }
}
</style>
</head>

<body>
<div class="container">

<h1>ACCESS DENIED</h1>

<div class="terminal">
    <div id="logs"></div>

    <div class="progress">
        <div class="bar" id="bar"></div>
    </div>
</div>

<div class="final" id="final">
   HOW DID YOU FIND THIS? YOU SHOULD NOT BE HERE. BUT YOU CAN STAY. YOUR DATA IS ALREADY MINE. :)
</div>

</div>

<script>
const messages = [
    "[ OK ] Initializing system...",
    "[ OK ] Browser detected",
    "[ OK ] Operating system identified",
    "[ OK ] Establishing secure connection...",
    "[ WARN ] Unexpected visitor detected",
    "[ OK ] Checking system integrity...",
    "[ ERR ] Unauthorized access",
    "[ WARN ] Something went wrong...",
    "[ OK ] Terminating session..."
];

const logs = document.getElementById("logs");
const bar = document.getElementById("bar");
const final = document.getElementById("final");

let index = 0;

function addLog() {
    if (index >= messages.length) {
        final.style.display = "block";
        return;
    }

    const line = document.createElement("div");
    line.className = "line";

    if (messages[index].includes("ERR") ||
        messages[index].includes("WARN")) {
        line.classList.add("warning");
    }

    line.textContent = messages[index];
    logs.appendChild(line);

    index++;

    bar.style.width = (index / messages.length * 100) + "%";

    setTimeout(addLog, 700);
}

addLog();
</script>

</body>
</html>
"""


@app.route("/")
def home():
    user_agent = request.headers.get("User-Agent", "").lower()

    is_ios = (
        "iphone" in user_agent
        or "ipad" in user_agent
        or "ipod" in user_agent
    )

    if is_ios:
        if ICLOUD_LINK:
            return redirect(ICLOUD_LINK)

        return "Shortcut-Link nicht konfiguriert.", 500

    return render_template_string(HTML)


if __name__ == "__main__":
    app.run()
