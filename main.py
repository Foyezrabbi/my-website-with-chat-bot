from flask import Flask, render_template, request
from threading import Timer
import webbrowser
import requests
import json
import uuid
import os

myBid = "162594"  # This value can be changed to use your own bot
myKey = "HfLCrXnUDD9vjUpz"  # This value can be changed to use your own bot

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


@app.route("/about")
def abouts():
    return render_template("about.html")


@app.route("/content")
def content():
    return render_template("content.html")


@app.route("/chatbot")
def chatbot():
    return render_template("chatbot.html")


def serial_num():
    var = str(uuid.uuid1(uuid.getnode(), 0))[24:]
    try:
        username = os.getlogin()
    except Exception as e:
        print(e)
        print("Unable to get username")
        username = "Unknown User"
    var = var + "+" + username
    print(var)
    return var


@app.route("/get")
# function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    answer = give_answer(userText)
    return str(answer)


def give_answer(givenText):
    uid = serial_num()
    url = "http://api.brainshop.ai/get?bid=" + myBid + "&key=" + myKey + "&uid=" + uid + "&msg=" + givenText
    response = requests.get(url)
    parsed = json.loads(response.text)['cnt']
    print(parsed)
    return parsed


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
