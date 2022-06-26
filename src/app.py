from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

def fetch_details():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)

    return hostname, ip_address

@app.route("/", methods=["GET"])
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(status="UP")

@app.route("/details", methods=["GET"])
def details():
    hostname, ip_address = fetch_details()
    return render_template("index.html", hostname=hostname, ip_address=ip_address)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)