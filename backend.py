# This is from John Hammond's tutorial
# Needs to be cleaned up and updated further

from flask import Flask
from flask import render_template, send_file, make_response, request

app = Flask(__name__)

@app.route("/auth", methods=["POST"])
def auth():
    print(request.form.to_dict())
    return "ok"

@app.route("/")
def index():
    response = make_response(send_file("templates/login.html"))
    # Just for localhost demonstration sake
    response.headers.add("Acces-Control-Allow-Origin", "*")
    return response 

@app.route("/login")
def login():
    return send_file("templates/2fa.html")

if __name__ == "__main__":
    app.run()


