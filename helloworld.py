import os

#os.environ["GREETING"] = "Hello Rob"
#myvar = os.environ["GREETING"]
#if myvar == "Hello Rob":
#    print ("success")
#else:
#    print("fail")

#print os.environ["GREETING"]
#print("Goodbye, World!")

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

def test_greeting(x):
    if x == "foobar":
        return x
    else:
        return "foo"

