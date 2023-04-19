from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# Put your app in here.


@app.get("/add")
def add_nums():
    """Returns string after performing operations.add"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    sum = add(a, b)
    return str(sum)


@app.get("/sub")
def sub_nums():
    """Returns string after performing operations.sub"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a, b))


@app.get("/mult")
def mult_nums():
    """Returns string after performing operations.mult"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a, b))


@app.get("/div")
def div_nums():
    """Returns string after performing operations.div"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a, b))

@app.get("/math/<operation>")
def all_in_one(operation):
    """Returns string after performing specific operation"""
    
    OPERATIONS = {"add":add, "sub":sub, "mult":mult, "div":div}
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    return str(OPERATIONS[operation](a, b))