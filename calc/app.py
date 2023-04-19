from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# Put your app in here.
# TODO: add docstrings


@app.get("/add")
def add_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    sum = add(a, b)
    return str(sum)


@app.get("/sub")
def sub_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a, b))


@app.get("/mult")
def mult_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a, b))


@app.get("/div")
def div_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a, b))
