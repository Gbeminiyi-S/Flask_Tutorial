from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return "This is my first Flask aoo! Yay!"

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'POST':
        return "You have used a POST request!"
    return "You are probably using a get request!"

app.run()