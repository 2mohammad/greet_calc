from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a+b)

@app.route('/sub')
def sub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a-b)

@app.route('/mult')
def mult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a*b)

@app.route('/div')
def div():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(a/b)